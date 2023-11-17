from humanos.Catastrofe import Catastrofe
from gestorAplicacion.comida.Ingrediente import Ingrediente
from humanos.Trabajador import Trabajador
from gestorAplicacion.comida.ComidaDefault import ComidaDefault

class Domiciliario(Trabajador, ComidaDefault):
    def __init__(self, nombre="", panaderia=None, habilidad=None, calificacion=None, dineroEnMano=None, licencia=None):
        super().__init__(panaderia, nombre, habilidad, calificacion, dineroEnMano)
        self.licencia = False if licencia is None else licencia
        self.ocupado = False
        self.canasta = None
        self.empaqueFrio = False
        self.panaderia = panaderia
        panaderia.getDomiciliarios().append(self)

    def isLicencia(self):
        return self.licencia

    def setLicencia(self, licencia):
        self.licencia = licencia

    def isOcupado(self):
        return self.ocupado

    def setOcupado(self, ocupado):
        self.ocupado = ocupado

    def getCanasta(self):
        return self.canasta

    def setCanasta(self, canasta):
        self.canasta = canasta

    def isEmpaqueFrio(self):
        return self.empaqueFrio

    def setEmpaqueFrio(self, empaqueFrio):
        self.empaqueFrio = empaqueFrio

    def getPanaderia(self):
        return self.panaderia

    def setPanaderia(self, panaderia):
        self.panaderia = panaderia

    def calcularCostoDomicilio(self, cliente, canasta):
        productos = canasta.getProductos()
        costo = sum(producto.getCosto() for producto in productos)
        if len(productos) > 15:
            costo *= 0.7

        direccion = cliente.getDireccion()
        if direccion.getDistancia() == "Medio":
            costo += 10000
        if direccion.getDistancia() == "Lejos":
            costo += 20000

        costo += ComidaDefault.tarifaDomicilio
        costo *= ComidaDefault.tarifaGanancias
        return costo

    def laborParticular(self, canasta):
        transito = Catastrofe()
        if not transito.paradaTransito(self):
            x = False
            #GestionDomicilioCliente.estadoDomicilio(x)
            return x
        else:
            self.canasta = None
            self.ocupado = False
            x = True
            #GestionDomicilioCliente.estadoDomicilio(x)
            return x

    def conseguirIngredientes(self, listIngredientes):
        valorcompra = 0

        Ingrediente.organizarTopMasVendidos()
        top = Ingrediente.getTopMasVendidos()

        for ingredienteNombre, cantidad in listIngredientes.items():

            topp = False

            for ingredientes in top:

                if ingredientes.getNombre() == ingredienteNombre:

                    if cantidad + self.panaderia.getInventario().verificarCantidadIngredientePorNombre(ingredienteNombre) + (cantidad * 2) <= 40:
                        
                        valorcompra = valorcompra+ ((Ingrediente.obtenerObjetoPorNombreI(ingredienteNombre).getPrecioDeCompra()) * (cantidad)) + 100000
                        topp = True

                    else:

                        if self.panaderia.getInventario().verificarCantidadIngredientePorNombre(ingredienteNombre) + (cantidad * 2) <= 40:

                            if self.robado == True:

                                cantidad = cantidad*2

                            valorcompra = valorcompra + ((Ingrediente.obtenerObjetoPorNombreI(ingredienteNombre).getPrecioDeCompra()) * (cantidad))
                            topp = True

                        else:

                            if self.robado == True:

                                cantidad = (40 - self.panaderia.getInventario().verificarCantidadIngredientePorNombre(ingredienteNombre))

                            valorcompra = valorcompra + ((Ingrediente.obtenerObjetoPorNombreI(ingredienteNombre).getPrecioDeCompra()) * (cantidad))
                            topp = True
            
            if topp == False:

                if cantidad + self.panaderia.getInventario().verificarCantidadIngredientePorNombre(ingredienteNombre) > 20:

                    valorcompra = valorcompra+ ((Ingrediente.obtenerObjetoPorNombreI(ingredienteNombre).getPrecioDeCompra()) * (cantidad)) + 50000
                    topp = True

                else:

                    if self.panaderia.getInventario().verificarCantidadIngredientePorNombre(ingredienteNombre) + (cantidad) <= 20:

                        valorcompra = valorcompra + ((Ingrediente.obtenerObjetoPorNombreI(ingredienteNombre).getPrecioDeCompra()) * (cantidad))

                    else:

                        if self.robado == True:

                            cantidad = (20 - self.panaderia.getInventario().verificarCantidadIngredientePorNombre(ingredienteNombre))

                        valorcompra = valorcompra + ((Ingrediente.obtenerObjetoPorNombreI(ingredienteNombre).getPrecioDeCompra()) * (cantidad))
            
            listIngredientes[ingredienteNombre] = cantidad #revisar esto 
        
        if valorcompra <= self.panaderia.getPanaderia():
            
            self.dineroEnMano += valorcompra  
            dinero = self.panaderia.getPanaderia()
            self.panaderia.setDinero((dinero-valorcompra))

            if self.robado == True:

                ladron = Catastrofe()
                postRobo = ladron.robarComprador(self)

                if postRobo.getRobado() == False:
                    return True
                
            for ingredienteNombre, cantidad in listIngredientes.items():

                for i in range (0,cantidad):

                    ingrdt = Ingrediente.crearIngrediente(ingredienteNombre)
                    self.getPanaderia().getInventario().agregarIngrediente(ingrdt)
            
            self.dineroEnMano -= valorcompra
            return False
        
        else:

            self.panaderia.conseguirPrestamo(valorcompra)
            self.dineroEnMano += valorcompra  
            dinero = self.panaderia.getPanaderia()
            self.panaderia.setDinero((dinero-valorcompra))

            if self.robado == True:

                ladron = Catastrofe()
                postRobo = ladron.robarComprador(self)

                if postRobo.getRobado() == False:
                    return True
                
            for ingredienteNombre, cantidad in listIngredientes.items():

                for i in range (0,cantidad):

                    ingrdt = Ingrediente.crearIngrediente(ingredienteNombre)
                    self.getPanaderia().getInventario().agregarIngrediente(ingrdt)
            
            self.dineroEnMano -= valorcompra
            return False