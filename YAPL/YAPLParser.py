# Generated from C:/Users/Jose/Documents/GitHub/Fork/Lab0_Compiladores/YAPL.g4 by ANTLR 4.13.0
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
        4,1,39,213,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,5,0,22,8,0,10,0,12,0,25,9,0,1,0,1,
        0,1,1,1,1,1,1,1,1,3,1,33,8,1,1,1,1,1,5,1,37,8,1,10,1,12,1,40,9,1,
        1,1,1,1,1,2,1,2,3,2,46,8,2,1,3,1,3,1,3,1,3,1,3,3,3,53,8,3,1,3,1,
        3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,67,8,4,10,4,12,4,70,
        9,4,1,4,1,4,1,4,1,5,3,5,76,8,5,1,5,1,5,5,5,80,8,5,10,5,12,5,83,9,
        5,1,6,1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,110,8,8,10,8,12,8,113,
        9,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,123,8,8,1,8,1,8,1,8,1,8,
        1,8,1,8,3,8,131,8,8,5,8,133,8,8,10,8,12,8,136,9,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,149,8,8,10,8,12,8,152,9,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,169,
        8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,181,8,8,10,8,12,
        8,184,9,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,197,8,
        8,10,8,12,8,200,9,8,1,8,1,8,5,8,204,8,8,10,8,12,8,207,9,8,1,9,1,
        9,1,9,1,9,1,9,0,1,16,10,0,2,4,6,8,10,12,14,16,18,0,1,2,0,11,16,33,
        33,233,0,23,1,0,0,0,2,28,1,0,0,0,4,45,1,0,0,0,6,47,1,0,0,0,8,56,
        1,0,0,0,10,75,1,0,0,0,12,84,1,0,0,0,14,88,1,0,0,0,16,168,1,0,0,0,
        18,208,1,0,0,0,20,22,3,2,1,0,21,20,1,0,0,0,22,25,1,0,0,0,23,21,1,
        0,0,0,23,24,1,0,0,0,24,26,1,0,0,0,25,23,1,0,0,0,26,27,5,0,0,1,27,
        1,1,0,0,0,28,29,5,1,0,0,29,32,5,39,0,0,30,31,5,2,0,0,31,33,5,39,
        0,0,32,30,1,0,0,0,32,33,1,0,0,0,33,34,1,0,0,0,34,38,5,3,0,0,35,37,
        3,4,2,0,36,35,1,0,0,0,37,40,1,0,0,0,38,36,1,0,0,0,38,39,1,0,0,0,
        39,41,1,0,0,0,40,38,1,0,0,0,41,42,5,4,0,0,42,3,1,0,0,0,43,46,3,6,
        3,0,44,46,3,8,4,0,45,43,1,0,0,0,45,44,1,0,0,0,46,5,1,0,0,0,47,48,
        5,33,0,0,48,49,5,5,0,0,49,52,3,14,7,0,50,51,5,6,0,0,51,53,3,16,8,
        0,52,50,1,0,0,0,52,53,1,0,0,0,53,54,1,0,0,0,54,55,5,7,0,0,55,7,1,
        0,0,0,56,57,5,33,0,0,57,58,5,8,0,0,58,59,3,10,5,0,59,60,5,9,0,0,
        60,61,5,5,0,0,61,62,3,14,7,0,62,68,5,3,0,0,63,64,3,16,8,0,64,65,
        5,7,0,0,65,67,1,0,0,0,66,63,1,0,0,0,67,70,1,0,0,0,68,66,1,0,0,0,
        68,69,1,0,0,0,69,71,1,0,0,0,70,68,1,0,0,0,71,72,3,18,9,0,72,73,5,
        4,0,0,73,9,1,0,0,0,74,76,3,12,6,0,75,74,1,0,0,0,75,76,1,0,0,0,76,
        81,1,0,0,0,77,78,5,10,0,0,78,80,3,12,6,0,79,77,1,0,0,0,80,83,1,0,
        0,0,81,79,1,0,0,0,81,82,1,0,0,0,82,11,1,0,0,0,83,81,1,0,0,0,84,85,
        5,33,0,0,85,86,5,5,0,0,86,87,3,14,7,0,87,13,1,0,0,0,88,89,7,0,0,
        0,89,15,1,0,0,0,90,91,6,8,-1,0,91,92,5,17,0,0,92,93,3,16,8,0,93,
        94,5,18,0,0,94,95,3,16,8,0,95,96,5,19,0,0,96,97,3,16,8,0,97,98,5,
        20,0,0,98,169,1,0,0,0,99,100,5,21,0,0,100,101,3,16,8,0,101,102,5,
        22,0,0,102,103,3,16,8,0,103,104,5,23,0,0,104,169,1,0,0,0,105,106,
        5,3,0,0,106,111,3,16,8,0,107,108,5,7,0,0,108,110,3,16,8,0,109,107,
        1,0,0,0,110,113,1,0,0,0,111,109,1,0,0,0,111,112,1,0,0,0,112,114,
        1,0,0,0,113,111,1,0,0,0,114,115,5,4,0,0,115,169,1,0,0,0,116,117,
        5,24,0,0,117,118,5,33,0,0,118,119,5,5,0,0,119,122,3,14,7,0,120,121,
        5,6,0,0,121,123,3,16,8,0,122,120,1,0,0,0,122,123,1,0,0,0,123,134,
        1,0,0,0,124,125,5,10,0,0,125,126,5,33,0,0,126,127,5,5,0,0,127,130,
        3,14,7,0,128,129,5,6,0,0,129,131,3,16,8,0,130,128,1,0,0,0,130,131,
        1,0,0,0,131,133,1,0,0,0,132,124,1,0,0,0,133,136,1,0,0,0,134,132,
        1,0,0,0,134,135,1,0,0,0,135,137,1,0,0,0,136,134,1,0,0,0,137,138,
        5,25,0,0,138,139,3,16,8,14,139,169,1,0,0,0,140,141,5,33,0,0,141,
        142,5,6,0,0,142,169,3,16,8,13,143,144,5,33,0,0,144,145,5,8,0,0,145,
        150,3,16,8,0,146,147,5,10,0,0,147,149,3,16,8,0,148,146,1,0,0,0,149,
        152,1,0,0,0,150,148,1,0,0,0,150,151,1,0,0,0,151,153,1,0,0,0,152,
        150,1,0,0,0,153,154,5,9,0,0,154,169,1,0,0,0,155,156,5,28,0,0,156,
        169,3,16,8,9,157,158,5,29,0,0,158,169,5,33,0,0,159,169,5,33,0,0,
        160,169,5,34,0,0,161,169,5,35,0,0,162,169,5,30,0,0,163,169,5,31,
        0,0,164,165,5,8,0,0,165,166,3,16,8,0,166,167,5,9,0,0,167,169,1,0,
        0,0,168,90,1,0,0,0,168,99,1,0,0,0,168,105,1,0,0,0,168,116,1,0,0,
        0,168,140,1,0,0,0,168,143,1,0,0,0,168,155,1,0,0,0,168,157,1,0,0,
        0,168,159,1,0,0,0,168,160,1,0,0,0,168,161,1,0,0,0,168,162,1,0,0,
        0,168,163,1,0,0,0,168,164,1,0,0,0,169,205,1,0,0,0,170,171,10,1,0,
        0,171,172,5,38,0,0,172,204,3,16,8,2,173,174,10,12,0,0,174,175,5,
        26,0,0,175,176,5,33,0,0,176,177,5,8,0,0,177,182,3,16,8,0,178,179,
        5,10,0,0,179,181,3,16,8,0,180,178,1,0,0,0,181,184,1,0,0,0,182,180,
        1,0,0,0,182,183,1,0,0,0,183,185,1,0,0,0,184,182,1,0,0,0,185,186,
        5,9,0,0,186,204,1,0,0,0,187,188,10,11,0,0,188,189,5,27,0,0,189,190,
        3,14,7,0,190,191,5,26,0,0,191,192,5,33,0,0,192,193,5,8,0,0,193,198,
        3,16,8,0,194,195,5,10,0,0,195,197,3,16,8,0,196,194,1,0,0,0,197,200,
        1,0,0,0,198,196,1,0,0,0,198,199,1,0,0,0,199,201,1,0,0,0,200,198,
        1,0,0,0,201,202,5,9,0,0,202,204,1,0,0,0,203,170,1,0,0,0,203,173,
        1,0,0,0,203,187,1,0,0,0,204,207,1,0,0,0,205,203,1,0,0,0,205,206,
        1,0,0,0,206,17,1,0,0,0,207,205,1,0,0,0,208,209,5,32,0,0,209,210,
        3,16,8,0,210,211,5,7,0,0,211,19,1,0,0,0,18,23,32,38,45,52,68,75,
        81,111,122,130,134,150,168,182,198,203,205
    ]

class YAPLParser ( Parser ):

    grammarFileName = "YAPL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'class'", "'inherits'", "'{'", "'}'", 
                     "':'", "'<-'", "';'", "'('", "')'", "','", "'SELF_TYPE'", 
                     "'Int'", "'String'", "'Bool'", "'IO'", "'Object'", 
                     "'if'", "'then'", "'else'", "'fi'", "'while'", "'loop'", 
                     "'pool'", "'let'", "'in'", "'.'", "'@'", "'isvoid'", 
                     "'new'", "'true'", "'false'", "'return'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "INT", "STRING", "WS", "COMMENT", 
                      "OP", "CLASS_ID" ]

    RULE_program = 0
    RULE_classDef = 1
    RULE_feature = 2
    RULE_attr = 3
    RULE_method = 4
    RULE_formals = 5
    RULE_formal = 6
    RULE_type = 7
    RULE_expr = 8
    RULE_func_return = 9

    ruleNames =  [ "program", "classDef", "feature", "attr", "method", "formals", 
                   "formal", "type", "expr", "func_return" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    ID=33
    INT=34
    STRING=35
    WS=36
    COMMENT=37
    OP=38
    CLASS_ID=39

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(YAPLParser.EOF, 0)

        def classDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAPLParser.ClassDefContext)
            else:
                return self.getTypedRuleContext(YAPLParser.ClassDefContext,i)


        def getRuleIndex(self):
            return YAPLParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = YAPLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 20
                self.classDef()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 26
            self.match(YAPLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS_ID(self, i:int=None):
            if i is None:
                return self.getTokens(YAPLParser.CLASS_ID)
            else:
                return self.getToken(YAPLParser.CLASS_ID, i)

        def feature(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAPLParser.FeatureContext)
            else:
                return self.getTypedRuleContext(YAPLParser.FeatureContext,i)


        def getRuleIndex(self):
            return YAPLParser.RULE_classDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDef" ):
                listener.enterClassDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDef" ):
                listener.exitClassDef(self)




    def classDef(self):

        localctx = YAPLParser.ClassDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(YAPLParser.T__0)
            self.state = 29
            self.match(YAPLParser.CLASS_ID)
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 30
                self.match(YAPLParser.T__1)
                self.state = 31
                self.match(YAPLParser.CLASS_ID)


            self.state = 34
            self.match(YAPLParser.T__2)
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==33:
                self.state = 35
                self.feature()
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 41
            self.match(YAPLParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FeatureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attr(self):
            return self.getTypedRuleContext(YAPLParser.AttrContext,0)


        def method(self):
            return self.getTypedRuleContext(YAPLParser.MethodContext,0)


        def getRuleIndex(self):
            return YAPLParser.RULE_feature

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFeature" ):
                listener.enterFeature(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFeature" ):
                listener.exitFeature(self)




    def feature(self):

        localctx = YAPLParser.FeatureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_feature)
        try:
            self.state = 45
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.attr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.method()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(YAPLParser.ID, 0)

        def type_(self):
            return self.getTypedRuleContext(YAPLParser.TypeContext,0)


        def expr(self):
            return self.getTypedRuleContext(YAPLParser.ExprContext,0)


        def getRuleIndex(self):
            return YAPLParser.RULE_attr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttr" ):
                listener.enterAttr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttr" ):
                listener.exitAttr(self)




    def attr(self):

        localctx = YAPLParser.AttrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_attr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(YAPLParser.ID)
            self.state = 48
            self.match(YAPLParser.T__4)
            self.state = 49
            self.type_()
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 50
                self.match(YAPLParser.T__5)
                self.state = 51
                self.expr(0)


            self.state = 54
            self.match(YAPLParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(YAPLParser.ID, 0)

        def formals(self):
            return self.getTypedRuleContext(YAPLParser.FormalsContext,0)


        def type_(self):
            return self.getTypedRuleContext(YAPLParser.TypeContext,0)


        def func_return(self):
            return self.getTypedRuleContext(YAPLParser.Func_returnContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAPLParser.ExprContext)
            else:
                return self.getTypedRuleContext(YAPLParser.ExprContext,i)


        def getRuleIndex(self):
            return YAPLParser.RULE_method

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod" ):
                listener.enterMethod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod" ):
                listener.exitMethod(self)




    def method(self):

        localctx = YAPLParser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(YAPLParser.ID)
            self.state = 57
            self.match(YAPLParser.T__7)
            self.state = 58
            self.formals()
            self.state = 59
            self.match(YAPLParser.T__8)
            self.state = 60
            self.match(YAPLParser.T__4)
            self.state = 61
            self.type_()
            self.state = 62
            self.match(YAPLParser.T__2)
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 64175079688) != 0):
                self.state = 63
                self.expr(0)
                self.state = 64
                self.match(YAPLParser.T__6)
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 71
            self.func_return()
            self.state = 72
            self.match(YAPLParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormalsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def formal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAPLParser.FormalContext)
            else:
                return self.getTypedRuleContext(YAPLParser.FormalContext,i)


        def getRuleIndex(self):
            return YAPLParser.RULE_formals

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormals" ):
                listener.enterFormals(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormals" ):
                listener.exitFormals(self)




    def formals(self):

        localctx = YAPLParser.FormalsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_formals)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 74
                self.formal()


            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 77
                self.match(YAPLParser.T__9)
                self.state = 78
                self.formal()
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(YAPLParser.ID, 0)

        def type_(self):
            return self.getTypedRuleContext(YAPLParser.TypeContext,0)


        def getRuleIndex(self):
            return YAPLParser.RULE_formal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormal" ):
                listener.enterFormal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormal" ):
                listener.exitFormal(self)




    def formal(self):

        localctx = YAPLParser.FormalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_formal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(YAPLParser.ID)
            self.state = 85
            self.match(YAPLParser.T__4)
            self.state = 86
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(YAPLParser.ID, 0)

        def getRuleIndex(self):
            return YAPLParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type_(self):

        localctx = YAPLParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8590063616) != 0)):
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


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAPLParser.ExprContext)
            else:
                return self.getTypedRuleContext(YAPLParser.ExprContext,i)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(YAPLParser.ID)
            else:
                return self.getToken(YAPLParser.ID, i)

        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAPLParser.TypeContext)
            else:
                return self.getTypedRuleContext(YAPLParser.TypeContext,i)


        def INT(self):
            return self.getToken(YAPLParser.INT, 0)

        def STRING(self):
            return self.getToken(YAPLParser.STRING, 0)

        def OP(self):
            return self.getToken(YAPLParser.OP, 0)

        def getRuleIndex(self):
            return YAPLParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = YAPLParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 91
                self.match(YAPLParser.T__16)
                self.state = 92
                self.expr(0)
                self.state = 93
                self.match(YAPLParser.T__17)
                self.state = 94
                self.expr(0)
                self.state = 95
                self.match(YAPLParser.T__18)
                self.state = 96
                self.expr(0)
                self.state = 97
                self.match(YAPLParser.T__19)
                pass

            elif la_ == 2:
                self.state = 99
                self.match(YAPLParser.T__20)
                self.state = 100
                self.expr(0)
                self.state = 101
                self.match(YAPLParser.T__21)
                self.state = 102
                self.expr(0)
                self.state = 103
                self.match(YAPLParser.T__22)
                pass

            elif la_ == 3:
                self.state = 105
                self.match(YAPLParser.T__2)
                self.state = 106
                self.expr(0)
                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==7:
                    self.state = 107
                    self.match(YAPLParser.T__6)
                    self.state = 108
                    self.expr(0)
                    self.state = 113
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 114
                self.match(YAPLParser.T__3)
                pass

            elif la_ == 4:
                self.state = 116
                self.match(YAPLParser.T__23)
                self.state = 117
                self.match(YAPLParser.ID)
                self.state = 118
                self.match(YAPLParser.T__4)
                self.state = 119
                self.type_()
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==6:
                    self.state = 120
                    self.match(YAPLParser.T__5)
                    self.state = 121
                    self.expr(0)


                self.state = 134
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==10:
                    self.state = 124
                    self.match(YAPLParser.T__9)
                    self.state = 125
                    self.match(YAPLParser.ID)
                    self.state = 126
                    self.match(YAPLParser.T__4)
                    self.state = 127
                    self.type_()
                    self.state = 130
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==6:
                        self.state = 128
                        self.match(YAPLParser.T__5)
                        self.state = 129
                        self.expr(0)


                    self.state = 136
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 137
                self.match(YAPLParser.T__24)
                self.state = 138
                self.expr(14)
                pass

            elif la_ == 5:
                self.state = 140
                self.match(YAPLParser.ID)
                self.state = 141
                self.match(YAPLParser.T__5)
                self.state = 142
                self.expr(13)
                pass

            elif la_ == 6:
                self.state = 143
                self.match(YAPLParser.ID)
                self.state = 144
                self.match(YAPLParser.T__7)
                self.state = 145
                self.expr(0)
                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==10:
                    self.state = 146
                    self.match(YAPLParser.T__9)
                    self.state = 147
                    self.expr(0)
                    self.state = 152
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 153
                self.match(YAPLParser.T__8)
                pass

            elif la_ == 7:
                self.state = 155
                self.match(YAPLParser.T__27)
                self.state = 156
                self.expr(9)
                pass

            elif la_ == 8:
                self.state = 157
                self.match(YAPLParser.T__28)
                self.state = 158
                self.match(YAPLParser.ID)
                pass

            elif la_ == 9:
                self.state = 159
                self.match(YAPLParser.ID)
                pass

            elif la_ == 10:
                self.state = 160
                self.match(YAPLParser.INT)
                pass

            elif la_ == 11:
                self.state = 161
                self.match(YAPLParser.STRING)
                pass

            elif la_ == 12:
                self.state = 162
                self.match(YAPLParser.T__29)
                pass

            elif la_ == 13:
                self.state = 163
                self.match(YAPLParser.T__30)
                pass

            elif la_ == 14:
                self.state = 164
                self.match(YAPLParser.T__7)
                self.state = 165
                self.expr(0)
                self.state = 166
                self.match(YAPLParser.T__8)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 205
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 203
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                    if la_ == 1:
                        localctx = YAPLParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 170
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 171
                        localctx.op = self.match(YAPLParser.OP)
                        self.state = 172
                        self.expr(2)
                        pass

                    elif la_ == 2:
                        localctx = YAPLParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 173
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 174
                        self.match(YAPLParser.T__25)
                        self.state = 175
                        self.match(YAPLParser.ID)
                        self.state = 176
                        self.match(YAPLParser.T__7)
                        self.state = 177
                        self.expr(0)
                        self.state = 182
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==10:
                            self.state = 178
                            self.match(YAPLParser.T__9)
                            self.state = 179
                            self.expr(0)
                            self.state = 184
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 185
                        self.match(YAPLParser.T__8)
                        pass

                    elif la_ == 3:
                        localctx = YAPLParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 187
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 188
                        self.match(YAPLParser.T__26)
                        self.state = 189
                        self.type_()
                        self.state = 190
                        self.match(YAPLParser.T__25)
                        self.state = 191
                        self.match(YAPLParser.ID)
                        self.state = 192
                        self.match(YAPLParser.T__7)
                        self.state = 193
                        self.expr(0)
                        self.state = 198
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==10:
                            self.state = 194
                            self.match(YAPLParser.T__9)
                            self.state = 195
                            self.expr(0)
                            self.state = 200
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 201
                        self.match(YAPLParser.T__8)
                        pass

             
                self.state = 207
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Func_returnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(YAPLParser.ExprContext,0)


        def getRuleIndex(self):
            return YAPLParser.RULE_func_return

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_return" ):
                listener.enterFunc_return(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_return" ):
                listener.exitFunc_return(self)




    def func_return(self):

        localctx = YAPLParser.Func_returnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_func_return)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(YAPLParser.T__31)
            self.state = 209
            self.expr(0)
            self.state = 210
            self.match(YAPLParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[8] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 11)
         




