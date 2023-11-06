import datetime

class Recibo:
    totalFacturas = 0
    formato = "%d/%m/%Y"

    def __init__(self, cliente, canasta, domiciliario):
        Recibo.totalFacturas += 1
        self.cliente = cliente
        self.idRecibo = Recibo.totalFacturas
        self.subtotal = canasta.getCostoTrasDescuentoEnLista()
        self.total = self.subtotal * (1 - cliente.getTipoDescuento().getValor())
        self.descuento = cliente.getTipoDescuento().getValor() if cliente.getTipoDescuento() else 0
        self.fecha = datetime.datetime.now()
        self.pagado = False
        self.canasta = canasta
        self.costoDomicilio = domiciliario.getCostoDomicilio()
        self.factura = []

    def getCostoDomicilio(self):
        return self.costoDomicilio

    def setCostoDomicilio(self, costoDomicilio):
        self.costoDomicilio = costoDomicilio

    def getDomiciliario(self):
        return self.domiciliario

    def setDomiciliario(self, domiciliario):
        self.domiciliario = domiciliario

    def getCanasta(self):
        return self.canasta

    def setCanasta(self, canasta):
        self.canasta = canasta

    def isPagado(self):
        return self.pagado

    def setPagado(self, pagado):
        self.pagado = pagado

    def getSubtotal(self):
        return self.subtotal

    def getCliente(self):
        return self.cliente

    def getIdRecibo(self):
        return self.idRecibo

    def setCliente(self, cliente):
        self.cliente = cliente

    def setIdRecibo(self, idRecibo):
        self.idRecibo = idRecibo

    @staticmethod
    def setTotalFacturas(totalFacturas):
        Recibo.totalFacturas = totalFacturas

    def setSubtotal(self, subtotal):
        self.subtotal = subtotal

    def setTotal(self, total):
        self.total = total

    def setDescuento(self, descuento):
        self.descuento = descuento

    def setFecha(self, fecha):
        self.fecha = fecha

    def setFactura(self, factura):
        self.factura = factura

    @staticmethod
    def getTotalFacturas():
        return Recibo.totalFacturas

    def getFecha(self):
        return self.fecha

    def getTotal(self):
        return self.total

    def getDescuento(self):
        return self.descuento

    def getFactura(self):
        return self.factura
