from gestorAplicacion.comida.Producto import Producto

class ProductoCaliente(Producto):
    def __init__(self, nombre, ids, ingredientes, costo, vecesVendido):
        super().__init__(nombre, ids, ingredientes, costo, vecesVendido)
        self._horno = False

    
    def horno(self):
        return self._horno

    def horno(self, value):
        self._horno = value
