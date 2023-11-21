from gestorAplicacion.humanos.Catastrofe import Catastrofe
from gestorAplicacion.comida.Ingrediente import Ingrediente
from gestorAplicacion.humanos.Trabajador import Trabajador
from gestorAplicacion.comida.ComidaDefault import ComidaDefault
from UIMain.GestionDomicilioCliente import GestionDomicilioClienteApp
from tkinter import Text
import tkinter as tk
import time
import random

class Domiciliario(Trabajador, ComidaDefault):
    def __init__(self, nombre="", panaderia=None, calificacion=None, dineroEnMano=0, licencia=None):
        super().__init__(panaderia, nombre, calificacion, dineroEnMano)
        self.licencia = False if licencia is None else licencia
        self.ocupado = False
        self.canasta = None
        self.empaqueFrio = False
        self.panaderia = panaderia
        panaderia.getDomiciliarios().append(self)

    def isLicencia(self):
        return self.licencia

    def setLicencia(self, licencia):
        self.licencia = licencia

    def isOcupado(self):
        return self.ocupado

    def setOcupado(self, ocupado):
        self.ocupado = ocupado

    def getCanasta(self):
        return self.canasta

    def setCanasta(self, canasta):
        self.canasta = canasta

    def isEmpaqueFrio(self):
        return self.empaqueFrio

    def setEmpaqueFrio(self, empaqueFrio):
        self.empaqueFrio = empaqueFrio

    def getPanaderia(self):
        return self.panaderia

    def setPanaderia(self, panaderia):
        self.panaderia = panaderia
    

    def calcularCostoDomicilio(self, cliente, canasta):
        productos = canasta.getProductos()
        costo = sum(producto.getCosto() for producto in productos)
        if len(productos) > 15:
            costo *= 0.7

        direccion = cliente.getDireccion()
        
        if direccion.get_distancia() == "Medio":
            costo += 10000
        if direccion.get_distancia() == "Lejos":
            costo += 20000
        

        costo += ComidaDefault.tarifaDomicilio
        costo *= ComidaDefault.tarifaGanancias
        return costo

    def laborParticular(self, canasta):
        transito = Catastrofe()
        if transito.paradaTransito(self):
            x = False
            GestionDomicilioClienteApp.estado_domicilio(x)
            return x
        else:
            self.canasta = None
            self.ocupado = False
            x = True
            GestionDomicilioClienteApp.estado_domicilio(x)
            return x

    def conseguirIngredientes(self, listIngredientes, text = None):
        valorcompra = 0

        Ingrediente.organizarTopMasVendidos()
        top = Ingrediente.getTopMasVendidos()

        for ingredienteNombre, cantidad in listIngredientes.items():

            topp = False

            for ingredientes in top:

                if ingredientes.getNombre() == ingredienteNombre:

                    if 40 < cantidad + self.panaderia.getInventario().verificarCantidadIngredientePorNombre(ingredienteNombre):
                        
                        valorcompra = valorcompra + ((Ingrediente.obtenerObjetoPorNombreI(ingredienteNombre).getPrecioDeCompra()) * (cantidad)) + 100000
                        topp = True

                        if text != None:
                            text.config(state=tk.NORMAL)
                            text.insert(tk.END, f"El ingrediente {ingredienteNombre} está en el top mas vendido por tanto su máximo en el inventario es de 40 unidades, sin embargo se cobró 100000 más a la compra para poder ampliar el inventario y comprar {cantidad} unidades\n")
                            text.config(state=tk.DISABLED)

                    else:

                        if self.panaderia.getInventario().verificarCantidadIngredientePorNombre(ingredienteNombre) + (cantidad * 2) <= 40:

                            if self.robado == True:

                                cantidad = cantidad*2

                            valorcompra = valorcompra + ((Ingrediente.obtenerObjetoPorNombreI(ingredienteNombre).getPrecioDeCompra()) * (cantidad))
                            topp = True
                           
                            if text != None:
                                text.config(state=tk.NORMAL)
                                text.insert(tk.END, f"El ingrediente {ingredienteNombre} está en el top mas vendido por tanto su máximo en el inventario es de 40 unidades y se prioriza comprar el doble, como había suficiente espacio en el inventario se comprpó {cantidad * 2} unidades\n")
                                text.config(state=tk.DISABLED)

                        else:

                            if self.robado == True:

                                cantidad = (40 - self.panaderia.getInventario().verificarCantidadIngredientePorNombre(ingredienteNombre))

                            valorcompra = valorcompra + ((Ingrediente.obtenerObjetoPorNombreI(ingredienteNombre).getPrecioDeCompra()) * (cantidad))
                            topp = True

                            if text != None:
                                text.config(state=tk.NORMAL)
                                text.insert(tk.END, f"El ingrediente {ingredienteNombre} está en el top mas vendido por tanto su máximo en el inventario es de 40 unidades y se prioriza comprar el doble, sin embargo esta vez no había suficiente espacio en el inventario para adquirir el doble así que se compró {40 - self.panaderia.getInventario().verificarCantidadIngredientePorNombre(ingredienteNombre)} unidades para completar 40 unidades en el inventario\n")
                                text.config(state=tk.DISABLED)
            
            if topp == False:

                if cantidad + self.panaderia.getInventario().verificarCantidadIngredientePorNombre(ingredienteNombre) > 20:

                    valorcompra = valorcompra+ ((Ingrediente.obtenerObjetoPorNombreI(ingredienteNombre).getPrecioDeCompra()) * (cantidad)) + 50000
                    topp = True

                    if text != None:
                        text.config(state=tk.NORMAL)
                        text.insert(tk.END, f"El ingrediente {ingredienteNombre} no está en el top mas vendido por tanto su máximo en el inventario es de 20 unidades, sin embargo se cobró 50000 más a la compra para poder ampliar el inventario y comprar {cantidad} unidades\n")
                        text.config(state=tk.DISABLED)

                else:

                    if self.panaderia.getInventario().verificarCantidadIngredientePorNombre(ingredienteNombre) + (cantidad) <= 20:

                        valorcompra = valorcompra + ((Ingrediente.obtenerObjetoPorNombreI(ingredienteNombre).getPrecioDeCompra()) * (cantidad))

                        if text != None:
                            text.config(state=tk.NORMAL)
                            text.insert(tk.END, f"El ingrediente {ingredienteNombre} no está en el top mas vendido por tanto su máximo en el inventario es de 20 unidades, como había suficiente espacio en el inventario se compró {cantidad} unidades\n")
                            text.config(state=tk.DISABLED)

                    else:

                        if self.robado == True:

                            cantidad = (20 - self.panaderia.getInventario().verificarCantidadIngredientePorNombre(ingredienteNombre))

                        valorcompra = valorcompra + ((Ingrediente.obtenerObjetoPorNombreI(ingredienteNombre).getPrecioDeCompra()) * (cantidad))
                        
                        if text != None:
                            text.config(state=tk.NORMAL)
                            text.insert(tk.END, f"El ingrediente {ingredienteNombre} no está en el top mas vendido por tanto su máximo en el inventario es de 20 unidades, como no había suficiente espacio en el inventario se compró {20 - self.panaderia.getInventario().verificarCantidadIngredientePorNombre(ingredienteNombre)} unidades para completar 20 unidades \n")
                            text.config(state=tk.DISABLED)
            
            listIngredientes[ingredienteNombre] = cantidad #revisar esto 
        
        if valorcompra <= self.panaderia.getDinero():
            
            x = self.dinero_en_mano + valorcompra
            self.dinero_en_mano = x  
            dinero = self.panaderia.getDinero()
            self.panaderia.setDinero((dinero-valorcompra))

            if self.robado == True:

                ladron = Catastrofe()
                postRobo = ladron.robarComprador(self)

                if postRobo.isRobado() == False:
                    return True
                
            for ingredienteNombre, cantidad in listIngredientes.items():

                for i in range (0,cantidad):

                    ingrdt = Ingrediente.crearIngrediente(ingredienteNombre)
                    self.getPanaderia().getInventario().agregarIngrediente(ingrdt)
                
                if text != None:
                    text.config(state=tk.NORMAL)
                    text.insert(tk.END, f"Se han comprado {cantidad} unidades de {ingredienteNombre}\n")
                    text.config(state=tk.DISABLED)
            
            if text != None:
                text.config(state=tk.NORMAL)
                text.insert(tk.END, f"El valor total de la compra fue {valorcompra}\n")
                text.config(state=tk.DISABLED)
            
            x = self.dinero_en_mano - valorcompra
            self.dinero_en_mano = x  
            return False
        
        else:

            self.panaderia.conseguirPrestamo(valorcompra, text)
            x = self.dinero_en_mano + valorcompra
            self.dinero_en_mano = x  
            dinero = self.panaderia.getDinero()
            self.panaderia.setDinero((dinero-valorcompra))

            if self.robado == True:

                ladron = Catastrofe()
                postRobo = ladron.robarComprador(self)

                if postRobo.isRobado() == False:
                    return True
                
            for ingredienteNombre, cantidad in listIngredientes.items():

                for i in range (0,cantidad):

                    ingrdt = Ingrediente.crearIngrediente(ingredienteNombre)
                    self.getPanaderia().getInventario().agregarIngrediente(ingrdt)
                
                if text != None:
                    text.config(state=tk.NORMAL)
                    text.insert(tk.END, f"Se han comprado {cantidad} unidades de {ingredienteNombre}\n")
                    text.config(state=tk.DISABLED)
            
            if text != None:
                text.config(state=tk.NORMAL)
                text.insert(tk.END, f"El valor total de la compra fue {valorcompra}\n")
                text.config(state=tk.DISABLED)

            x = self.dinero_en_mano - valorcompra
            self.dinero_en_mano = x
            return False