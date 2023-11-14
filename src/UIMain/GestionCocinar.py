import tkinter as tk
from tkinter import ttk

class GestionCocinar:
    @staticmethod
    def barrasCocinando(proceso_cook, longitud, ventana_principal):
        # Oculta la ventana principal al inicio
        ventana_principal.withdraw()

        # Crea la ventana de progreso
        ventana = tk.Toplevel()
        ventana.title("Proceso de Cocina")

        barra_progreso = ttk.Progressbar(ventana, length=200, mode="determinate", maximum=longitud)
        barra_progreso.pack(pady=20)

        etiqueta_proceso = tk.Label(ventana, text="")
        etiqueta_proceso.pack(pady=5)

        # Función para actualizar la barra de progreso y la etiqueta
        def actualizar_progreso(valor):
            if valor < longitud:
                barra_progreso['value'] = valor
                etiqueta_proceso.config(text=proceso_cook[valor])
                ventana.after(1000, lambda: actualizar_progreso(valor + 1))
            else:
                ventana.destroy()
                ventana_principal.deiconify()  # Mostramos la ventana principal al finalizar

        # Inicia la actualización de la barra de progreso
        actualizar_progreso(0)

        ventana.mainloop()