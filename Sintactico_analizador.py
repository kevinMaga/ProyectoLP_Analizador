import ply.yacc as yacc
import datetime
from Lexico_analizador import tokens

#Inicio Kevin Magallanes
# Reglas de producción

# Regla principal: lista
def p_lista(p):
    """
    lista : LBRACKET elementos RBRACKET
    """
    p[0] = p[2]  # Devuelve los elementos de la lista

# Elementos de la lista
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
    p[0] = {p[1]: p[3]}  # Devuelve un diccionario con clave y valor

# Valores simples
def p_valor(p):
    """
    valor : NUMBER
          | FLOAT
          | STRING
          | BOOLEAN
    """
    p[0] = p[1]  # Devuelve el valor simple
#Fin Kevin Magallanes
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

