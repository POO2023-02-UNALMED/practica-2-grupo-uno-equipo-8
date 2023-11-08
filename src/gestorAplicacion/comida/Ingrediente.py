import random

from gestorAplicacion.comida import Producto
from gestorAplicacion.gestion.Panaderia import Panaderia
import math


class Ingrediente:
    _baseDatosIngredientes = []
    _cantidadIngredientesUnicos = 0
    probabilidadConstante = 1
    _topMasVendidos = []

    def __init__(self, nombre, identificador=None, precioVenta=None, precioCompra=None, vecesVendido=None):
        self._nombre = nombre
        if identificador is None:
            aleatorio = random.Random()
            numeroAleatorio = aleatorio.randint(300, 3000)
            self._precioDeCompra = numeroAleatorio
            self._precioDeVenta = math.ceil(numeroAleatorio * ComidaDefault.tarifaGanancias)
            Ingrediente.cantidadIngredientesUnicos += 1
            self._id = str(Ingrediente.cantidadIngredientesUnicos + Producto.cantidadProductosUnicos)
            Ingrediente.baseDatosIngredientes.append(self)
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

    @staticmethod
    def getCantidadIngredientesUnicos():
        return Ingrediente._cantidadIngredientesUnicos

    @staticmethod
    def setCantidadIngredientesUnicos(NewcantidadIngredientesUnicos):
        Ingrediente._cantidadIngredientesUnicos = NewcantidadIngredientesUnicos

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

    @staticmethod
    def getBaseDatosIngredientes():
        return Ingrediente._baseDatosIngredientes
    
    @staticmethod
    def setBaseDatosIngredientes(baseDatosIngredientes):
        Ingrediente._baseDatosIngredientes = baseDatosIngredientes

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
    def verificacionExistenciaPorNombre(nombre):
        existe = False
        for ingrediente in Ingrediente._baseDatosIngredientes:
            if ingrediente._nombre == nombre:
                existe = True
                break
        return existe
    
    @staticmethod
    def verificarExistenciaPorId(id):
        existe = False
        for ingrediente in Ingrediente._baseDatosIngredientes:
            if ingrediente._id == id:
                existe = True
                break
        return existe

    @staticmethod
    def obtenerObjetoPorNombre(nombre):
        for ingrediente in Ingrediente._baseDatosIngredientes:
            if ingrediente._nombre == nombre:
                return ingrediente
        return None
    
    @staticmethod
    def obtenerObjetoPorId(id):
        for ingrediente in Ingrediente._baseDatosIngredientes:
            if ingrediente._id == id:
                return ingrediente
        return None
    
    @staticmethod
    def crearIngrediente(nombreId):
        if Ingrediente.verificacionExistenciaPorNombre(nombreId) or Ingrediente.verificacionExistenciaPorId(nombreId):
            ingredienteExistente = Ingrediente.obtenerObjetoPorNombre(nombreId)
            return Ingrediente(
                ingredienteExistente.getNombre(),
                ingredienteExistente.getId(),
                ingredienteExistente.getPrecioDeVenta(),
                ingredienteExistente.getPrecioDeCompra(),
                ingredienteExistente.getVecesVendido()
            )
        else:
            return Ingrediente(nombreId)

    def caducidad(self, ingrediente):
        ingrediente.set_caducado(False)
        caducidad = random.randint(0, 19)
        if caducidad == Ingrediente.probabilidadConstante:
            ingrediente.set_caducado(True)
            
    def revisarCaducidad(self, cantidad, panaderia):
        self.caducidad()
        vencido = self.isCaducado()
        if vencido:
            ingredienteId = self.getId()
            panaderia.getInventario().restarIngrediente(ingredienteId, cantidad)
            GestionCocinar.falloCaducado()
            self.setCaducado(False)

