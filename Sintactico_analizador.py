import ply.yacc as yacc
import datetime
import os
from Lexico_analizador import tokens, lexer

usuario_git_global = None

symbol_table = {}
#llll
#Inicio Kevin Magallanes
def p_padre(p):
    """
    padre : PHP_START cuerpo PHP_END
    """
    p[0] = ('programa', p[2])


# Definición del cuerpo del programa
def p_cuerpo(p):
    """
    cuerpo : instrucciones
           | empty
    """
    p[0] = p[1]

# Reglas ya existentes para las instrucciones
def p_instrucciones(p):
    """
    instrucciones : instruccion
                  | instrucciones instruccion
    """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_instruccion(p):
    """
    instruccion : imprimir
                | solicitud_datos
                | input
                | indexacion
                | estructurasControl
                | asignacion
                | estructurasDatos
                | funciones
                | operacion
                | increment
    """
    p[0] = p[1]
    
##Impresión con cero, uno o más argumentos
def p_imprimir(p):
    """
    imprimir : PRINT LPAREN valor RPAREN PUNTOYCOMA
             | PRINT LPAREN argumentos RPAREN PUNTOYCOMA
             | PRINT_R LPAREN valor RPAREN PUNTOYCOMA
             | PRINT_R LPAREN argumentos RPAREN PUNTOYCOMA
             | ECHO valor PUNTOYCOMA
             | ECHO concatenar PUNTOYCOMA
             | ECHO valor COMA VARIABLE valor PUNTOYCOMA
    """
    if len(p) == 5:  # Caso PRINT(valor) o PRINT_R(valor)
        if isinstance(p[3], (int, float, str, bool)):  # Validar si es imprimible
            p[0] = ('imprimir', p[3])
        else:
            semantic_errors.append(f"Error semántico: No se puede imprimir el tipo '{type(p[3]).__name__}' (línea {p.lineno(2)})")
    elif len(p) == 7:  # Caso ECHO(valor, variable, valor)
        variable_name = p[4]
        if variable_name not in symbol_table:
            semantic_errors.append(f"Error semántico: La variable '{variable_name}' no está definida (línea {p.lineno(4)})")
        p[0] = ('imprimir', [p[3], variable_name, p[5]])
    else:  # PRINT(argumentos) o concatenación
        p[0] = ('imprimir', p[3])

def p_valor(p):
    """
    valor : NUMBER
          | FLOAT
          | STRING
          | BOOLEAN
          | VARIABLE
          | ID
          | expression
    """
    if p.slice[1].type == "VARIABLE":
        if p[1] not in symbol_table:  # Validar si la variable está definida
            error_message = f"Error semántico: La variable '{p[1]}' no está definida (línea {p.lineno(1)})"
            semantic_errors.append(error_message)
            p[0] = None  # Asignar un valor nulo si hay un error
        else:
            p[0] = symbol_table[p[1]]
    else:
        p[0] = p[1]  # Asignar el valor literal directamente
def p_argumentos(p):
    """
    argumentos : valor
               | argumentos COMA valor
    """
    if len(p) == 2:  # Un único valor
        if not isinstance(p[1], (int, float, str, bool)):  # Validar tipo imprimible
            semantic_errors.append(f"Error semántico: No se puede usar '{type(p[1]).__name__}' como argumento para imprimir (línea {p.lineno(1)})")
        p[0] = [p[1]]
    else:  # Múltiples valores
        if not isinstance(p[3], (int, float, str, bool)):  # Validar tipo imprimible
            semantic_errors.append(f"Error semántico: No se puede usar '{type(p[3]).__name__}' como argumento para imprimir (línea {p.lineno(3)})")
        p[0] = p[1] + [p[3]]
        

def p_concatenar(p):
    '''
    concatenar : valor
               | valor PUNTO concatenar
    '''
    if len(p) == 2:  # Un único valor
        if not isinstance(p[1], str):  # Validar si es una cadena
            semantic_errors.append(f"Error semántico: La concatenación solo es válida para cadenas, encontrado '{type(p[1]).__name__}' (línea {p.lineno(1)})")
        p[0] = p[1]
    else:  # Concatenación múltiple
        if not isinstance(p[1], str):  # Validar si el primer valor es cadena
            semantic_errors.append(f"Error semántico: La concatenación solo es válida para cadenas, encontrado '{type(p[1]).__name__}' (línea {p.lineno(1)})")
        if not isinstance(p[3], str):  # Validar si el segundo valor es cadena
            semantic_errors.append(f"Error semántico: La concatenación solo es válida para cadenas, encontrado '{type(p[3]).__name__}' (línea {p.lineno(3)})")
        p[0] = p[1] + p[3]  # Concatenar cadenas

        
#Solicitud de datos por teclado
def p_solicitud_datos(p):
    """
    solicitud_datos : VARIABLE IGUAL READLINE LPAREN STRING RPAREN PUNTOYCOMA
                    | VARIABLE IGUAL READLINE LPAREN RPAREN PUNTOYCOMA
    """
    p[0] = ('solicitud_datos', p[3])

#input
def p_input(p):
  """
  input : VARIABLE IGUAL FGETS LPAREN VARIABLE RPAREN PUNTOYCOMA

  """
#indexacion
def p_indexacion(p):
   '''indexacion :  VARIABLE LBRACKET valor RBRACKET
                  | ECHO VARIABLE LBRACKET valor RBRACKET PUNTOYCOMA'''
#estructuras de control
def p_estructurasControl(p):
  '''estructurasControl : while
                        | if
                        | else
                        | for_statement
  '''
def p_if(p):
    '''
    if : IF LPAREN comparaciones RPAREN  LLLAVE instrucciones RLLAVE 
       | IF LPAREN VARIABLE RPAREN LLLAVE instrucciones RLLAVE 
    '''

def p_comparaciones(p):
	''' comparaciones : comparacion  
					 | comparacion operadores comparaciones
	'''
def p_comparacion(p):
	''' comparacion :  VARIABLE comparadorNum VARIABLE 
                    | valor comparador valor 
                    | VARIABLE comparadorNum valor
	'''
def p_comparadorNum(p):
    ''' comparadorNum : MAYOR
                      | MAYORIGUAL
                      | MENOR
                      | MENORIGUAL
    '''
    p[0] = p[1]

def p_comparador(p):
    ''' comparador : EQUAL
                 | NOT_IDENTICAL
                 | NOT_EQUAL
                 | IGUAL
                 | IDENTICAL
                 | MAYOR
                 | MENOR
    '''
    p[0] = p[1]

def p_operadores(p):
    '''operadores : AND_LOGICAL
                 | OR_LOGICAL
    '''
    p[0] = p[1]
#asignacion
def p_asignacion(p):
    '''
    asignacion : VARIABLE IGUAL valor PUNTOYCOMA
               | VARIABLE IGUAL ARRAY PUNTOYCOMA
               | VARIABLE IGUAL ARRAY LPAREN elementos RPAREN PUNTOYCOMA
    '''
    if len(p) == 5 and p[3] != "ARRAY":  # Caso: VARIABLE = valor;
        symbol_table[p[1]] = p[3]
        p[0] = f"Asignación: {p[1]} = {p[3]}"
    elif len(p) == 5:  # Caso: VARIABLE = ARRAY;
        symbol_table[p[1]] = []
        p[0] = f"Asignación: {p[1]} = []"
    else:  # Caso: VARIABLE = ARRAY(elementos);
        if not isinstance(p[5], list):  # Validar que los elementos sean una lista
            semantic_errors.append(f"Error semántico: '{p[5]}' no es una lista válida (línea {p.lineno(5)})")
        else:
            symbol_table[p[1]] = p[5]
        p[0] = f"Asignación: {p[1]} = {p[5]}"

def p_operacion(p): 
    ''' operacion : valor operadorAritmetico valor PUNTOYCOMA
                 | operacion operadorAritmetico operacion
    '''
    
def p_operadorAritmetico(p):
    '''operadorAritmetico : PLUS
                          | MINUS
                          | TIMES
                          | DIVIDE
                          | MOD
                          | POT
    '''
    p[0] = p[1]

def p_else(p):
    ''' 
        else    : ELSE LLLAVE instrucciones RLLAVE
    '''
def p_while(p):
    """
        while : WHILE LPAREN condicion RPAREN LLLAVE instrucciones RLLAVE
    """
    p[0] = ('while', p[3], p[5])

def p_condicion(p):
    """ 
    condicion : condicion_simple
              | condicion compuesta_logica condicion
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ('condicion_compuesta', p[2], p[1], p[3])

def p_condicion_simple(p):
    """
    condicion_simple    : valor comparador valor
                        | VARIABLE comparador valor
                        | VARIABLE comparador VARIABLE
    """
    p[0] = ('condicion_simple', p[1], p[2], p[3])

def p_compuesta_logica(p):
    """
    compuesta_logica : AND_LOGICAL
                     | OR_LOGICAL
    """
    p[0] = p[1]

def p_for_statement(p):
    '''for_statement : FOR LPAREN initialization PUNTOYCOMA condicion PUNTOYCOMA increment RPAREN LLLAVE instrucciones RLLAVE'''
    print("Bucle 'for' válido")

def p_initialization(p):
    '''initialization : VARIABLE IGUAL valor
                      | empty'''
    pass

def p_increment(p):
    '''increment : VARIABLE INCREMENT
                 | VARIABLE DECREMENT
                 | VARIABLE DECREMENT PUNTOYCOMA
                 | VARIABLE PLUS_ASSIGN valor
                 | VARIABLE MINUS_ASSIGN valor
                 | empty
                 | VARIABLE INCREMENT PUNTOYCOMA'''
    pass

def p_empty(p):
    'empty :'
    pass

def p_estructurasDatos(p):
    '''
        estructurasDatos   : array
                            | lista
                            | diccionario
    '''
#$frutas = array ("Manzana", "Banano", "Cereza");

def p_array(p):
  ''' array : VARIABLE IGUAL ARRAY LPAREN RPAREN PUNTOYCOMA
            | VARIABLE IGUAL ARRAY LPAREN elementos RPAREN PUNTOYCOMA
            | VARIABLE IGUAL ARRAY LPAREN valor RPAREN PUNTOYCOMA
            | VARIABLE IGUAL LBRACKET RBRACKET PUNTOYCOMA
            | VARIABLE IGUAL LBRACKET elementos RBRACKET PUNTOYCOMA
  '''
  if len(p) == 6: 
      p[0] = ('array', p[1], [])
  elif len(p) == 8: 
      p[0] = ('array', p[1], p[5])

def p_elementos(p):
    """
    elementos : elemento
              | elementos COMA elemento
    """
    if len(p) == 2:
        p[0] = [p[1]]  # Una lista con un único elemento
    else:
        p[0] = p[1] + [p[3]]  # Concatenar listas

def p_elemento(p):
    """
    elemento : valor
             | lista
             | clave_valor
    """
    p[0] = p[1]
    
# Clave-valor (para listas asociativas)
def p_clave_valor(p):
    """
    clave_valor : valor ARROW valor
    """
    p[0] = {p[1]: p[3]}  # Diccionario clave-valor


def p_lista(p):
    """
    lista : LBRACKET RBRACKET
          | LBRACKET elementos RBRACKET
    """
    if len(p) == 3:
        p[0] = []  # Lista vacía
    else:
        p[0] = p[2]  # Lista con elementos

def p_diccionario(p):
    """
    diccionario : LBRACE pares RBRACE
    """
    p[0] = dict(p[2])

def p_pares(p):
    """
    pares : par
          | pares COMA par
    """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_par(p):
    """
    par : STRING ARROW valor
    """
    p[0] = [(p[1], p[3])]

def p_funciones(p):
    '''
        funciones   : funcion
                    | funcioninbuilt
                    | funcion_anonima
                    | arrow_function
    '''

def p_funcion(p):
    '''
    funcion : FUNCTION ID LPAREN RPAREN LLLAVE instrucciones RLLAVE
            | FUNCTION ID LPAREN parametros RPAREN LLLAVE instrucciones RLLAVE
    '''

def p_funcioninbuilt(p):
    '''
    funcioninbuilt : VARIABLE IGUAL funcionesdefin LPAREN operaciones RPAREN PUNTOYCOMA
                   | VARIABLE IGUAL funcionesdefin LPAREN RPAREN PUNTOYCOMA
    '''


def p_funcionesdefin(p):
    '''
    funcionesdefin : STRLEN
                | STRPOS
                | ARRAY_PUSH
                | ARRAY_POP
                | IN_ARRAY
                | COUNT
                | SORT
    '''


def p_operaciones(p): 
    ''' operaciones : operacion
                    | operacion PUNTOYCOMA
                    | operacion operadorAritmetico operaciones 
                    | VARIABLE IGUAL operaciones
                    | VARIABLE'''
    p[0] = p[1]
  
def p_funcion_anonima(p):
    """
    funcion_anonima : VARIABLE IGUAL FUNCTION LPAREN parametros RPAREN LLLAVE instrucciones RLLAVE PUNTOYCOMA
    """
    p[0] = ('funcion_anonima', p[3], p[6])

def p_parametros(p):
    """
    parametros : STRING
               | parametros COMA STRING
               | VARIABLE
               | parametros COMA VARIABLE
    """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_arrow_function(p):
    '''arrow_function : VARIABLE IGUAL FN LPAREN parameter_list RPAREN ARROW expression PUNTOYCOMA'''
    print("Función flecha válida:", p[1])

def p_parameter_list(p):
    '''parameter_list : VARIABLE
                      | VARIABLE COMA parameter_list'''
    pass

def p_expression(p):
    '''expression : VARIABLE
                  | NUMBER
                  | VARIABLE TIMES VARIABLE
                  | VARIABLE PLUS VARIABLE
                  | VARIABLE MINUS VARIABLE
                  | VARIABLE DIVIDE VARIABLE
                  | VARIABLE TIMES NUMBER
                  | VARIABLE PLUS NUMBER
                  | VARIABLE MINUS NUMBER
                  | VARIABLE DIVIDE NUMBER
                  | VARIABLE MOD VARIABLE'''
    pass

# # Función de manejo de errores para el log
# def p_error(p):
#     global usuario_git_global
#     # Si se encuentra un error, crear un archivo de log
#     if p:
#         # Obtener la fecha y hora actual
#         now = datetime.datetime.now()
#         fecha_hora = now.strftime("%d%m%Y-%Hh%M")  # Formato: 20062024-23h32

#         # Nombre del archivo de log, incluyendo el nombre de usuario Git y la fecha/hora
#         log_filename = f"sintactico-{usuario_git_global}-{fecha_hora}.txt"

#         # Abrir el archivo en modo append
#         with open(log_filename, 'a') as log_file:
#             log_file.write(f"Error de sintaxis en el token: {p.type}, valor: {p.value}\n")
#             log_file.write(f"Ubicación: Línea {p.lineno}, Columna {p.lexpos}\n")

#         print(f"Error de sintaxis registrado en {log_filename}")

#     else:
#         print(f"Error de sintaxis al final de la entrada para el usuario {usuario_git_global}.")

# # Build the parser
# parser = yacc.yacc()

# # Función para analizar el archivo PHP
# def analizar_php(archivo_php, usuario_git):
#     lexer.lineno = 1  # Reinicia el contador de líneas antes de analizar
#     global usuario_git_global
#     # Asignamos el valor de usuario_git a la variable global
#     usuario_git_global = usuario_git
#     try:
#         # Verificar si el archivo existe antes de intentar abrirlo
#         if not os.path.isfile(archivo_php):
#             raise FileNotFoundError(f"El archivo {archivo_php} no fue encontrado.")

#         # Abrir el archivo PHP
#         with open(archivo_php, 'r') as f:
#             php_code = f.read()
#         try:
#             # Analizar el código PHP con el parser
#             result = parser.parse(php_code, lexer=lexer)
#             print(f"Resultado del análisis de {archivo_php}: {result}")
#         except Exception as e:
#             # Manejo de errores en el análisis sintáctico
#             print(f"Error al analizar el archivo PHP: {str(e)}")
#             p_error(None)  # Llamar a p_error si hay un error en el análisis
#             # Crear un archivo de log en caso de error durante el análisis
#             now = datetime.datetime.now()
#             fecha_hora = now.strftime("%d%m%Y-%Hh%M")
#             log_filename = f"sintactico-{usuario_git}-{fecha_hora}-error.txt"
#             with open(log_filename, 'a') as log_file:  # Modo append
#                 log_file.write(f"Error de sintaxis en el archivo: {archivo_php}\n")
#                 log_file.write(f"Error: {str(e)}\n")
#     except FileNotFoundError as fnf_error:
#         # Manejo de errores si el archivo no se encuentra
#         print(fnf_error)
#         # Generar log de error con usuario_git
#         now = datetime.datetime.now()
#         fecha_hora = now.strftime("%d%m%Y-%Hh%M")
#         log_filename = f"sintactico-{usuario_git}-{fecha_hora}-error.txt"
#         with open(log_filename, 'a') as log_file:  # Modo append
#             log_file.write(f"Error: El archivo {archivo_php} no fue encontrado.\n")
#     except Exception as e:
#         # Captura cualquier otro tipo de excepción
#         print(f"Error inesperado: {str(e)}")
#         # Generar log de error con usuario_git
#         now = datetime.datetime.now()
#         fecha_hora = now.strftime("%d%m%Y-%Hh%M")
#         log_filename = f"sintactico-{usuario_git}-{fecha_hora}-error.txt"
#         with open(log_filename, 'a') as log_file:  # Modo append
#             log_file.write(f"Error inesperado: {str(e)}\n")
# # Llamar a la función de análisis con el archivo PHP y el usuario Git
# analizar_php('algoritmos/algoritmo5.php', 'kevinMaga')
# analizar_php('algoritmos/algoritmo6.php', 'ArianaGonzabay')
# analizar_php('algoritmos/algoritmo7.php', 'LeoParra')


#Funciones para la INTERFAZ
parser_errors = []

def analizar_codigoSintactico(codigo):
    lexer.lineno = 1
    parser.parse(codigo, lexer=lexer)

    
def checkErrors():
    if len(parser_errors)==0:
        return False
    else:
        return True
    
def getErrors():
    for error in parser_errors:
        print(error)
    return parser_errors

def deleteErrors():
    parser_errors.clear()

def p_error(p):
    if p:
        error_message = f"Error de sintaxis en el token: {p.value}, Linea: {p.lineno}"
        parser_errors.append(error_message)
        print(f"Error en token: {p.value}, Linea: {p.lineno}") 
        yacc.errok()
    else:
        parser_errors.append("Error de sintaxis al final de la entrada")

# Construcción del parser
parser = yacc.yacc()

# Lista para almacenar errores semánticos
semantic_errors = []

# Función para analizar código con reglas semánticas
def analizar_codigoSemantico(codigo):
    lexer.lineno = 1  # Reiniciar el contador de líneas
    semantic_errors.clear()  # Limpiar errores previos
    parser.parse(codigo, lexer=lexer)

# Verificar si hay errores semánticos
def checkSemanticErrors():
    return len(semantic_errors) > 0

# Obtener la lista de errores semánticos
def getSemanticErrors():
    for error in semantic_errors:
        print(error)
    return semantic_errors

# Limpiar la lista de errores semánticos
def deleteSemanticErrors():
    semantic_errors.clear()

    
# def p_error(p):
#     global parser_errors
#     if p:
#         parser_errors.append(f"Syntax error at '{p.value}' (line {p.lineno})")
#     else:
#         parser_errors.append("Syntax error at EOF")

# # Variable para errores sintácticos
# parser_errors = []

# # Función para inicializar el parser
# def get_parser():
#     return yacc.yacc()    
