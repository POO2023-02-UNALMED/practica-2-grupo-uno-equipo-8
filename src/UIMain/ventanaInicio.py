import tkinter as tk
from tkinter import FLAT, Menu
from tkinter import StringVar
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
        self.frame = tk.Frame(master, bd=1, relief=FLAT, padx=1, pady=1, bg="#FCD9EF")
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

        self.frame_arriba_izquierda = tk.Frame(self.frame_izquierda, bg="#DCF7F0")
        self.frame_arriba_izquierda.grid(row=0, column=0, sticky="nsew")

        self.frame_abajo_izquierda = tk.Frame(self.frame_izquierda, bg="blue")
        self.frame_abajo_izquierda.grid(row=1, column=0, sticky="nsew")

        self.frame_arriba_derecha = tk.Frame(self.frame_derecha, bg="green")
        self.frame_arriba_derecha.grid(row=0, column=0, sticky="nsew")

        self.frame_abajo_derecha = tk.Frame(self.frame_derecha, bg="yellow")
        self.frame_abajo_derecha.grid(row=1, column=0, sticky="nsew")

        # Elementos en la parte superior izquierda
        self.label_bienvenida = tk.Label(self.frame_arriba_izquierda, text="¡Bienvenido a POO Bakery!", font=("Arial", 15))
        self.label_bienvenida.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Elementos en la parte superior derecha


        self.text_hoja_vida = tk.Label(self.frame_arriba_derecha, width=40, height=10, anchor="center", cursor="hand1", relief="groove", borderwidth=5, text="Hoja de vida del desarrollador 1\n\nSahely, una joven apasionada por el conocimiento, cumple años un día después de la entrega de este trabajo y espera un gran regalo de cumpleaños.\n\nEstudiosa y encantadora, su amor por el color rosa es evidente en cada aspecto de su vida. Aunque ama la brujería y practica amarres para esparcir alegría, tiene un miedo irracional a las palomas.\n\nCon su cumpleaños cercano, su mayor deseo es triunfar en su proyecto de Programación Orientada a Objetos, una meta que aborda con determinación y energía. Su vida está llena de colores vibrantes, amor por el conocimiento y una determinación inquebrantable para superar sus miedos y alcanzar sus metas.")
        self.text_hoja_vida.pack(expand=True, fill='both', pady=5)
        self.text_hoja_vida.configure(wraplength=380, justify="center")
        self.text_hoja_vida.configure(state=tk.DISABLED)

        # Elementos en la parte inferior izquierda
        self.button_ingreso = tk.Button(self.frame_abajo_izquierda, text="Ingresar al Sistema", command=self.ingresar_sistema, height=3, width=20, font=("Arial", 13))
        self.button_ingreso.pack(side=tk.BOTTOM, pady=40)

        self.indice_imagen_actual = 0
        self.imagenes = [PhotoImage(file=f"../resources/imagen{i+1}.png").subsample(1) for i in range(5)]

        self.label_imagen = tk.Label(self.frame_abajo_izquierda, bg="white", width=400, height=300)
        self.label_imagen.pack(fill='x', expand=True, pady=10, side=tk.BOTTOM)
        self.label_imagen.bind("<Enter>", self.mostrar_siguiente_imagen)

        # Mostrar la primera imagen al inicio
        self.label_imagen.configure(image=self.imagenes[self.indice_imagen_actual])
        self.label_imagen.image = self.imagenes[self.indice_imagen_actual]  # Mantener una referencia a la imagen

        # Inicializar el índice actual de la imagen
        #self.canvas_imagen.bind("<Configure>", self.configurar_ancho_imagen)


        # Nueva configuración de Frames
        for i in range(2):
            tk.Grid.columnconfigure(self.frame_abajo_derecha, i, weight=1)

        for i in range(2):
            tk.Grid.rowconfigure(self.frame_abajo_derecha, i, weight=1)

        # Imágenes
        self.rutas_imagenes_desarrollador = [
            [f"../resources/desarrollador{desarrollador + 1}{i + 1}.png" for i in range(4)] for desarrollador in range(5)
        ]

        # Lista para almacenar objetos PhotoImage
        self.imagenes_desarrollador = [
            [PhotoImage(file=image_path) for image_path in desarrollador_images] for desarrollador_images in self.rutas_imagenes_desarrollador
        ]

        # Labels para mostrar las imágenes
        self.labels_imagenes = [
            [
                tk.Label(self.frame_abajo_derecha, bg="white", image=self.imagenes_desarrollador[desarrollador][i])
                for i in range(4)
            ] for desarrollador in range(5)
        ]

        tamaño_imagenes = (150, 150)  # El tamaño que desees para las imágenes
        # Labels para mostrar las imágenes
        self.label_imagen1 = tk.Label(self.frame_abajo_derecha, bg="white", width=tamaño_imagenes[0], height=tamaño_imagenes[1])
        self.label_imagen1.grid(row=0, column=0, sticky="nsew")

        self.label_imagen2 = tk.Label(self.frame_abajo_derecha, bg="white", width=tamaño_imagenes[0], height=tamaño_imagenes[1])
        self.label_imagen2.grid(row=0, column=1, sticky="nsew")

        self.label_imagen3 = tk.Label(self.frame_abajo_derecha, bg="white", width=tamaño_imagenes[0], height=tamaño_imagenes[1])
        self.label_imagen3.grid(row=1, column=0, sticky="nsew")

        self.label_imagen4 = tk.Label(self.frame_abajo_derecha, bg="white", width=tamaño_imagenes[0], height=tamaño_imagenes[1])
        self.label_imagen4.grid(row=1, column=1, sticky="nsew")

        self.label_imagen1.configure(image=self.imagenes_desarrollador[0][0])
        self.label_imagen2.configure(image=self.imagenes_desarrollador[0][1])
        self.label_imagen3.configure(image=self.imagenes_desarrollador[0][2])
        self.label_imagen4.configure(image=self.imagenes_desarrollador[0][3])

        for i, label in enumerate([self.label_imagen1, self.label_imagen2, self.label_imagen3, self.label_imagen4]):
            imagen = self.imagenes_desarrollador[0][i]  # Utiliza la primera lista de imágenes, correspondiente al primer desarrollador
            imagen_resized = imagen.subsample(3)  # Escala la imagen a la mitad, puedes ajustar este valor según tus necesidades
            label.configure(image=imagen_resized)
            label.image = imagen_resized  # Mantener una referencia a la imagen para evitar que el recolector de basura la elimine

        self.indice_hoja_vida = 0
        # Menú de cambio de hoja de vida
        self.menu_hoja_vida = ["Hoja de vida del desarrollador 1\n\nSahely, una joven apasionada por el conocimiento, cumple años un día después de la entrega de este trabajo y espera un gran regalo de cumpleaños.\n\nEstudiosa y encantadora, su amor por el color rosa es evidente en cada aspecto de su vida. Aunque ama la brujería y practica amarres para esparcir alegría, tiene un miedo irracional a las palomas.\n\nCon su cumpleaños cercano, su mayor deseo es triunfar en su proyecto de Programación Orientada a Objetos, una meta que aborda con determinación y energía. Su vida está llena de colores vibrantes, amor por el conocimiento y una determinación inquebrantable para superar sus miedos y alcanzar sus metas.","Hoja de vida del desarrollador 2\n\nMateo, estudiante de ingeniería de sistemas, destaca por su atractiva apariencia y dedicación al fitness.\n\nFiel asistente del gimnasio, combina su pasión por la tecnología con una perseverancia tranquila, recordando a una tortuga que avanza con determinación.\n\nEste joven busca el equilibrio perfecto entre el desarrollo físico y académico, demostrando que la fuerza y la tenacidad pueden estar envueltas en una apariencia serena.", "Hoja de vida del desarrollador 3\n\nRichard, actualmente estudiante de ciencias de la computación, se sumerge con entusiasmo en el vasto campo de la tecnología\n\nSu aprecio por las manzanas va más allá de la fruta, y se está planteando cambiar a la carrera de ingeniería de sistemas.\n\nAdemás de su compromiso con la informática, Richard destaca como un amigo leal y confiable, siempre dispuesto a apoyar a quienes lo rodean.", "Hoja de vida del desarrollador 4\n\nSamuel, estudiante de ingeniería de sistemas y apasionado del fútbol, encuentra su equilibrio entre el mundo tecnológico y su amor por el deporte.\n\nCon un estilo distintivo, colecciona gorras que reflejan su personalidad única.\n\nAdemás de sus logros académicos, este joven entusiasta está a punto de celebrar su cumpleaños el lunes 20 de noviembre, y su energía contagiosa y amistosa siempre lo convierte en el alma de cualquier reunión.", "Hoja de vida del desarrollador 5\n\nNicolas, dedicado estudiante de ingeniería de sistemas, encuentra inspiración en el genio innovador de Tesla.\n\nSu fascinación por la ciencia y la tecnología se refleja en su admiración por el número 3.\n\nAdemás, el color morado es su preferido, simbolizando su creatividad y espiritualidad.\n\nCon una mente inquisitiva y apasionada, Nicolas busca constantemente la conexión entre la ingeniería y la innovación, creando un espacio donde la ciencia y la creatividad convergen."]
        self.text_hoja_vida.bind("<Button-1>", self.cambiar_hoja_vida)

        # Menú
        self.menu_bar = Menu(self.master,)
        self.master.config(menu=self.menu_bar)
        self.menu_inicio = Menu(self.menu_bar, tearoff=0)
        self.menu_inicio.add_command(label="Salir de la aplicación", command=self.salir_aplicacion, font=("Arial", 10))
        self.menu_inicio.add_command(label="Descripción del sistema", command=self.mostrar_descripcion, font=("Arial", 10))
        self.menu_bar.add_cascade(label="Inicio", menu=self.menu_inicio)

    def ingresar_sistema(self):
        self.master.destroy()  # Cerrar la ventana actual
        # Abrir la ventana principal
        """
        app = VentanaPrincipal()
        """

    def salir_aplicacion(self):
        self.master.destroy()

    def cambiar_hoja_vida(self, event):
        # Cambiar la hoja de vida al hacer clic
        self.indice_hoja_vida = (self.indice_hoja_vida + 1) % len(self.menu_hoja_vida)
        self.texto_anadir = StringVar()
        self.texto_anadir.set(self.menu_hoja_vida[self.indice_hoja_vida])
        self.text_hoja_vida.config(textvariable=self.texto_anadir)
        # Cambiar las imágenes del desarrollador
        # Actualizar imágenes
        # Actualizar las imágenes en los labels
        imagenes_nuevas = self.imagenes_desarrollador[self.indice_hoja_vida]
        for i, label in enumerate([self.label_imagen1, self.label_imagen2, self.label_imagen3, self.label_imagen4]):
            imagen_resized = imagenes_nuevas[i].subsample(3)  # Escala la imagen al tamaño deseado
            label.configure(image=imagen_resized)
            label.image = imagen_resized  # Mantener una referencia a la imagen

        # Actualizar texto de la hoja de vida
        self.texto_anadir.set(self.menu_hoja_vida[self.indice_hoja_vida])

        self.text_hoja_vida.configure(state=tk.DISABLED)

    def mostrar_siguiente_imagen(self, event):
        # Cambiar la imagen al pasar el ratón sobre ella
        self.indice_imagen_actual = (self.indice_imagen_actual + 1) % len(self.imagenes)
        self.label_imagen.configure(image=self.imagenes[self.indice_imagen_actual])
        self.label_imagen.image = self.imagenes[self.indice_imagen_actual]  # Mantener una referencia a la imagen

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