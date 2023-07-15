from antlr4 import *
from SimpleMathLexer import SimpleMathLexer
from SimpleMathParser import SimpleMathParser

# Obtén la entrada del usuario
input_stream = InputStream(input('=> '))

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
