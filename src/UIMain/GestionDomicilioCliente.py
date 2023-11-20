import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from time import sleep

class GestionDomicilioClienteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión Domicilio Cliente")

        # Configuración para centrar la ventana en la pantalla
        window_width = 300
        window_height = 200
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_pos = (screen_width // 2) - (window_width // 2)
        y_pos = (screen_height // 2) - (window_height // 2)
        self.root.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")

        self.frame = ttk.Frame(root)
        self.frame.pack(padx=20, pady=20)

        # Botón para iniciar la simulación de barras de domicilio
        self.barras_button = ttk.Button(self.frame, text="Simular Barras Domicilio", command=self.simular_barras_domicilio)
        self.barras_button.pack(pady=10)

        # Variable para controlar la habilitación de la barra de calificación
        self.calificacion_var = tk.IntVar()
        self.calificacion_bar = ttk.Scale(self.frame, from_=1, to=5, orient=tk.HORIZONTAL, variable=self.calificacion_var, state='disabled')
        self.calificacion_bar.pack(pady=10)

        # Botón para enviar canastas a facturar
        self.facturar_button = ttk.Button(self.frame, text="Enviar Canastas a Facturar", command=self.enviar_canastas_a_facturar)
        self.facturar_button.pack(pady=10)

        # Botón para pedir calificación
        self.calificacion_button = ttk.Button(self.frame, text="Calificar Domiciliario", command=self.pedir_calificacion)
        self.calificacion_button.pack(pady=10)

        # Botón para mostrar estado de domicilio
        self.estado_button = ttk.Button(self.frame, text="Mostrar Estado Domicilio", command=self.mostrar_estado_domicilio)
        self.estado_button.pack(pady=10)

    def simular_barras_domicilio(self):
        self.barras_domicilio()
        # Una vez completado el domicilio, habilitar la barra de calificación
        self.calificacion_bar['state'] = 'normal'

    def enviar_canastas_a_facturar(self):
        respuesta = self.enviar_canastas_a_facturar_dialog()
        if respuesta:
            print("Canastas enviadas a facturar")
        else:
            print("Operación cancelada")

    def pedir_calificacion(self):
        calificacion = self.pedir_calificacion_dialog()
        print(f"Calificación ingresada: {calificacion}")

    def mostrar_estado_domicilio(self):
        estado = True  # Puedes cambiar esto según el resultado deseado
        self.estado_domicilio(estado)

    @staticmethod
    def barras_domicilio():
        proceso_entrega = ["Recibiendo pedido", "En camino", "Entrega completada"]
        etapas = len(proceso_entrega)
        progreso = 0

        while progreso < etapas:
            # Simula el progreso de cada etapa.
            sleep(1)

            # Calcula el porcentaje de progreso.
            porcentaje = ((progreso + 1.0) / etapas) * 100

            # Muestra el progreso actual.
            etapa_actual = proceso_entrega[progreso]
            print(f"{porcentaje:.1f}%  [#{'#' * (progreso * 10)}] 100%")
            print(f"Proceso de {etapa_actual} completado")

            progreso += 1

        # Comprueba si la entrega se realizó con éxito.
        if progreso == etapas:
            print("¡Entrega a domicilio realizada con éxito!")
        else:
            print("La entrega a domicilio no se pudo completar.")

    def enviar_canastas_a_facturar_dialog(self):
        respuesta = tk.messagebox.askquestion("Enviar Canastas a Facturar", "¿Desea enviar la canasta a facturar?")
        return respuesta == "yes"

    @staticmethod
    def pedir_calificacion_dialog():
        numero = 0
        while True:
            eleccion = tk.simpledialog.askstring("Pedir Calificación", "Ingrese un número del 1 al 5 para calificar a su domiciliario:")
            if eleccion in ["1", "2", "3", "4", "5"]:
                numero = int(eleccion)
                break
            elif eleccion is None:
                break
            else:
                tk.messagebox.showwarning("Valor Inválido", "Ingrese un valor válido (1 al 5)")
        return numero

    @staticmethod
    def estado_domicilio(estado):
        if estado:
            tk.messagebox.showinfo("Estado Domicilio", "El domicilio se ha realizado con éxito")
        else:
            tk.messagebox.showinfo("Estado Domicilio", "El domicilio no se ha podido realizar\nYa te enviaremos tu domicilio")

if __name__ == "__main__":
    root = tk.Tk()
    app = GestionDomicilioClienteApp(root)
    root.mainloop()
