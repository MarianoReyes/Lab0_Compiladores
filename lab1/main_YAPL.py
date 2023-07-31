import os
from tkinter import filedialog, Tk
from anytree.exporter import DotExporter
from antlr4 import *
from YAPLLexer import YAPLLexer
from YAPLParser import YAPLParser
from anytree import Node, RenderTree
from anytree.exporter import UniqueDotExporter
import antlr4
import re
from antlr4.tree.Tree import TerminalNode

# Define a symbol table class to store symbols in the current scope


class SymbolTable:
    def __init__(self):
        self.scopes = [{}]

    def enter_scope(self):
        self.scopes.append({})

    def exit_scope(self):
        if len(self.scopes) > 1:
            self.scopes.pop()

    def add_symbol(self, name, symbol):
        self.scopes[-1][name] = symbol

    def lookup_symbol(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        return None


# Define a symbol class to represent symbols


class Symbol:
    def __init__(self, name, type_, value=None):
        self.name = name
        self.type = type_
        self.value = value


class CustomErrorListener(antlr4.error.ErrorListener.ErrorListener):
    def __init__(self):
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # error en español
        translations = {
            r"missing (.+) at (.+)": r"falta \1 en \2",
            r"mismatched input (.+) expecting (.+)": r"entrada no coincidente \1, se esperaba \2",
            r"extraneous input '(.+)' expecting (.+)": r"entrada innecesaria '\1', se esperaba \2",
            # Agrega más traducciones aquí si lo deseas
        }

        # Buscar coincidencias con las expresiones regulares y traducir el mensaje
        for pattern, translation in translations.items():
            msg = re.sub(pattern, translation, msg)

        # Personalizar el mensaje de error aquí
        custom_msg = f"Error en la línea {line}, columna {column}, mensaje: {msg}"
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
input_file = filedialog.askopenfilename(initialdir=os.getcwd(
), filetypes=(('YAPL files', '*.yapl'), ('All files', '*.*')))
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
tree = parser.program()  # Linea a cambiar en funcion de la regla inicial del parser


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
            # Replace double quotes with single quotes
            value = value.replace('"', "'")
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

    # LAB 1, TABLA DE SIMBOLOS
    # Create the symbol table and enter the global scope
    symbol_table = SymbolTable()

    # Function to build the symbol table from the AST
    def build_symbol_table(node):
        if node.name == "classDef":
            # Get the class identifier from node name
            class_name = node.children[1].name
            symbol_table.add_symbol(class_name, Symbol(class_name, "class"))
            symbol_table.enter_scope()

        elif node.name == "attr":
            # Get the attribute name from node name
            attr_name = node.children[0].name
            # Get the attribute type from node name
            attr_type = node.children[2].children[0].name
            symbol_table.add_symbol(attr_name, Symbol(attr_name, attr_type))

        elif node.name == "method":
            # Get the method name from node name
            method_name = node.children[0].name
            # Get the method return type from node name
            method_return_type = node.children[5].children[0].name
            symbol_table.add_symbol(method_name, Symbol(
                method_name, f"method -> {method_return_type}"))

        for child in node.children:
            build_symbol_table(child)

        if node.name == "classDef":
            symbol_table.exit_scope()

    # Build the symbol table from the AST
    build_symbol_table(root)

    # Collect symbols and their types into a list from all scopes
    symbol_list = []
    for scope_index, scope in enumerate(symbol_table.scopes, start=1):
        for symbol_name, symbol in scope.items():
            symbol_list.append(
                f"Scope {scope_index}: {symbol_name} \t>>\t {symbol.type}")

    # Print the list of symbols and types
    print("\nTabla de Simbolos:")
    print("NOMBRE \t>>\t TIPO")
    for symbol_info in symbol_list:
        print(symbol_info)
