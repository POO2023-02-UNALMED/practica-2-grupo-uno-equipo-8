from gestorAplicacion.comida.Producto import Producto

class ProductoCaliente(Producto):
    def __init__(self, nombre, ids, ingredientes, costo, vecesVendido):
        super().__init__(nombre, ids, ingredientes, costo, vecesVendido)
        self._horno = False

    
    def getHorno(self):
        return self._horno

    def setHorno(self, value):
        self._horno = value
