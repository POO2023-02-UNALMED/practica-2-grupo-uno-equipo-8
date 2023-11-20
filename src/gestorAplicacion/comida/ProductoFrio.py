from random import randint, sample

from gestorAplicacion.comida.Producto import Producto

import random

class ProductoFrio(Producto):
    def __init__(self, nombre, ingredientes, ids=None, costo=0, vecesVendido=0, tiempoDeCongelamiento=0):
        """
        Inicializa un objeto ProductoFrio.

        Args:
            nombre (str): El nombre del producto frío.
            ingredientes (list): La lista de ingredientes del producto frío.
            ids (int, optional): El identificador del producto frío. Por defecto es None.
            costo (float, optional): El costo del producto frío. Por defecto es 0.
            vecesVendido (int, optional): El número de veces que se ha vendido el producto frío. Por defecto es 0.
            tiempoDeCongelamiento (int, optional): El tiempo de congelamiento del producto frío en minutos. Por defecto es 0.
        """
        super().__init__(nombre, ingredientes, ids, costo, vecesVendido)
        self._congelador = False
        self._tiempoDeCongelamiento = tiempoDeCongelamiento

#getters y setters

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
        """
        Crea un nuevo objeto ProductoFrio a partir de un objeto Producto existente.

        Parámetros:
        - Nnombre: El nombre del producto existente.

        Retorna:
        - Un objeto ProductoFrio con los mismos atributos que el producto existente.

        """
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
        """
        Crea un producto personalizado con el nombre y los ingredientes especificados.

        Args:
            Nnombre (str): El nombre del producto personalizado.
            ingredientes (dict): Un diccionario que contiene los ingredientes y sus cantidades.

        Returns:
            ProductoFrio: El objeto ProductoFrio creado.

        """
        from gestorAplicacion.comida.Ingrediente import Ingrediente
        for nombre, cantidad in ingredientes.items():
            if not Ingrediente.verificacionExistenciaPorNombreI(nombre):
                Ingrediente(nombre)
        return ProductoFrio(Nnombre, ingredientes)
    

    def seleccionProcesosDeCocina(self):
        """
        Devuelve una lista de procesos de cocina seleccionados al azar.

        Returns:
            list: Lista de procesos de cocina seleccionados al azar.
        """
        procesos = ["Gelatinificar", "Amasar", "Mezclar", "Congelar", "Licuar", "Decoracion"]
        cuantosProcesos = randint(1, 3)
        numerosIndices = sample(range(6), cuantosProcesos)
        procesosFinales = [procesos[numero] for numero in numerosIndices]
        return procesosFinales
    
    def empaqueCongelador(self, domiciliario):
        """
        Método que verifica si el domiciliario tiene empaque frío y, en caso contrario, lo habilita.

        Args:
            domiciliario (Domiciliario): El objeto domiciliario a verificar y habilitar el empaque frío.

        Returns:
            Domiciliario: El objeto domiciliario con el empaque frío habilitado.
        """
        if domiciliario.isEmpaqueFrio():
            return domiciliario
        else:
            domiciliario.setEmpaqueFrio(True)
            return domiciliario
        
    def calcularCongelamiento(self):
        """
        Calcula el tiempo de congelamiento de un producto frío.

        Returns:
            int: El tiempo de congelamiento generado de forma aleatoria.
        """
        tiempoDeCongelamiento = random.randint(0, 19)
        return tiempoDeCongelamiento
    
    def procesoCongelamiento(self, cocinero):
        """
        Realiza el proceso de congelamiento del producto frío.

        Args:
            cocinero (Cocinero): El cocinero encargado del proceso.

        Returns:
            Cocinero: El cocinero después de realizar el proceso de congelamiento.
        """
        if cocinero.isNevera():
            return cocinero
        else:
            cocinero.setNevera(True)
            return cocinero
