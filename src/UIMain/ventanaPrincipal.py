import tkinter as tk
from tkinter import ttk, messagebox

class FieldFrame(tk.Frame):
    def __init__(self, parent, titulo_criterios, criterios, titulo_valores, valores, habilitado):
        super().__init__(parent)

        # Crear etiquetas y cuadros de texto dinámicamente
        for i, criterio in enumerate(criterios):
            label = tk.Label(self, text=f"{titulo_criterios} {criterio}:")
            label.grid(row=i, column=0, sticky="e", padx=5, pady=5)

            entry = tk.Entry(self, state='normal' if habilitado is None or habilitado[i] else 'disabled')
            entry.insert(tk.END, '' if valores is None else valores[i])
            entry.grid(row=i, column=1, sticky="w", padx=5, pady=5)

        # Botones Aceptar y Borrar
        self.boton_aceptar = tk.Button(self, text="Aceptar", command=self.aceptar)
        self.boton_aceptar.grid(row=len(criterios), column=0, columnspan=2, pady=10)

        self.boton_borrar = tk.Button(self, text="Borrar", command=self.borrar)
        self.boton_borrar.grid(row=len(criterios) + 1, column=0, columnspan=2)

    def aceptar(self):
        # Validar que todos los campos tengan un valor
        for widget in self.winfo_children():
            if isinstance(widget, tk.Entry) and not widget.get():
                messagebox.showwarning("Campos Vacíos", "Todos los campos deben tener un valor.")
                return

        # Obtener los valores ingresados
        valores = [widget.get() for widget in self.winfo_children() if isinstance(widget, tk.Entry)]

        # Aquí puedes realizar la lógica necesaria con los valores ingresados

        # Limpiar los campos después de procesar
        for widget in self.winfo_children():
            if isinstance(widget, tk.Entry):
                widget.delete(0, tk.END)

    def borrar(self):
        # Borrar los valores de los campos
        for widget in self.winfo_children():
            if isinstance(widget, tk.Entry):
                widget.delete(0, tk.END)

class VentanaPrincipal(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)

        self.title("Ventana Principal")
        self.geometry("800x600")

        # Crear frames
        self.frame_titulo = tk.Frame(self, bg="red", height=50)
        self.frame_titulo.pack(fill="x")

        self.frame_menu = tk.Frame(self, bg="blue", height=30)
        self.frame_menu.pack(fill="x")

        self.frame_interaccion = tk.Frame(self, bg="green")
        self.frame_interaccion.pack(fill="both", expand=True)

        # Configuración de expansión
        tk.Grid.rowconfigure(self, 2, weight=1)
        tk.Grid.columnconfigure(self.frame_interaccion, 0, weight=1)

        # Menú superior
        self.menu_principal = tk.Menu(self)

        menu_archivo = tk.Menu(self.menu_principal, tearoff=0)
        menu_archivo.add_command(label="Aplicación", command=self.mostrar_info)
        menu_archivo.add_command(label="Salir", command=self.salir)
        self.menu_principal.add_cascade(label="Archivo", menu=menu_archivo)

        menu_procesos = tk.Menu(self.menu_principal, tearoff=0)
        # Agregar procesos y consultas a menu_procesos
        # ...
        self.menu_principal.add_cascade(label="Procesos y Consultas", menu=menu_procesos)

        menu_ayuda = tk.Menu(self.menu_principal, tearoff=0)
        menu_ayuda.add_command(label="Acerca de", command=self.mostrar_autores)
        self.menu_principal.add_cascade(label="Ayuda", menu=menu_ayuda)

        self.config(menu=self.menu_principal)

        # Zona de interacción usuario
        self.text_resultados = tk.Text(self.frame_interaccion, wrap=tk.WORD)
        self.text_resultados.pack(fill="both", expand=True)

        # Mostrar la interfaz de inicio
        self.mostrar_interfaz_inicio()

    def mostrar_interfaz_inicio(self):
        # Aquí puedes mostrar una interfaz de inicio formativa para el usuario
        texto_inicio = """
        Bienvenido a la aplicación. Aquí puedes encontrar información sobre ...
        Para comenzar, selecciona una opción del menú superior.
        """
        self.text_resultados.delete(1.0, tk.END)
        self.text_resultados.insert(tk.END, texto_inicio)

    def mostrar_info(self):
        # Aquí puedes mostrar información detallada sobre la aplicación
        pass

    def mostrar_autores(self):
        # Aquí puedes mostrar información sobre los autores de la aplicación
        pass

    def salir(self):
        self.destroy()

class VentanaInicioSesion(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)

        self.title("Inicio de Sesión")
        self.geometry("400x200")

        # Elementos en la ventana de inicio de sesión
        self.label_usuario = tk.Label(self, text="Usuario:")
        self.label_usuario.pack(pady=10)

        self.entry_usuario = tk.Entry(self)
        self.entry_usuario.pack(pady=10)

        self.label_contrasena = tk.Label(self, text="Contraseña:")
        self.label_contrasena.pack(pady=10)

        self.entry_contrasena = tk.Entry(self, show="*")
        self.entry_contrasena.pack(pady=10)

        self.boton_iniciar_sesion = tk.Button(self, text="Iniciar Sesión", command=self.iniciar_sesion)
        self.boton_iniciar_sesion.pack(pady=10)

    def iniciar_sesion(self):
        # Aquí puedes agregar la lógica de inicio de sesión
        # Por ahora, simplemente abre la VentanaPrincipal
        self.withdraw()  # Oculta la ventana de inicio de sesión
        ventana_principal = VentanaPrincipal(self)
        ventana_principal.grab_set()  # Bloquea eventos en otras ventanas mientras esta esté abierta
        ventana_principal.wait_window()  # Espera a que se cierre la VentanaPrincipal
        self.destroy()  # Destruye la ventana de inicio de sesión cuando se cierra la VentanaPrincipal

if __name__ == "__main__":
    app = VentanaInicioSesion()
    app.mainloop()
