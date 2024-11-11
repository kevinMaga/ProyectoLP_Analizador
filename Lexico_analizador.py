import ply.lex as lex 
import time

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
    'include': 'INCLUDE',
    'require': 'REQUIRE',
    'return': 'RETURN',
    'switch': 'SWITCH',
    'try': 'TRY',
    'catch': 'CATCH',
    'throw': 'THROW',
    'function': 'FUNCTION',
    'default' : 'DEFAULT',
    'break' : 'BREAK',
    # Fin LEONARDOPARRA

    # Inicio Ariana Gonzabay
    'abstract': 'ABSTRACT',
    'and': 'AND',
    'as': 'AS',
    'callable': 'CALLABLE',
    'case': 'CASE',
    'clone': 'CLONE',
    'declare': 'DECLARE',
    'die': 'DIE',
    'elseif': 'ELSEIF',
    'empty': 'EMPTY',
    'endfor': 'ENDFOR',
    'endforeach': 'ENDFOREACH',
    'endif': 'ENDIF',
    'endswitch': 'ENDSWITCH',
    'endwhile': 'ENDWHILE',
    'eval': 'EVAL',
    'exit': 'EXIT',
    'extends': 'EXTENDS',
    'final': 'FINAL',
    'finally': 'FINALLY',
    'fn': 'FN',
    'foreach': 'FOREACH',
    'global': 'GLOBAL',
    'goto': 'GOTO',
    'implements': 'IMPLEMENTS',
    'instanceof': 'INSTANCEOF',
    'insteadof': 'INSTEADOF',
    'interface': 'INTERFACE',
    'isset': 'ISSET',
    'list': 'LIST',
    'match': 'MATCH',
    'new': 'NEW',
    'or': 'OR',
    'trait': 'TRAIT',
    'unset': 'UNSET',
    'use': 'USE',
    'var': 'VAR',
    'xor': 'XOR',
    'yield': 'YIELD',
    'yield_from': 'YIELD_FROM'
    # Fin Ariana Gonzabay


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
   'BOOLEAN',
   'PUNTOYCOMA',
   'VARIABLE',
   'NUMERAL',
   'STRING',
   'LLLAVE',     # {
   'RLLAVE',     # }
   'MAYOR',         # >
   'MENOR',         # <
   'IGUAL',     # =
   'PUNTO',
   'DOBLEPUNTO',
   'CLOSEINTER',
   
   # FIN lEONARDOPARRA

   #Inicio Kevin Magallanes
   'ARRAY' ,    
   'LBRACKET',    
   'RBRACKET',   
   'ARROW',
   'COMA',
   'INCREMENT',
   'DECREMENT',
   'AND_LOGICAL',
   'OR_LOGICAL',
   'NOT_LOGICAL',
   'AND_WORD',
   'OR_WORD',
   'XOR_WORD',
   'PLUS_ASSIGN', 
   'MINUS_ASSIGN', 
   'TIMES_ASSIGN', 
   'DIVIDE_ASSIGN', 
   'MODULO_ASSIGN',
   'EQUAL', 'IDENTICAL', 
   'NOT_EQUAL', 
   'NOT_IDENTICAL',
   'GREATER_EQUAL', 
   'LESS_EQUAL', 
   #Fin Kevin Magallanes
   
   #Inicio Ariana Gonzabay
   'VIRGULILLA',      # ~
   'MENOR_MAYOR',     # <>
   'COMENTARIO_LINEA',
   'COMENTARIO_MULTILINEA',
   'COMENTARIO_SHELL',
   'DELIM_INICIO',
   'DELIM_FIN'
   #Fin Ariana Gonzabay

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
t_PUNTO = R'\.'
t_DOBLEPUNTO = R'\:'
t_CLOSEINTER = R'\?'
 # Fin lEONARDOPARRA

#Inicio Kevin Magallanes
t_COMA = r','
t_ARROW = r'=>'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_INCREMENT = r'\+\+'
t_DECREMENT = r'--'
t_AND_LOGICAL = r'&&'
t_OR_LOGICAL = r'\|\|'
t_NOT_LOGICAL = r'!'
t_AND_WORD = r'\band\b'
t_OR_WORD = r'\bor\b'
t_XOR_WORD = r'\bxor\b'
t_PLUS_ASSIGN = r'\+='
t_MINUS_ASSIGN = r'-='
t_TIMES_ASSIGN = r'\*='
t_DIVIDE_ASSIGN = r'/='
t_MODULO_ASSIGN = r'%='
t_EQUAL = r'=='
t_IDENTICAL = r'==='
t_NOT_EQUAL = r'!='
t_NOT_IDENTICAL = r'!=='
t_GREATER_EQUAL = r'>='
t_LESS_EQUAL = r'<=' 
#Fin Kevin Magallanes



#Inicio Ariana Gonzabay
t_VIRGULILLA = r'~'
t_MENOR_MAYOR = r'<>'
#Fin Ariana Gonzabay

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

def t_BOOLEAN(t):
    r'\bTRUE\b|\bFALSE\b'  # Coincide solo con TRUE y FALSE como palabras completas
    t.type = 'BOOLEAN'  # Aseguramos que el tipo sea 'BOOLEAN'
    return t


def t_ID(t):
    r'\$?(this(?:->\w+)?|\w+)'
    t.type = reserved.get(t.value, 'VARIABLE')  
    return t


 # FIN lEONARDOPARRA

# Inicio Kevin Magallanes
def t_ARRAY(t):
    r'array\s*\('
    return t
# Fin Kevin Magallanes

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'



#Inicio Ariana Gonzabay
#Comentario de una línea: //
def t_COMENTARIO_LINEA(t):
    r'//.*'
    pass

#Comentarios de una linea: #
def t_COMENTARIO_SHELL(t):
    r'\#.*'
    pass

#Comentarios multilínea: /* */
def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    pass

#Delimitadores
def t_DELIM_INICIO(t):
    r'[/#~\[{(<]'
    return t

def t_DELIM_FIN(t):
    r'[/#~\]})>]'
    return t
#Fin Ariana Gonzabay

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
$numeros = array(1, 2, 3, 4);
$colores = ["rojo", "verde", "azul"];
$mixto = ["texto", 123, 4.56, array("anidado", 42)];

// Este es un comentario de una línea
#Este es un comentario shell
/* Este es un comentario multilinea */

$expresion1 = /expresion/;
$expresion2 = #expresion#;
$expresion3 = ~expresion~;
$expresion4 = [expresion];
$expresion5 = {expresion};
$expresion6 = (expresion);
$expresion7 = <expresion>;
'''

# Función para generar el nombre del archivo de log
def generate_log_filename(usuario_git):
    fecha_hora = time.strftime("%d%m%Y-%Hh%M")
    return f"lexico-{usuario_git}-{fecha_hora}.txt"

# Función para manejar errores de caracteres ilegales
def t_error(t):
    log_filename = generate_log_filename("user")
    with open(log_filename, 'a') as log_file:
        log_file.write(f"Illegal character '{t.value[0]}' at line {t.lineno}\n")
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Función principal para analizar el código y guardar los resultados en el log
def analyze_code_and_generate_log(file_path, usuario_git):
    # Leer el archivo a analizar
    with open(file_path, 'r') as file:
        data = file.read()

    # Inicializa el lexer
    lexer = lex.lex()

    # Genera el nombre del archivo de log usando el usuario proporcionado
    log_filename = generate_log_filename(usuario_git)

    # Abre el archivo de log para escribir
    with open(log_filename, 'w') as log_file:
        lexer.input(data)
        
        while True:
            tok = lexer.token()
            if not tok:
                break
            # Escribe el token y su valor en el archivo de log
            log_file.write(f"Token: {tok.type}, Value: {tok.value}, Line: {tok.lineno}\n")
        
        print(f"Log guardado en {log_filename}")

# Analizar archivos PHP
analyze_code_and_generate_log('algoritmos/algoritmo1.php', "LeoParra03")
analyze_code_and_generate_log('algoritmos/algoritmo2.php', "kevinMaga")
analyze_code_and_generate_log('algoritmos/algoritmo3.php', "kevinMaga")
analyze_code_and_generate_log('algoritmos/algoritmo4.php', "ArianaGonzabay")