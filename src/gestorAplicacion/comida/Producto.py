import random
from comida.Ingrediente import Ingrediente
from comida.ComidaDefault import ComidaDefault

class Producto(ComidaDefault):
    topMasVendidos = []
    
    def __init__(self, nombre, ingredientes, id=None, vecesVendido=0, costo=None):
        self.nombre = nombre
        self.ingredientes = ingredientes
        if vecesVendido is None:
            self.vecesVendido = 0
        else:
            self.vecesVendido = vecesVendido+1
        self.costo = self.calcularCosto()

        if id is None:
            Producto.baseDatosProductos.append(self)
        self.id = id if id is not None else str(Producto.obtener_proximo_id())
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
        newProducto = Producto.obtenerObjetoPorIdP(Nnombre)
        return Producto(newProducto.getNombre(),newProducto.getIngredientes(), newProducto.getId(), newProducto.getCosto(), newProducto.getVecesVendido())

    def crearProductoPersonalizado(Nnombre, ingredientes):
        for ingrediente, cantidad in ingredientes.items():
            if not ComidaDefault.verificacionExistenciaPorNombreI(ingrediente):
                Ingrediente(ingrediente)
        return Producto(Nnombre, ingredientes)

    def calcularCosto(self):
        costo = 0
        for ingrediente, cantidad in self.ingredientes.items():
            costo += Producto.obtenerObjetoPorNombreI(ingrediente).getPrecioDeVenta() * cantidad
        return costo * ComidaDefault.tarifaGanancias
    
    @staticmethod
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
        for i in range(len(ComidaDefault.baseDatosProductos)):
            for j in range(len(ComidaDefault.baseDatosProductos)):
                if ComidaDefault.baseDatosProductos[i].getVecesVendido() > ComidaDefault.baseDatosProductos[j].getVecesVendido():
                    aux = ComidaDefault.baseDatosProductos[i]
                    ComidaDefault.baseDatosProductos[i] = ComidaDefault.baseDatosProductos[j]
                    ComidaDefault.baseDatosProductos[j] = aux

        for i in range(len(ComidaDefault.baseDatosProductos)):
            if i < 5:
                Producto.topMasVendidos.append(ComidaDefault.baseDatosProductos[i])


