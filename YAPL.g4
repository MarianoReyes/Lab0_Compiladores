grammar YAPL;

// Parser rules

program: classDef* EOF;

classDef: 'class' ID ('inherits' ID)? '{' feature* '}';

feature: attr | method;

attr: ID ':' type ('<-' expr)? ';';

method: ID '(' formals ')' ':' type '{' expr '}';

formals: formal (',' formal)*;

formal: ID ':' type;

type: ID | 'SELF_TYPE' | 'Int' | 'String' | 'Bool' | 'IO' | 'Object';

expr: 
    | 'if' expr 'then' expr 'else' expr 'fi'
    | 'while' expr 'loop' expr 'pool'
    | '{' expr (';' expr)* '}'
    | 'let' ID ':' type ('<-' expr)? (',' ID ':' type ('<-' expr)?)* 'in' expr
    | ID '<-' expr
    | expr '.' ID '(' expr (',' expr)* ')'
    | expr '@' type '.' ID '(' expr (',' expr)* ')'
    | ID '(' expr (',' expr)* ')'
    | 'isvoid' expr
    | 'new' ID
    | ID
    | INT
    | STRING
    | 'true'
    | 'false'
    | '(' expr ')'
    ;

// Lexer rules

ID: [a-z][a-zA-Z0-9]*;

INT: [0-9]+;

STRING: '"' .*? '"';

WS : [ \t\r\n]+ -> skip;

COMMENT: '/*' .*? '*/' -> skip;
