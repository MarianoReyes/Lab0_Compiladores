grammar SimpleMath;

// Reglas del parser
expr:   expr '+' term
    |   term
    ;

term:   INT
    ;

// Reglas del lexer
INT :   [0-9]+
    ;

WS  :   [ \r\n\t]+ -> skip
    ;
