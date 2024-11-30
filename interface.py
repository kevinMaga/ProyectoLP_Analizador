import tkinter as tk
from tkinter import scrolledtext
from Lexico_analizador import analizar_codigoLexico, checkErrorsL, getErrorsL, deleteErrorsL
from Sintactico_analizador import analizar_codigoSintactico, checkErrors, getErrors, deleteErrors, analizar_codigoSemantico, checkSemanticErrors, getSemanticErrors, deleteSemanticErrors

# Función para analizar código desde la interfaz
# Función para analizar el código desde la interfaz
def analyze_code():
    code = code_input.get("1.0", tk.END).strip()
    result_output.delete("1.0", tk.END)

    # Limpiar errores previos
    deleteErrorsL()
    deleteErrors()
    deleteSemanticErrors()

    # Ejecutar el analizador léxico
    analizar_codigoLexico(code)
    if checkErrorsL():
        result_output.insert(tk.END, "Errores léxicos:\n" + "\n".join(getErrorsL()) + "\n\n")

    # Ejecutar el analizador sintáctico
    analizar_codigoSintactico(code)
    if checkErrors():
        result_output.insert(tk.END, "Errores sintácticos:\n" + "\n".join(getErrors()) + "\n\n")

    # Ejecutar el analizador semántico
    analizar_codigoSemantico(code)
    if checkSemanticErrors():
        result_output.insert(tk.END, "Errores semánticos:\n" + "\n".join(getSemanticErrors()) + "\n\n")

    # Si no hay errores
    if not checkErrorsL() and not checkErrors() and not checkSemanticErrors():
        result_output.insert(tk.END, "Análisis completado sin errores.\n")

# Crear interfaz gráfica
root = tk.Tk()
root.title("Analizador Léxico y Sintáctico de PHP")

# Área de entrada de código
tk.Label(root, text="Código PHP:").grid(row=0, column=0, padx=10, pady=5)
code_input = scrolledtext.ScrolledText(root, width=60, height=20)
code_input.grid(row=1, column=0, padx=10, pady=5)

# Botón para analizar
analyze_button = tk.Button(root, text="Analizar Código", command=analyze_code)
analyze_button.grid(row=2, column=0, pady=10)

# Área de resultados
tk.Label(root, text="Resultados del Análisis:").grid(row=0, column=1, padx=10, pady=5)
result_output = scrolledtext.ScrolledText(root, width=40, height=20, state="normal", bg="#E8E8E8")
result_output.grid(row=1, column=1, padx=10, pady=5)

# Ejecutar interfaz
root.mainloop()
