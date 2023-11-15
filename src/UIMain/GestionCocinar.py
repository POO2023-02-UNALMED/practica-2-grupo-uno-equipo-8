import tkinter as tk
from tkinter import ttk
from gestorAplicacion.humanos.Cocinero import Cocinero
import time

class GestionCocinar:
    
    @staticmethod
    def barraProgresoDeTodos(ventanaPrincipal):
        listaDeListas = Cocinero.getProcesosDeProductosCocinados()
        fallos = Cocinero.getFallosCocinando()
        if fallos != 0:
            print("fallo aleatorio")
            time.sleep(2)
            for lista in listaDeListas:
                GestionCocinar.barrasCocinando(lista, len(lista), ventanaPrincipal)
        else:
            for lista in listaDeListas:
                GestionCocinar.barrasCocinando(lista, len(lista), ventanaPrincipal)
        
    
    @staticmethod
    def barrasCocinando(proceso_cook, longitud, ventana_principal):
        # Crea una variable de control para la barra de progreso
        progreso_var = tk.DoubleVar()

        # Crea la barra de progreso y etiqueta en la ventana principal
        barra_progreso = ttk.Progressbar(ventana_principal, variable=progreso_var, length=200, mode="determinate", maximum=longitud)
        barra_progreso.pack(pady=20)

        etiqueta_proceso = tk.Label(ventana_principal, text="")
        etiqueta_proceso.pack(pady=5)

        # Función para actualizar la barra de progreso y la etiqueta
        def actualizar_progreso(valor):
            if valor < longitud:
                progreso_var.set(valor)
                etiqueta_proceso.config(text=proceso_cook[valor])
                ventana_principal.after(1000, lambda: actualizar_progreso(valor + 1))
            else:
                barra_progreso.destroy()
                etiqueta_proceso.destroy()

        # Inicia la actualización de la barra de progreso
        actualizar_progreso(0)