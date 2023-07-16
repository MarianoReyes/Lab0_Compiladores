# Generated from first_grammar.g4 by ANTLR 4.13.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,6,35,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,
        0,4,0,15,8,0,11,0,12,0,16,1,0,1,0,1,1,1,1,5,1,23,8,1,10,1,12,1,26,
        9,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,0,0,6,1,1,3,2,5,3,7,4,9,5,11,
        6,1,0,3,3,0,9,10,13,13,32,32,2,0,65,90,97,122,3,0,48,57,65,90,97,
        122,36,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,
        0,0,11,1,0,0,0,1,14,1,0,0,0,3,20,1,0,0,0,5,27,1,0,0,0,7,29,1,0,0,
        0,9,31,1,0,0,0,11,33,1,0,0,0,13,15,7,0,0,0,14,13,1,0,0,0,15,16,1,
        0,0,0,16,14,1,0,0,0,16,17,1,0,0,0,17,18,1,0,0,0,18,19,6,0,0,0,19,
        2,1,0,0,0,20,24,7,1,0,0,21,23,7,2,0,0,22,21,1,0,0,0,23,26,1,0,0,
        0,24,22,1,0,0,0,24,25,1,0,0,0,25,4,1,0,0,0,26,24,1,0,0,0,27,28,5,
        43,0,0,28,6,1,0,0,0,29,30,5,42,0,0,30,8,1,0,0,0,31,32,5,40,0,0,32,
        10,1,0,0,0,33,34,5,41,0,0,34,12,1,0,0,0,3,0,16,24,1,6,0,0
    ]

class first_grammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS = 1
    ID = 2
    PLUS = 3
    TIMES = 4
    LPAREN = 5
    RPAREN = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'*'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "ID", "PLUS", "TIMES", "LPAREN", "RPAREN" ]

    ruleNames = [ "WS", "ID", "PLUS", "TIMES", "LPAREN", "RPAREN" ]

    grammarFileName = "first_grammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


