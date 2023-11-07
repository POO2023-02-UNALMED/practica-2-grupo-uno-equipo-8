from gestorAplicacion.comida.Ingrediente import Ingrediente
from gestorAplicacion.comida.Producto import Producto


class Inventario:
    def __init__(self, panaderia):
        self.panaderia = panaderia
        self.invIngredientes = []
        self.invProductos = []
        self.maxCantidad = 20

    # Getter y setter para panaderia
    def getPanaderia(self):
        return self.panaderia

    def setPanaderia(self, panaderia):
        self.panaderia = panaderia

    # Getter y setter para invIngredientes
    def getInvIngredientes(self):
        return self.invIngredientes

    def setInvIngredientes(self, invIngredientes):
        self.invIngredientes = invIngredientes

    # Getter y setter para invProductos
    def getInvProductos(self):
        return self.invProductos

    def setInvProductos(self, invProductos):
        self.invProductos = invProductos

    # Getter y setter para maxCantidad
    def getMaxCantidad(self):
        return self.maxCantidad

    def setMaxCantidad(self, maxCantidad):
        self.maxCantidad = maxCantidad
        

    def verificarCantidadIngredientePorNombre(self, ingrd):
        contador = 0
        for ingrediente in self.invIngredientes:
            if ingrediente.getNombre() == ingrd:
                contador += 1
        return contador

    
    def revisarCantidadIngredientes(self, ingredientesNecesarios):
        ingredientesFaltantes = {}
        for ingrediente, cantidad in ingredientesNecesarios.items():
            cantidadExistente = self.verificarCantidadIngredientePorNombre(ingrediente)
            if cantidadExistente - cantidad < 0:
                ingredientesFaltantes[ingrediente] = (cantidadExistente - cantidad) * (-2)
        return ingredientesFaltantes



