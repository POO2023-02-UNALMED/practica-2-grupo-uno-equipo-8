from UIMain import Texto
import datetime

from gestorAplicacion.comida import Ingrediente, Producto

class Recibo:
    totalFacturas = 0
    formato = "%d/%m/%Y"

    def __init__(self, cliente, canasta, domiciliario):
        """
        Inicializa una instancia de la clase Recibo.

        Parámetros:
        - cliente: El objeto Cliente asociado al recibo.
        - canasta: El objeto Canasta asociado al recibo.
        - domiciliario: El objeto Domiciliario asociado al recibo.

        Atributos:
        - cliente: El objeto Cliente asociado al recibo.
        - idRecibo: El identificador único del recibo.
        - subtotal: El costo total de la canasta sin descuento.
        - total: El costo total de la canasta con descuento aplicado.
        - descuento: El valor del descuento aplicado al total.
        - fecha: La fecha y hora en que se creó el recibo.
        - pagado: Un indicador booleano que indica si el recibo ha sido pagado o no.
        - canasta: El objeto Canasta asociado al recibo.
        - costoDomicilio: El costo del domicilio asociado al recibo.
        - factura: Una lista que contiene los elementos de la factura.

        """
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

#getters y setters

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
    

    def mostrarCanasta(self, canasta):
        print("_".repeat(55))
        print("")
        print(Texto.centrar("PRODUCTOS"))
        print("_".repeat(55))
        print(Texto.alinear("Descripcion", "Cantidad", "Costo"))
        print("_".repeat(55))
        print("")
        for producto, cantidad in canasta.getProductosEnLista().items():
            costo = Producto.obtenerObjetoPorId(producto).getCosto() * cantidad
            print(Texto.alinear(Producto.obtenerObjetoPorId(producto).getNombre(), cantidad, costo))

        print("_".repeat(55))
        print("")
        print(Texto.centrar("INGREDIENTES"))
        print("_".repeat(55))
        print(Texto.alinear("Descripcion", "Cantidad", "Costo"))
        print("_".repeat(55))
        print("")
        for ingrediente, cantidad2 in canasta.getIngredientesEnLista().items():
            costo = Ingrediente.obtenerObjetoPorId(ingrediente).getPrecioDeVenta() * cantidad2
            print(Texto.alinear(Ingrediente.obtenerObjetoPorId(ingrediente).getNombre(), cantidad2, costo))

        print("_".repeat(55))
        print("")
        print(Texto.centrar("KITS"))
        print("_".repeat(55))
        print(Texto.alinear("Descripcion", "Cantidad", "Costo"))
        print("_".repeat(55))
        print("")
        for kit, cantidad2 in canasta.getKitsEnLista().items():
            costo = Producto.obtenerObjetoPorId(kit).getCosto() * cantidad2
            print(Texto.alinear(Producto.obtenerObjetoPorId(kit).getNombre(), cantidad2, costo))

        print("_".repeat(55))
        print(" ")
        print(Texto.alinear("Descuento efectuado:", " ", str(canasta.getDescuentoEnLista())))
        print(Texto.alinear("subtotal", canasta.getCostoTotalEnLista()))

    
    def imprimir_factura(self):
        recibo = self
        print("")
        print("")
        print(Texto.centrar("POO Bakery"))
        print(Texto.centrar("DOMICILIOS 24 HORAS"))
        print("")
        print(Texto.centrar("Factura Nro: {}".format(recibo.getIdRecibo())))
        print(Texto.centrar("Fecha y hora: {}".format(Recibo.formato.format(recibo.getFecha()))))
        print(Texto.centrar("Empleado que atendio su orden: {}".format(recibo.getDomiciliario().getNombre())))
        print(Texto.centrar("Ciudad: Medellin"))
        print(Texto.centrar("Cliente: {}".format(recibo.getCliente().getNombre())))
        print(Texto.centrar("Identificacion: {}".format(recibo.getCliente().getId())))
        print(Texto.centrar(""))
        print(Texto.centrar(Texto.centrar("DETALLE DE VENTA")))
        print(" ")
        self.mostrarCanasta(recibo.getCanasta())
        print("")
        print("")
        print("_".repeat(55))
        print(Texto.alinear("Domicilio", "", str(recibo.getCostoDomicilio())))
        print(Texto.alinear("Descuento", " ", " " + str(recibo.getSubtotal() * recibo.getDescuento())))
        print(Texto.alinear("****TOTAL*****", recibo.getTotal()))
        print("")
        print("_".repeat(55))
        print(Texto.centrar(Texto.centrar("DETALLE DE IMPUESTOS")))
        print("_".repeat(55))
        print(Texto.alinear("IVA", recibo.getTotal() * 0.19))
        print("_".repeat(55))
        print("")
        print(Texto.centrar(Texto.centrar("")))
        print(Texto.centrar("EN POO BAKERY SOMOS EXPERTOS EN AHORRO:"))
        print(Texto.centrar("TU AHORRO HOY FUE DEL {}%".format(recibo.getDescuento() * 100)))
        print(Texto.centrar("EQUIVALENTE A {}".format((recibo.getDescuento() * 100) * recibo.getSubtotal())))
        print(Texto.centrar("POO Bakery"))
        print(Texto.centrar("solo calidad"))
        print(Texto.centrar("Gracias por tu compra"))
        print(Texto.centrar("No se permiten devoluciones"))
        print("")

