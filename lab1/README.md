# Lab 1 Parser de Lenguaje y Tabla de Símbolos

## Requisitos

- `pip install antlr4-python3-runtime`
- `pip install pip install anytree`
- `pip install pip install prettytable`

## Uso

- `python main_YAPL.py`

## Funcionamiento

- La clase main_YAPL usa lo implementado en laboratorio 0 de un parseador del Lenguaje YAPL.
- La clase ClassSymbolTable implementa todas las funcionalidades de la tabla de símbolos sobre los input otorgados para el programa.

### ClassSymbolTable

Dentro de las clases y métodos de este archivo se encuentran:

- Clase Symbol
- Clase Scope: get_parent(), add_content(symbol), search_content(name), delete_content(name)
- Clase SymbolTable: \_\_check_or_get_default_scope(scope), \_\_get_expresion_to_str(expr_node), \_\_get_parameters_from_method(method_node), build_symbol_table(node, current_scope), delete_content(name, scope), insert(name, data_type, semantic_type, value, line, scope, is_function, parameters, parameter_passung_method), search(name, scope), start_scope(parent_scope, scope_id)
