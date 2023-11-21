from operator import attrgetter
from gestorAplicacion.comida import Ingrediente
from gestorAplicacion.comida import Producto
import tkinter as tk

def ordenarCocinerosPorRanking(panaderia):
    cocineros_ordenados = sorted(panaderia.getCocineros(), key=attrgetter('calificacion'), reverse=True)
    return cocineros_ordenados

def ordenarDomiciliariosPorRanking(panaderia):
    domiciliarios_ordenados = sorted(panaderia.getDomiciliarios(), key=attrgetter('calificacion'), reverse=True)
    return domiciliarios_ordenados

def ordenarIngredientesPorVecesVendidos(panderia):
    ingredientes_ordenados = sorted(panderia.getListaIngredientes(), key=attrgetter('vecesVendido'), reverse=True)
    return ingredientes_ordenados

def ordenarProductosPorVecesVendidos(panaderia):
    productos_ordenados = sorted(panaderia.getListaProductos(), key=attrgetter('vecesVendido'), reverse=True)
    return productos_ordenados

def imprimirCocinerosPorRanking(text, panaderia):
    cocineros_ordenados = ordenarCocinerosPorRanking(panaderia)
        
    for cocinero in cocineros_ordenados:
        text.config(state=tk.NORMAL)
        text.insert(tk.END, cocinero.getNombre() + " " + "- Calificación:" + " " + str(cocinero.getCalificacion()) +"\n")
        text.config(state=tk.DISABLED)
        text.tag_configure("center", justify="center")
        text.tag_add("center", "1.0", "end")

def imprimirDomiciliariosPorRanking(text, panaderia):
    domiciliarios_ordenados = ordenarDomiciliariosPorRanking(panaderia)

    for domiciliario in domiciliarios_ordenados:
        text.config(state=tk.NORMAL)
        text.insert(tk.END, domiciliario.getNombre() + " " + "- Calificación:" + " " + str(domiciliario.getCalificacion()) +"\n")
        text.config(state=tk.DISABLED)
        text.tag_configure("center", justify="center")
        text.tag_add("center", "1.0", "end")

def imprimirIngredientesPorVecesVendidos(text, panaderia):
    ingredientes_ordenados = ordenarIngredientesPorVecesVendidos(panaderia)
    
    for ingrediente in ingredientes_ordenados:
        text.config(state=tk.NORMAL)
        text.insert(tk.END, ingrediente.getNombre() + " " + "- Calificación:" + " " + str(ingrediente.getCalificacion()) +"\n")
        text.config(state=tk.DISABLED)
        text.tag_configure("center", justify="center")
        text.tag_add("center", "1.0", "end")   

def imprimirProductosPorVecesVendidos(text, panaderia):
    productos_ordenados = ordenarProductosPorVecesVendidos(panaderia)

    for producto in productos_ordenados:
        text.config(state=tk.NORMAL)
        text.insert(tk.END, producto.getNombre() + " " + "- Calificación:" + " " + str(producto.getCalificacion()) +"\n")
        text.config(state=tk.DISABLED)
        text.tag_configure("center", justify="center")
        text.tag_add("center", "1.0", "end")