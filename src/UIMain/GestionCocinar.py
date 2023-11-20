from random import Random
import tkinter as tk
from tkinter import ttk
from gestorAplicacion.humanos.Cocinero import Cocinero
import time

from gestorAplicacion.humanos import Catastrofe

class GestionCocinar:
    
    @staticmethod
    def barraProgresoDeTodos(ventanaPrincipal):
        listaDeListas = Cocinero.getProcesosDeProductosCocinados()
        fallos = Cocinero.getFallosCocinando()
        if fallos != 0:
            numero_random = Random.randint(0, 4)
            mensaje_fallo = "Perdón su pedido tartará un poco más porque" , Catastrofe.fallos_cocina[numero_random]
            # Crear un widget Label para mostrar el mensaje de fallo en el field frame ventanaPrincipal
            label_fallo = tk.Label(ventanaPrincipal, text=mensaje_fallo)
            label_fallo.pack()  # Agregar el widget Label al field frame ventanaPrincipal
            ventanaPrincipal.update()  # Actualizar la ventana para que se muestre el mensaje
            
            time.sleep(2)
            label_fallo.destroy()  # Eliminar el mensaje de fallo después de 2 segundos
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
        
    @staticmethod
    def notaCocina(frameCalificacion):
        valorSeleccionado = frameCalificacion.comboBoxValor.get()
        return valorSeleccionado
        