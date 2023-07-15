# Generated from SimpleMath.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .SimpleMathParser import SimpleMathParser
else:
    from SimpleMathParser import SimpleMathParser

# This class defines a complete listener for a parse tree produced by SimpleMathParser.
class SimpleMathListener(ParseTreeListener):

    # Enter a parse tree produced by SimpleMathParser#intExpr.
    def enterIntExpr(self, ctx:SimpleMathParser.IntExprContext):
        pass

    # Exit a parse tree produced by SimpleMathParser#intExpr.
    def exitIntExpr(self, ctx:SimpleMathParser.IntExprContext):
        pass


    # Enter a parse tree produced by SimpleMathParser#addSubExpr.
    def enterAddSubExpr(self, ctx:SimpleMathParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by SimpleMathParser#addSubExpr.
    def exitAddSubExpr(self, ctx:SimpleMathParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by SimpleMathParser#mulDivExpr.
    def enterMulDivExpr(self, ctx:SimpleMathParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by SimpleMathParser#mulDivExpr.
    def exitMulDivExpr(self, ctx:SimpleMathParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by SimpleMathParser#parenExpr.
    def enterParenExpr(self, ctx:SimpleMathParser.ParenExprContext):
        pass

    # Exit a parse tree produced by SimpleMathParser#parenExpr.
    def exitParenExpr(self, ctx:SimpleMathParser.ParenExprContext):
        pass



del SimpleMathParser