import tkinter as tk
from tkinter import filedialog, messagebox
from Lexico_analizador import analizar_codigoLexico
from Lexico_analizador import checkErrorsL
from Lexico_analizador import getErrorsL
from Lexico_analizador import deleteErrorsL
from Sintactico_analizador import analizar_codigoSintactico
from Sintactico_analizador import checkErrors
from Sintactico_analizador import getErrors
from Sintactico_analizador import deleteErrors

class PHPAnalyzer:
    def __init__(self, master):
        self.ventana = master
        self.ventana.title("Analizador de Código PHP")
        self.ventana.geometry("800x500")
        
        self.erroresText = []
        
        self.crear_interfaz()
    
    def crear_interfaz(self):
        # Frame para botones de archivo
        frame_botones = tk.Frame(self.ventana)
        frame_botones.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Botones de archivo
        boton_abrir = tk.Button(frame_botones, text="Abrir Archivo", command=self.abrir_archivo)
        boton_abrir.grid(row=0, column=0, padx=5)
        
        boton_guardar = tk.Button(frame_botones, text="Guardar Archivo", command=self.guardar_archivo)
        boton_guardar.grid(row=0, column=1, padx=5)
        
        boton_exportar = tk.Button(frame_botones, text="Exportar Resultados", command=self.exportar_resultados)
        boton_exportar.grid(row=0, column=2, padx=5)
        
        # Etiqueta y cuadro de texto para el cuadro de entrada
        label_entrada = tk.Label(self.ventana, text="Ingrese su texto aquí:")
        label_entrada.grid(row=1, column=0, padx=10)
        
        self.entrada_texto = tk.Text(self.ventana, height=20, width=50)
        self.entrada_texto.grid(row=2, column=0, rowspan=2, padx=10, pady=10)
        
        # Etiqueta y cuadro de texto para el cuadro de respuesta
        label_respuesta = tk.Label(self.ventana, text="Respuesta y Errores:")
        label_respuesta.grid(row=1, column=1, padx=10)
        
        self.texto_respuesta = tk.Text(self.ventana, height=5, width=50)
        self.texto_respuesta.grid(row=2, column=1, padx=10)
        
        self.texto_errores = tk.Text(self.ventana, height=15, width=50)
        self.texto_errores.grid(row=3, column=1, padx=10)
        
        # Botón para obtener la respuesta
        boton_respuesta = tk.Button(self.ventana, text="Obtener Respuesta", command=self.obtener_respuesta)
        boton_respuesta.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
    
    def abrir_archivo(self):
        """Abre un archivo PHP y carga su contenido en el área de texto"""
        archivo = filedialog.askopenfilename(
            defaultextension=".php",
            filetypes=[("Archivos PHP", "*.php"), ("Todos los archivos", "*.*")]
        )
        
        if archivo:
            try:
                with open(archivo, 'r', encoding='utf-8') as f:
                    contenido = f.read()
                    
                # Limpiar el área de texto y insertar el contenido
                self.entrada_texto.delete("1.0", tk.END)
                self.entrada_texto.insert("1.0", contenido)
                
                messagebox.showinfo("Éxito", f"Archivo {archivo} cargado correctamente.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo abrir el archivo: {str(e)}")
    
    def guardar_archivo(self):
        """Guarda el contenido del área de texto en un archivo PHP"""
        contenido = self.entrada_texto.get("1.0", tk.END).strip()
        
        if not contenido:
            messagebox.showwarning("Advertencia", "No hay contenido para guardar.")
            return
        
        archivo = filedialog.asksaveasfilename(
            defaultextension=".php",
            filetypes=[("Archivos PHP", "*.php"), ("Todos los archivos", "*.*")]
        )
        
        if archivo:
            try:
                with open(archivo, 'w', encoding='utf-8') as f:
                    f.write(contenido)
                
                messagebox.showinfo("Éxito", f"Archivo guardado en {archivo}")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo: {str(e)}")
    
    def exportar_resultados(self):
        """Exporta los resultados del análisis a un archivo de texto"""
        respuesta = self.texto_respuesta.get("1.0", tk.END).strip()
        errores = self.texto_errores.get("1.0", tk.END).strip()
        
        if not respuesta and not errores:
            messagebox.showwarning("Advertencia", "No hay resultados para exportar.")
            return
        
        archivo = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Archivos de Texto", "*.txt"), ("Todos los archivos", "*.*")]
        )
        
        if archivo:
            try:
                with open(archivo, 'w', encoding='utf-8') as f:
                    f.write("Respuesta:\n")
                    f.write(respuesta + "\n\n")
                    f.write("Errores:\n")
                    f.write(errores)
                
                messagebox.showinfo("Éxito", f"Resultados exportados a {archivo}")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo exportar los resultados: {str(e)}")
    
    def analizar_codigo(self, entrada_usuario):
        """Realiza el análisis léxico y sintáctico"""
        analizar_codigoLexico(entrada_usuario)
        analizar_codigoSintactico(entrada_usuario)
        
        ErroresL = []
        ErroresSS = []
        
        if checkErrorsL():
            ErroresL = getErrorsL()
            self.erroresText.extend(ErroresL)
        
        if checkErrors():
            ErroresSS = getErrors()
            self.erroresText.extend(ErroresSS)
    
    def obtener_respuesta(self):
        """Obtiene la respuesta del análisis y muestra los resultados"""
        # Limpiar errores previos
        self.erroresText = []
        
        # Obtener contenido del área de texto
        entrada_usuario = self.entrada_texto.get("1.0", "end-1c")
        
        # Realizar análisis
        self.analizar_codigo(entrada_usuario)
        
        # Determinar respuesta
        respuestaText = "No se han encontrado errores"
        if checkErrorsL() or checkErrors():
            respuestaText = "Se han encontrado errores."
        
        # Actualizar áreas de texto
        self.texto_respuesta.delete("1.0", tk.END)
        self.texto_respuesta.insert("1.0", respuestaText)
        
        self.texto_errores.delete("1.0", tk.END)
        self.texto_errores.insert("1.0", '\n'.join(self.erroresText))
        
        # Limpiar errores y reiniciar análisis
        self.erroresText.clear()
        deleteErrorsL()
        deleteErrors()

def main():
    root = tk.Tk()
    app = PHPAnalyzer(root)
    root.mainloop()

if __name__ == "__main__":
    main()