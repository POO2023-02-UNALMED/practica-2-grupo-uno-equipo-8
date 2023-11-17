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
    def getBaseDatosIngredientes(cls):
        return cls._baseDatosIngredientes
    
    @classmethod
    def setBaseDatosIngredientes(cls,baseDatosIngredientes):
        cls._baseDatosIngredientes = baseDatosIngredientes
    
    @classmethod
    def verificacionExistenciaPorNombreI(cls,nombre):
        existe = False
        for ingrediente in cls._baseDatosIngredientes:
            if ingrediente._nombre == nombre:
                existe = True
                break
        return existe
    
    @classmethod
    def verificacionExistenciaPorIdI(cls,id):
        existe = False
        for ingrediente in cls._baseDatosIngredientes:
            if ingrediente._id == id:
                existe = True
                break
        return existe

    @classmethod
    def obtenerObjetoPorNombreI(cls,nombre):
        for ingrediente in cls._baseDatosIngredientes:
            if ingrediente._nombre == nombre:
                return ingrediente
        return None
    
    @classmethod
    def obtenerObjetoPorIdI(cls,id):
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
    def verificarExistenciaPorNombreP(cls,nombre):
        existe = False
        for producto in cls.baseDatosProductos:
            if producto.getNombre() == nombre:
                existe = True
                break
        return existe
    
    @classmethod
    def verificarExistenciaPorIdP(cls,id):
        existe = False
        for producto in cls.baseDatosProductos:
            if producto.getId() == id:
                existe = True
        return existe
    
    @classmethod
    def obtenerObjetoPorNombreP(cls,nombre):
        producto = None
        for productoActual in cls.baseDatosProductos:
            if productoActual.getNombre() == nombre:
                producto = productoActual
        return producto
    
    @classmethod
    def obtenerObjetoPorIdP(cls,id):
        producto = None
        for productoActual in cls.baseDatosProductos:
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
