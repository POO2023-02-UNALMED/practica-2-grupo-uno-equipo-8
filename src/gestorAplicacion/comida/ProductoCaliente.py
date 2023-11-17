from random import randint, sample
from gestorAplicacion.comida.Producto import Producto
from gestorAplicacion.comida.Producto import Ingrediente
import random

class ProductoCaliente(Producto):
    def __init__(self, nombre, ingredientes, ids=None, costo=0, vecesVendido=0):
        super().__init__(nombre, ingredientes, ids, costo, vecesVendido)
        self._horno = False

    
    def getHorno(self):
        return self._horno

    def setHorno(self, value):
        self._horno = value

    @classmethod
    def crearProducto(cls, Nnombre):
        newProducto = cls.obtenerObjetoPorIdP(Nnombre)
        return cls(
            newProducto.getNombre(),
            newProducto.getId(),
            newProducto.getIngredientes(),
            newProducto.getCosto(),
            newProducto.getVecesVendido()
        )

    @classmethod
    def crearProductoPersonalizado(cls, Nnombre, ingredientes):
        for nombreIngrediente, cantidad in ingredientes.items():
            if not Ingrediente.verificacionExistenciaPorNombreI(nombreIngrediente):
                Ingrediente(nombreIngrediente)

        return ProductoCaliente(Nnombre, ingredientes)
    
    def procesoHornear(self, cocinero):
        if cocinero.isHorno():
            return cocinero
        else:
            cocinero.setHorno(True)
            return cocinero
        

    def seleccionProcesosDeCocina(self):
        procesos = ["Hornear", "Amasar", "Mezclar", "Fritar", "Asar", "Decoracion"]
        cuantosProcesos = randint(1, 3)
        numerosIndices = sample(range(6), cuantosProcesos)
        procesosFinales = [procesos[numero] for numero in numerosIndices]
        return procesosFinales