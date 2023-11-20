import random

from gestorAplicacion.comida.ComidaDefault import ComidaDefault

class Producto(ComidaDefault):
    topMasVendidos = []
    
    def __init__(self, nombre, ingredientes, id=None, vecesVendido=0, costo=None):
        """
        Inicializa un objeto Producto con los siguientes atributos:

        Args:
            nombre (str): El nombre del producto.
            ingredientes (list): Una lista de los ingredientes del producto.
            id (str, optional): El identificador del producto. Si no se proporciona, se generará automáticamente. Default es None.
            vecesVendido (int, optional): El número de veces que se ha vendido el producto. Default es 0.
            costo (float, optional): El costo del producto. Si no se proporciona, se calculará automáticamente. Default es None.
        """
        self.nombre = nombre
        self.ingredientes = ingredientes
        if vecesVendido is None:
            self.vecesVendido = 0
        else:
            self.vecesVendido = vecesVendido+1
        self.costo = self.calcularCosto()

        if id is None:
            Producto.baseDatosProductos.append(self)
        self.id = id if id is not None else str(ComidaDefault.obtener_proximo_id())
        self.procesosDeCocina = []

    # Getter y Setter para el atributo 'nombre'
    def getNombre(self):
        return self.nombre

    def setNombre(self, nuevoNombre):
        self.nombre = nuevoNombre

    # Getter y Setter para el atributo 'ingredientes'
    def getIngredientes(self):
        return self.ingredientes

    def setIngredientes(self, nuevosIngredientes):
        self.ingredientes = nuevosIngredientes

    # Getter y Setter para el atributo 'vecesVendido'
    def getVecesVendido(self):
        return self.vecesVendido

    def setVecesVendido(self, nuevasVecesVendido):
        self.vecesVendido = nuevasVecesVendido

    # Getter y Setter para el atributo 'costo'
    def getCosto(self):
        return self.costo

    def setCosto(self, nuevoCosto):
        self.costo = nuevoCosto

    # Getter y Setter para el atributo 'id'
    def getId(self):
        return self.id

    def setId(self, nuevoId):
        self.id = nuevoId
        
    # Getter y Setter para el atributo 'procesosDeCocina'
    def getProcesosDeCocina(self):
        return self.procesosDeCocina
    
    def setProcesosDeCocina(self, nuevosProcesosDeCocina):
        self.procesosDeCocina = nuevosProcesosDeCocina
        
    # Getter y Setter para el atributo 'topMasVendidos'
    @staticmethod
    def getTopMasVendidos():
        return Producto.topMasVendidos
    
    @staticmethod
    def setTopMasVendidos(nuevoTopMasVendidos):
        Producto.topMasVendidos = nuevoTopMasVendidos
    

    def crearProducto(Nnombre):
        """
        Crea un nuevo objeto Producto a partir del nombre proporcionado.

        Parámetros:
        - Nnombre (str): El nombre del producto.

        Retorna:
        - Producto: El objeto Producto creado.

        """
        newProducto = Producto.obtenerObjetoPorIdP(Nnombre)
        return Producto(newProducto.getNombre(), newProducto.getIngredientes(), newProducto.getId(), newProducto.getCosto(), newProducto.getVecesVendido())

    def crearProductoPersonalizado(Nnombre, ingredientes):
        """
        Crea un producto personalizado con el nombre y los ingredientes especificados.

        Parámetros:
        - Nnombre (str): El nombre del producto personalizado.
        - ingredientes (dict): Un diccionario que contiene los ingredientes y sus cantidades.

        Retorna:
        - Producto: El objeto Producto creado.

        """
        from gestorAplicacion.comida.Ingrediente import Ingrediente
        for ingrediente, cantidad in ingredientes.items():
            if not Ingrediente.verificacionExistenciaPorNombreI(ingrediente):
                Ingrediente(ingrediente)
        return Producto(Nnombre, ingredientes)

    def calcularCosto(self):
        """
        Calcula el costo total del producto.

        Retorna el costo total del producto, teniendo en cuenta el precio de venta de los ingredientes
        y la tarifa de ganancias establecida.

        Returns:
            float: El costo total del producto.
        """
        from gestorAplicacion.comida.Ingrediente import Ingrediente
        costo = 0
        for ingrediente, cantidad in self.ingredientes.items():
            costo += Ingrediente.obtenerObjetoPorNombreI(ingrediente).getPrecioDeVenta() * cantidad
        return costo * ComidaDefault.tarifaGanancias
    
    @staticmethod
    def seleccionProcesosDeCocina():
        """
        Devuelve una lista de procesos de cocina seleccionados al azar.

        Returns:
            list: Lista de procesos de cocina seleccionados al azar.
        """
        procesos = ["Hornear", "Gelatinificar", "Amasar", "Mezclar", "Fritar", "Asar", "Congelar", "Licuar", "Decoracion"]

        cuantosProcesos = random.randint(1, 3)

        numerosIndices = []
        for i in range(cuantosProcesos):
            numerosDelProceso = None
            repetido = False
            while not numerosDelProceso or repetido:
                numerosDelProceso = random.randint(0, 8)  # Usamos 8, ya que hay 9 procesos en la lista
                repetido = numerosDelProceso in numerosIndices

            numerosIndices.append(numerosDelProceso)

        procesosFinales = [procesos[numero] for numero in numerosIndices]

        return procesosFinales
    
    @staticmethod
    def organizarTopMasVendidos():
        """
        Organiza los productos más vendidos en orden descendente según el número de veces vendido.
        Limpia la lista de productos más vendidos y luego realiza una comparación entre todos los productos
        en la base de datos de productos. Los productos se intercambian de posición si el número de veces vendido
        del producto actual es mayor que el número de veces vendido del producto siguiente.
        Finalmente, se agrega a la lista de productos más vendidos los primeros 5 productos de la base de datos
        ordenados por número de veces vendido.
        """
        Producto.topMasVendidos.clear()
        for i in range(len(ComidaDefault.baseDatosProductos)):
            for j in range(len(ComidaDefault.baseDatosProductos)):
                if ComidaDefault.baseDatosProductos[i].getVecesVendido() > ComidaDefault.baseDatosProductos[j].getVecesVendido():
                    aux = ComidaDefault.baseDatosProductos[i]
                    ComidaDefault.baseDatosProductos[i] = ComidaDefault.baseDatosProductos[j]
                    ComidaDefault.baseDatosProductos[j] = aux

        for i in range(len(ComidaDefault.baseDatosProductos)):
            if i < 5:
                Producto.topMasVendidos.append(ComidaDefault.baseDatosProductos[i])


