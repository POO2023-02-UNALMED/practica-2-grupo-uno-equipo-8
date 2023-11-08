from gestorAplicacion.comida.Ingrediente import Ingrediente
from gestorAplicacion.comida.Producto import Producto


class Inventario:
    def __init__(self, panaderia):
        self._panaderia = panaderia
        self._invIngredientes = []
        self._invProductos = []
        self._maxCantidad = 20

    # Getter y setter para panaderia
    def getPanaderia(self):
        return self._panaderia

    def setPanaderia(self, panaderia):
        self._panaderia = panaderia

    # Getter y setter para invIngredientes
    def getInvIngredientes(self):
        return self._invIngredientes

    def setInvIngredientes(self, invIngredientes):
        self._invIngredientes = invIngredientes

    # Getter y setter para invProductos
    def getInvProductos(self):
        return self._invProductos

    def setInvProductos(self, invProductos):
        self._invProductos = invProductos

    # Getter y setter para maxCantidad
    def getMaxCantidad(self):
        return self._maxCantidad

    def setMaxCantidad(self, maxCantidad):
        self._maxCantidad = maxCantidad
        

    def verificarCantidadIngredientePorNombre(self, ingrd):
        contador = 0
        for ingrediente in self._invIngredientes:
            if ingrediente.getNombre() == ingrd:
                contador += 1
        return contador

    def verificarCantidadIngredientePorId(self,ingrd):
        contador = 0
        for ingrediente in self._invIngredientes:
            if ingrediente.getId() == ingrd:
                contador += 1
        return contador

    def verificarCantidadProductoPorId(self,prdct):
        contador = 0
        for producto in self._invProductos:
            if producto.getId() == prdct:
                contador += 1
        return contador

    def verificarCantidadProductoPorNombre(self,prdct):
        contador = 0
        for producto in self._invProductos:
            if producto.getNombre() == prdct:
                contador += 1
        return contador

    def buscarProductoPorId(self,id):
        for producto in self._invProductos:
            if producto.getId() == id:
                return producto
        return None
    
    def buscarProductoPorNombre(self,nombre):
        for producto in self._invProductos:
            if producto.getNombre() == nombre:
                return producto
        return None

    def buscarIngredientePorId(self,id):
        for ingrediente in self._invIngredientes:
            if ingrediente.getId() == id:
                return ingrediente
        return None
    
    def ingredientePorNombreBuscar(self,nombre):
        for ingrediente in self._invIngredientes:
            if ingrediente.getNombre() == nombre:
                return ingrediente
        return None

    def revisarCantidadIngredientes(self, ingredientesNecesarios):
        ingredientesFaltantes = {}
        for ingrediente, cantidad in ingredientesNecesarios.items():
            cantidadExistente = self.verificarCantidadIngredientePorNombre(ingrediente)
            if cantidadExistente - cantidad < 0:
                ingredientesFaltantes[ingrediente] = (cantidadExistente - cantidad) * (-2)
        return ingredientesFaltantes

