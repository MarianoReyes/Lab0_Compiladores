grammar YAPL;

program: classDeclaration+ EOF;

classDeclaration
    : 'class' ID ('inherits' ID)? '{' feature* '}'
    ;

feature
    : ID ':' type ';'                                         // attribute
    | ID '(' (formalParameter (',' formalParameter)* )? ')' ':' type '{' expression '}'    // method
    ;

formalParameter
    : ID ':' type
    ;

type
    : ID
    | 'SELF_TYPE'
    ;

expression
    : 'if' expression 'then' expression 'else' expression 'fi'
    | 'while' expression 'loop' expression 'pool'
    | '{' expression (';' expression)* '}'
    | 'let' ID ':' type ('<-' expression)? ('in' expression)?
    | 'new' type
    | 'isvoid' expression
    | ID '<-' expression
    | expression '.' ID '(' (expression (',' expression)*)? ')'
    | expression '@' type '.' ID '(' (expression (',' expression)*)? ')'
    | expression '<' expression
    | expression '<=' expression
    | expression '=' expression
    | expression '+' expression
    | expression '-' expression
    | expression '*' expression
    | expression '/' expression
    | '~' expression
    | '(' expression ')'
    | ID
    | INT
    | STRING
    | 'true'
    | 'false'
    ;

ID: [a-zA-Z][a-zA-Z0-9_]* ;
INT: [0-9]+ ;
STRING: '"' .*? '"' ;
WS: [ \t\r\n]+ -> skip ;
