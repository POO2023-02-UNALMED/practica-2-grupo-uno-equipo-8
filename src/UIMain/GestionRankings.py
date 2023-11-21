from operator import attrgetter
from gestorAplicacion.comida.Ingrediente import Ingrediente
from gestorAplicacion.comida.Producto import Producto
import tkinter as tk
from tkinter import messagebox
from UIMain.ErrorAplicacion import CamposVaciosError
from UIMain.ErrorAplicacion import CantidadInvalidaError
from UIMain.ErrorAplicacion import ProductoNoEncontradoError
from UIMain.ErrorAplicacion import UsuarioNoEncontradoError
from UIMain.ErrorAplicacion import usuarioExistenteError

def ordenarCocinerosPorRanking(panaderia):
    try:
        if panaderia.getCocineros() == []:
            raise ProductoNoEncontradoError(panaderia.getCocineros())
        else:
            cocineros_ordenados = sorted(panaderia.getCocineros(), key=attrgetter('calificacion'), reverse=True)
            return cocineros_ordenados
    
    except ProductoNoEncontradoError as e:
        messagebox.showinfo("Info", "Lamentamos los inconvenientes pero este ranking no se encuentra disponible")
        return []

def ordenarDomiciliariosPorRanking(panaderia):
    try:
        if panaderia.getDomiciliarios() == []:
            raise ProductoNoEncontradoError(panaderia.getDomiciliarios())
        else:
            domiciliarios_ordenados = sorted(panaderia.getDomiciliarios(), key=lambda x: x.calificacion if x.calificacion is not None else 0, reverse=True)
            return domiciliarios_ordenados
    
    except ProductoNoEncontradoError as e:
        messagebox.showinfo("Info", "Lamentamos los inconvenientes pero este ranking no se encuentra disponible")
        return []

def ordenarIngredientesPorVecesVendidos(panderia):
    try:
        if Ingrediente.getBaseDatosIngredientes() == []:
            raise ProductoNoEncontradoError(Ingrediente.getBaseDatosIngredientes())
        else:
            ingredientes_ordenados = sorted(Ingrediente.getBaseDatosIngredientes(), key=attrgetter('_vecesVendido'), reverse=True)
            return ingredientes_ordenados
        
    except ProductoNoEncontradoError as e:
        messagebox.showinfo("Info", "Lamentamos los inconvenientes pero este ranking no se encuentra disponible")
        return []

def ordenarProductosPorVecesVendidos(panaderia):
    try:
        if Producto.baseDatosProductos == []:
            raise ProductoNoEncontradoError(Producto.baseDatosProductos)
        else:
            productos_ordenados = sorted(Producto.baseDatosProductos, key=attrgetter('vecesVendido'), reverse=True)
            return productos_ordenados
    
    except ProductoNoEncontradoError as e:
        messagebox.showinfo("Info", "Lamentamos los inconvenientes pero este ranking no se encuentra disponible")
        return []

def imprimirCocinerosPorRanking(text, panaderia):
    cocineros_ordenados = ordenarCocinerosPorRanking(panaderia)
    
    if cocineros_ordenados == []:
        text.config(state=tk.NORMAL)
        text.delete(1.0, "end")
        text.config(state=tk.DISABLED)

    else:
        text.config(state=tk.NORMAL)
        text.delete(1.0, "end")
        text.config(state=tk.DISABLED)
        for cocinero in cocineros_ordenados:
            text.config(state=tk.NORMAL)
            text.insert(tk.END, cocinero.getNombre() + " " + "- Calificación:" + " " + "☆"*int(cocinero.getCalificacion()) +"\n")
            #text.insert(tk.END, cocinero.getNombre() + " " + "- Calificación:" + " " + str(cocinero.getCalificacion()) +"\n")
            text.config(state=tk.DISABLED)
            text.tag_configure("center", justify="center")
            text.tag_add("center", "1.0", "end")

def imprimirDomiciliariosPorRanking(text, panaderia):
    domiciliarios_ordenados = ordenarDomiciliariosPorRanking(panaderia)

    if domiciliarios_ordenados == []:
        text.config(state=tk.NORMAL)
        text.delete(1.0, "end")
        text.config(state=tk.DISABLED)

    else:
        text.config(state=tk.NORMAL)
        text.delete(1.0, "end")
        text.config(state=tk.DISABLED)
        for domiciliario in domiciliarios_ordenados:
            text.config(state=tk.NORMAL)
            text.insert(tk.END, domiciliario.getNombre() + " " + "- Calificación:" + " " + "☆"*int(domiciliario.getCalificacion()) +"\n")
            #text.insert(tk.END, domiciliario.getNombre() + " " + "- Calificación:" + " " + str(domiciliario.getCalificacion()) +"\n")
            text.config(state=tk.DISABLED)
            text.tag_configure("center", justify="center")
            text.tag_add("center", "1.0", "end")

def imprimirIngredientesPorVecesVendidos(text, panaderia):
    ingredientes_ordenados = ordenarIngredientesPorVecesVendidos(panaderia)

    if ingredientes_ordenados == []:
        text.config(state=tk.NORMAL)
        text.delete(1.0, "end")
        text.config(state=tk.DISABLED)
    
    else:
        text.config(state=tk.NORMAL)
        text.delete(1.0, "end")
        text.config(state=tk.DISABLED)
        for ingrediente in ingredientes_ordenados:
            text.config(state=tk.NORMAL)
            text.insert(tk.END, ingrediente.getNombre() + " " + "- Veces Vendido:" + " " + "☆"*int(ingrediente.getVecesVendido()) +"\n")
            #text.insert(tk.END, ingrediente.getNombre() + " " + "- Calificación:" + " " + str(ingrediente.getVecesVendido()) +"\n")
            text.config(state=tk.DISABLED)
            text.tag_configure("center", justify="center")
            text.tag_add("center", "1.0", "end")   

def imprimirProductosPorVecesVendidos(text, panaderia):
    productos_ordenados = ordenarProductosPorVecesVendidos(panaderia)

    if productos_ordenados == []:
        text.config(state=tk.NORMAL)
        text.delete(1.0, "end")
        text.config(state=tk.DISABLED)

    else:
        text.config(state=tk.NORMAL)
        text.delete(1.0, "end")
        text.config(state=tk.DISABLED)
        for producto in productos_ordenados:
            text.config(state=tk.NORMAL)
            text.insert(tk.END, producto.getNombre() + " " + "- Veces Vendido:" + " " + "☆"*int(producto.getVecesVendido()) +"\n")
            #text.insert(tk.END, producto.getNombre() + " " + "- Calificación:" + " " + str(producto.getVecesVendido()) +"\n")
            text.config(state=tk.DISABLED)
            text.tag_configure("center", justify="center")
            text.tag_add("center", "1.0", "end")