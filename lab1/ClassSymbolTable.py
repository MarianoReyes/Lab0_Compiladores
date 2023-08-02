from collections import defaultdict
from dataclasses import dataclass, field
from typing import List

@dataclass
class Symbol:
    name: str
    type: str
    line: str
    value: any = None
    memory_position: int = None
    scope: str = None
    is_function: bool = False
    parameters: List[str] = field(default_factory=list)  # Tipos de parámetros.
    parameter_passing_method: str = None  # Método para paso de parámetro.

class Scope:
    def __init__(self, previous = None, scope_id = "global") -> None:
        self.previous:Scope = previous
        self.scope_id = scope_id  # identificador de alcance
        self.content = {}

    def get_previous(self):
        return self.previous

    def add_content(self, symbol: Symbol)-> Symbol:
        self.content[symbol.name] = symbol
        return symbol

    def search_content(self, name: str)->Symbol:
        if name in self.content:
            return self.content[name]
        return None

class SymbolTable:
    def __init__(self, root) -> None:
        self.content = defaultdict(dict)  
        self.global_scope = Scope(previous=None, scope_id = "global") #Global / Root
        self.scopes = { "global": self.global_scope }
        self.build_symbol_table(root, current_scope=self.global_scope) # Build the symbol table right after the object initialization

    def build_symbol_table(self, node, current_scope = None):
        if node.name == "program":
            for child in node.children:
                self.build_symbol_table(child, current_scope)

        elif node.name == "classDef":
            # nombre de la clase
            class_name = node.children[1].name
            self.insert(name = class_name, type = "class", line = None, scope = current_scope)

            # scope en la clase
            current_scope = self.start_scope(current_scope)

            for child in node.children:
                self.build_symbol_table(child, current_scope)

            # salir del scope
            current_scope = current_scope.get_previous()

        elif node.name == "attr":
            # nombre del atributo
            attr_name = node.children[0].name
            # tipo del atributo
            attr_type = node.children[2].children[0].name
            self.insert(name = attr_name, type = attr_type, line = None, scope = current_scope)

        elif node.name == "method":
            # nombre del metodo
            method_name = node.children[0].name
            # tipo del metodo
            method_return_type = node.children[5].children[0].name

            # todo acerca del metodo
            param_types = [param.children[0].name for param in node.children[2].children]
            full_signature = f"método -> ({', '.join(param_types)}) -> {method_return_type}"

            if current_scope != self.global_scope:
                # si se esta adentro de una clase, apendear el nombre de la clase
                class_name = current_scope.search_content("__class_name")
                if class_name:
                    full_signature = f"{class_name}.{full_signature}"

            self.insert(name = method_name, type = full_signature, line = None, scope = current_scope)

        else:
            for child in node.children:
                self.build_symbol_table(child, current_scope)

    def get_all_symbols(self):
        symbol_list = []
        for scope_id, symbols in self.content.items():
            for symbol_name, symbol in symbols.items():
                symbol_info = f"{scope_id}.{symbol_name} \t>>\t {symbol.type}"
                symbol_list.append(symbol_info)
        return symbol_list

    
    def insert(self, name, type, line, scope = None, is_function = False, parameters = [], parameter_passing_method = None):
        scope = self.__get_scope(scope)
        symbol = Symbol(name = name, type = type, line=line, value=None, scope=scope.scope_id, is_function = is_function, parameters=parameters, parameter_passing_method=parameter_passing_method)
        scope.add_content(symbol)
        self.content[scope.scope_id][symbol.name] = symbol  # <- Change here
 
    def search(self, name, scope = None):
        scope: Scope = self.__get_scope(scope)
        item: Symbol = None
        found_item = False
        while not found_item and scope == None:
            item = scope.search_content(name)
            if item==None:
                scope = scope.get_previous()
            else:
                found_item = True
        
        return item

    def start_scope(self, current_scope = None):
        current_scope = self.__get_scope(current_scope)
        return Scope(previous=current_scope)
        
    def __get_scope(self, scope):
        if scope == None:
            return self.global_scope
        return scope