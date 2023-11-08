from random import randint

class Cliente:
    _sesion = None

    def __init__(self, nombre="", id=0, contrasena="", direccion=None, tipoDescuento=None, presupuesto=0):
        self._nombre = nombre
        self._id = id
        self._contrasena = contrasena
        self._direccionTXT = ""
        self._direccion = direccion
        self._tipoDescuento = tipoDescuento
        self._presupuesto = presupuesto
        self._canastaOrden = None
        self._canastaEnMano = None
        self._historialOrdenes = []
        self._cantidadOrdenes = 0
        self._panaderia = None
        self._recibos = []
        self._domiciliario = None

    def setNombre(self, nombre):
        self._nombre = nombre

    def setId(self, id):
        self._id = id

    def setContrasena(self, contrasena):
        self._contrasena = contrasena

    def setDireccionTXT(self, direccionTXT):
        self._direccionTXT = direccionTXT

    def setDireccion(self, direccion):
        self._direccion = direccion

    def setTipoDescuento(self, tipoDescuento):
        self._tipoDescuento = tipoDescuento

    def setPresupuesto(self, presupuesto):
        self._presupuesto = presupuesto

    def setCanastaEnMano(self, canastaEnMano):
        self._canastaEnMano = canastaEnMano

    def setDomiciliario(self, domiciliario):
        self._domiciliario = domiciliario

    def setRecibos(self, recibos):
        self._recibos = recibos

    def setPanaderia(self, panaderia):
        self._panaderia = panaderia

    def setCanastaOrden(self, canastaOrden):
        self._canastaOrden = canastaOrden

    def setHistorialOrdenes(self, historialOrdenes):
        self._historialOrdenes = historialOrdenes

    def setCantidadOrdenes(self, cantidadOrdenes):
        self._cantidadOrdenes = cantidadOrdenes

    def getNombre(self):
        return self._nombre

    def getId(self):
        return self._id
    
    def getContrasena(self):
        return self._contrasena

    def getDireccionTXT(self):
        return self._direccionTXT

    def getDireccion(self):
        return self._direccion

    def getTipoDescuento(self):
        return self._tipoDescuento

    def getPresupuesto(self):
        return self._presupuesto

    def getCanastaEnMano(self):
        return self._canastaEnMano

    def getHistorialOrdenes(self):
        return self._historialOrdenes

    def getCantidadOrdenes(self):
        return self._cantidadOrdenes

    def getPanaderia(self):
        return self._panaderia

    def setSesion(self, sesion):
        Cliente._sesion = sesion

    def getDomiciliario(self):
        return self._domiciliario
    
    def getRecibos(self):
        return self._recibos
    
    def getCanastaOrden(self):
        return self._canastaOrden
    
    def getCanastaEnMano(self):
        return self._canastaEnMano
    
    def getHistorialOrdenes(self):
        return self._historialOrdenes
    
    @classmethod
    def getSesion(cls):
        return cls._sesion
    
    @classmethod
    def setSesion(cls, sesion):
        cls._sesion = sesion

