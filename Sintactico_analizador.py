import ply.yacc as yacc
import datetime
from Lexico_analizador import tokens

#Inicio Kevin Magallanes
# Reglas de producción





# Valores simples
#---------------------------Estructura Basica---------------------
def p_input(p):
  "input : VARIABLE IGUAL FGETS LPAREN VARIABLE RPAREN PUNTOYCOMA"


def p_impresion(p):
    '''impresion : print
                | echo
                | input
                '''

def p_indexacion(p):
   '''indexacion : VARIABLE LBRACKET valor RBRACKET
                  | VARIABLE LBRACKET valor RBRACKET PUNTOYCOMA'''

def p_numero(p):
  '''numero : NUMBER
            | MINUS NUMBER
            | FLOAT
  '''

def p_valor(p):
    """
    valor : NUMBER
          | FLOAT
          | STRING
          | BOOLEAN
          | VARIABLE
    """
#-------------------------COMPARADORES----------------   
def p_comparadorNum(p):
	''' comparadorNum : MAYOR
					| MAYORIGUAL
					| MENOR
					| MENORIGUAL
	'''
def p_comparador(p):
	''' comparador : EQUAL
					| NOT_IDENTICAL
                    | NOT_EQUAL
					| IGUAL
                    | IDENTICAL

	'''
    
def p_variableOperacion(p):
    ''' variable : NUMBER
                  | VARIABLE
    '''

def p_comparaciones(p):
	''' comparaciones : comparacion  
					 | comparacion operadores comparaciones
	'''

def p_comparacion(p):
	''' comparacion :  variable comparadorNum variable 
            | valor comparador valor 
	'''

def p_operadores(p):
   '''operadores : OPERADOR
	         | AND_LOGICAL
	         | OR_LOGICAL
	'''
#----------------OPERACIONES ASIGNACION e INCREMENTACION/DECREMENTACION-----------------
def p_operacionesASIG(p):
  '''OperacionASIG : VARIABLE PLUS_ASSIGN NUMBER
                          | VARIABLE MINUS_ASSIGN NUMBER
                          | VARIABLE TIMES_ASSIGN NUMBER
                          | VARIABLE DIVIDE_ASSIGN NUMBER
                          | VARIABLE MODULO_ASSIGN NUMBER
                          | VARIABLE PLUS_ASSIGN NUMBER PUNTOYCOMA
                          | VARIABLE MINUS_ASSIGN NUMBER PUNTOYCOMA
                          | VARIABLE TIMES_ASSIGN NUMBER PUNTOYCOMA
                          | VARIABLE DIVIDE_ASSIGN NUMBER PUNTOYCOMA
                          | VARIABLE MODULO_ASSIGN NUMBER PUNTOYCOMA
  '''
def p_incrementoDecremento(p):
  '''incrementoDecremento : variable INCREMENT 
                          | variable DECREMENT
                          | variable INCREMENT PUNTOYCOMA
                          | variable DECREMENT PUNTOYCOMA
  '''
#----------------OPERACIONES ARITMETICAS-----------------

def p_operacion(p): 
   ''' operacion : variable operadorAritmetico variable
                | operacion operadorAritmetico operacion
   '''

def p_operadorAritmetico(p):
    '''operadorAritmetico : PLUS
						  | MINUS
						  | TIMES
						  | DIVIDE 
                          | DOBLEDIVIDE
						  | MOD
						  | POT
	'''

def p_operaciones(p): 
   ''' operaciones : operacion
                    | operacion PUNTOYCOMA
                    | operacion operadorAritmetico operaciones 
                    | VARIABLE IGUAL operaciones'''


#----------------ESTRUCTURA DE DATOS--------------------
# (Leonardo Parra) Regla principal: Lista
def p_array(p):
  ''' array : VARIABLE IGUAL ARRAY LPAREN RPAREN PUNTOYCOMA
            | VARIABLE IGUAL ARRAY LPAREN elementos RPAREN PUNTOYCOMA
            | VARIABLE IGUAL LBRACKET RBRACKET PUNTOYCOMA
            | VARIABLE IGUAL LBRACKET elementos RBRACKET PUNTOYCOMA
  '''

# (Kevin Magallanes) Regla principal: Lista

def p_lista(p):
    """
    lista : LBRACKET RBRACKET
          | LBRACKET elementos RBRACKET
    """
    p[0] = p[2]  # Devuelve los elementos de la lista

# Elementos de la lista
def p_elemento(p):
    """
    elemento : valor
             | lista
             | clave_valor
    """
    p[0] = p[1]
def p_elementos(p):
    """
    elementos : elemento
              | elementos COMA elemento
    """
    if len(p) == 2:
        p[0] = [p[1]]  # Una lista con un solo elemento
    else:
        p[0] = p[1] + [p[3]]  # Combina los elementos anteriores con el nuevo

# Elemento: puede ser un valor simple, una lista anidada o una clave-valor


# Clave-valor (para listas asociativas)
def p_clave_valor(p):
    """
    clave_valor : valor ARROW valor
    """
    p[0] = {p[1]: p[3]}  # Devuelve un diccionario con clave y valor

#Fin Kevin Magallanes

#-------------ESTRUCTURAS DE CONTROL-----------------------

# (Leonardo Parra) Regla principal: IF/ELSE


def p_estructurasControl(p):
  '''estructurasControl : while
                        | if
                        | else
                        | for
  '''
def p_if(p):
    '''
    if : IF LPAREN comparaciones RPAREN LLLAVE declaraciones RLLAVE
       | IF LPAREN VARIABLE RPAREN LLLAVE declaraciones RLLAVE
    '''

#if ($edad >= 18) {
#if ($esAdmin) { 


#} elseif ($numero2 > $numero1) {

def p_else(p):
  ''' else : RLLAVE ELSE LLLAVE declaraciones RLLAVE
          | ELSE LLLAVE declaraciones RLLAVE

          '''
#} else {
# else {

def p_declaraciones(p):
    '''
    declaraciones : declaracion
                  | declaraciones declaracion
    '''
def p_declaracion(p):
    '''
    declaracion : if
                | asignacion
                | else
                | operacion
                | while
                | for
                | funcion_inbuilt
    '''
def p_asignacion(p):
    '''
    asignacion : VARIABLE IGUAL valor PUNTOYCOMA
                | VARIABLE IGUAL valor 
    '''


#----------------FUNCIONES----------------------

# (Leonardo Parra) Regla principal: funcion_inbuilt
def p_funcioninbuilt(p):
    '''
    funcioninbuilt : funciones LPAREN operaciones RPAREN
                   | funciones LPAREN RPAREN
    '''

def p_funcionesdefin(p):
    '''
    funciones : strlen
                | strpos
                | array_push
                | array_pop
                | in_array
                | count
                | sort
    '''


# Función de manejo de errores para el log
def p_error(p):
    # Si se encuentra un error, crear un archivo de log
    if p:
        # Obtener la fecha y hora actual
        now = datetime.datetime.now()
        fecha_hora = now.strftime("%d%m%Y-%Hh%M")

        # Nombre del archivo de log
        log_filename = f"sintactico-usuarioGit-{fecha_hora}.txt"

        # Abrir el archivo en modo escritura
        with open(log_filename, 'w') as log_file:
            log_file.write(f"Error de sintaxis en el token: {p.type}, valor: {p.value}\n")
            log_file.write(f"Ubicación: Línea {p.lineno}, Columna {p.lexpos}\n")
        
        print(f"Error de sintaxis registrado en {log_filename}")
    else:
        print("Error de sintaxis al final de la entrada.")

# Build the parser
parser = yacc.yacc(debug=True)

# Función para analizar el archivo PHP
def analizar_php(archivo_php):
    # Abrir el archivo PHP
    try:
        with open(archivo_php, 'r') as f:
            php_code = f.read()
        
        # Analizar el código PHP con el parser
        result = parser.parse(php_code)
        print(f"Resultado: {result}")

    except FileNotFoundError:
        print(f"El archivo {archivo_php} no fue encontrado.")

# Llamar a la función de análisis con el archivo PHP
analizar_php('algoritmos/algoritmo5.php')  # Aquí es donde colocas tu archivo PHP para analizar

