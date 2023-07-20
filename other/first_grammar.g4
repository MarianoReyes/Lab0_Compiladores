grammar first_grammar;

// Lexer rules
WS     : (' ' | '\t' | '\n' | '\r')+ -> skip ;
ID     : ('A'..'Z'|'a'..'z')('A'..'Z'|'a'..'z'|'0'..'9')* ;
PLUS   : '+' ;
TIMES  : '*' ;
LPAREN : '(' ;
RPAREN : ')' ;

// Parser rules
expression
    : expression PLUS term
    | term
    ;

term
    : term TIMES factor
    | factor
    ;

factor
    : LPAREN expression RPAREN
    | ID
    ;
