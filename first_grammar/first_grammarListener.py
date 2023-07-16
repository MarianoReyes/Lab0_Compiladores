# Generated from first_grammar.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .first_grammarParser import first_grammarParser
else:
    from first_grammarParser import first_grammarParser

# This class defines a complete listener for a parse tree produced by first_grammarParser.
class first_grammarListener(ParseTreeListener):

    # Enter a parse tree produced by first_grammarParser#expression.
    def enterExpression(self, ctx:first_grammarParser.ExpressionContext):
        pass

    # Exit a parse tree produced by first_grammarParser#expression.
    def exitExpression(self, ctx:first_grammarParser.ExpressionContext):
        pass


    # Enter a parse tree produced by first_grammarParser#term.
    def enterTerm(self, ctx:first_grammarParser.TermContext):
        pass

    # Exit a parse tree produced by first_grammarParser#term.
    def exitTerm(self, ctx:first_grammarParser.TermContext):
        pass


    # Enter a parse tree produced by first_grammarParser#factor.
    def enterFactor(self, ctx:first_grammarParser.FactorContext):
        pass

    # Exit a parse tree produced by first_grammarParser#factor.
    def exitFactor(self, ctx:first_grammarParser.FactorContext):
        pass



del first_grammarParser