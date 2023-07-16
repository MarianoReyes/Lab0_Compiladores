# Generated from AdvanceCalculation.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,12,5,2,0,7,0,1,0,1,0,1,0,0,0,1,0,0,1,1,0,1,11,3,0,2,1,0,0,0,
        2,3,7,0,0,0,3,1,1,0,0,0,0
    ]

class AdvanceCalculationParser ( Parser ):

    grammarFileName = "AdvanceCalculation.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'-'", "'.'", "'='", "'+'", 
                     "'*'", "<INVALID>", "<INVALID>", "<INVALID>", "'^'" ]

    symbolicNames = [ "<INVALID>", "DIGITO", "NEGATIVO", "PUNTO", "IGUAL", 
                      "SUMA", "MULTIPLICACION", "NUMERO", "NUMERO_HEXADECIMAL", 
                      "NUMERO_FLOTANTE", "POTENCIA", "NUMERO_POTENCIADO", 
                      "WS" ]

    RULE_okens = 0

    ruleNames =  [ "okens" ]

    EOF = Token.EOF
    DIGITO=1
    NEGATIVO=2
    PUNTO=3
    IGUAL=4
    SUMA=5
    MULTIPLICACION=6
    NUMERO=7
    NUMERO_HEXADECIMAL=8
    NUMERO_FLOTANTE=9
    POTENCIA=10
    NUMERO_POTENCIADO=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class OkensContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGITO(self):
            return self.getToken(AdvanceCalculationParser.DIGITO, 0)

        def PUNTO(self):
            return self.getToken(AdvanceCalculationParser.PUNTO, 0)

        def NUMERO(self):
            return self.getToken(AdvanceCalculationParser.NUMERO, 0)

        def POTENCIA(self):
            return self.getToken(AdvanceCalculationParser.POTENCIA, 0)

        def NUMERO_POTENCIADO(self):
            return self.getToken(AdvanceCalculationParser.NUMERO_POTENCIADO, 0)

        def NUMERO_HEXADECIMAL(self):
            return self.getToken(AdvanceCalculationParser.NUMERO_HEXADECIMAL, 0)

        def NUMERO_FLOTANTE(self):
            return self.getToken(AdvanceCalculationParser.NUMERO_FLOTANTE, 0)

        def NEGATIVO(self):
            return self.getToken(AdvanceCalculationParser.NEGATIVO, 0)

        def IGUAL(self):
            return self.getToken(AdvanceCalculationParser.IGUAL, 0)

        def SUMA(self):
            return self.getToken(AdvanceCalculationParser.SUMA, 0)

        def MULTIPLICACION(self):
            return self.getToken(AdvanceCalculationParser.MULTIPLICACION, 0)

        def getRuleIndex(self):
            return AdvanceCalculationParser.RULE_okens

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOkens" ):
                listener.enterOkens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOkens" ):
                listener.exitOkens(self)




    def okens(self):

        localctx = AdvanceCalculationParser.OkensContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_okens)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4094) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





