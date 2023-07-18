import os
from anytree.exporter import DotExporter
from antlr4 import *
from YAPLLexer import YAPLLexer
from YAPLParser import YAPLParser
from anytree import Node, RenderTree
from anytree.exporter import UniqueDotExporter
import antlr4
from antlr4.tree.Tree import TerminalNode


class CustomErrorListener(antlr4.error.ErrorListener.ErrorListener):

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # Customize the error message here
        custom_msg = f"Error en la linea {line}, columna {column}, mensaje: {msg}"
        print(custom_msg)

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        pass

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        pass

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        pass


# Obtén la entrada del usuario
input_stream = InputStream(input('Ingrese cadena a evaluar en árbol: '))

error_listener = CustomErrorListener()  # Crea un lexer con la entrada
lexer = YAPLLexer(input_stream)
lexer.removeErrorListeners()
lexer.addErrorListener(error_listener)

# Crea un stream de tokens a partir del lexer
stream = CommonTokenStream(lexer)

# Crea un parser con el stream de tokens
parser = YAPLParser(stream)
parser.removeErrorListeners()
parser.addErrorListener(error_listener)

# Aplica la regla inicial de la gramática (expr)
tree = parser.expression()  # Linea a cambiar en funcion de la regla inicial del parser

# Imprime el árbol de sintaxis (para depuración)
print(tree.toStringTree(recog=parser))

# Función recursiva para construir el árbol anytree


def build_anytree(node, antlr_node):
    if isinstance(antlr_node, TerminalNode):
        value = antlr_node.getText()
        Node(value, parent=node)
    else:
        rule_name = parser.ruleNames[antlr_node.getRuleIndex()]
        child_node = Node(rule_name, parent=node)
        for child in antlr_node.getChildren():
            build_anytree(child_node, child)


# Construye el árbol anytree a partir del árbol de sintaxis
root = Node(parser.ruleNames[tree.getRuleIndex()])
build_anytree(root, tree)

# Imprime el árbol anytree
for pre, fill, node in RenderTree(root):
    print(f'{pre}{node.name}')

# Genera una representación visual del árbol anytree
dot_exporter = UniqueDotExporter(root)
dot_exporter.to_picture("visual_tree.png")
os.system(f"start visual_tree.png")
