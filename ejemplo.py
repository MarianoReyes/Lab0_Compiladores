from anytree.exporter import DotExporter
from antlr4 import *
from SimpleMathLexer import SimpleMathLexer
from SimpleMathParser import SimpleMathParser
from anytree import Node, RenderTree

# Obtén la entrada del usuario
input_stream = InputStream(input('? '))

# Crea un lexer con la entrada
lexer = SimpleMathLexer(input_stream)

# Crea un stream de tokens a partir del lexer
stream = CommonTokenStream(lexer)

# Crea un parser con el stream de tokens
parser = SimpleMathParser(stream)

# Aplica la regla inicial de la gramática (expr)
tree = parser.expr()

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
    print(f"{pre}{node.name}")

# Genera una representación visual del árbol anytree
DotExporter(root).to_picture("tree.png")