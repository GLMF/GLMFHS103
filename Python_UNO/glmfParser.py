# Generated from glmf.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\13")
        buf.write("\"\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\3\3\3\3\7\3\16")
        buf.write("\n\3\f\3\16\3\21\13\3\3\3\3\3\3\4\3\4\7\4\27\n\4\f\4\16")
        buf.write("\4\32\13\4\6\4\34\n\4\r\4\16\4\35\3\4\3\4\3\4\2\2\5\2")
        buf.write("\4\6\2\2\2!\2\b\3\2\2\2\4\13\3\2\2\2\6\33\3\2\2\2\b\t")
        buf.write("\5\4\3\2\t\n\7\2\2\3\n\3\3\2\2\2\13\17\7\n\2\2\f\16\7")
        buf.write("\6\2\2\r\f\3\2\2\2\16\21\3\2\2\2\17\r\3\2\2\2\17\20\3")
        buf.write("\2\2\2\20\22\3\2\2\2\21\17\3\2\2\2\22\23\5\6\4\2\23\5")
        buf.write("\3\2\2\2\24\30\7\13\2\2\25\27\7\6\2\2\26\25\3\2\2\2\27")
        buf.write("\32\3\2\2\2\30\26\3\2\2\2\30\31\3\2\2\2\31\34\3\2\2\2")
        buf.write("\32\30\3\2\2\2\33\24\3\2\2\2\34\35\3\2\2\2\35\33\3\2\2")
        buf.write("\2\35\36\3\2\2\2\36\37\3\2\2\2\37 \7\t\2\2 \7\3\2\2\2")
        buf.write("\5\17\30\35")
        return buf.getvalue()


class glmfParser ( Parser ):

    grammarFileName = "glmf.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "' '" ]

    symbolicNames = [ "<INVALID>", "LOWER_ACCENTED_LATEX_LETTER", "UPPER_ACCENTED_LATEX_LETTER", 
                      "ACCENTED_LATEX_LETTER", "WHITESPACE", "SEPARATOR_MARK", 
                      "END_MARK", "NEWLINE", "KEY_TITLE", "STRING" ]

    RULE_article = 0
    RULE_title = 1
    RULE_paragraph = 2

    ruleNames =  [ "article", "title", "paragraph" ]

    EOF = Token.EOF
    LOWER_ACCENTED_LATEX_LETTER=1
    UPPER_ACCENTED_LATEX_LETTER=2
    ACCENTED_LATEX_LETTER=3
    WHITESPACE=4
    SEPARATOR_MARK=5
    END_MARK=6
    NEWLINE=7
    KEY_TITLE=8
    STRING=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ArticleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def title(self):
            return self.getTypedRuleContext(glmfParser.TitleContext,0)


        def EOF(self):
            return self.getToken(glmfParser.EOF, 0)

        def getRuleIndex(self):
            return glmfParser.RULE_article

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArticle" ):
                listener.enterArticle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArticle" ):
                listener.exitArticle(self)




    def article(self):

        localctx = glmfParser.ArticleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_article)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.title()
            self.state = 7
            self.match(glmfParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TitleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEY_TITLE(self):
            return self.getToken(glmfParser.KEY_TITLE, 0)

        def paragraph(self):
            return self.getTypedRuleContext(glmfParser.ParagraphContext,0)


        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(glmfParser.WHITESPACE)
            else:
                return self.getToken(glmfParser.WHITESPACE, i)

        def getRuleIndex(self):
            return glmfParser.RULE_title

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTitle" ):
                listener.enterTitle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTitle" ):
                listener.exitTitle(self)




    def title(self):

        localctx = glmfParser.TitleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_title)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self.match(glmfParser.KEY_TITLE)
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==glmfParser.WHITESPACE:
                self.state = 10
                self.match(glmfParser.WHITESPACE)
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 16
            self.paragraph()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParagraphContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(glmfParser.NEWLINE, 0)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(glmfParser.STRING)
            else:
                return self.getToken(glmfParser.STRING, i)

        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(glmfParser.WHITESPACE)
            else:
                return self.getToken(glmfParser.WHITESPACE, i)

        def getRuleIndex(self):
            return glmfParser.RULE_paragraph

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParagraph" ):
                listener.enterParagraph(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParagraph" ):
                listener.exitParagraph(self)




    def paragraph(self):

        localctx = glmfParser.ParagraphContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_paragraph)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.match(glmfParser.STRING)
                self.state = 22
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==glmfParser.WHITESPACE:
                    self.state = 19
                    self.match(glmfParser.WHITESPACE)
                    self.state = 24
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==glmfParser.STRING):
                    break

            self.state = 29
            self.match(glmfParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





