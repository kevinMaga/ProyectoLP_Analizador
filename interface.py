import os
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
        # Color de fondo
        master.configure(bg='#f0f0f4')
        
        # Ruta del proyecto
        self.project_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Ruta de carpetas
        self.algoritmos_dir = os.path.join(self.project_dir, 'algoritmos')
        self.resultados_dir = os.path.join(self.project_dir, 'resultados')
        
        # Se crean los directorios si no existen
        os.makedirs(self.algoritmos_dir, exist_ok=True)
        os.makedirs(self.resultados_dir, exist_ok=True)
        
        self.ventana = master
        self.ventana.title("PHP Code Analyzer")
        self.ventana.geometry("1200x700")
        
        self.erroresText = []
        
        self.crear_interfaz()
    
    def crear_interfaz(self):
        # Configuración del grid
        self.ventana.grid_columnconfigure(0, weight=3)
        self.ventana.grid_columnconfigure(1, weight=1)
        self.ventana.grid_rowconfigure(2, weight=1)
        
        # Estilo de la interfaz
        header_frame = tk.Frame(self.ventana, bg='#3498db', padx=10, pady=10) #header
        header_frame.grid(row=0, column=0, columnspan=2, sticky="ew")

        #Label del header
        header_label = tk.Label(
            header_frame, 
            text="PHP Code Analyzer", 
            font=("Arial", 16, "bold"), 
            fg='white', 
            bg='#3498db'
        )
        header_label.pack()
        
        # Botones de la interfaz
        frame_botones = tk.Frame(self.ventana, bg='#f0f0f4')
        frame_botones.grid(row=1, column=0, columnspan=2, pady=10, padx=10, sticky="ew") 
        
        # Configuración del frame de botones para centrar
        frame_botones.grid_columnconfigure(0, weight=1)
        frame_botones.grid_columnconfigure(1, weight=1)
        frame_botones.grid_columnconfigure(2, weight=1)
        
        # Estilo de los botones
        button_style = {
            'font': ('Arial', 10, 'bold'),
            'bg': '#3498db', 
            'fg': 'white',
            'activebackground': '#2980b9',
            'relief': tk.FLAT,
            'padx': 10,
            'pady': 5,
            'width': 20  
        }
        
        boton_abrir = tk.Button(
            frame_botones, 
            text="Abrir Archivo", 
            command=self.abrir_archivo,
            **button_style
        )
        boton_abrir.grid(row=0, column=0, padx=5, sticky='ew')
        
        boton_guardar = tk.Button(
            frame_botones, 
            text="Guardar Archivo", 
            command=self.guardar_archivo,
            **button_style
        )
        boton_guardar.grid(row=0, column=1, padx=5, sticky='ew')
        
        boton_exportar = tk.Button(
            frame_botones, 
            text="Exportar Resultados", 
            command=self.exportar_resultados,
            **button_style
        )
        boton_exportar.grid(row=0, column=2, padx=5, sticky='ew')
        
        # Frame para el área de texto
        frame_texto = tk.Frame(self.ventana, bg='#f0f0f4')
        frame_texto.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        
        # Linea de números para el código
        self.numeros_linea = tk.Canvas(
            frame_texto, 
            width=40, 
            bg="#ecf0f1", 
            highlightthickness=0
        )
        self.numeros_linea.pack(side="left", fill="y")
        
        # Scrollbars
        text_scrollbar_y = tk.Scrollbar(frame_texto)
        text_scrollbar_x = tk.Scrollbar(frame_texto, orient="horizontal")
        
        # Entrada de texto
        self.entrada_texto = tk.Text(
            frame_texto, 
            wrap="none", 
            undo=True, 
            font=("Consolas", 10),
            xscrollcommand=text_scrollbar_x.set,
            yscrollcommand=text_scrollbar_y.set,
            bg='white',
            fg='black',
            insertbackground='black'
        )
        text_scrollbar_y.pack(side="right", fill="y")
        text_scrollbar_x.pack(side="bottom", fill="x")
        self.entrada_texto.pack(side="left", fill="both", expand=True)
        
        # Configurar scrollbars
        text_scrollbar_y.config(command=self.entrada_texto.yview)
        text_scrollbar_x.config(command=self.entrada_texto.xview)
        
        # Configurar eventos para actualizar los números de línea
        self.entrada_texto.bind("<KeyRelease>", self.actualizar_numeros_linea)
        self.entrada_texto.bind("<MouseWheel>", self.actualizar_numeros_linea)
        self.entrada_texto.bind("<Configure>", self.actualizar_numeros_linea)
        
        # Sección de resultados y errores
        results_frame = tk.Frame(self.ventana, bg='#f0f0f4')
        results_frame.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
        
        # Titulos de las secciones
        response_label = tk.Label(
            results_frame, 
            text="Resultado de Análisis:", 
            font=('Arial', 10, 'bold'),
            bg='#f0f0f4'
        )
        response_label.pack(pady=(0,5))
        
        response_scrollbar = tk.Scrollbar(results_frame)
        self.texto_respuesta = tk.Text(
            results_frame, 
            height=5, 
            wrap="word",
            yscrollcommand=response_scrollbar.set,
            bg='white',
            fg='black'
        )
        response_scrollbar.pack(side="right", fill="y")
        self.texto_respuesta.pack(fill="x", expand=False)
        response_scrollbar.config(command=self.texto_respuesta.yview)
        
        # Sección de errores
        errors_label = tk.Label(
            results_frame, 
            text="Errores:", 
            font=('Arial', 10, 'bold'),
            fg='red',
            bg='#f0f0f4'
        )
        errors_label.pack(pady=(10,5))
        
        errors_scrollbar = tk.Scrollbar(results_frame)
        self.texto_errores = tk.Text(
            results_frame, 
            height=15, 
            wrap="word",
            yscrollcommand=errors_scrollbar.set,
            bg='white',
            fg='black'
        )
        errors_scrollbar.pack(side="right", fill="y")
        self.texto_errores.pack(fill="both", expand=True)
        errors_scrollbar.config(command=self.texto_errores.yview)
        
        # Boton de análisis
        boton_respuesta = tk.Button(
            self.ventana, 
            text="Analizar Código", 
            command=self.obtener_respuesta,
            font=('Arial', 12, 'bold'),
            bg='#2ecc71',
            fg='white',
            activebackground='#27ae60',
            relief=tk.FLAT,
            padx=20,
            pady=10
        )
        boton_respuesta.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        
        # Actualizar los números de línea
        self.actualizar_numeros_linea()
    
    def actualizar_numeros_linea(self, event=None):
        """Actualiza los números de línea del área de texto"""
        self.numeros_linea.delete("all")
        i = self.entrada_texto.index("@0,0")
        while True:
            dline = self.entrada_texto.dlineinfo(i)
            if dline is None:
                break
            y = dline[1]
            linea = str(i).split(".")[0]
            self.numeros_linea.create_text(
                30, y, 
                anchor="ne", 
                text=linea, 
                fill="#7f8c8d", 
                font=("Consolas", 8)
            )
            i = self.entrada_texto.index(f"{i}+1line")
    
    def abrir_archivo(self):
        """Abre un archivo PHP desde la carpeta 'algoritmos'"""
        archivo = filedialog.askopenfilename(
            initialdir=self.algoritmos_dir,
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
        """Guarda el contenido del área de texto en un archivo PHP en la carpeta 'algoritmos'"""
        contenido = self.entrada_texto.get("1.0", tk.END).strip()
        
        if not contenido:
            messagebox.showwarning("Advertencia", "No hay contenido para guardar.")
            return
        
        archivo = filedialog.asksaveasfilename(
            initialdir=self.algoritmos_dir,
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
        """Exporta los resultados del análisis a un archivo de texto en la carpeta 'resultados'"""
        respuesta = self.texto_respuesta.get("1.0", tk.END).strip()
        errores = self.texto_errores.get("1.0", tk.END).strip()
        
        if not respuesta and not errores:
            messagebox.showwarning("Advertencia", "No hay resultados para exportar.")
            return
        
        archivo = filedialog.asksaveasfilename(
            initialdir=self.resultados_dir,
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