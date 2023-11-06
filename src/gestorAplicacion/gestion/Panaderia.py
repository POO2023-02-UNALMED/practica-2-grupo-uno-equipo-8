from gestorAplicacion.comida.Ingrediente import Ingrediente
from gestorAplicacion.comida.Producto import Producto
from gestorAplicacion.comida.ProductoFrio import ProductoFrio
from gestorAplicacion.humanos.Cocinero import Cocinero
from gestorAplicacion.humanos.Domiciliario import Domiciliario
from gestorAplicacion.humanos.Cliente import Cliente
from gestorAplicacion.humanos.Catastrofe import Catastrofe
from gestorAplicacion.humanos.Trabajador import Trabajador

class Panaderia():

    _canastaDelDia = None

    def __init__(self, trabajadores = None, cocineros = None, domiciliarios = None, clientes = None, dinero = 1000000, deudas = 0, quiebra = False, canastasP = None, inventario = None):
        
        if trabajadores == None:
            trabajadores = []

        if cocineros == None:
            cocineros = []

        if domiciliarios == None:
            domiciliarios = []

        if clientes == None:
            clientes = []

        if canastasP == None:
            canastasP = []

        self._trabajadores = trabajadores
        self._cocineros = cocineros
        self._domiciliarios = domiciliarios
        self._clientes = clientes
        self._dinero = dinero
        self._valorDeudas = deudas
        self._enQuiebra = quiebra
        self._canastasPublicadas = canastasP
        self._inventario = Inventario()

    def getTrabajadores(self):
        return self._trabajadores

    def setTrabajadores(self, value):
        self._trabajadores = value

    def getCocineros(self):
        return self._cocineros

    def setCocineros(self, value):
        self._cocineros = value

    def getDomiciliarios(self):
        return self._domiciliarios

    def setDomiciliarios(self, value):
        self._domiciliarios = value

    def getClientes(self):
        return self._clientes

    def setClientes(self, value):
        self._clientes = value

    def getDinero(self):
        return self._dinero

    def setDinero(self, value):
        self._dinero = value

    def getValorDeudas(self):
        return self._valorDeudas

    def setValorDeudas(self, value):
        self._valorDeudas = value

    def getEnQuiebra(self):
        return self._enQuiebra

    def setEnQuiebra(self, value):
        self._enQuiebra = value

    def getCanastasPublicadas(self):
        return self._canastasPublicadas

    def setCanastasPublicadas(self, value):
        self._canastasPublicadas = value

    def getInventario(self):
        return self._inventario

    def setInventario(self, value):
        self._inventario = value
