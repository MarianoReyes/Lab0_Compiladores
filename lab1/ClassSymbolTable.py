from dataclasses import dataclass, field
from collections import defaultdict
from typing import List

@dataclass
class Symbol:
    name: str
    data_type: str
    semantic_type:str
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


    def __get_parameters_from_method(self, method_node) -> List[set]:
            formals_node = method_node.children[2]
            parameters = []
            for child in formals_node.children:
                
                if child.name == "formal":
                    parameter_parts = []
                    for part in child.children:
                        if part.name != ":":
                            if part.name == "type":
                                parameter_type = part.children[0].name
                                parameter_parts.append(parameter_type)
                            else:
                                parameter_parts.append(part.name)
                                pass

                    parameters.append(tuple(parameter_parts))
            return parameters


    def build_symbol_table(self, node, current_scope = None):
        if node.name == "program":
            for child in node.children:
                self.build_symbol_table(child, current_scope)

        elif node.name == "classDef":
            parent_class = "Object"
            children = node.children
            if len(children)>4:
                if children[2].name == 'inherits':
                    parent_class = children[3].name

            class_name = node.children[1].name
            self.insert(name = class_name, data_type = parent_class, semantic_type="class", value=None,line = None, scope = current_scope)

            # start new scope in the class
            current_scope = self.start_scope(parent_scope=current_scope, scope_id=class_name)

            for child in node.children:
                self.build_symbol_table(child, current_scope)

            # end of scope
            current_scope = current_scope.get_previous()

        elif node.name == "method":
            # method name
            method_name = node.children[0].name
            # method return type
            method_return_type = node.children[5].children[0].name

            # everything about the method
            param_types = [param.children[0].name for param in node.children[2].children]
            full_signature = f"method -> ({', '.join(param_types)}) -> {method_return_type}"

            # start new scope in the method
            method_scope_id = f"{current_scope.scope_id}"
            method_scope = self.start_scope(parent_scope=current_scope, scope_id=method_scope_id)
            parameters = self.__get_parameters_from_method(node)

            self.insert(name = method_name, semantic_type="method", data_type = full_signature, value=None, line = None, scope = method_scope, parameters=parameters )

            for child in node.children:
                self.build_symbol_table(child, method_scope)

            # end of method scope
            current_scope = method_scope.get_previous()

        elif node.name == "attr":
            children = node.children
            attr_name = children[0].name
            attr_type = children[2].children[0].name
            attr_value =  children[-2] if len(children)>3 else None # Cambiar esta parte

            self.insert(name = attr_name, data_type=attr_type, semantic_type="attr" ,value=attr_value, line=None, scope=current_scope, is_function=False, parameters=[], parameter_passing_method=None,  )
            


            print("")


        else:
            for child in node.children:
                self.build_symbol_table(child, current_scope)

    def get_all_symbols(self):
        symbol_list = []
        for scope_id, symbols in self.content.items():
            for symbol_name, symbol in symbols.items():
                symbol_info = f"{scope_id}.{symbol_name} \t>>\t {symbol.data_type}"
                symbol_list.append(symbol_info)
        return symbol_list

    def print_tbl(self):
        pass


    def insert(self, name, data_type, semantic_type, value, line = None, scope = None, is_function = False, parameters = [], parameter_passing_method = None):
        scope = self.__get_scope(scope)
        symbol = Symbol(name = name, value = value, data_type = data_type,semantic_type=semantic_type, line=line, scope=scope.scope_id, is_function = is_function, parameters=parameters, parameter_passing_method=parameter_passing_method)
        scope.add_content(symbol)
        self.content[scope.scope_id][symbol.name] = symbol  # <- Change here
 
    def search(self, name, scope = None):
        scope: Scope = self.__get_scope(scope)
        item: Symbol = None
        found_item = False
        while not found_item and scope != None:
            item = scope.search_content(name)
            if item==None:
                scope = scope.get_previous()
            else:
                found_item = True
        
        return item

    def start_scope(self, parent_scope = None, scope_id = None):
        new_scope = Scope(previous=parent_scope, scope_id=scope_id)
        self.scopes[scope_id] = new_scope
        return new_scope
        
    def __get_scope(self, scope):
        if scope == None:
            return self.global_scope
        return scope