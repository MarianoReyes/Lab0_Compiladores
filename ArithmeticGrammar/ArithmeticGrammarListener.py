# Generated from ArithmeticGrammar.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .ArithmeticGrammarParser import ArithmeticGrammarParser
else:
    from ArithmeticGrammarParser import ArithmeticGrammarParser

# This class defines a complete listener for a parse tree produced by ArithmeticGrammarParser.
class ArithmeticGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by ArithmeticGrammarParser#expression.
    def enterExpression(self, ctx:ArithmeticGrammarParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ArithmeticGrammarParser#expression.
    def exitExpression(self, ctx:ArithmeticGrammarParser.ExpressionContext):
        pass


    # Enter a parse tree produced by ArithmeticGrammarParser#term.
    def enterTerm(self, ctx:ArithmeticGrammarParser.TermContext):
        pass

    # Exit a parse tree produced by ArithmeticGrammarParser#term.
    def exitTerm(self, ctx:ArithmeticGrammarParser.TermContext):
        pass


    # Enter a parse tree produced by ArithmeticGrammarParser#factor.
    def enterFactor(self, ctx:ArithmeticGrammarParser.FactorContext):
        pass

    # Exit a parse tree produced by ArithmeticGrammarParser#factor.
    def exitFactor(self, ctx:ArithmeticGrammarParser.FactorContext):
        pass



del ArithmeticGrammarParser