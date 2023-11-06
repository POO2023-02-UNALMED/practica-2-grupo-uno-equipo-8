from gestorAplicacion.humanos.Trabajador import Trabajador

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
