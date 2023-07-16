import os
import subprocess

def generate_main_file(directory):
    with open(f"{directory}/main.py", "w", encoding="utf-8") as f:
        f.write("import os\n")
        f.write("from anytree.exporter import DotExporter\n")
        f.write("from antlr4 import *\n")
        f.write(f"from {directory}Lexer import {directory}Lexer\n")
        f.write(f"from {directory}Parser import {directory}Parser\n")
        f.write("from anytree import Node, RenderTree\n")
        f.write("from antlr4.tree.Tree import TerminalNode\n\n")
        
        f.write("# Obtén la entrada del usuario\n")
        f.write("input_stream = InputStream(input('Ingrese cadena a evaluar en árbol: '))\n\n")
        
        f.write("# Crea un lexer con la entrada\n")
        f.write(f"lexer = {directory}Lexer(input_stream)\n\n")
        
        f.write("# Crea un stream de tokens a partir del lexer\n")
        f.write("stream = CommonTokenStream(lexer)\n\n")
        
        f.write("# Crea un parser con el stream de tokens\n")
        f.write(f"parser = {directory}Parser(stream)\n\n")
        
        f.write("# Aplica la regla inicial de la gramática (expr)\n")
        f.write("tree = parser.expr()# Linea a cambiar en funcion de la regla inicial del parser\n\n")
        
        f.write("# Imprime el árbol de sintaxis (para depuración)\n")
        f.write("print(tree.toStringTree(recog=parser))\n\n")
        
        f.write("# Función recursiva para construir el árbol anytree\n")
        f.write("def build_anytree(node, antlr_node):\n")
        f.write("    if isinstance(antlr_node, TerminalNode):\n")
        f.write("        value = antlr_node.getText()\n")
        f.write("        Node(value, parent=node)\n")
        f.write("    else:\n")
        f.write("        rule_name = parser.ruleNames[antlr_node.getRuleIndex()]\n")
        f.write("        child_node = Node(rule_name, parent=node)\n")
        f.write("        for child in antlr_node.getChildren():\n")
        f.write("            build_anytree(child_node, child)\n\n")
        
        f.write("# Construye el árbol anytree a partir del árbol de sintaxis\n")
        f.write("root = Node(parser.ruleNames[tree.getRuleIndex()])\n")
        f.write("build_anytree(root, tree)\n\n")
        
        f.write("# Imprime el árbol anytree\n")
        f.write("for pre, fill, node in RenderTree(root):\n")
        f.write("    print(f'{pre}{node.name}')\n\n")
        
        f.write("# Genera una representación visual del árbol anytree\n")
        f.write('DotExporter(root).to_picture(f"{os.getcwd()}/tree.png")')

def list_g4_files():
    return [f for f in os.listdir() if f.endswith('.g4')]

def generate_antlr_files(file):
    directory = file.rsplit(".", maxsplit = 1)[0]
    cmd = f"java -jar antlr-4.13.0-complete.jar -Dlanguage=Python3 -o {directory} {file}"
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
        process = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
        output = process.stdout
        print(output)

        # Generate main.py file for the grammar
        generate_main_file(directory)
        
    except subprocess.CalledProcessError as e:
        print(f"Error generating ANTLR files for {file}. Command '{cmd}' returned non-zero exit status {e.returncode}.")


def main():
    while True:
        print("ANTLR .g4 files in this directory:")
        g4_files = list_g4_files()
        for i, file in enumerate(g4_files, start=1):
            print(f"{i}. {file}")
        print("Enter the number of the file you want to process, or 'q' to quit.")
        choice = input()
        if choice.lower() == 'q':
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(g4_files):
            generate_antlr_files(g4_files[int(choice)-1])
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
