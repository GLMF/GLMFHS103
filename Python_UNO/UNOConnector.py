import socket
import uno
import subprocess
import os
from com.sun.star.beans import PropertyValue
from com.sun.star.text.ControlCharacter import PARAGRAPH_BREAK



class UNOConnector:
    FORMAT = {
                 'odt': 'writer8',
                 'pdf': 'writer_pdf_export',
                 'doc': 'MS Word 97',
                 'txt': 'Text'
             }

    def __init__(self, port : int = 2002, host : str = 'localhost', serverManager : bool = True):
        self.port = port
        self.host = host
        self.serverManager = serverManager
        self.localContext = uno.getComponentContext()
        self.resolver = self.localContext.ServiceManager.createInstanceWithContext('com.sun.star.bridge.UnoUrlResolver', self.localContext)

        try:
            self.ctx = self.resolver.resolve('uno:socket,host={},port={};urp;StarOffice.ComponentContext'.format(self.host, self.port))
        except:
            if self.serverManager:
                subprocess.call('soffice --headless --nologo --nofirststartwizard --accept="socket,host={},port={};urp;StarOffice.ServiceManager" &'.format(self.host, self.port), shell=True)
                print('Server started at {}:{}'.format(self.host, self.port))
            try:
                self.ctx = self.resolver.resolve('uno:socket,host={},port={};urp;StarOffice.ComponentContext'.format(self.host, self.port))
            except Exception as e:
                print('Unable to join server')
                print(e)
                exit(1)

        self.smgr = self.ctx.ServiceManager
        self.desktop = self.smgr.createInstanceWithContext('com.sun.star.frame.Desktop', self.ctx)
        self.closed = False


    def __del__(self):
        if not self.closed:
            self.close()
        if self.serverManager:
            subprocess.call('kill $(ps ax|grep "soffice.bin --headless"|grep -v grep|cut -d \  -f 1)', shell=True)


    def accessCurrentDocument(self) -> None:
        self.model = self.desktop.getCurrentComponent()
        self.text = self.model.Text
        self.cursor = self.text.createTextCursor()

    
    def accessNewDocument(self) -> None:
        self.model = self.desktop.loadComponentFromURL('private:factory/swriter', '_blank', 0, ())
        self.text = self.model.Text
        self.cursor = self.text.createTextCursor()


    def accessDocument(self, filename : str) -> None:
        url = uno.systemPathToFileUrl(os.path.join(os.getcwd(), filename))
        self.model = self.desktop.loadComponentFromURL(url, '_blank', 0, ())
        self.text = self.model.Text
        self.cursor = self.text.createTextCursor()


    def paragraphBreak(self) -> None:
        self.text.insertControlCharacter(self.cursor, PARAGRAPH_BREAK, 0)


    def selectParagraphStyle(self, paraStyleName : str) -> None:
        self.cursor.ParaStyleName = paraStyleName


    def selectCharStyle(self, charStyleName : str) -> None:
        self.cursor.CharStyleName = charStyleName


    def insertText(self, text : str, paraStyleName : str = 'Style par défaut', charStyleName : str = 'Style par défaut', position : int = 0, newLine : bool = False) -> None:
        if paraStyleName is not None:
            self.selectParagraphStyle(paraStyleName)
        if charStyleName is not None:
            self.selectCharStyle(charStyleName)
        self.text.insertString(self.cursor, text, position)
        if newLine:
            self.paragraphBreak()


    def close(self) -> None:
        self.ctx.ServiceManager
        self.closed = True


    def saveTo(self, filename : str = 'out.odt', fileFormat : str = 'odt') -> None:
        args = (PropertyValue('FilterName', 0, UNOConnector.FORMAT[fileFormat], 0),)
        url = uno.systemPathToFileUrl(os.path.join(os.getcwd(), filename))
        self.model.storeToURL(url, args)
        self.model.dispose()



if __name__ == '__main__':
    doc = UNOConnector()
    doc.accessDocument('empty.odt')
    doc.insertText('Titre de mon article', newLine=True, paraStyleName='Titre')
    doc.insertText('Une phrase qui suit le ', paraStyleName='Normal')
    doc.insertText('titre', paraStyleName='Normal', charStyleName='gras')
    doc.saveTo()
    doc.close()
