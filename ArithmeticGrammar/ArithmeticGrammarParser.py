# Generated from ArithmeticGrammar.g4 by ANTLR 4.13.0
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
        4,1,9,43,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,
        1,0,5,0,16,8,0,10,0,12,0,19,9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,5,1,30,8,1,10,1,12,1,33,9,1,1,2,1,2,1,2,1,2,1,2,1,2,3,2,41,8,
        2,1,2,0,2,0,2,3,0,2,4,0,0,45,0,6,1,0,0,0,2,20,1,0,0,0,4,40,1,0,0,
        0,6,7,6,0,-1,0,7,8,3,2,1,0,8,17,1,0,0,0,9,10,10,3,0,0,10,11,5,4,
        0,0,11,16,3,2,1,0,12,13,10,2,0,0,13,14,5,5,0,0,14,16,3,2,1,0,15,
        9,1,0,0,0,15,12,1,0,0,0,16,19,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,
        0,18,1,1,0,0,0,19,17,1,0,0,0,20,21,6,1,-1,0,21,22,3,4,2,0,22,31,
        1,0,0,0,23,24,10,3,0,0,24,25,5,6,0,0,25,30,3,4,2,0,26,27,10,2,0,
        0,27,28,5,7,0,0,28,30,3,4,2,0,29,23,1,0,0,0,29,26,1,0,0,0,30,33,
        1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,3,1,0,0,0,33,31,1,0,0,0,34,
        35,5,8,0,0,35,36,3,0,0,0,36,37,5,9,0,0,37,41,1,0,0,0,38,41,5,2,0,
        0,39,41,5,3,0,0,40,34,1,0,0,0,40,38,1,0,0,0,40,39,1,0,0,0,41,5,1,
        0,0,0,5,15,17,29,31,40
    ]

class ArithmeticGrammarParser ( Parser ):

    grammarFileName = "ArithmeticGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'+'", "'-'", "'*'", "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "WS", "ID", "NUMBER", "PLUS", "MINUS", 
                      "TIMES", "DIV", "LPAREN", "RPAREN" ]

    RULE_expression = 0
    RULE_term = 1
    RULE_factor = 2

    ruleNames =  [ "expression", "term", "factor" ]

    EOF = Token.EOF
    WS=1
    ID=2
    NUMBER=3
    PLUS=4
    MINUS=5
    TIMES=6
    DIV=7
    LPAREN=8
    RPAREN=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(ArithmeticGrammarParser.TermContext,0)


        def expression(self):
            return self.getTypedRuleContext(ArithmeticGrammarParser.ExpressionContext,0)


        def PLUS(self):
            return self.getToken(ArithmeticGrammarParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(ArithmeticGrammarParser.MINUS, 0)

        def getRuleIndex(self):
            return ArithmeticGrammarParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ArithmeticGrammarParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 17
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 15
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        localctx = ArithmeticGrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 9
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 10
                        self.match(ArithmeticGrammarParser.PLUS)
                        self.state = 11
                        self.term(0)
                        pass

                    elif la_ == 2:
                        localctx = ArithmeticGrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 12
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 13
                        self.match(ArithmeticGrammarParser.MINUS)
                        self.state = 14
                        self.term(0)
                        pass

             
                self.state = 19
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(ArithmeticGrammarParser.FactorContext,0)


        def term(self):
            return self.getTypedRuleContext(ArithmeticGrammarParser.TermContext,0)


        def TIMES(self):
            return self.getToken(ArithmeticGrammarParser.TIMES, 0)

        def DIV(self):
            return self.getToken(ArithmeticGrammarParser.DIV, 0)

        def getRuleIndex(self):
            return ArithmeticGrammarParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ArithmeticGrammarParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 31
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 29
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = ArithmeticGrammarParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 23
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 24
                        self.match(ArithmeticGrammarParser.TIMES)
                        self.state = 25
                        self.factor()
                        pass

                    elif la_ == 2:
                        localctx = ArithmeticGrammarParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 26
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 27
                        self.match(ArithmeticGrammarParser.DIV)
                        self.state = 28
                        self.factor()
                        pass

             
                self.state = 33
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ArithmeticGrammarParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(ArithmeticGrammarParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(ArithmeticGrammarParser.RPAREN, 0)

        def ID(self):
            return self.getToken(ArithmeticGrammarParser.ID, 0)

        def NUMBER(self):
            return self.getToken(ArithmeticGrammarParser.NUMBER, 0)

        def getRuleIndex(self):
            return ArithmeticGrammarParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = ArithmeticGrammarParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_factor)
        try:
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.match(ArithmeticGrammarParser.LPAREN)
                self.state = 35
                self.expression(0)
                self.state = 36
                self.match(ArithmeticGrammarParser.RPAREN)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.match(ArithmeticGrammarParser.ID)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 39
                self.match(ArithmeticGrammarParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

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
        self._predicates[0] = self.expression_sempred
        self._predicates[1] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




