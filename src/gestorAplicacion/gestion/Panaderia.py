# Ahora puedes importar Ingrediente desde Panaderia
from ..comida.Ingrediente import Ingrediente
from ..comida.Producto import Producto
from ..humanos.Cocinero import Cocinero
from ..gestion.Inventario import Inventario
from ..gestion.Canasta import Canasta
from random import shuffle
from tkinter import Text
import tkinter as tk

class Panaderia():

    _canastaDelDia = None
    


    def __init__(self, trabajadores = None, cocineros = None, domiciliarios = None, clientes = None, dinero = 1000000, deudas = 0, quiebra = False, canastasP = None):
        
        if trabajadores == None: 
            trabajadores = []

        if cocineros == None:
            cocineros = []

        if domiciliarios == None:
            domiciliarios = []

        if clientes == None:
            clientes = []

        if canastasP == None:
            canastasP = []

        self._trabajadores = trabajadores
        self._cocineros = cocineros
        self._domiciliarios = domiciliarios
        self._clientes = clientes
        self._dinero = dinero
        self._valorDeudas = deudas
        self._enQuiebra = quiebra
        self._canastasPublicadas = canastasP
        self._inventario = Inventario()

    def getTrabajadores(self):
        return self._trabajadores

    def setTrabajadores(self, value):
        self._trabajadores = value

    def getCocineros(self):
        return self._cocineros

    def setCocineros(self, value):
        self._cocineros = value

    def getDomiciliarios(self):
        return self._domiciliarios

    def setDomiciliarios(self, value):
        self._domiciliarios = value

    def getClientes(self):
        return self._clientes

    def setClientes(self, value):
        self._clientes = value

    def getDinero(self):
        return self._dinero

    def setDinero(self, value):
        self._dinero = value

    def getValorDeudas(self):
        return self._valorDeudas

    def setValorDeudas(self, value):
        self._valorDeudas = value

    def isEnQuiebra(self):
        return self._enQuiebra

    def setEnQuiebra(self, value):
        self._enQuiebra = value

    def getCanastasPublicadas(self):
        return self._canastasPublicadas

    def setCanastasPublicadas(self, value):
        self._canastasPublicadas = value

    def getInventario(self):
        return self._inventario

    def setInventario(self, value):
        self._inventario = value

    @classmethod
    def getCanastaDelDia(cls):
        return cls._canastaDelDia
    
    @classmethod
    def setCanastaDelDia(cls, value):
        cls._canastaDelDia = value
        
    def contratarCocinero(self, nombre, especialidad, habilidad, calificacion, dineroEnMano):
        indicado = Cocinero(nombre, especialidad, self, habilidad, calificacion, dineroEnMano)
        return indicado

    def obtenerCanastaPorId(self,id):
        for canasta in self._canastasPublicadas:
            if canasta.getIdentificador() == id:
                return canasta
        return None

    def cocinar(self,productosParaCocinar):
        canastaDeProductosCocinar = Canasta()
        canastaDeProductosCocinar.setProductosEnLista(productosParaCocinar)
        cocinero = self.cocineroAleatorio()
        Cocinero.setProcesosDeProductosCocinados([])
        Cocinero.setFallosCocinando(0)
        while True:
            if cocinero.laborParticular(canastaDeProductosCocinar):
                break

    def agregarProductosACanasta(self,productos):
        productosCanasta = []
        productosFaltantes = {}
        for producto, cantidad in productos.items():
            cantidadExistente = self._inventario.verificarCantidadIngredientePorId(producto)
            if cantidadExistente - cantidad < 0:
                productosFaltantes[producto] = (cantidadExistente - cantidad) * (-2)
        if productosFaltantes:
            self.cocinar(productosFaltantes)
        for producto, cantidad in productos.items():
            for i in range(cantidad):
                productosCanasta.append(self._inventario.buscarProductoPorId(producto))
                self._inventario.restarProducto(producto, cantidad)
        return productosCanasta

    def agregarIngredientesACanasta(self,ingredientes):
        ingredientesCanasta = []
        ingredientesFaltantes = {}
        for ingrediente, cantidad in ingredientes.items():
            cantidadExistente = self._inventario.verificarCantidadIngredientePorId(ingrediente)
            if cantidadExistente - cantidad < 0:
                ingredientesFaltantes[ingrediente] = (cantidadExistente - cantidad) * (-2)
        if ingredientesFaltantes:
            for ingrediente, cantidad in ingredientesFaltantes.items():
                ingredientesFaltantes[Ingrediente.obtenerObjetoPorIdI(ingrediente).getNombre()] = cantidad
            self.comprarIngredientes(ingredientesFaltantes)
        for ingrediente, cantidad in ingredientes.items():
            for i in range(cantidad):
                ingredientesCanasta.append(self._inventario.buscarIngredientePorId(ingrediente))
                self._inventario.restarIngrediente(ingrediente, cantidad)
                Ingrediente.obtenerObjetoPorIdI(ingrediente).setVecesVendido(Ingrediente.obtenerObjetoPorIdI(ingrediente).getVecesVendido() + 1)
                Ingrediente.organizarTopMasVendidos()
        return ingredientesCanasta

    def agregarKitsACanasta(self, kitsEnLista):
        kitsCanasta = []
        ingredientesFaltantes = {}
        for kit, cantidad in kitsEnLista.items():
            idKit = kit
            cantidad = cantidad
            ingredientesKit = Producto.obtenerObjetoPorIdP(idKit).getIngredientes()
            for ingrediente, cantidadIngrediente in ingredientesKit.items():
                ingredientesKit[ingrediente] = cantidadIngrediente * cantidad
            for ingrediente, cantidadIngrediente in ingredientesKit.items():
                cantidadExistente = self._inventario.verificarCantidadIngredientePorId(ingrediente)
                if cantidadExistente - cantidadIngrediente < 0:
                    if ingrediente in ingredientesFaltantes:
                        ingredientesFaltantes[ingrediente] += (cantidadExistente - cantidadIngrediente) * (-2)
                    else:
                        ingredientesFaltantes[ingrediente] = (cantidadExistente - cantidadIngrediente) * (-2)
        if ingredientesFaltantes:
            self.comprarIngredientes(ingredientesFaltantes)
        for kit, cantidad in kitsEnLista.items():
            idKit = kit
            cantidad = cantidad
            for i in range(cantidad):
                kitCanasta = []
                for ingrediente, cantidadIngrediente in Producto.obtenerObjetoPorIdP(idKit).getIngredientes().items():
                    for j in range(cantidadIngrediente):
                        kitCanasta.append(self._inventario.buscarIngredientePorId(ingrediente))
                        Ingrediente.obtenerObjetoPorNombre(ingrediente).setVecesVendido(Ingrediente.obtenerObjetoPorNombreI(ingrediente).getVecesVendido() + 1)
                        Ingrediente.organizarTopMasVendidos()
                        self._inventario.restarIngrediente(ingrediente, 1)
                kitsCanasta.append(kitCanasta)
        return kitsCanasta

    def saldarDeudas(self):

        if self._valorDeudas < self._dinero: 

            self._dinero = self._dinero - self._valorDeudas
            self._valorDeudas = 0
            self._enQuiebra = False
            return self._enQuiebra
        
        else:

            self._enQuiebra = True
            self._dinero = 10000000
            return self._enQuiebra
    
    def conseguirPrestamo(self, valorNecesitado, text = None):
        
        if self._valorDeudas == 0:

            self._dinero += valorNecesitado
            self._valorDeudas = valorNecesitado

        else:

            self.saldarDeudas()

            while self._enQuiebra == True:
                
                #GestionConseguirIngredientes.lecturaQuiebra(self._enQuiebra) #Crear estas lecturas

                if self._enQuiebra == True:
                    text.config(state=tk.NORMAL)
                    text.insert("La panadería no tenía dinero para realizar su pedido y ha entrado en quiebra :( , pero una franquicia más grande la ha comprado :D , podremos proseguir con su pedido")
                    text.config(state=tk.DISABLED)
                else:
                    text.config(state=tk.NORMAL)
                    text.insert("La panadería no tenía dinero para realizar su pedido :( , pero ha pedido un prestamo y ya puede comprar lo que necesita para preparar su pedido :D")
                    text.config(state=tk.DISABLED)

                self.saldarDeudas()

            self._dinero += valorNecesitado
            self._valorDeudas = valorNecesitado

        #GestionConseguirIngredientes.lecturaQuiebra(self._enQuiebra) #Crear estas lecturas
        if self._enQuiebra == True:
            text.config(state=tk.NORMAL)
            text.insert("La panadería no tenía dinero para realizar su pedido y ha entrado en quiebra :( , pero una franquicia más grande la ha comprado :D , podremos proseguir con su pedido")
            text.config(state=tk.DISABLED)
        else:
            text.config(state=tk.NORMAL)
            text.insert("La panadería no tenía dinero para realizar su pedido :( , pero ha pedido un prestamo y ya puede comprar lo que necesita para preparar su pedido :D")
            text.config(state=tk.DISABLED)

    def cocineroAleatorio(self):
        
        listaprovicional = self._cocineros.copy()
        shuffle(listaprovicional)
        elegido = listaprovicional[0]
        return elegido 

    def domiciliarioAleatorio(self):
        
        listaprovicional = self._domiciliarios.copy()
        shuffle(listaprovicional)
        elegido = listaprovicional[0]
        return elegido 
    
    def trabajadorAleatorio(self):

        listaprovicional = self._trabajadores.copy()
        listaprovicional.shuffle()
        elegido = listaprovicional[0]
        return elegido
    
    def comprarIngredientes(self, listIngredientes, text=None):

        elegido = self.domiciliarioAleatorio()
        #GestionConseguirIngredientes.lecturaCompra(elegido.isRobado()) #Recordar hacer este lector
        if elegido.isRobado() == True:
            text.config(state=tk.NORMAL)
            text.insert("Se ha enviado a comprar mas ingredientes, por favor espere a que se compren correctamente")
            text.config(state=tk.DISABLED)
        else:
            text.config(state=tk.NORMAL)
            text.insert("Estamos en proceso de conseguir los ingredientes, lamentamos los inconvenientes")
            text.config(state=tk.DISABLED)

        x = elegido.conseguirIngredientes(listIngredientes)
        #GestionConseguirIngredientes.lecturaRobo(x)
        if x == True:
            text.config(state=tk.NORMAL)
            text.insert("Han robado al trabajador que iba por los ingredientes, pedimos disculpas por el atraso, enviaremos a alguien mas por la compra")
            text.config(state=tk.DISABLED)
        else:
            text.config(state=tk.NORMAL)
            text.insert("El trabajador ha regresado con los ingredientes!!")
            text.config(state=tk.DISABLED)


        while(x == True):

            elegido.setRobado(False)
            #GestionConseguirIngredientes.lecturaCompra(elegido.isRobado()) #Recordar hacer este lector
            if elegido.isRobado() == True:
                text.config(state=tk.NORMAL)
                text.insert("Se ha enviado a comprar mas ingredientes, por favor espere a que se compren correctamente")
                text.config(state=tk.DISABLED)
            else:
                text.config(state=tk.NORMAL)
                text.insert("Estamos en proceso de conseguir los ingredientes, lamentamos los inconvenientes")
                text.config(state=tk.DISABLED)
            #GestionConseguirIngredientes.lecturaRobo(x)
            if x == True:
                text.config(state=tk.NORMAL)
                text.insert("Han robado al trabajador que iba por los ingredientes, pedimos disculpas por el atraso, enviaremos a alguien mas por la compra")
                text.config(state=tk.DISABLED)
            else:
                text.config(state=tk.NORMAL)
                text.insert("El trabajador ha regresado con los ingredientes!!")
                text.config(state=tk.DISABLED)

        elegido.setRobado(True)

    def reviewDomiciliario(self, domiciliario):

        calificacion = domiciliario.getCalificacion()     
        if calificacion < 3:
            domiciliario.setSalario(domiciliario.getSalario() * 0.9)
        elif calificacion == 5:
            domiciliario.setSalario(domiciliario.getSalario() * 1.1)

    def reviewCocinero(self, cocinero):
        
        calificacion = cocinero.getCalificacion()     
        if calificacion < 3:
            cocinero.setSalario(cocinero.getSalario() * 0.9)
        elif calificacion == 5:
            cocinero.setSalario(cocinero.getSalario() * 1.1)