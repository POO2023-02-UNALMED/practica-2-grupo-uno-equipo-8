import tkinter as tk
import os

# Obtener el directorio del script actual
script_directory = os.path.dirname(os.path.abspath(__file__))

# Cambiar el directorio de trabajo al directorio del script
os.chdir(script_directory)

class VentanaInicio:
    def __init__(self, master):
        self.master = master
        self.master.title("Ventana de Inicio")

        #Frames
        self.frame_izquierda = tk.Frame(self.master)
        self.frame_izquierda.grid(row=0, column=0, rowspan=2, padx=10, pady=10)
        self.frame_derecha = tk.Frame(self.master)
        self.frame_derecha.grid(row=0, column=1, rowspan=2, padx=10, pady=10)

        self.frame_arriba_izquierda = tk.Frame(self.frame_izquierda)
        self.frame_arriba_izquierda.grid(row=0, column=0)

        self.frame_abajo_izquierda = tk.Frame(self.frame_izquierda)
        self.frame_abajo_izquierda.grid(row=1, column=0)

        self.frame_arriba_derecha = tk.Frame(self.frame_derecha)
        self.frame_arriba_derecha.grid(row=0, column=0)

        self.frame_abajo_derecha = tk.Frame(self.frame_derecha)
        self.frame_abajo_derecha.grid(row=1, column=0)

        # Elementos en la parte superior izquierda
        self.label_bienvenida = tk.Label(self.frame_arriba_izquierda, text="¡Bienvenido al POO Bakery!")
        self.label_bienvenida.pack(anchor='w')

        # Elementos en la parte superior derecha
        self.text_hoja_vida = tk.Text(self.frame_arriba_derecha, wrap=tk.WORD, width=40, height=10)
        self.text_hoja_vida.insert(tk.END, "Hoja de vida del desarrollador 1\n\n[Detalles del desarrollador 1]")
        self.text_hoja_vida.pack()

        # Elementos en la parte inferior izquierda
        self.button_ingreso = tk.Button(self.frame_abajo_izquierda, text="Ingresar al Sistema", command=self.ingresar_sistema)
        self.button_ingreso.pack()

        imagen_path = f"../resources/imagen_desarrollador1.png"
        print("Ruta completa de la imagen:", os.path.abspath(imagen_path))
        self.imagenes_desarrolladores = [tk.PhotoImage(file=imagen_path) for i in range(1, 6)]


        # Elementos en la parte inferior derecha (contenedor de imágenes)
        self.imagenes_desarrolladores = [tk.PhotoImage(file=f"../resources/imagen_desarrollador{i}.png") for i in range(1, 6)]
        self.label_imagen = tk.Label(self.frame_abajo_derecha, image=self.imagenes_desarrolladores[0])
        self.label_imagen.pack()

        # Asociar evento al pasar el ratón sobre la imagen
        self.label_imagen.bind("<Enter>", self.cambiar_imagen)

        # Inicializar el índice actual de la hoja de vida e imagen
        self.indice_hoja_vida = 0
        self.indice_imagen = 0

        # Menú de cambio de hoja de vida
        self.menu_hoja_vida = ["Hoja de vida del desarrollador 1\n\n[Detalles del desarrollador 1]","Hoja de vida del desarrollador 2\n\n[Detalles del desarrollador 2]","Hoja de vida del desarrollador 3\n\n[Detalles del desarrollador 3]","Hoja de vida del desarrollador 4\n\n[Detalles del desarrollador 4]","Hoja de vida del desarrollador 5\n\n[Detalles del desarrollador 5]"]

        self.text_hoja_vida.bind("<Button-1>", self.cambiar_hoja_vida)

    def ingresar_sistema(self):
        # Aquí puedes manejar el evento de ingreso al sistema
        print("Ingresando al sistema")

    def cambiar_hoja_vida(self, event):
        # Cambiar la hoja de vida al hacer clic
        self.indice_hoja_vida = (self.indice_hoja_vida + 1) % len(self.menu_hoja_vida)
        self.text_hoja_vida.delete("1.0", tk.END)
        self.text_hoja_vida.insert(tk.END, self.menu_hoja_vida[self.indice_hoja_vida])

    def cambiar_imagen(self, event):
        # Cambiar la imagen al pasar el ratón sobre ella
        self.indice_imagen = (self.indice_imagen + 1) % len(self.imagenes_desarrolladores)
        self.label_imagen.configure(image=self.imagenes_desarrolladores[self.indice_imagen])

def main():
    root = tk.Tk()
    app = VentanaInicio(root)
    root.mainloop()

if __name__ == "__main__":
    main()
