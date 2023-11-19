import random

from gestorAplicacion.comida.ComidaDefault import ComidaDefault
import math

class Ingrediente(ComidaDefault):
    probabilidadConstante = 1
    _topMasVendidos = []
    contador1 = 0

    def __init__(self, nombre, identificador=None, precioVenta=None, precioCompra=None, vecesVendido=None):
        from gestorAplicacion.comida.Producto import Producto
        self._nombre = nombre
        if identificador is None:
            aleatorio = random.Random()
            numeroAleatorio = aleatorio.randint(300, 3000)
            self._precioDeCompra = numeroAleatorio
            self._precioDeVenta = math.ceil(numeroAleatorio * ComidaDefault.tarifaGanancias)
            self._id = str(ComidaDefault.obtener_proximo_id())
            Ingrediente.getBaseDatosIngredientes().append(self)
            self._vecesVendido = 0
            self._caducado = False
            self._inventario = None
        else:
            self._id = identificador
            self._precioDeVenta = precioVenta
            self._precioDeCompra = precioCompra
            self._vecesVendido = vecesVendido

    def getNombre(self):
        return self._nombre

    def setNombre(self, Newnombre):
        self._nombre = Newnombre

    def getId(self):
        return self._id

    def setId(self, Newid):
        self._id = Newid

    def getPrecioDeVenta(self):
        return self._precioDeVenta

    def setPrecioDeVenta(self, precioDeVenta):
        self._precioDeVenta = precioDeVenta

    def getPrecioDeCompra(self):
        return self._precioDeCompra

    def setPrecioDeCompra(self, precioDeCompra):
        self._precioDeCompra = precioDeCompra

    def getVecesVendido(self):
        return self._vecesVendido

    def setVecesVendido(self, vecesVendido):
        self._vecesVendido = vecesVendido

    def isCaducado(self):
        return self._caducado

    def setCaducado(self, caducado):
        self._caducado = caducado

    def getInventario(self):
        return self._inventario

    def setInventario(self, inventario):
        self._inventario = inventario

    @staticmethod
    def getTopMasVendidos():
        return Ingrediente._topMasVendidos
    
    @staticmethod
    def getProbabilidadConstante():
        return Ingrediente.probabilidadConstante

    @classmethod
    def getTopMasVendidos(cls):
        return cls._topMasVendidos

    @classmethod
    def setTopMasVendidos(cls, topMasVendidos):
        cls._topMasVendidos = topMasVendidos

    @classmethod
    def crearIngrediente(cls,nombreId):
        if Ingrediente.verificacionExistenciaPorNombreI(nombreId) or Ingrediente.verificacionExistenciaPorIdI(nombreId):
            ingredienteExistente = Ingrediente.obtenerObjetoPorNombreI(nombreId)
            return Ingrediente(
                ingredienteExistente.getNombre(),
                ingredienteExistente.getId(),
                ingredienteExistente.getPrecioDeVenta(),
                ingredienteExistente.getPrecioDeCompra(),
                ingredienteExistente.getVecesVendido()
            )
        else:
            return Ingrediente(nombreId)

    def caducidad(cls, ingrediente):
        ingrediente.setCaducado(False)
        caducidad = random.randint(0, 19)
        if caducidad == cls.probabilidadConstante:
            ingrediente.setCaducado(True)
            
    def revisarCaducidad(self, cantidad, panaderia):
        self.caducidad(self)
        vencido = self.isCaducado()
        if vencido:
            ingredienteId = self.getId()
            panaderia.getInventario().restarIngrediente(ingredienteId, cantidad)
            #GestionCocinar.falloCaducado()
            self.setCaducado(False)
    
    #cambiar
    @classmethod
    def organizarTopMasVendidos(cls):
        Ingrediente._topMasVendidos.clear()
        for i in range(len(ComidaDefault._baseDatosIngredientes)):
            for j in range(len(ComidaDefault._baseDatosIngredientes)):
                if (ComidaDefault._baseDatosIngredientes[i].getVecesVendido() >
                    ComidaDefault._baseDatosIngredientes[j].getVecesVendido()):
                    aux = ComidaDefault._baseDatosIngredientes[i]
                    ComidaDefault._baseDatosIngredientes[i] = ComidaDefault._baseDatosIngredientes[j]
                    ComidaDefault._baseDatosIngredientes[j] = aux

        for i in range(len(ComidaDefault._baseDatosIngredientes)):
            if i < 5:
                Ingrediente._topMasVendidos.append(ComidaDefault._baseDatosIngredientes[i])