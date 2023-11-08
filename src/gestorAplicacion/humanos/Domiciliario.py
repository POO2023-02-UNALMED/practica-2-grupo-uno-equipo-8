from gestorAplicacion.humanos.Trabajador import Trabajador
from gestorAplicacion.comida.Ingrediente import Ingrediente

class Domiciliario(Trabajador):
    def __init__(self):
        super().__init__()
        self.licencia = True
        self.ocupado = False
        self.canasta = None
    
    def getLicencia(self):
        return self.licencia
    
    def getOcupado(self):
        return self.ocupado
    
    def getCanasta(self):
        return self.canasta
    
    def setLicencia(self, licencia):
        self.licencia = licencia

    def setOcupado(self, ocupado):
        self.ocupado = ocupado

    def setCanasta(self, canasta):
        self.canasta = canasta
    
    def calcular_costo_domicilio(cliente, canasta):
        productos = canasta.productos
        costo = 0
        for producto in productos:
            costo += producto.costo
        longitud = len(productos)
        if longitud > 15:
            costo += costo * 0.7

        direccion = cliente.direccion
        if direccion.distancia == "Medio":
            costo += 10000
        if direccion.distancia == "Lejos":
            costo += 20000

        costo += tarifa_domicilio
        costo *= tarifa_ganancias
        return costo
    
    def labor_particular(self, canasta):
        transito = Catastrofe()
        if not transito.parada_transito(self):
            x = False
            GestionDomicilioCliente.estado_domicilio(x)
            return x
        else:
            self.canasta = None
            self.ocupado = False
            x = True
            GestionDomicilioCliente.estado_domicilio(x)
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
                        
                        valorcompra = valorcompra+ ((Ingrediente.obtenerObjetoPorNombre(ingredienteNombre).getPrecioDeCompra()) * (cantidad)) + 100000
                        topp = True

                    else:

                        if self.panaderia.getInventario().verificarCantidadIngredientePorNombre(ingredienteNombre) + (cantidad * 2) <= 40:

                            if self.robado == True:

                                cantidad = cantidad*2

                            valorcompra = valorcompra + ((Ingrediente.obtenerObjetoPorNombre(ingredienteNombre).getPrecioDeCompra()) * (cantidad))
                            topp = True

                        else:

                            if self.robado == True:

                                cantidad = (40 - self.panaderia.getInventario().verificarCantidadIngredientePorNombre(ingredienteNombre))

                            valorcompra = valorcompra + ((Ingrediente.obtenerObjetoPorNombre(ingredienteNombre).getPrecioDeCompra()) * (cantidad))
                            topp = True
            
            if topp == False:

                if cantidad + self.panaderia.getInventario().verificarCantidadIngredientePorNombre(ingredienteNombre) > 20:

                    valorcompra = valorcompra+ ((Ingrediente.obtenerObjetoPorNombre(ingredienteNombre).getPrecioDeCompra()) * (cantidad)) + 50000
                    topp = True

                else:

                    if self.panaderia.getInventario().verificarCantidadIngredientePorNombre(ingredienteNombre) + (cantidad) <= 20:

                        valorcompra = valorcompra + ((Ingrediente.obtenerObjetoPorNombre(ingredienteNombre).getPrecioDeCompra()) * (cantidad))

                    else:

                        if self.robado == True:

                            cantidad = (20 - self.panaderia.getInventario().verificarCantidadIngredientePorNombre(ingredienteNombre))

                        valorcompra = valorcompra + ((Ingrediente.obtenerObjetoPorNombre(ingredienteNombre).getPrecioDeCompra()) * (cantidad))
            
            listIngredientes[ingredienteNombre] = cantidad #revisar esto 