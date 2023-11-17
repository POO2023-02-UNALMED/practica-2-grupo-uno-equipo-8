from random import randint, sample

from gestorAplicacion.comida.Producto import Producto
from gestorAplicacion.comida.Producto import Ingrediente
import random

class ProductoFrio(Producto):
    def __init__(self, nombre, ingredientes, ids=None, costo=0, vecesVendido=0, tiempoDeCongelamiento=0):
        super().__init__(nombre,ingredientes, ids, costo, vecesVendido)
        self._congelador = False
        self._tiempoDeCongelamiento = tiempoDeCongelamiento


    def getCongelador(self):
        return self._congelador


    def setCongelador(self, value):
        self._congelador = value


    def getTiempoDeCongelamiento(self):
        return self._tiempoDeCongelamiento


    def setTiempoDeCongelamiento(self, value):
        self._tiempoDeCongelamiento = value

    @classmethod
    def crearProducto(cls, Nnombre):
        newProducto = Producto.obtenerObjetoPorId(Nnombre)
        return Producto(
            newProducto.nombre,
            newProducto.id, 
            newProducto.ingredientes,
            newProducto.costo, 
            newProducto.vecesVendido, 
            newProducto.tiempoDeCongelamiento)
    
    @classmethod
    def crearProductoPersonalizado(cls, Nnombre, ingredientes):
        for nombre, cantidad in ingredientes.items():
            if not Ingrediente.verificacionExistenciaPorNombreI(nombre):
                Ingrediente(nombre)
        return ProductoFrio(Nnombre, ingredientes)
    

    def seleccionProcesosDeCocina(self):
        procesos = ["Gelatinificar", "Amasar", "Mezclar", "Congelar", "Licuar", "Decoracion"]
        cuantosProcesos = randint(1, 3)
        numerosIndices = sample(range(6), cuantosProcesos)
        procesosFinales = [procesos[numero] for numero in numerosIndices]
        return procesosFinales
    
    def empaqueCongelador(self, domiciliario):
        if domiciliario.isEmpaqueFrio():
            return domiciliario
        else:
            domiciliario.setEmpaqueFrio(True)
            return domiciliario
        
    def calcularCongelamiento(self):
        tiempoDeCongelamiento = random.randint(0, 19)
        return tiempoDeCongelamiento
    
    def procesoCongelamiento(self, cocinero):
        if cocinero.isNevera():
            return cocinero
        else:
            cocinero.setNevera(True)
            return cocinero
