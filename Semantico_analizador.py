import logging
import Sintactico_analizador  # Importa tu analizador sintáctico

# Configuración de logs para errores semánticos
logging.basicConfig(
    filename="semantico_error.txt",
    level=logging.ERROR,
    format="%(asctime)s - %(message)s",
)

# Tabla de tipos (almacena las variables y sus tipos)
tabla_tipos = {}

# Reglas de tipos para operaciones
reglas_operaciones = {
    "+": {"int": {"int": "int", "float": "float"}, "float": {"float": "float", "int": "float"}},
    "-": {"int": {"int": "int", "float": "float"}, "float": {"float": "float", "int": "float"}},
    "*": {"int": {"int": "int", "float": "float"}, "float": {"float": "float", "int": "float"}},
    "/": {"int": {"int": "float", "float": "float"}, "float": {"float": "float", "int": "float"}},
    ".": {"string": {"string": "string"}},
}

# Función para registrar errores semánticos
def registrar_error(mensaje):
    print(f"Error Semántico: {mensaje}")
    logging.error(mensaje)

# Validar tipos en asignaciones
def validar_asignacion(variable, tipo_valor):
    if variable in tabla_tipos:
        tipo_esperado = tabla_tipos[variable]
        if tipo_esperado != tipo_valor:
            registrar_error(f"La variable '{variable}' esperaba tipo '{tipo_esperado}', pero se le asignó tipo '{tipo_valor}'.")
    else:
        tabla_tipos[variable] = tipo_valor  # Nueva variable, se registra en la tabla.

# Validar tipos en operaciones
def validar_operacion(tipo1, operador, tipo2):
    if operador in reglas_operaciones:
        if tipo1 in reglas_operaciones[operador] and tipo2 in reglas_operaciones[operador][tipo1]:
            return reglas_operaciones[operador][tipo1][tipo2]
        else:
            registrar_error(f"Operación no válida: {tipo1} {operador} {tipo2}.")
            return None
    else:
        registrar_error(f"Operador '{operador}' no definido para tipos '{tipo1}' y '{tipo2}'.")
        return None

# Determinar el tipo de un valor
def determinar_tipo(valor):
    if isinstance(valor, int):
        return "int"
    elif isinstance(valor, float):
        return "float"
    elif isinstance(valor, str):
        return "string"
    elif isinstance(valor, bool):
        return "bool"
    elif valor in tabla_tipos:
        return tabla_tipos[valor]  # Tipo de variable previamente registrada
    else:
        registrar_error(f"No se pudo determinar el tipo de '{valor}'.")
        return None

# Analizar el árbol sintáctico desde el analizador sintáctico
def analizar_semantico(archivo_php):
    print(f"Analizando archivo: {archivo_php}")
    try:
        # Invocar al analizador sintáctico
        arbol_sintactico = Sintactico_analizador.analizar_php(archivo_php, "kevinMaga")
        
        if not arbol_sintactico:
            print("El árbol sintáctico está vacío. No hay nada que analizar.")
            return
        
        for nodo in arbol_sintactico:
            tipo_nodo = nodo[0]
            if tipo_nodo == "asignacion":
                variable, valor = nodo[1], nodo[2]
                tipo_valor = determinar_tipo(valor)
                validar_asignacion(variable, tipo_valor)
            elif tipo_nodo == "operacion":
                tipo1 = determinar_tipo(nodo[1])
                operador = nodo[2]
                tipo2 = determinar_tipo(nodo[3])
                validar_operacion(tipo1, operador, tipo2)
            else:
                print(f"Nodo no reconocido: {tipo_nodo}")
    except Exception as e:
        registrar_error(f"Error al analizar semánticamente: {str(e)}")

# Ejemplo de uso
archivo_php = "algoritmos/algoritmo5.php"  # Cambia por tu archivo PHP
analizar_semantico(archivo_php)
