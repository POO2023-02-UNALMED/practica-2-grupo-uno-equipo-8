from gestorAplicacion.comida.Ingrediente import Ingrediente
from gestorAplicacion.comida.Producto import Producto
from gestorAplicacion.comida.ProductoFrio import ProductoFrio
from gestorAplicacion.humanos.Cocinero import Cocinero
from gestorAplicacion.humanos.Domiciliario import Domiciliario
from gestorAplicacion.humanos.Cliente import Cliente
from gestorAplicacion.humanos.Catastrofe import Catastrofe
from gestorAplicacion.humanos.Trabajador import Trabajador
from gestion import Inventario
from gestion import Canasta

class Panaderia():

    _canastaDelDia = None

    def __init__(self, trabajadores = None, cocineros = None, domiciliarios = None, clientes = None, dinero = 1000000, deudas = 0, quiebra = False, canastasP = None, inventario = None):
        
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

    def getEnQuiebra(self):
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
        
    def contratarCocinero(self, nombre, habilidad, calificacion, dineroEnMano, especialidad):
        indicado = Cocinero(nombre, habilidad, calificacion, dineroEnMano, especialidad, self)
        return indicado

    def cocinar(productosParaCocinar):
        canastaDeProductosCocinar = Canasta()
        canastaDeProductosCocinar.setProductosEnLista(productosParaCocinar)
        cocinero = cocineroAleatorio()
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
            cocinar(productosFaltantes)
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
                ingredientesFaltantes[Ingrediente.obtenerObjetoPorId(ingrediente).getNombre()] = cantidad
            comprarIngredientes(ingredientesFaltantes)
        for ingrediente, cantidad in ingredientes.items():
            for i in range(cantidad):
                ingredientesCanasta.append(self._inventario.buscarIngredientePorId(ingrediente))
                self._inventario.restarIngrediente(ingrediente, cantidad)
                Ingrediente.obtenerObjetoPorId(ingrediente).setVecesVendido(Ingrediente.obtenerObjetoPorId(ingrediente).getVecesVendido() + 1)
                Ingrediente.organizarTopMasVendidos()
        return ingredientesCanasta

    def agregarKitsACanasta(self, kitsEnLista):
        kitsCanasta = []
        ingredientesFaltantes = {}
        for kit, cantidad in kitsEnLista.items():
            idKit = kit
            cantidad = cantidad
            ingredientesKit = Producto.obtenerObjetoPorId(idKit).getIngredientes()
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
            comprarIngredientes(ingredientesFaltantes)
        for kit, cantidad in kitsEnLista.items():
            idKit = kit
            cantidad = cantidad
            for i in range(cantidad):
                kitCanasta = []
                for ingrediente, cantidadIngrediente in Producto.obtenerObjetoPorId(idKit).getIngredientes().items():
                    for j in range(cantidadIngrediente):
                        kitCanasta.append(self._inventario.buscarIngredientePorId(ingrediente))
                        Ingrediente.obtenerObjetoPorNombre(ingrediente).setVecesVendido(Ingrediente.obtenerObjetoPorNombre(ingrediente).getVecesVendido() + 1)
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
