grammar SimpleMath;

// Reglas del parser
expr:   expr ('+' | '-') expr   # addSubExpr
    |   expr ('*' | '/') expr   # mulDivExpr
    |   '(' expr ')'             # parenExpr
    |   INT                      # intExpr
    ;

// Reglas del lexer
INT :   [0-9]+ ;
WS  :   [ \r\n\t]+ -> skip ;
