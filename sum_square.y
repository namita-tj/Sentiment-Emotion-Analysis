%{
#include <stdio.h>
%}

%token NUMBER

%%

input: 
     | input line
     | input /* empty */
     ;

line: NUMBER '\n'     { $$ = $1 * $1; printf("Square of %d is %d\n", $1, $$); }
    ;

%%

int main() {
    yyparse();
    return 0;
}
