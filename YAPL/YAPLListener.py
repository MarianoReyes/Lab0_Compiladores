# Generated from YAPL.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .YAPLParser import YAPLParser
else:
    from YAPLParser import YAPLParser

# This class defines a complete listener for a parse tree produced by YAPLParser.
class YAPLListener(ParseTreeListener):

    # Enter a parse tree produced by YAPLParser#program.
    def enterProgram(self, ctx:YAPLParser.ProgramContext):
        pass

    # Exit a parse tree produced by YAPLParser#program.
    def exitProgram(self, ctx:YAPLParser.ProgramContext):
        pass


    # Enter a parse tree produced by YAPLParser#classDeclaration.
    def enterClassDeclaration(self, ctx:YAPLParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by YAPLParser#classDeclaration.
    def exitClassDeclaration(self, ctx:YAPLParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by YAPLParser#feature.
    def enterFeature(self, ctx:YAPLParser.FeatureContext):
        pass

    # Exit a parse tree produced by YAPLParser#feature.
    def exitFeature(self, ctx:YAPLParser.FeatureContext):
        pass


    # Enter a parse tree produced by YAPLParser#formalParameter.
    def enterFormalParameter(self, ctx:YAPLParser.FormalParameterContext):
        pass

    # Exit a parse tree produced by YAPLParser#formalParameter.
    def exitFormalParameter(self, ctx:YAPLParser.FormalParameterContext):
        pass


    # Enter a parse tree produced by YAPLParser#type.
    def enterType(self, ctx:YAPLParser.TypeContext):
        pass

    # Exit a parse tree produced by YAPLParser#type.
    def exitType(self, ctx:YAPLParser.TypeContext):
        pass


    # Enter a parse tree produced by YAPLParser#expression.
    def enterExpression(self, ctx:YAPLParser.ExpressionContext):
        pass

    # Exit a parse tree produced by YAPLParser#expression.
    def exitExpression(self, ctx:YAPLParser.ExpressionContext):
        pass



del YAPLParser