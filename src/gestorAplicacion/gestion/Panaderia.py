# Ahora puedes importar Ingrediente desde Panaderia
from ..comida.Ingrediente import Ingrediente
from ..comida.Producto import Producto
from ..humanos.Cocinero import Cocinero
from ..gestion.Inventario import Inventario
from ..gestion.Canasta import Canasta
from ..humanos.Catastrofe import Catastrofe
from ..comida.ProductoFrio import ProductoFrio
from random import shuffle
from tkinter import Text
import tkinter as tk
import time

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

    def cocinar(self,productosParaCocinar,texto=None):
        canastaDeProductosCocinar = Canasta()
        canastaDeProductosCocinar.setProductosEnLista(productosParaCocinar)
        cocinero = self.cocineroAleatorio()
        Cocinero.setProcesosDeProductosCocinados([])
        Cocinero.setFallosCocinando([])
        Cocinero.setProductosCocinados([])
        while True:
            if cocinero.laborParticular(canastaDeProductosCocinar,texto):
                break

    def agregarProductosACanasta(self,productos,texto=None):
        productosCanasta = []
        productosFaltantes = {}
        for producto, cantidad in productos.items():
            cantidadExistente = self._inventario.verificarCantidadIngredientePorId(producto)
            if cantidadExistente - cantidad < 0:
                productosFaltantes[producto] = (cantidadExistente - cantidad) * (-2)
        if productosFaltantes:
            self.cocinar(productosFaltantes,texto)
        for producto, cantidad in productos.items():
            for i in range(cantidad):
                productosCanasta.append(self._inventario.buscarProductoPorId(producto))
                self._inventario.restarProducto(producto, cantidad)
        return productosCanasta

    def agregarIngredientesACanasta(self,ingredientes):
        ingredientesCanasta = []
        ingredientesFaltantes = {}
        ingredientesFaltantesCopia = {}
        for ingrediente, cantidad in ingredientes.items():
            cantidadExistente = self._inventario.verificarCantidadIngredientePorId(ingrediente)
            if cantidadExistente - cantidad < 0:
                ingredientesFaltantes[ingrediente] = (cantidadExistente - cantidad) * (-2)
        if ingredientesFaltantes:
            for ingrediente, cantidad in ingredientesFaltantes.items():
                ingredientesFaltantesCopia[Ingrediente.obtenerObjetoPorIdI(ingrediente).getNombre()] = cantidad
            self.comprarIngredientes(ingredientesFaltantesCopia)
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
                        Ingrediente.obtenerObjetoPorNombreI(ingrediente).setVecesVendido(Ingrediente.obtenerObjetoPorNombreI(ingrediente).getVecesVendido() + 1)
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
                    
                    if text != None:
                        text.config(state=tk.NORMAL)
                        text.insert(tk.END, "La panadería no tenía dinero para realizar su pedido y ha entrado en quiebra :( , pero una franquicia más grande la ha comprado :D , podremos proseguir con su pedido" + "\n")
                        text.config(state=tk.DISABLED)
                        text.tag_configure("center", justify="center")
                        text.tag_add("center", "1.0", "end")

                else:

                    if text != None:
                        text.config(state=tk.NORMAL)
                        text.insert(tk.END, "La panadería no tenía dinero para realizar su pedido :( , pero ha pedido un prestamo y ya puede comprar lo que necesita para preparar su pedido :D" + "\n")
                        text.config(state=tk.DISABLED)
                        text.tag_configure("center", justify="center")
                        text.tag_add("center", "1.0", "end")

                self.saldarDeudas()

            self._dinero += valorNecesitado
            self._valorDeudas = valorNecesitado

        #GestionConseguirIngredientes.lecturaQuiebra(self._enQuiebra) #Crear estas lecturas
        if self._enQuiebra == True:
            
            if text != None:
                text.config(state=tk.NORMAL)
                text.insert(tk.END, "La panadería no tenía dinero para realizar su pedido y ha entrado en quiebra :( , pero una franquicia más grande la ha comprado :D , podremos proseguir con su pedido" + "\n")
                text.config(state=tk.DISABLED)
                text.tag_configure("center", justify="center")
                text.tag_add("center", "1.0", "end")

        else:

            if text != None:
                text.config(state=tk.NORMAL)
                text.insert(tk.END, "La panadería no tenía dinero para realizar su pedido :( , pero ha pedido un prestamo y ya puede comprar lo que necesita para preparar su pedido :D" + "\n")
                text.config(state=tk.DISABLED)
                text.tag_configure("center", justify="center")
                text.tag_add("center", "1.0", "end")

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
        if text != None:
            text.delete(1.0,tk.END)
        elegido = self.domiciliarioAleatorio()
        #GestionConseguirIngredientes.lecturaCompra(elegido.isRobado()) #Recordar hacer este lector
        if elegido.isRobado() == True:
            
            if text != None:
                text.config(state=tk.NORMAL)
                text.insert(tk.END, "Se ha enviado a comprar mas ingredientes, por favor espere a que se compren correctamente" + "\n")
                text.config(state=tk.DISABLED)
                text.tag_configure("center", justify="center")
                text.tag_add("center", "1.0", "end")

        else:

            if text != None:
                text.config(state=tk.NORMAL)
                text.insert(tk.END, "Estamos en proceso de conseguir los ingredientes, lamentamos los inconvenientes" + "\n")
                text.config(state=tk.DISABLED)
                text.tag_configure("center", justify="center")
                text.tag_add("center", "1.0", "end")

        x = elegido.conseguirIngredientes(listIngredientes, text)
        #GestionConseguirIngredientes.lecturaRobo(x)
        if x == True:

            if text != None:
                text.config(state=tk.NORMAL)
                text.insert(tk.END, "Han robado al trabajador que iba por los ingredientes, pedimos disculpas por el atraso, enviaremos a alguien mas por la compra" + "\n")
                text.config(state=tk.DISABLED)
                text.tag_configure("center", justify="center")
                text.tag_add("center", "1.0", "end")

        else:
            
            if text != None:
                text.config(state=tk.NORMAL)
                text.insert(tk.END, "El trabajador ha regresado con los ingredientes!!" + "\n")
                text.config(state=tk.DISABLED)
                text.tag_configure("center", justify="center")
                text.tag_add("center", "1.0", "end")

        while(x == True):

            elegido.setRobado(False)
            #GestionConseguirIngredientes.lecturaCompra(elegido.isRobado()) #Recordar hacer este lector
            if elegido.isRobado() == True:
                
                if text != None:
                    text.config(state=tk.NORMAL)
                    text.insert(tk.END, "Se ha enviado a comprar mas ingredientes, por favor espere a que se compren correctamente" + "\n")
                    text.config(state=tk.DISABLED)
                    text.tag_configure("center", justify="center")
                    text.tag_add("center", "1.0", "end")

            else:

                if text != None:
                    text.config(state=tk.NORMAL)
                    text.insert(tk.END, "Estamos en proceso de conseguir los ingredientes, lamentamos los inconvenientes" + "\n")
                    text.config(state=tk.DISABLED)
                    text.tag_configure("center", justify="center")
                    text.tag_add("center", "1.0", "end")

            if x == True:

                if text != None:
                    text.config(state=tk.NORMAL)
                    text.insert(tk.END, "Han robado al trabajador que iba por los ingredientes, pedimos disculpas por el atraso, enviaremos a alguien mas por la compra" + "\n")
                    text.config(state=tk.DISABLED)
                    text.tag_configure("center", justify="center")
                    text.tag_add("center", "1.0", "end")

            else:

                if text != None:
                    text.config(state=tk.NORMAL)
                    text.insert(tk.END, "El trabajador ha regresado con los ingredientes!!" + "\n")
                    text.config(state=tk.DISABLED)
                    text.tag_configure("center", justify="center")
                    text.tag_add("center", "1.0", "end")

        elegido.setRobado(True)

    def enviar_domicilio(self, canasta, cliente, text=None):
        domiciliario = cliente.getDomiciliario()

        cliente.setDomiciliario(domiciliario)
        productos = canasta.getProductos()

        for producto in productos:
            if isinstance(producto, ProductoFrio):
                domiciliario = producto.empaqueCongelador(domiciliario)

        malechor = Catastrofe()
        domiciliario = malechor.pincharLlanta(domiciliario)

        if not domiciliario.isLicencia():
            self.setDinero(self.getDinero()-10000)
            domiciliario.setLicencia(True)

        domiciliario.setCanasta(canasta)
        domiciliario.setOcupado(True)

        while not domiciliario.laborParticular(canasta):
            domiciliario.setHabilidad(domiciliario.getHabilidad() + 10)
            self.setDinero(self.getDinero()-10000)
            domiciliario.setLicencia(True)
            if text != None:
                text.config(state=tk.NORMAL)
                text.insert(tk.END, "Hubo un problema con el domiciliario, estamos trabajando para solucionarlo" + "\n")
                text.config(state=tk.DISABLED)
                text.tag_configure("center", justify="center")
                text.tag_add("center", "1.0", "end")
        
        if text != None:
                text.config(state=tk.NORMAL)
                text.insert(tk.END, "Preparate que el domiciliario ha salido a tu direccion" + "\n")
                text.config(state=tk.DISABLED)
                text.tag_configure("center", justify="center")
                text.tag_add("center", "1.0", "end")
            
                for i in range(20):  # Ajusta el número de iteraciones según sea necesario
                    time.sleep(0.1)  # Simula algún tiempo de espera entre actualizaciones
                    text.config(state=tk.NORMAL)
                    text.insert(tk.END, "#"*i + "\n")
                    text.config(state=tk.DISABLED)
                    text.tag_configure("center", justify="center")
                    text.tag_add("center", "1.0", "end")
            
                text.config(state=tk.NORMAL)
                text.insert(tk.END, "Tu domicilio ha llegado, que lo disfrutes" + "\n")
                text.insert(tk.END, "Se entregó" + "\n")
                """
                for elements in canasta.getProductos():
                    text.insert(tk.END, "Producto: " + elements.getNombre() + "\n")
                for elements in canasta.getIngredientes():
                    text.insert(tk.END, "Ingrediente: "  + elements.getNombre() + "\n")
                for elements in canasta.getKits():
                    text.insert(tk.END, "Kits: "  + elements.getNombre() + "\n")
                """
                text.config(state=tk.DISABLED)
                text.tag_configure("center", justify="center")
                text.tag_add("center", "1.0", "end")

        cliente.setCanastaEnMano(domiciliario.getCanasta())


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


"""¡Oh, código mágico de bytes y lógica,
En el vasto reino de la programación,
Te conjuro con poder y sintaxis armoniosa,
Que mi proyecto escape de la evaluación!

Con bytes de buena fortuna y algoritmos sagrados,
Que la magia del código fluya en cada línea,
Que los errores se disuelvan como niebla matutina,
Y que la ejecución sea impecable, divina.

Que los bucles sean infinitos de éxito,
Y que las variables guarden la esencia de la perfección,
Que el hechizo de la eficiencia teja su red,
Y que el compilador cante la canción de la aprobación.

En el reino de los píxeles y los bits,
Donde el tiempo se mide en ciclos y milisegundos,
Que mi código sea un faro de luz brillante,
Guiando a los profesores por senderos fecundos.

Oh, compilador, acepta este conjuro,
Que mi código sea como un poema bien rimado,
Que los comentarios sean versos de sabiduría,
Y que la indentación sea un mapa bien trazado.

Que el flujo de datos sea un río tranquilo,
Navegando por los módulos con gracia y sin error,
Que las excepciones sean tan raras como estrellas fugaces,
Y que la memoria sea un jardín de flores en flor.

Que las pruebas sean como oráculos confiables,
Revelando la verdad de cada función y método,
Que la cobertura sea un manto protector,
Guardando mi proyecto de cualquier tormento.

Que el tiempo de ejecución sea breve como un suspiro,
Y que la complejidad sea simple como un eco,
Que el debugger sea un aliado leal,
En la danza de bits y bytes, un compañero.

Con este conjuro, mi proyecto te encomiendo,
A las manos justas y sabias de los profesores,
Que encuentren deleite en la lectura de documentos,
Y que la magia del código les cause asombro.

¡Así sea este conjuro de programación,
Que mi proyecto florezca y prospere con devoción,
Que la suerte me acompañe en este trance,
Y que la programación sea mi eterna danza!
"""