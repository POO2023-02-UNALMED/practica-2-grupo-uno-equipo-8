import tkinter as tk
from tkinter import FLAT, Menu
from PIL import Image, ImageTk
from tkinter import PhotoImage
from tkinter import messagebox

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
        self.text_hoja_vida.configure(state=tk.DISABLED)

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

        # Nueva configuración de Frames
        for i in range(2):
            tk.Grid.columnconfigure(self.frame_abajo_derecha, i, weight=1)

        for i in range(2):
            tk.Grid.rowconfigure(self.frame_abajo_derecha, i, weight=1)

        # Canvas
        self.canvas_imagen1 = tk.Canvas(self.frame_abajo_derecha, bg="white")
        self.canvas_imagen1.grid(row=0, column=0, sticky="nsew")

        self.canvas_imagen2 = tk.Canvas(self.frame_abajo_derecha, bg="white")
        self.canvas_imagen2.grid(row=0, column=1, sticky="nsew")

        self.canvas_imagen3 = tk.Canvas(self.frame_abajo_derecha, bg="white")
        self.canvas_imagen3.grid(row=1, column=0, sticky="nsew")

        self.canvas_imagen4 = tk.Canvas(self.frame_abajo_derecha, bg="white")
        self.canvas_imagen4.grid(row=1, column=1, sticky="nsew")

        # Rutas de las imágenes asociadas al sistema
        self.rutas_imagenes_desarrollador = [[f"../resources/desarrollador{i}{j}.png" for j in range(1, 5)] for i in range(1, 6)]
        # Lista para almacenar objetos PhotoImage
        self.imagenes_canvas = [[PhotoImage() for _ in range(4)] for _ in range(5)]
        
        # Inicializar el índice actual de las imágenes del desarrollador
        self.indice_desarrollador = 0
        self.indice_hoja_vida = 0
        # Cargar las imágenes en los Canvas
        self.cargar_imagenes_canvas()
        # Evento al cambiar el tamaño de la ventana
        self.master.bind("<Configure>", self.configurar_tamanio_canvas)

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
        imagen_redimensionada = imagen_original.resize((ancho_canvas, 300), Image.Resampling.LANCZOS)
        self.imagenes_sistema[self.indice_imagenes] = ImageTk.PhotoImage(imagen_redimensionada)
        self.canvas_imagen.create_image(0, 0, anchor=tk.NW, image=self.imagenes_sistema[self.indice_imagenes])

    def ingresar_sistema(self):
        self.master.destroy()  # Cerrar la ventana actual
        # Abrir la ventana principal
        """
        app = VentanaPrincipal()
        """

    def salir_aplicacion(self):
        self.master.destroy()

    def cambiar_hoja_vida(self, event):
        self.text_hoja_vida.configure(state=tk.NORMAL)
        # Cambiar la hoja de vida al hacer clic
        self.indice_hoja_vida = (self.indice_hoja_vida + 1) % len(self.menu_hoja_vida)
        self.text_hoja_vida.delete("1.0", tk.END)
        self.text_hoja_vida.insert(tk.END, self.menu_hoja_vida[self.indice_hoja_vida])

        # Cambiar las imágenes del desarrollador
        self.indice_desarrollador = (self.indice_desarrollador + 1) % len(self.rutas_imagenes_desarrollador)
        self.cargar_imagenes_canvas()
        self.configurar_tamanio_canvas(None)
        self.text_hoja_vida.configure(state=tk.DISABLED)

    def mostrar_siguiente_imagen(self, event):
        # Cambiar la imagen al pasar el ratón sobre ella
        self.indice_imagenes = (self.indice_imagenes + 1) % len(self.rutas_imagenes_sistema)
        self.cargar_imagen()

    def cargar_imagen(self):
        ancho_canvas = self.canvas_imagen.winfo_width()
        # Limpiar el canvas
        self.canvas_imagen.delete("all")
        # Cargar la imagen desde la ruta
        imagen_original = Image.open(self.rutas_imagenes_sistema[self.indice_imagenes])
        # Redimensionar la imagen para que llene el canvas
        imagen_redimensionada = imagen_original.resize((ancho_canvas, 300), Image.Resampling.LANCZOS)
        # Convertir la imagen a formato compatible con Tkinter
        self.imagenes_sistema[self.indice_imagenes] = ImageTk.PhotoImage(imagen_redimensionada)
        # Mostrar la imagen en el canvas
        self.canvas_imagen.create_image(0, 0, anchor=tk.NW, image=self.imagenes_sistema[self.indice_imagenes])

    def cargar_imagenes_canvas(self):
        for i, canvas in enumerate([self.canvas_imagen1, self.canvas_imagen2, self.canvas_imagen3, self.canvas_imagen4]):
            ruta_imagen = f"../resources/desarrollador{self.indice_desarrollador+1}{i + 1}.png"
            imagen_original = Image.open(ruta_imagen)
            self.imagenes_canvas[i] = ImageTk.PhotoImage(imagen_original)
            canvas.create_image(0, 0, anchor=tk.NW, image=self.imagenes_canvas[i])

    def configurar_tamanio_canvas(self, event):
        # Redimensionar las imágenes proporcionalmente al tamaño del Canvas
        for i, canvas in enumerate([self.canvas_imagen1, self.canvas_imagen2, self.canvas_imagen3, self.canvas_imagen4]):
            ancho_canvas = canvas.winfo_width()
            alto_canvas = canvas.winfo_height()
            imagen_original = Image.open(f"../resources/desarrollador{self.indice_desarrollador+1}{i + 1}.png")
            imagen_redimensionada = imagen_original.resize((ancho_canvas, alto_canvas), Image.Resampling.LANCZOS)
            self.imagenes_canvas[i] = ImageTk.PhotoImage(imagen_redimensionada)
            canvas.itemconfig(canvas.find_all()[0], image=self.imagenes_canvas[i])  # Actualizar la imagen

    def mostrar_descripcion(self):
        descripcion = "Este proyecto es una aplicación de panadería virtual que permite realizar pedidos " \
                    "en línea de una amplia variedad de productos frescos y deliciosos. La plataforma " \
                    "ofrece una experiencia fácil de usar, desde la selección de productos hasta el pago " \
                    "y la entrega a domicilio. ¡Disfruta de la comodidad de ordenar tus productos de panadería " \
                    "favoritos desde la comodidad de tu hogar!"
        
        # Mostrar el pop-up con la descripción
        messagebox.showinfo("Descripción del Sistema", descripcion)

def main():
    root = tk.Tk()
    app = VentanaInicio(root)
    root.mainloop()

if __name__ == "__main__":
    main()