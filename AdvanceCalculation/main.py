import os
from anytree.exporter import DotExporter
from antlr4 import *
from AdvanceCalculationLexer import AdvanceCalculationLexer
from AdvanceCalculationParser import AdvanceCalculationParser
from anytree import Node, RenderTree
from antlr4.tree.Tree import TerminalNode

from antlr4 import CommonTokenStream, InputStream, ErrorListener
# Error Listener personalizado en español
class MiErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"Error en la línea {line}, posición {column}: {msg}")
# Quitamos los listeners por defecto y agregamos nuestro error listener personalizado
parser.removeErrorListeners()
parser.addErrorListener(MiErrorListener())

# Obtén la entrada del usuario
input_stream = InputStream(input('Ingrese cadena a evaluar en árbol: '))

# Crea un lexer con la entrada
lexer = AdvanceCalculationLexer(input_stream)

# Crea un stream de tokens a partir del lexer
stream = CommonTokenStream(lexer)

# Crea un parser con el stream de tokens
parser = AdvanceCalculationParser(stream)


# Error Listener personalizado en español
class MiErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"Error en la línea {line}, posición {column}: {msg}")
# Quitamos los listeners por defecto y agregamos nuestro error listener personalizado
parser.removeErrorListeners()
parser.addErrorListener(MiErrorListener())

# Aplica la regla inicial de la gramática (expr)
tree = parser.expr()# Linea a cambiar en funcion de la regla inicial del parser

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
DotExporter(root).to_picture(f"{os.getcwd()}/tree.png")