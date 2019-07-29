/******************************************/
/*    Grammaire définissant un article    */
/******************************************/
grammar glmf;



/****************/
/*    TOKENS    */
/****************/
fragment UPPER_LETTER : [A-Z];
fragment LOWER_LETTER : [a-z];
fragment LETTER : UPPER_LETTER
                | LOWER_LETTER
                ;

fragment DIGIT : [0-9];

fragment LOWER_ACCENTED_LETTER : 'à'
                               | 'é'
                               | 'è'
                               | 'ê'
                               | 'ë'
                               | 'ô'
                               | 'ö'
                               | 'ù'
                               | 'û'
                               | 'î'
                               | 'ï'
                               ;

fragment UPPER_ACCENTED_LETTER : 'É'
                               | 'È'
                               | 'À'
                               ;

fragment ACCENTED_LETTER : LOWER_ACCENTED_LETTER 
                         | UPPER_ACCENTED_LETTER
                         ;

LOWER_ACCENTED_LATEX_LETTER : '\\' '\'' 'e'
                            | '\\' '`' 'e'
                            | '\\' '"' 'e'
                            | '\\' '^' 'e'
                            | '\\' '`' 'a'
                            | '\\' '^' 'a'
                            | '\\' '^' 'o'
                            | '\\' '^' 'i'
                            | '\\' '`' 'u'
                            | '\\' '^' 'u'
                            ;

UPPER_ACCENTED_LATEX_LETTER : '\\' '\'' 'E'
                            | '\\' '`' 'E'
                            | '\\' '"' 'E'
                            | '\\' '^' 'E'
                            | '\\' '`' 'A'
                            | '\\' '^' 'A'
                            | '\\' '^' 'O'
                            | '\\' '^' 'I'
                            | '\\' '`' 'U'
                            | '\\' '^' 'U'
                            ;

ACCENTED_LATEX_LETTER : LOWER_ACCENTED_LATEX_LETTER
                      | UPPER_ACCENTED_LATEX_LETTER
                      ;

WHITESPACE : ' ';

SEPARATOR_MARK : ',' 
               | WHITESPACE ';'
               | ';' 
               | WHITESPACE ':'
               | ':' 
               ;

END_MARK : '.'
         | WHITESPACE '?' 
         | '?'
         | WHITESPACE '!'
         | '!'
         ;

fragment SPECIAL_CHAR : '_' 
            | '$' 
            | '-' 
            | '#'
            | '+'
            | '*'
            | '/'
            | '\''
            | '='
            | SEPARATOR_MARK
            | END_MARK
            ;

fragment CHAR : LETTER
              | ACCENTED_LETTER
              | ACCENTED_LATEX_LETTER
              | DIGIT
              | SPECIAL_CHAR
              ;

NEWLINE : ('\r'? '\n')+;

KEY_TITLE : '=' 'T' 'I' 'T' 'L' 'E' '='; 

STRING : (CHAR)+;



/***************/
/*    RULES    */
/***************/
article : title EOF;
title : KEY_TITLE WHITESPACE* paragraph;
paragraph : (STRING WHITESPACE*)+ NEWLINE;
