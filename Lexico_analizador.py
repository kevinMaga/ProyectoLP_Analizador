import ply.lex as lex 

reserved = {
    # Inicio lEONARDOPARRA
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'print': 'PRINT',
    'echo': 'ECHO',
    'class': 'CLASS',
    'public': 'PUBLIC',
    'private': 'PRIVATE',
    'protected': 'PROTECTED',
    'static': 'STATIC',
    'namespace': 'NAMESPACE',
    'include': 'INCLUDE',
    'require': 'REQUIRE',
    'return': 'RETURN',
    'switch': 'SWITCH',
    'try': 'TRY',
    'catch': 'CATCH',
    'throw': 'THROW'
    # Fin LEONARDOPARRA
}

tokens = (

     # Inicio lEONARDOPARRA
   'NUMBER',
   'FLOAT',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'LPAREN',
   'RPAREN',
   'MOD',
   'PUNTOYCOMA',
   'VARIABLE',
   'NUMERAL',
   'STRING',
   'LLLAVE',     # {
   'RLLAVE',     # }
   'MAYOR',         # >
   'MENOR',         # <
   'IGUAL',     # =

    # FIN lEONARDOPARRA

) + tuple(reserved.values())

# Regular expression rules for simple tokens

 # Inicio lEONARDOPARRA

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_MOD     = r'%'
t_PUNTOYCOMA = r';'
t_NUMERAL    = r'\#'
t_LLLAVE     = r'\{'
t_RLLAVE   = r'\}'
t_MAYOR         = r'>'
t_MENOR         = r'<'
t_IGUAL    = r'='

 # Fin lEONARDOPARRA


 # Inicio lEONARDOPARRA
def t_STRING(t):
    r'(\".*?\"|\'.*?\'|<<<[A-Z]+\n.*?\n[A-Z]+;|<<<\'[A-Z]+\'\n.*?\n[A-Z]+;)'
    return t


def t_FLOAT(t):
    r'[0-9]*\.0*[1-9]+'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'\$?[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'VARIABLE')  # Check for reserved words
    return t

 # FIN lEONARDOPARRA


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

# Test con tokens
data = '''
3 + 5 - 2 * 10 / 5 % 2;
(3 + 5) * 2;

if (3 > 2) {
    print("La condición es verdadera");
} else {
    print("La condición es falsa");
}

$variable = 42;
$float_var = 3.1415;

"Esto es una cadena entre comillas dobles"
'Esto es una cadena entre comillas simples'
<<<EOT
Este es un ejemplo de cadena heredoc
EOT;
<<<'EOT'
Este es un ejemplo de cadena nowdoc
EOT;
'''


lexer.input(data)


while True:
    tok = lexer.token()
    if not tok:
        break      
    print(tok)

