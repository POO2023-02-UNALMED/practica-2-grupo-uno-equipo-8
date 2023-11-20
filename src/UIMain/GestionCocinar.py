import random
import tkinter as tk
from tkinter import ttk
from gestorAplicacion.humanos.Cocinero import Cocinero
import time

from gestorAplicacion.humanos import Catastrofe

class GestionCocinar:
    
    @staticmethod
    def barraProgresoDeTodos(frame_principal):
        listaDeListas = Cocinero.getProcesosDeProductosCocinados()
        fallos = Cocinero.getFallosCocinando()
        print(fallos)
        print(listaDeListas)
        if fallos != 0:
            numero_random = random.randint(0, 4)
            mensaje_fallo = f"Perdón su pedido tartará un poco más porque {Cocinero.fallos_cocina[numero_random]}"
            
            label_fallo = tk.Label(frame_principal, text=mensaje_fallo)
            label_fallo.pack()
            frame_principal.update()
            
            time.sleep(2)
            label_fallo.destroy()
            
            for lista in listaDeListas:
                GestionCocinar.barrasCocinando(lista, len(lista), frame_principal)
        else:
            for lista in listaDeListas:
                GestionCocinar.barrasCocinando(lista, len(lista), frame_principal)
    
    @staticmethod
    def barrasCocinando(proceso_cook, longitud, frame_principal):
        progreso_var = tk.DoubleVar()

        barra_progreso = ttk.Progressbar(frame_principal, variable=progreso_var, length=200, mode="determinate", maximum=longitud)
        barra_progreso.pack(pady=20)

        etiqueta_proceso = tk.Label(frame_principal, text="")
        etiqueta_proceso.pack(pady=5)

        def actualizar_progreso(valor):
            if valor < longitud:
                progreso_var.set(valor)
                etiqueta_proceso.config(text=proceso_cook[valor])
                frame_principal.after(1000, lambda: actualizar_progreso(valor + 1))
            else:
                barra_progreso.destroy()
                etiqueta_proceso.destroy()

        # Inicia la actualización de la barra de progreso
        actualizar_progreso(0)
        
    @staticmethod
    def notaCocina(frameCalificacion):
        valorSeleccionado = frameCalificacion.comboBoxValor.get()
        return valorSeleccionado
        