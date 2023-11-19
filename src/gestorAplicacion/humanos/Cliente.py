from gestorAplicacion.gestion.Canasta import Canasta
from gestorAplicacion.gestion.Panaderia import Panaderia
from random import randint as random
from enum import Enum

class Cliente:
    _sesion = None
    _panaderia = None

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

    @classmethod
    def getPanaderia(cls):
        return cls._panaderia
    
    @classmethod
    def setPanaderia(cls, panaderia):
        cls._panaderia = panaderia

    def guardarCanastaEnHistorial(self, canasta):
        productosEnLista = {}
        ingredientesEnLista = {}
        kitsEnLista = {}

        if canasta.getProductosEnLista() is not None:
            productosEnLista.update(canasta.getProductosEnLista())
        if canasta.getIngredientesEnLista() is not None:
            ingredientesEnLista.update(canasta.getIngredientesEnLista())
        if canasta.getKitsEnLista() is not None:
            kitsEnLista.update(canasta.getKitsEnLista())

        identificador = canasta.getIdentificador()
        itemsTotalesEnCanasta = canasta.getItemsTotalesEnCanasta()
        itemsTotalesEnLista = canasta.getItemsTotalesEnLista()
        costoTotalEnLista = canasta.getCostoTotalEnLista()
        costoTrasDescuentoEnLista = canasta.getCostoTrasDescuentoEnLista()
        descuentoEnLista = canasta.getDescuentoEnLista()

        newCanasta = Canasta(productosEnLista, ingredientesEnLista, kitsEnLista, itemsTotalesEnCanasta, itemsTotalesEnLista, costoTotalEnLista, costoTrasDescuentoEnLista, descuentoEnLista, identificador)
        self._historialOrdenes.append(newCanasta)

    def crearCanastaPorHistorial(self, id):
        for canasta in self._historialOrdenes:
            if canasta.getIdentificador() == id:
                productosEnLista = {}
                ingredientesEnLista = {}
                kitsEnLista = {}

                if canasta.getProductosEnLista() is not None:
                    productosEnLista.update(canasta.getProductosEnLista())
                if canasta.getIngredientesEnLista() is not None:
                    ingredientesEnLista.update(canasta.getIngredientesEnLista())
                if canasta.getKitsEnLista() is not None:
                    kitsEnLista.update(canasta.getKitsEnLista())

                identificador = canasta.getIdentificador()
                itemsTotalesEnCanasta = canasta.getItemsTotalesEnCanasta()
                itemsTotalesEnLista = canasta.getItemsTotalesEnLista()
                costoTotalEnLista = canasta.getCostoTotalEnLista()
                costoTrasDescuentoEnLista = canasta.getCostoTrasDescuentoEnLista()
                descuentoEnLista = canasta.getDescuentoEnLista()

                newCanasta = Canasta(productosEnLista, ingredientesEnLista, kitsEnLista, itemsTotalesEnCanasta,itemsTotalesEnLista, costoTotalEnLista, costoTrasDescuentoEnLista, descuentoEnLista, identificador)
                self._cantidadOrdenes += 1
                self._canastaOrden = newCanasta
                self._canastaOrden.setIdentificador(str(self._cantidadOrdenes))
                break

        return self._canastaOrden
    
    def crearCanastaPublicada(self, id):
        if Cliente._panaderia.obtenerCanastaPorId(id) is None:
            return None
        else:
            canasta = Cliente._panaderia.obtenerCanastaPorId(id)
            productosEnLista = {}
            ingredientesEnLista = {}
            kitsEnLista = {}

            if canasta.getProductosEnLista() is not None:
                productosEnLista.update(canasta.getProductosEnLista())
            if canasta.getIngredientesEnLista() is not None:
                ingredientesEnLista.update(canasta.getIngredientesEnLista())
            if canasta.getKitsEnLista() is not None:
                kitsEnLista.update(canasta.getKitsEnLista())

            identificador = canasta.getIdentificador()
            itemsTotalesEnCanasta = canasta.getItemsTotalesEnCanasta()
            itemsTotalesEnLista = canasta.getItemsTotalesEnLista()
            costoTotalEnLista = canasta.getCostoTotalEnLista()
            costoTrasDescuentoEnLista = canasta.getCostoTrasDescuentoEnLista()
            descuentoEnLista = canasta.getDescuentoEnLista()

            newCanasta = Canasta(productosEnLista, ingredientesEnLista, kitsEnLista, itemsTotalesEnCanasta,itemsTotalesEnLista, costoTotalEnLista, costoTrasDescuentoEnLista, descuentoEnLista, identificador)
            self._cantidadOrdenes += 1
            self._canastaOrden = newCanasta
            self._canastaOrden.setIdentificador(str(self._cantidadOrdenes))

        return self._canastaOrden

    def publicarCanasta(self, canasta):
        listaVacia = []
        listaVacia2 = []
        listaVacia3 = []
        canasta.setProductos(listaVacia)
        canasta.setIngredientes(listaVacia2)
        canasta.setKits(listaVacia3)
        canasta.setPagada(False)
        Cliente._panaderia.agregarCanastasPublicadas(canasta)

    def crearCanastaDelDia(self):
        canasta = Panaderia.getCanastaDelDia()
        productosEnLista = {}
        ingredientesEnLista = {}
        kitsEnLista = {}

        if canasta.getProductosEnLista() is not None:
            productosEnLista.update(canasta.getProductosEnLista())
        if canasta.getIngredientesEnLista() is not None:
            ingredientesEnLista.update(canasta.getIngredientesEnLista())
        if canasta.getKitsEnLista() is not None:
            kitsEnLista.update(canasta.getKitsEnLista())

        identificador = canasta.getIdentificador()
        itemsTotalesEnCanasta = canasta.getItemsTotalesEnCanasta()
        itemsTotalesEnLista = canasta.getItemsTotalesEnLista()
        costoTotalEnLista = canasta.getCostoTotalEnLista()
        costoTrasDescuentoEnLista = canasta.getCostoTrasDescuentoEnLista()
        descuentoEnLista = canasta.getDescuentoEnLista()

        newCanasta = Canasta(productosEnLista, ingredientesEnLista, kitsEnLista, itemsTotalesEnCanasta,itemsTotalesEnLista, costoTotalEnLista, costoTrasDescuentoEnLista, descuentoEnLista, identificador)
        self._cantidadOrdenes += 1
        self._canastaOrden = newCanasta
        self._canastaOrden.setIdentificador(str(self._cantidadOrdenes))
        return self._canastaOrden
    
    def crearCanastaNueva(self):
        canasta = Canasta()
        self._canastaOrden = canasta
        self._cantidadOrdenes += 1
        self._canastaOrden.setIdentificador(str(self._cantidadOrdenes))
        return self._canastaOrden

    def publicarCanasta(self, canasta, calificacion=5, comentario=""):
        listaVacia = []
        listaVacia2 = []
        listaVacia3 = []

        identificadorActual = int(canasta.getIdentificador())
        nuevoIdentificador = identificadorActual + random.randint(0, 1000)

        canasta.setIdentificador(str(nuevoIdentificador))
        canasta.setProductos(listaVacia)
        canasta.setIngredientes(listaVacia2)
        canasta.setKits(listaVacia3)
        canasta.setPagada(False)
        canasta.setCalificacion(calificacion)
        canasta.setComentario(comentario)
        Cliente._panaderia.agregarCanastasPublicadas(canasta)

    def calificarDomiciliario(self, domiciliario, calificacion):
        calificacionVieja = domiciliario.getCalificacion()
        calificacionNueva = (calificacionVieja + calificacion) / 2
        domiciliario.setCalificacion(calificacionNueva)

    def calificarCocina(self, cocinero, calificacion):
        calificacionVieja = cocinero.getCalificacion()
        calificacionNueva = (calificacionVieja + calificacion) / 2
        cocinero.setCalificacion(calificacionNueva)

        for calificarCocinero in Cliente._panaderia.getCocineros():
            if cocinero.isTrabajo():
                Cliente._panaderia.reviewCocinero(calificarCocinero)
                cocinero.setTrabajo(False)

    def notaCocineros(self):
        calificacion = GestionCocinar.gestionCocina()
        for cocinero in Cliente._panaderia.getCocineros():
            if cocinero.isTrabajo():
                self._calificarCocina(cocinero, calificacion)

    def enviarCanastasADomicilio(self, canastas):
        Cliente._panaderia.enviarDomicilio(canastas, self)
        calificacion = GestionDomicilioCliente.pedirCalificacion()
        self.calificarDomiciliario(self._domiciliario, calificacion)
        Cliente._panaderia.reviewDomiciliario(self._domiciliario)
        self.notaCocineros()

    def gestionDatosFaltantes(self, valorCompra):
        x = self.verificarDireccion()
        y = self.verificarPresupuesto(valorCompra)
        z = self.verificarDescuentoPorTipo()

        if not x and y and z:
            return "Falta dirección"
        elif not x and not y and z:
            return "Falta dirección y presupuesto"
        elif not x and y and not z:
            return "Falta dirección y descuento"
        elif x and not y and z:
            return "Falta presupuesto"
        elif x and not y and not z:
            return "Falta presupuesto y descuento"
        elif x and y and not z:
            return "Falta descuento"
        else:
            return ""

    def verificarDireccion(self):
        return False if self._direccion is None else True

    def verificarPresupuesto(self, valorCompra):
        return False if self._presupuesto <= valorCompra else True

    def verificarPresupuesto(self):
        return False if self._presupuesto == 0 else True

    def verificarDescuentoPorTipo(self):
        return False if self._tipoDescuento is None else True
    
    def establecerDomicilioValido(self, direccion, ciudad):
        try:
            ciudad = ciudad.upper()
            ciudad_valida = self.Direccion[ciudad]
            self._direccion = ciudad_valida
        except Exception as e:
            return False

        self._direccionTXT = direccion
        return True

    def establecerPresupuestoValido(self, presupuesto, valorCompra):
        return True if presupuesto >= valorCompra else False

    def establecerDescuentoPorTipoValido(self, descuento):
        try:
            descuento = descuento.upper()
            tipo_descuento = self.DescuentoPorTipo[descuento]
            self._tipoDescuento = tipo_descuento
        except Exception as e:
            return False
        return True

    def verificarContrasenaNueva(self, contrasena):
        if len(contrasena) < 8:
            self._contrasena = contrasena
            return "La contraseña debe tener al menos 8 caracteres"
        else:
            return "Contraseña válida"
        
    # Métodos para la gestión de cuentas de los clientes

    @staticmethod
    def inicioSesionId(id):
        for cliente in Cliente._panaderia.getClientes():
            if cliente.getId() == id:
                return cliente
        return None

    @classmethod
    def inicioSesionContrasena(cls,cliente, contrasena):
        if not isinstance(cliente, int) or cliente <= 0:
            raise ValueError("El identificador del cliente debe ser un entero positivo")
        if cliente.getContrasena() == contrasena:
            cls.setSesion(cliente)
            return "Inicio de sesión exitoso"
        else:
            return "Contraseña incorrecta"

    def crearCuenta(self,nombre, id, contrasena):
        cliente = Cliente(nombre, id, contrasena)
        Cliente._panaderia._clientes.append(cliente)
        Cliente.setSesion(cliente)
        return "Cuenta creada con éxito"


    class Direccion(Enum):
        MEDELLIN = "Cerca"
        BOGOTA = "Lejos"
        ENVIGADO = "Medio"
        ITAGUI = "Cerca"

        def get_distancia(self):
            return self.value

    class DescuentoPorTipo(Enum):
        ESTUDIANTE = 0.1
        PROFESOR = 0.1
        NINGUNO = 0
        SENIOR = 0.2
        EMPLEADO = 0.3

        def get_valor(self):
            return self.value