import os
from tkinter import filedialog, Tk
from anytree.exporter import DotExporter
from antlr4 import *
from YAPLLexer import YAPLLexer
from YAPLParser import YAPLParser
from anytree import Node, RenderTree
from anytree.exporter import UniqueDotExporter
import antlr4
from antlr4.tree.Tree import TerminalNode


class CustomErrorListener(antlr4.error.ErrorListener.ErrorListener):
    def __init__(self):
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # Customize the error message here
        custom_msg = f"Error en la linea {line}, columna {column}, mensaje: {msg}"
        self.errors.append(custom_msg)

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        pass

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        pass

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        pass
                
    def get_errors(self):
        return self.errors

root = Tk()
root.withdraw()
input_file = filedialog.askopenfilename(initialdir=os.getcwd(),filetypes=(('YAPL files', '*.yapl'),('All files', '*.*')))
with open(input_file, 'r') as file:
    input_data = file.read()
input_stream = InputStream(input_data)
error_listener = CustomErrorListener()
lexer = YAPLLexer(input_stream)
lexer.removeErrorListeners()
lexer.addErrorListener(error_listener)

stream = CommonTokenStream(lexer)
parser = YAPLParser(stream)
parser.removeErrorListeners()
parser.addErrorListener(error_listener)

# Aplica la regla inicial de la gramática (expr)
tree = parser.program()# Linea a cambiar en funcion de la regla inicial del parser


# tdos los errores se imprimen si hay
errors = error_listener.get_errors()
for error in errors:
    print(error)

if errors:
    print("----------------------------------------------------------------------------------")
    print("\nYa que hay 1 o más errores no se armará el árbol sintáctico del archivo input.\n")
    print("----------------------------------------------------------------------------------")
else:
    print(tree.toStringTree(recog=parser))

    def build_anytree(node, antlr_node):
        if isinstance(antlr_node, TerminalNode):
            value = antlr_node.getText()
            Node(value, parent=node)
        else:
            rule_name = parser.ruleNames[antlr_node.getRuleIndex()]
            child_node = Node(rule_name, parent=node)
            for child in antlr_node.getChildren():
                build_anytree(child_node, child)

    root = Node(parser.ruleNames[tree.getRuleIndex()])
    build_anytree(root, tree)

    # Imprime el árbol anytree
    for pre, fill, node in RenderTree(root):
        print(f'{pre}{node.name}')

    # Genera una representación visual del árbol anytree
    dot_exporter = UniqueDotExporter(root)
    dot_exporter.to_picture("visual_tree.png")
    os.system(f"start visual_tree.png")
