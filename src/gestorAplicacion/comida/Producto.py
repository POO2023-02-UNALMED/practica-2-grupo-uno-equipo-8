import random
from gestorAplicacion.comida import Ingrediente

class Producto:
    cantidadProductosUnicos = 0
    baseDatosProductos = []
    topMasVendidos = []
    
    def __init__(self, nombre, id=None, ingredientes=None, costo=None, vecesVendido=None):
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.vecesVendido = vecesVendido
        self.costo = self.calcularCosto()
        self.id = id if id is not None else str(Producto.cantidadProductosUnicos + Ingrediente.getCantidadIngredientesUnicos())
        self.procesosDeCocina = []
        
        if id is None:
            Producto.cantidadProductosUnicos += 1
            Producto.baseDatosProductos.append(self)
            
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
        
    # Getter y Setter para el atributo 'cantidadProductosUnicos'
    @staticmethod
    def getCantidadProductosUnicos():
        return Producto.cantidadProductosUnicos
    
    @staticmethod
    def setCantidadProductosUnicos(nuevaCantidadProductosUnicos):
        Producto.cantidadProductosUnicos = nuevaCantidadProductosUnicos
        
    # Getter y Setter para el atributo 'baseDatosProductos'
    @staticmethod
    def getBaseDatosProductos():
        return Producto.baseDatosProductos
    
    @staticmethod
    def setBaseDatosProductos(nuevaBaseDatosProductos):
        Producto.baseDatosProductos = nuevaBaseDatosProductos
        
    # Getter y Setter para el atributo 'topMasVendidos'
    @staticmethod
    def getTopMasVendidos():
        return Producto.topMasVendidos
    
    @staticmethod
    def setTopMasVendidos(nuevoTopMasVendidos):
        Producto.topMasVendidos = nuevoTopMasVendidos
        
    @staticmethod
    def verificarExistenciaPorNombre(nombre):
        existe = False
        for producto in Producto.baseDatosProductos:
            if producto.getNombre() == nombre:
                existe = True
                break
        return existe
    
    @staticmethod
    def verificarExistenciaPorId(id):
        existe = False
        for producto in Producto.baseDatosProductos:
            if producto.getId() == id:
                existe = True
        return existe
    
    @staticmethod
    def obtenerObjetoPorNombre(nombre):
        producto = None
        for productoActual in Producto.baseDatosProductos:
            if productoActual.getNombre() == nombre:
                producto = productoActual
        return producto
    
    @staticmethod
    def obtenerObjetoPorId(id):
        producto = None
        for productoActual in Producto.baseDatosProductos:
            if productoActual.getId() == id:
                producto = productoActual
        return producto
    
    @staticmethod
    def crearProducto(Nnombre):
        newProducto = Producto.obtenerObjetoPorId(Nnombre)
        return Producto(newProducto.getNombre(), newProducto.getId(), newProducto.getIngredientes(), newProducto.getCosto(), newProducto.getVecesVendido())
    
    @staticmethod
    def crearProductoPersonalizado(Nnombre, ingredientes):
        for ingrediente, cantidad in ingredientes.items():
            if not Ingrediente.verificacionExistenciaPorNombre(ingrediente):
                Ingrediente(ingrediente)

        return Producto(Nnombre, ingredientes)
    
    def calcularCosto(self):
        costo = 0
        for ingrediente, cantidad in self.ingredientes.items():
            costo += Ingrediente.obtenerObjetoPorNombre(ingrediente).getPrecioDeVenta() * cantidad
        return costo * ComidaDefault.tarifaGanancias
    
    def seleccionProcesosDeCocina():
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
        Producto.topMasVendidos.clear()
        for i in range(len(Producto.baseDatosProductos)):
            for j in range(len(Producto.baseDatosProductos)):
                if Producto.baseDatosProductos[i].getVecesVendido() > Producto.baseDatosProductos[j].getVecesVendido():
                    aux = Producto.baseDatosProductos[i]
                    Producto.baseDatosProductos[i] = Producto.baseDatosProductos[j]
                    Producto.baseDatosProductos[j] = aux

        for i in range(len(Producto.baseDatosProductos)):
            if i < 5:
                Producto.topMasVendidos.append(Producto.baseDatosProductos[i])


