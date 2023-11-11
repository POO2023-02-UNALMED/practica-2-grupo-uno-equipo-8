import tkinter as tk
from tkinter import FLAT
from tkinter import Menu
import os

# Obtener el directorio del script actual
script_directory = os.path.dirname(os.path.abspath(__file__))

# Cambiar el directorio de trabajo al directorio del script
os.chdir(script_directory)

class VentanaInicio:
    def __init__(self, master):
        self.master = master
        self.master.title("Ventana de Inicio")

        # Crear Frames
        self.frame = tk.Frame(master, bd=1, relief=FLAT, padx=1, pady=1, bg="green")
        self.frame.pack(padx=5, pady=5, fill="both", expand=True)
        tk.Grid.rowconfigure(self.frame, 0, weight=1)
        tk.Grid.rowconfigure(self.frame, 1, weight=2)
        tk.Grid.columnconfigure(self.frame, 0, weight=1)
        tk.Grid.columnconfigure(self.frame, 1, weight=1)

        # Frames
        self.frame_izquierda = tk.Frame(self.frame, bg="gray")
        self.frame_izquierda.grid(row=0, column=0, rowspan=2, padx=10, pady=10, sticky="nsew")
        tk.Grid.rowconfigure(self.frame_izquierda, 1, weight=1)  
        self.frame_derecha = tk.Frame(self.frame, bg="purple")
        self.frame_derecha.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")

        self.frame_arriba_izquierda = tk.Frame(self.frame_izquierda, bg="red")
        self.frame_arriba_izquierda.grid(row=0, column=0, sticky="nsew")

        self.frame_abajo_izquierda = tk.Frame(self.frame_izquierda, bg="blue")
        self.frame_abajo_izquierda.grid(row=1, column=0, sticky="nsew")

        self.frame_arriba_derecha = tk.Frame(self.frame_derecha, bg="green")
        self.frame_arriba_derecha.grid(row=0, column=0, sticky="nsew")

        self.frame_abajo_derecha = tk.Frame(self.frame_derecha, bg="yellow")
        self.frame_abajo_derecha.grid(row=1, column=0, sticky="nsew")

        # Elementos en la parte superior izquierda
        self.label_bienvenida = tk.Label(self.frame_arriba_izquierda, text="¡Bienvenido a POO Bakery!", font=("Arial", 15))
        self.label_bienvenida.pack(pady=10)

        # Elementos en la parte superior derecha
        self.text_hoja_vida = tk.Text(self.frame_arriba_derecha, wrap=tk.WORD, width=40, height=10)
        self.text_hoja_vida.insert(tk.END, "Hoja de vida del desarrollador 1\n\n[Detalles del desarrollador 1]")
        self.text_hoja_vida.pack(side=tk.BOTTOM, pady=10)

        # Elementos en la parte inferior izquierda
        self.button_ingreso = tk.Button(self.frame_abajo_izquierda, text="Ingresar al Sistema", command=self.ingresar_sistema)
        self.button_ingreso.pack(side=tk.BOTTOM, pady=10)

        # Widget para mostrar las imágenes
        self.label_imagenes = tk.Label(self.frame_abajo_izquierda, image=self.imagenes_sistema[0])
        self.label_imagenes.pack(pady=10)

        # Evento al pasar el ratón sobre el label_imagenes
        self.label_imagenes.bind("<Enter>", self.mostrar_siguiente_imagen)

        # Inicializar el índice actual de la imagen
        self.indice_imagenes = 0

        # Elementos en la parte inferior derecha (contenedor de imágenes)
        self.canvas_imagenes = tk.Canvas(self.frame_abajo_derecha, width=200, height=150)
        self.canvas_imagenes.pack()

        # Asociar evento al pasar el ratón sobre el canvas
        # self.canvas_imagenes.bind("<Enter>", self.cambiar_imagen)

        # Inicializar el índice actual de la hoja de vida e imagen
        self.indice_hoja_vida = 0
        self.indice_imagen = 0

        # Menú de cambio de hoja de vida
        self.menu_hoja_vida = ["Hoja de vida del desarrollador 1\n\n[Detalles del desarrollador 1]", "Hoja de vida del desarrollador 2\n\n[Detalles del desarrollador 2]","Hoja de vida del desarrollador 3\n\n[Detalles del desarrollador 3]","Hoja de vida del desarrollador 4\n\n[Detalles del desarrollador 4]","Hoja de vida del desarrollador 5\n\n[Detalles del desarrollador 5]"]

        self.text_hoja_vida.bind("<Button-1>", self.cambiar_hoja_vida)

        # Menú
        self.menu_bar = Menu(self.master)
        self.master.config(menu=self.menu_bar)
        self.menu_inicio = Menu(self.menu_bar, tearoff=0)
        self.menu_inicio.add_command(label="Salir de la aplicación", command=self.salir_aplicacion)
        self.menu_inicio.add_command(label="Descripción del sistema", command=self.mostrar_descripcion)
        self.menu_bar.add_cascade(label="Inicio", menu=self.menu_inicio)

    def ingresar_sistema(self):
        # Aquí puedes manejar el evento de ingreso al sistema
        print("Ingresando al sistema")

    def salir_aplicacion(self):
        self.master.destroy()

    def cambiar_hoja_vida(self, event):
        # Cambiar la hoja de vida al hacer clic
        self.indice_hoja_vida = (self.indice_hoja_vida + 1) % len(self.menu_hoja_vida)
        self.text_hoja_vida.delete("1.0", tk.END)
        self.text_hoja_vida.insert(tk.END, self.menu_hoja_vida[self.indice_hoja_vida])

    def cambiar_imagen(self, event):
        # Cambiar la imagen al pasar el ratón sobre ella
        self.indice_imagen = (self.indice_imagen + 1) % len(self.imagenes_desarrolladores)
        self.label_imagen.configure(image=self.imagenes_desarrolladores[self.indice_imagen])

    def mostrar_descripcion(self):
        # Aquí puedes mostrar una breve descripción del sistema en algún lugar de la ventana
        print("Mostrando descripción del sistema")

def main():
    root = tk.Tk()
    app = VentanaInicio(root)
    root.mainloop()

if __name__ == "__main__":
    main()
