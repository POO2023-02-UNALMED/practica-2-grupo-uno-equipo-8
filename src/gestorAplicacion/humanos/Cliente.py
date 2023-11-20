from gestorAplicacion.gestion.Canasta import Canasta
from gestorAplicacion.gestion.Panaderia import Panaderia
from random import randint as random
from enum import Enum

from UIMain.GestionCocinar import GestionCocinar
#from UIMain.GestionDomicilioCliente import GestionDomicilioCliente

class DescuentoPorTipo(Enum):
    """
    Enumeración que representa los tipos de descuento disponibles para un cliente.
    """

    ESTUDIANTE = 0.1
    PROFESOR = 0.1
    NINGUNO = 0
    SENIOR = 0.2
    EMPLEADO = 0.3

    def get_valor(self):
        """
        Devuelve el valor del descuento para el tipo de cliente.

        Returns:
            float: El valor del descuento.
        """
        return self.value

class Cliente:
    _sesion = None  # Variable de clase para almacenar la sesión del cliente
    _panaderia = None  # Variable de clase para almacenar la panadería asociada

    def __init__(self, nombre="", id=0, contrasena="", direccion=None, tipoDescuento=DescuentoPorTipo.NINGUNO, presupuesto=0):
        """
        Constructor de la clase Cliente.

        Parámetros:
        - nombre (str): Nombre del cliente.
        - id (int): Identificador único del cliente.
        - contrasena (str): Contraseña del cliente.
        - direccion (str): Dirección del cliente.
        - tipoDescuento (str): Tipo de descuento aplicado al cliente.
        - presupuesto (float): Presupuesto disponible para el cliente.
        """
        self._nombre = nombre  # Nombre del cliente
        self._id = id  # Identificador único del cliente
        self._contrasena = contrasena  # Contraseña del cliente
        self._direccionTXT = ""  # Dirección en formato de texto (posiblemente no se utiliza)
        self._direccion = direccion  # Dirección del cliente (puede ser un objeto, dependiendo de la implementación)
        self._tipoDescuento = tipoDescuento  # Tipo de descuento aplicado al cliente
        self._presupuesto = presupuesto  # Presupuesto disponible para el cliente
        self._canastaOrden = None  # Canasta actual que está siendo ordenada por el cliente
        self._canastaEnMano = None  # Canasta actual que el cliente tiene en su posesión
        self._historialOrdenes = []  # Lista para almacenar el historial de órdenes del cliente
        self._cantidadOrdenes = 0  # Número total de órdenes realizadas por el cliente
        self._recibos = []  # Lista para almacenar recibos de pago del cliente
        self._domiciliario = None  # Domiciliario asignado al cliente para entregas

    #getters y setters

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
        """
        Guarda una canasta en el historial de órdenes del cliente.

        Parameters:
        - canasta: La canasta a guardar en el historial.

        Returns:
        None
        """
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
        """
        Crea una nueva canasta a partir del historial de órdenes del cliente.

        Args:
            id (int): El identificador de la canasta a crear.

        Returns:
            Canasta: La nueva canasta creada a partir del historial de órdenes.

        """
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
        """
        Crea una canasta publicada a partir de un identificador.

        Args:
            id (int): El identificador de la canasta.

        Returns:
            Canasta: La canasta publicada creada.

        """
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
        """
        Publica una canasta en la panadería.

        Parameters:
        - canasta: La canasta a publicar.

        Returns:
        None
        """
        listaVacia = []
        listaVacia2 = []
        listaVacia3 = []
        canasta.setProductos(listaVacia)
        canasta.setIngredientes(listaVacia2)
        canasta.setKits(listaVacia3)
        canasta.setPagada(False)
        Cliente._panaderia.agregarCanastasPublicadas(canasta)

    def crearCanastaDelDia(self):
        """
        Crea una nueva canasta del día para el cliente.

        Returns:
            Canasta: La nueva canasta del día creada.
        """
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
        """
        Actualiza la calificación de un domiciliario.

        Args:
            domiciliario (Domiciliario): El domiciliario al que se le actualizará la calificación.
            calificacion (float): La calificación a agregar.

        Returns:
            None
        """
        calificacionVieja = domiciliario.getCalificacion()
        calificacionNueva = (calificacionVieja + calificacion) / 2
        domiciliario.setCalificacion(calificacionNueva)

    def calificarCocina(self, cocinero, calificacion):
        """
        Califica la cocina de un cocinero y actualiza su calificación promedio.

        Args:
            cocinero (Cocinero): El cocinero al que se le va a calificar la cocina.
            calificacion (float): La calificación que se va a asignar a la cocina.

        Returns:
            None
        """
        calificacionVieja = cocinero.getCalificacion()
        calificacionNueva = (calificacionVieja + calificacion) / 2
        cocinero.setCalificacion(calificacionNueva)

        for calificarCocinero in Cliente._panaderia.getCocineros():
            if cocinero.isTrabajo():
                Cliente._panaderia.reviewCocinero(calificarCocinero)
                cocinero.setTrabajo(False)

    def notaCocineros(self):
        """
        Calcula la calificación de los cocineros de la panadería y los califica.

        Returns:
            None
        """
        calificacion = GestionCocinar.notaCocina()
        for cocinero in Cliente._panaderia.getCocineros():
            if cocinero.isTrabajo():
                self._calificarCocina(cocinero, calificacion)

    def enviarCanastasADomicilio(self, canastas):
        """
        Envía las canastas a domicilio.

        Args:
            canastas (list): Lista de canastas a enviar.

        Returns:
            None
        """
        Cliente._panaderia.enviarDomicilio(canastas, self)
        calificacion = GestionDomicilioCliente.pedirCalificacion()
        self.calificarDomiciliario(self._domiciliario, calificacion)
        Cliente._panaderia.reviewDomiciliario(self._domiciliario)
        self.notaCocineros()

    def gestionDatosFaltantes(self, valorCompra):
        """
        Verifica los datos faltantes para realizar una compra.

        Args:
            valorCompra (float): El valor de la compra.

        Returns:
            str: Un mensaje indicando los datos faltantes. Si no faltan datos, retorna una cadena vacía.
        """
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
        """
        Verifies if the client has a valid address.

        Returns:
            bool: True if the client has a valid address, False otherwise.
        """
        return False if self._direccion is None else True

    def verificarPresupuesto(self, valorCompra):
        """
        Verifies if the client has enough budget to make a purchase.

        Args:
            valorCompra (float): The value of the purchase.

        Returns:
            bool: True if the client has enough budget, False otherwise.
        """
        return False if self._presupuesto <= valorCompra else True

    def verificarPresupuesto(self):
        """
        Verifies if the client has a budget.

        Returns:
            bool: True if the client has a budget, False otherwise.
        """
        return False if self._presupuesto == 0 else True

    def verificarDescuentoPorTipo(self):
        """
        Verifica si el cliente tiene un tipo de descuento asignado.

        Returns:
            bool: True si el cliente tiene un tipo de descuento asignado, False en caso contrario.
        """
        return False if self._tipoDescuento is None else True
    
    def establecerDomicilioValido(self, direccion, ciudad):
        """
        Establece el domicilio válido del cliente.

        Args:
            direccion (str): La dirección del domicilio.
            ciudad (str): La ciudad del domicilio.

        Returns:
            bool: True si se estableció el domicilio válido correctamente, False en caso contrario.
        """
        try:
            ciudad = ciudad.upper()
            ciudad_valida = self.Direccion[ciudad]
            self._direccion = ciudad_valida
        except Exception as e:
            return False

        self._direccionTXT = direccion
        return True

    def establecerPresupuestoValido(self, presupuesto, valorCompra):
        """
        Verifies if the budget is valid for a given purchase.

        Args:
            presupuesto (float): The available budget.
            valorCompra (float): The value of the purchase.

        Returns:
            bool: True if the budget is valid, False otherwise.
        """
        return True if presupuesto >= valorCompra else False

    def establecerDescuentoPorTipoValido(self, descuento):
        """
        Establece el descuento por tipo válido para el cliente.

        Parámetros:
        - descuento: str, el tipo de descuento a establecer.

        Retorna:
        - bool, True si se estableció el descuento correctamente, False en caso contrario.
        """
        try:
            descuento = descuento.upper()
            tipo_descuento = self.DescuentoPorTipo[descuento]
            self._tipoDescuento = tipo_descuento
        except Exception as e:
            return False
        return True

    def verificarContrasenaNueva(self, contrasena):
        """
        Verifica si la contraseña cumple con los requisitos mínimos.

        Args:
            contrasena (str): La contraseña a verificar.

        Returns:
            str: Un mensaje indicando si la contraseña es válida o no.
        """
        if len(contrasena) < 1:
            self._contrasena = contrasena
            return "La contraseña debe tener al menos 8 caracteres"
        else:
            return "Contraseña válida"
        
    # Métodos para la gestión de cuentas de los clientes

    @staticmethod
    def inicioSesionId(id):
        """
        Busca un cliente en la panadería por su identificador.

        Args:
            id (int): El identificador del cliente.

        Returns:
            Cliente or None: El objeto Cliente si se encuentra un cliente con el identificador dado, None en caso contrario.

        Raises:
            ValueError: Si el identificador del cliente no es un entero positivo.
        """
        if not isinstance(id, int) or id <= 0:
            raise ValueError("El identificador del cliente debe ser un entero positivo")
        for cliente in Cliente._panaderia.getClientes():
            if cliente.getId() == id:
                return cliente
        return None

    @classmethod
    def inicioSesionContrasena(cls, cliente, contrasena):
        """
        Verifies if the given password matches the client's password and sets the session if it does.

        Args:
            cls (class): The class itself.
            cliente (Cliente): The client object.
            contrasena (str): The password to be verified.

        Returns:
            str: A message indicating whether the login was successful or the password is incorrect.
        """
        if cliente.getContrasena() == contrasena:
            cls.setSesion(cliente)
            return "Inicio de sesión exitoso"
        else:
            return "Contraseña incorrecta"

    @classmethod
    def crearCuenta(cls, nombre, id, contrasena):
        """
        Crea una cuenta de cliente con el nombre, ID y contraseña proporcionados.

        Args:
            nombre (str): El nombre del cliente.
            id (int): El ID único del cliente.
            contrasena (str): La contraseña de la cuenta del cliente.

        Returns:
            str: Un mensaje indicando si la cuenta se creó con éxito o si ya existe una cuenta con el mismo ID.
        """
        for cliente in Cliente._panaderia.getClientes():
            if cliente.getId() == id:
                return "Ya existe una cuenta con ese ID"
        cliente = Cliente(nombre, id, contrasena)
        Cliente._panaderia._clientes.append(cliente)
        Cliente.setSesion(cliente)
        return "Cuenta creada con éxito"


    class Direccion(Enum):
        """
        Enumeración que representa las diferentes direcciones.
        """

        MEDELLIN = "Cerca"
        BOGOTA = "Lejos"
        ENVIGADO = "Medio"
        ITAGUI = "Cerca"

        def get_distancia(self):
            """
            Devuelve la distancia asociada a la dirección.
            :return: La distancia asociada a la dirección.
            """
            return self.value

#tuve que mover esta clase para que se cargara antes de cliente att Richard
#    class DescuentoPorTipo(Enum):
#        """
#        Enumeración que representa los tipos de descuento disponibles para un cliente.
#        """
#
#        ESTUDIANTE = 0.1
#        PROFESOR = 0.1
#        NINGUNO = 0
#        SENIOR = 0.2
#        EMPLEADO = 0.3
#
#        def get_valor(self):
#            """
#            Devuelve el valor del descuento para el tipo de cliente.
#
#            Returns:
#                float: El valor del descuento.
#            """
#            return self.value