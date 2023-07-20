grammar AdvanceCalculation;
//ya1.lex reyes
// Lexer rules
DIGITO              : [0-9] ;
NEGATIVO            : '-' ;
PUNTO               : '.' ;
IGUAL               : '=' ;
SUMA                : '+' ;
MULTIPLICACION      : '*' ;
NUMERO              : NEGATIVO? DIGITO+ ;
NUMERO_HEXADECIMAL  :(DIGITO| 'a'..'f'|'A'..'F')+ ;
NUMERO_FLOTANTE     : DIGITO+ PUNTO DIGITO+ ;
POTENCIA            : '^' ;
NUMERO_POTENCIADO   : DIGITO+ (PUNTO DIGITO+)? POTENCIA DIGITO+ ;

WS                  : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

// Parser rules

okens 
    : DIGITO 
    | PUNTO 
    | NUMERO 
    | POTENCIA 
    | NUMERO_POTENCIADO 
    | NUMERO_HEXADECIMAL 
    | NUMERO_FLOTANTE 
    | NEGATIVO 
    | IGUAL 
    | SUMA 
    | MULTIPLICACION 
    ;
