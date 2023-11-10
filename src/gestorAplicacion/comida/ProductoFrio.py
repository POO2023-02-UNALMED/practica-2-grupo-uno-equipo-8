from gestorAplicacion.comida.Producto import Producto

class ProductoFrio(Producto):
    def __init__(self, nombre, ids, ingredientes, costo, vecesVendido, tiempoDeCongelamiento):
        super().__init__(nombre, ids, ingredientes, costo, vecesVendido)
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
