from random import randint, sample
from gestorAplicacion.comida.Producto import Producto

import random

class ProductoCaliente(Producto):
    def __init__(self, nombre, ingredientes, ids=None, costo=0, vecesVendido=0):
        """
        Inicializa un objeto ProductoCaliente.

        Args:
            nombre (str): El nombre del producto caliente.
            ingredientes (list): La lista de ingredientes del producto caliente.
            ids (int, optional): El identificador del producto caliente. Por defecto es None.
            costo (float, optional): El costo del producto caliente. Por defecto es 0.
            vecesVendido (int, optional): El número de veces que se ha vendido el producto caliente. Por defecto es 0.
        """
        super().__init__(nombre, ingredientes, ids, costo, vecesVendido)
        self._horno = False

    #getters y setters
    
    def getHorno(self):
        return self._horno

    def setHorno(self, value):
        self._horno = value

    @classmethod
    def crearProducto(cls, Nnombre):
        """
        Crea un nuevo objeto ProductoCaliente a partir de un objeto Producto existente.

        Args:
            Nnombre (str): El nombre del producto existente.

        Returns:
            ProductoCaliente: El nuevo objeto ProductoCaliente creado.

        """
        newProducto = Producto.obtenerObjetoPorIdP(Nnombre)
        return ProductoCaliente(
            newProducto.getNombre(),
            newProducto.getId(),
            newProducto.getIngredientes(),
            newProducto.getCosto(),
            newProducto.getVecesVendido()
        )

    @classmethod
    def crearProductoPersonalizado(cls, Nnombre, ingredientes):
        """
        Crea un producto personalizado con el nombre y los ingredientes especificados.

        Args:
            Nnombre (str): El nombre del producto personalizado.
            ingredientes (dict): Un diccionario que contiene los ingredientes y sus cantidades.

        Returns:
            ProductoCaliente: El objeto ProductoCaliente creado.

        """
        from gestorAplicacion.comida.Ingrediente import Ingrediente
        for nombreIngrediente, cantidad in ingredientes.items():
            if not Ingrediente.verificacionExistenciaPorNombreI(nombreIngrediente):
                Ingrediente(nombreIngrediente)
        return ProductoCaliente(Nnombre, ingredientes)

    def procesoHornear(self, cocinero):
        """
        Método que simula el proceso de hornear un producto caliente.

        Parámetros:
        - cocinero: El objeto cocinero encargado de hornear el producto.

        Retorna:
        - El objeto cocinero después de haber activado el horno.

        """
        if cocinero.isHorno():
            return cocinero
        else:
            cocinero.setHorno(True)
            return cocinero
        

    def seleccionProcesosDeCocina(self):
        """
        Devuelve una lista de procesos de cocina seleccionados al azar.

        Returns:
            list: Lista de procesos de cocina seleccionados al azar.
        """
        procesos = ["Hornear", "Amasar", "Mezclar", "Fritar", "Asar", "Decoracion"]
        cuantosProcesos = randint(1, 3)
        numerosIndices = sample(range(6), cuantosProcesos)
        procesosFinales = [procesos[numero] for numero in numerosIndices]
        return procesosFinales