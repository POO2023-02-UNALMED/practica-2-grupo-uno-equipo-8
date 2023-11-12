import tkinter as tk
from tkinter import FLAT, Menu
from PIL import Image, ImageTk
from tkinter import PhotoImage
import os

# Obtener el directorio del script actual
script_directory = os.path.dirname(os.path.abspath(__file__))

# Cambiar el directorio de trabajo al directorio del script
os.chdir(script_directory)

class VentanaInicio:
    def __init__(self, master):
        self.master = master
        self.master.title("Ventana de Inicio")
        self.master.geometry("1000x800")

        # Crear Frames
        self.frame = tk.Frame(master, bd=1, relief=FLAT, padx=1, pady=1, bg="green")
        self.frame.pack(padx=5, pady=5, fill="both", expand=True)

        # Configuración de la expansión
        tk.Grid.rowconfigure(self.frame, 0, weight=1)
        tk.Grid.rowconfigure(self.frame, 1, weight=1)
        tk.Grid.columnconfigure(self.frame, 0, weight=1)
        tk.Grid.columnconfigure(self.frame, 1, weight=1)

        # Frames
        self.frame_izquierda = tk.Frame(self.frame, bg="gray")
        self.frame_izquierda.grid(row=0, column=0, rowspan=2, padx=2, pady=5, sticky="nsew")
        tk.Grid.rowconfigure(self.frame_izquierda, 0, weight=1)
        tk.Grid.rowconfigure(self.frame_izquierda, 1, weight=3)
        tk.Grid.columnconfigure(self.frame_izquierda, 0, weight=1)

        self.frame_derecha = tk.Frame(self.frame, bg="purple")
        self.frame_derecha.grid(row=0, column=1, rowspan=2, padx=2, pady=5, sticky="nsew")
        tk.Grid.rowconfigure(self.frame_derecha, 0, weight=1)
        tk.Grid.rowconfigure(self.frame_derecha, 1, weight=3)
        tk.Grid.columnconfigure(self.frame_derecha, 0, weight=1)

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
        self.text_hoja_vida.pack(expand=True, fill='both', pady=5)

        # Elementos en la parte inferior izquierda
        self.button_ingreso = tk.Button(self.frame_abajo_izquierda, text="Ingresar al Sistema", command=self.ingresar_sistema, height=3, width=20, font=("Arial", 13))
        self.button_ingreso.pack(side=tk.BOTTOM, pady=40)

        # Canvas para mostrar la imagen
        self.canvas_imagen = tk.Canvas(self.frame_abajo_izquierda, bg="white", width=400, height=300)
        self.canvas_imagen.pack(fill='x', expand=True, pady=10, side=tk.BOTTOM)
        # Evento al cambiar el tamaño del Canvas
        

        # Rutas de las imágenes asociadas al sistema
        self.rutas_imagenes_sistema = [f"../resources/imagen{i}.png" for i in range(1, 6)]
        # Lista para almacenar objetos PhotoImage
        self.imagenes_sistema = [PhotoImage() for _ in range(5)]

        # Inicializar el índice actual de la imagen
        self.indice_imagenes = 0

        # Cargar la imagen inicial
        self.cargar_imagen()
        self.canvas_imagen.bind("<Configure>", self.configurar_ancho_imagen)

        # Evento al pasar el ratón sobre el canvas_imagen
        self.canvas_imagen.bind("<Enter>", self.mostrar_siguiente_imagen)

        # Canvas para mostrar las imágenes del desarrollador
        self.canvas_imagenes = tk.Canvas(self.frame_abajo_derecha, bg="white", width=400, height=200)
        self.canvas_imagenes.pack(expand=True, fill='both', pady=10)

        # Rutas de las imágenes asociadas al sistema
        self.rutas_imagenes_desarrollador = [f"../resources/desarrollador{j}{i}.png" for i in range(1, 5) for j in range(1, 6)]
        # Lista para almacenar objetos PhotoImage
        self.imagenes_desarrollador = [PhotoImage() for _ in range(4)]

        # Inicializar el índice actual de las imágenes del desarrollador
        self.indice_imagenes_desarrollador = 0
        self.indice_hoja_vida = 0

        # Cargar las imágenes iniciales del desarrollador
        self.cargar_imagenes_desarrollador()

        # Menú de cambio de hoja de vida
        self.menu_hoja_vida = ["Hoja de vida del desarrollador 1\n\n[Detalles del desarrollador 1]", "Hoja de vida del desarrollador 2\n\n[Detalles del desarrollador 2]", "Hoja de vida del desarrollador 3\n\n[Detalles del desarrollador 3]", "Hoja de vida del desarrollador 4\n\n[Detalles del desarrollador 4]", "Hoja de vida del desarrollador 5\n\n[Detalles del desarrollador 5]"]
        self.text_hoja_vida.bind("<Button-1>", self.cambiar_hoja_vida)

        # Menú
        self.menu_bar = Menu(self.master,)
        self.master.config(menu=self.menu_bar)
        self.menu_inicio = Menu(self.menu_bar, tearoff=0)
        self.menu_inicio.add_command(label="Salir de la aplicación", command=self.salir_aplicacion, font=("Arial", 10))
        self.menu_inicio.add_command(label="Descripción del sistema", command=self.mostrar_descripcion, font=("Arial", 10))
        self.menu_bar.add_cascade(label="Inicio", menu=self.menu_inicio)

    def configurar_ancho_imagen(self, event):
        # Obtener el ancho del Canvas
        ancho_canvas = self.canvas_imagen.winfo_width()
        self.canvas_imagen.delete("all")
        imagen_original = Image.open(self.rutas_imagenes_sistema[self.indice_imagenes])
        imagen_redimensionada = imagen_original.resize((ancho_canvas, 300), Image.ANTIALIAS)
        self.imagenes_sistema[self.indice_imagenes] = ImageTk.PhotoImage(imagen_redimensionada)
        self.canvas_imagen.create_image(0, 0, anchor=tk.NW, image=self.imagenes_sistema[self.indice_imagenes])

    def ingresar_sistema(self):
        # Aquí puedes manejar el evento de ingreso al sistema
        print("Ingresando al sistema")

    def salir_aplicacion(self):
        self.master.destroy()

    def cambiar_imagenes_desarrollador(self, event):
        # Cambiar las imágenes del desarrollador al hacer clic
        self.indice_imagenes_desarrollador = (self.indice_imagenes_desarrollador + 1) % len(self.rutas_imagenes_desarrollador)
        self.cargar_imagenes_desarrollador()

    def cambiar_hoja_vida(self, event):
        # Cambiar la hoja de vida al hacer clic
        self.indice_hoja_vida = (self.indice_hoja_vida + 1) % len(self.menu_hoja_vida)
        self.text_hoja_vida.delete("1.0", tk.END)
        self.text_hoja_vida.insert(tk.END, self.menu_hoja_vida[self.indice_hoja_vida])

    def mostrar_siguiente_imagen(self, event):
        # Cambiar la imagen al pasar el ratón sobre ella
        self.indice_imagenes = (self.indice_imagenes + 1) % len(self.rutas_imagenes_sistema)
        self.cargar_imagen()

    def cargar_imagenes_desarrollador(self):
        # Limpiar el canvas
        self.canvas_imagenes.delete("all")
        # Cargar las imágenes desde las rutas
        for i, ruta in enumerate(self.rutas_imagenes_desarrollador):
            imagen_original = Image.open(ruta)
            # Redimensionar la imagen para que llene el canvas
            imagen_redimensionada = imagen_original.resize((100, 100), Image.ANTIALIAS)
            # Convertir la imagen a formato compatible con Tkinter
            self.imagenes_desarrollador[i] = ImageTk.PhotoImage(imagen_redimensionada)
            # Mostrar la imagen en el canvas
            self.canvas_imagenes.create_image(100 * i, 0, anchor=tk.NW, image=self.imagenes_desarrollador[i])

    def cargar_imagen(self):
        ancho_canvas = self.canvas_imagen.winfo_width()
        # Limpiar el canvas
        self.canvas_imagen.delete("all")
        # Cargar la imagen desde la ruta
        imagen_original = Image.open(self.rutas_imagenes_sistema[self.indice_imagenes])
        # Redimensionar la imagen para que llene el canvas
        imagen_redimensionada = imagen_original.resize((ancho_canvas, 300), Image.ANTIALIAS)
        # Convertir la imagen a formato compatible con Tkinter
        self.imagenes_sistema[self.indice_imagenes] = ImageTk.PhotoImage(imagen_redimensionada)
        # Mostrar la imagen en el canvas
        self.canvas_imagen.create_image(0, 0, anchor=tk.NW, image=self.imagenes_sistema[self.indice_imagenes])

    def mostrar_descripcion(self):
        # Aquí puedes mostrar una breve descripción del sistema en algún lugar de la ventana
        print("Mostrando descripción del sistema")

def main():
    root = tk.Tk()
    app = VentanaInicio(root)
    root.mainloop()

if __name__ == "__main__":
    main()