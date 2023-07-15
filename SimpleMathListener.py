# Generated from SimpleMath.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .SimpleMathParser import SimpleMathParser
else:
    from SimpleMathParser import SimpleMathParser

# This class defines a complete listener for a parse tree produced by SimpleMathParser.
class SimpleMathListener(ParseTreeListener):

    # Enter a parse tree produced by SimpleMathParser#expr.
    def enterExpr(self, ctx:SimpleMathParser.ExprContext):
        pass

    # Exit a parse tree produced by SimpleMathParser#expr.
    def exitExpr(self, ctx:SimpleMathParser.ExprContext):
        pass


    # Enter a parse tree produced by SimpleMathParser#term.
    def enterTerm(self, ctx:SimpleMathParser.TermContext):
        pass

    # Exit a parse tree produced by SimpleMathParser#term.
    def exitTerm(self, ctx:SimpleMathParser.TermContext):
        pass



del SimpleMathParser