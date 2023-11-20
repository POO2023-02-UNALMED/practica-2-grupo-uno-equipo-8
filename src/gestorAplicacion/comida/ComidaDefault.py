class ComidaDefault:
    """
    Interfaz que define las tarifas y métodos por defecto para una comida.
    """

    _baseDatosIngredientes = []  # Base de datos de ingredientes
    _contador = 0  # Inicialización del contador único
    baseDatosProductos = []

    @classmethod
    def obtener_proximo_id(cls):
        cls._contador += 1
        return cls._contador

    # Tarifa por defecto para el servicio a domicilio.
    tarifaDomicilio = 2000

    # Tarifa por defecto para las ganancias.
    tarifaGanancias = 1.7

    # Tarifa por defecto para los impuestos.
    tarifaImpuestos = 0.19

    def getDescripcion(self):
        """
        Obtiene la descripción por defecto de la comida.
        """
        return "Ahora mismo no tenemos una descripcion para este producto, pero te invitamos a probarlo."

    @classmethod
    def setContador(cls,contador):
        cls._contador = contador

    @classmethod
    def getContador(cls):
        return cls._contador

    @classmethod
    def getBaseDatosIngredientes(cls):
        return cls._baseDatosIngredientes

    @classmethod
    def setBaseDatosIngredientes(cls,baseDatosIngredientes):
        cls._baseDatosIngredientes = baseDatosIngredientes

    @classmethod
    def verificacionExistenciaPorNombreI(cls, nombre):
        """
        Verifica si existe un ingrediente en la base de datos por su nombre.

        Args:
            cls (type): La clase ComidaDefault.
            nombre (str): El nombre del ingrediente a verificar.

        Returns:
            bool: True si el ingrediente existe, False en caso contrario.
        """
        existe = False
        for ingrediente in cls._baseDatosIngredientes:
            if ingrediente._nombre == nombre:
                existe = True
                break
        return existe

    @classmethod
    def verificacionExistenciaPorIdI(cls, id):
        """
        Verifica si existe un ingrediente en la base de datos por su ID.

        Args:
            cls (type): La clase ComidaDefault.
            id (int): El ID del ingrediente a verificar.

        Returns:
            bool: True si el ingrediente existe, False en caso contrario.
        """
        existe = False
        for ingrediente in cls._baseDatosIngredientes:
            if ingrediente._id == id:
                existe = True
                break
        return existe

    @classmethod
    def obtenerObjetoPorNombreI(cls, nombre):
        """
        Devuelve el objeto de ingrediente correspondiente al nombre dado.

        Parámetros:
        - cls: la clase ComidaDefault.
        - nombre: el nombre del ingrediente a buscar.

        Retorna:
        - El objeto de ingrediente correspondiente al nombre dado, si se encuentra.
        - None si no se encuentra ningún ingrediente con el nombre dado.
        """
        for ingrediente in cls._baseDatosIngredientes:
            if ingrediente._nombre == nombre:
                return ingrediente
        return None
    
    @classmethod
    def obtenerObjetoPorIdI(cls, id):
        """
        Devuelve el objeto de ingrediente correspondiente al ID proporcionado.

        Parámetros:
        - cls: la clase ComidaDefault.
        - id: el ID del ingrediente a buscar.

        Retorna:
        - El objeto de ingrediente correspondiente al ID proporcionado, o None si no se encuentra.

        """
        for ingrediente in cls._baseDatosIngredientes:
            if ingrediente._id == id:
                return ingrediente
        return None
    
    # Getter y Setter para el atributo 'baseDatosProductos'
    @classmethod
    def getBaseDatosProductos(cls):
        return cls.baseDatosProductos
    
    @classmethod
    def setBaseDatosProductos(cls,nuevaBaseDatosProductos):
        cls.baseDatosProductos = nuevaBaseDatosProductos

    @classmethod
    def verificarExistenciaPorNombreP(cls, nombre):
        """
        Verifica si existe un producto en la base de datos por su nombre.

        Args:
            cls (type): La clase ComidaDefault.
            nombre (str): El nombre del producto a buscar.

        Returns:
            bool: True si el producto existe, False en caso contrario.
        """
        existe = False
        for producto in cls.baseDatosProductos:
            if producto.getNombre() == nombre:
                existe = True
                break
        return existe
    
    @classmethod
    def verificarExistenciaPorIdP(cls, id):
        """
        Verifica si existe un producto en la base de datos de productos por su ID.

        Args:
            cls (type): La clase ComidaDefault.
            id (int): El ID del producto a verificar.

        Returns:
            bool: True si el producto existe, False de lo contrario.
        """
        existe = False
        for producto in cls.baseDatosProductos:
            if producto.getId() == id:
                existe = True
        return existe
    
    @classmethod
    def obtenerObjetoPorNombreP(cls, nombre):
        """
        Obtiene un objeto de tipo Producto por su nombre.

        Args:
            nombre (str): El nombre del producto a buscar.

        Returns:
            Producto: El objeto Producto encontrado, o None si no se encuentra.

        """
        from gestorAplicacion.comida.Producto import Producto
        producto = None
        for productoActual in Producto.baseDatosProductos:
            if productoActual.getNombre() == nombre:
                producto = productoActual
        return producto
    
    @classmethod
    def obtenerObjetoPorIdP(cls, id):
        """
        Obtiene un objeto Producto por su ID.

        Parámetros:
        - id: El ID del producto a buscar.

        Retorna:
        - El objeto Producto correspondiente al ID proporcionado, o None si no se encuentra.

        """
        from gestorAplicacion.comida.Producto import Producto
        producto = None
        for productoActual in Producto.baseDatosProductos:
            if productoActual.getId() == id:
                producto = productoActual
        return producto

    def getNutrientes(self, nombre):
        """
        Obtiene la información nutricional por porción de la comida.
        :param nombre: El nombre de la comida.
        :return: La información nutricional por porción de la comida.
        """
        m = (
            " _______________________________________________________ \n"
            f"|{'Producto: ' + nombre.center(48 - len(nombre))} |\n"
            "| Porcion: 30 g                                         |\n"
            "|_______________________________________________________| \n"
            "| Informacion nutricional por porcion                   |\n"
            "|______________________ ________ _______________________| \n"
            "| Energia              | 140 kcal| 7%% del valor diario  |\n"
            "|______________________ ________ _______________________|\n"
            "| Grasa total          | 6 g     | 9%% del valor diario  |\n"
            "| _ Grasa saturada     | 3 g     | 15%% del valor diario |\n"
            "| _ Grasa trans        | 0 g     |                      |\n"
            "|______________________ ________ _______________________| \n"
            "| Colesterol           | 0 mg    | 0%% del valor diario  |\n"
            "|______________________ ________ _______________________| \n"
            "| Sodio                | 75 mg   | 3%% del valor diario  |\n"
            "|______________________ ________ _______________________| \n"
            "| Carbohidratos totales| 20 g    | 7%% del valor diario  |\n"
            "| _ Fibra dietetica    | 1 g     | 4%% del valor diario  |\n"
            "| _ Azucares           | 10 g    |                      |\n"
            "|______________________ ________ _______________________| \n"
            "| Proteina             | 2 g     |                      |\n"
            "|______________________ ________ _______________________| \n"
            "| Vitamina A           | 0%% del valor diario            |\n"
            "| Vitamina C           | 0%% del valor diario            |\n"
            "| Calcio               | 2%% del valor diario            |\n"
            "| Hierro               | 6%% del valor diario            |\n"
            "|_______________________________________________________| \n"
        )
        return m
