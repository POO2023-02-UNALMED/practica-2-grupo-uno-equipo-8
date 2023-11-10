from gestorAplicacion.comida.Producto import Producto

class ProductoFrio(Producto):
    def __init__(self, nombre, ids, ingredientes, costo, vecesVendido, tiempoDeCongelamiento):
        super().__init__(nombre, ids, ingredientes, costo, vecesVendido)
        self._congelador = False
        self._tiempoDeCongelamiento = tiempoDeCongelamiento


    def congelador(self):
        return self._congelador


    def congelador(self, value):
        self._congelador = value


    def tiempoDeCongelamiento(self):
        return self._tiempoDeCongelamiento


    def tiempoDeCongelamiento(self, value):
        self._tiempoDeCongelamiento = value
