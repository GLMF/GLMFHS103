# Generated from glmf.g4 by ANTLR 4.7.1
from antlr4 import *
from UNOConnector import UNOConnector
import os.path
if __name__ is not None and "." in __name__:
    from .glmfParser import glmfParser
else:
    from glmfParser import glmfParser



# This class defines a complete listener for a parse tree produced by glmfParser.
class glmfListener(ParseTreeListener):
    LATEX_REPLACE = (
        ('\\\'e', 'é'),
        ('\\`e', 'è'),
        ('\\"e', 'ë'),
        ('\\^e', 'ê'),
        ('\\`a', 'à'),
        ('\\^a', 'â'),
        ('\\^o', 'ô'),
        ('\\^i', 'î'),
        ('\\`u', 'ù'),
        ('\\^u', 'û'),
        ('\\\'E', 'É'),
        ('\\`E', 'È'),
        ('\\"E', 'Ë'),
        ('\\^E', 'Ê'),
        ('\\`A', 'À'),
        ('\\^A', 'Â'),
        ('\\^O', 'Ô'),
        ('\\^I', 'Î'),
        ('\\`U', 'Ù'),
        ('\\^U', 'Û'),
    )


    def __init__(self, filename : str, latex : bool = False):
        self.latex = latex
        self.doc = UNOConnector()
        self.doc.accessDocument('empty.odt')
        self.filename = filename


    @staticmethod
    def accentedLettersLateXReplace(ctx:glmfParser.ParagraphContext) -> str:
        chain = ctx.getText()
        for latexAccent in glmfListener.LATEX_REPLACE:
            chain = chain.replace(latexAccent[0], latexAccent[1])
        return chain


    # Enter a parse tree produced by glmfParser#article.
    def enterArticle(self, ctx:glmfParser.ArticleContext):
        pass

    # Exit a parse tree produced by glmfParser#article.
    def exitArticle(self, ctx:glmfParser.ArticleContext):
        self.doc.saveTo(filename=os.path.splitext(self.filename)[0] + '.odt', fileFormat='odt')


    # Enter a parse tree produced by glmfParser#title.
    def enterTitle(self, ctx:glmfParser.TitleContext):
        self.doc.selectParagraphStyle('Titre')

    # Exit a parse tree produced by glmfParser#title.
    def exitTitle(self, ctx:glmfParser.TitleContext):
        self.doc.paragraphBreak()


    # Enter a parse tree produced by glmfParser#paragraph.
    def enterParagraph(self, ctx:glmfParser.ParagraphContext):
        if self.latex:
            localText = glmfListener.accentedLettersLateXReplace(ctx).rstrip()
        else:
            localText = ctx.getText().rstrip()
        self.doc.insertText(localText, paraStyleName=None, charStyleName=None)

    # Exit a parse tree produced by glmfParser#paragraph.
    def exitParagraph(self, ctx:glmfParser.ParagraphContext):
        pass
