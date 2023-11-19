from gestorAplicacion.comida.ComidaDefault import ComidaDefault
from gestorAplicacion.comida.Producto import Producto
from gestorAplicacion.comida.ProductoCaliente import ProductoCaliente
from gestorAplicacion.comida.ProductoFrio import ProductoFrio

from enum import Enum
import random

class Canasta:

    #Constructores Canasta
    def __init__(self, productos = None, ingredientes = None, kits = None, productosEnLista = None, ingredientesEnLista = None, kitsEnLista = None, identificador= "", itemsTotalesEnCanasta = 0, itemsTotalesEnLista = 0, costoTotalEnLista = 0.0, costoTrasDescuentoEnLista = 0.0, descuentoEnLista = 0.0, calificacion = 0.0, comentario = "", pagada = False, estadoOrden=False):
        if productos == None:
            productos = []

        if ingredientes == None:
            ingredientes = []

        if kits == None:
            kits = []

        if productosEnLista == None:
            productosEnLista = {}
        
        if ingredientesEnLista == None:
            ingredientesEnLista = {}

        if kitsEnLista == None:
            kitsEnLista = {}

        self._productos = productos
        self._ingredientes = ingredientes
        self._kits = kits
        self._productosEnLista = productosEnLista
        self._ingredientesEnLista = ingredientesEnLista
        self._kitsEnLista = kitsEnLista
        self._identificador = identificador
        self._itemsTotalesEnCanasta = itemsTotalesEnCanasta
        self._itemsTotalesEnLista = itemsTotalesEnLista
        self._costoTotalEnLista = costoTotalEnLista
        self._costoTrasDescuentoEnLista = costoTrasDescuentoEnLista
        self._descuentoEnLista = descuentoEnLista
        self._calificacion = calificacion
        self._comentario = comentario
        self._pagada = pagada
        self._estadoOrden = estadoOrden

    # Getters
    def getProductosEnLista(self):
        return self._productosEnLista

    def getIngredientesEnLista(self):
        return self._ingredientesEnLista

    def getKitsEnLista(self):
        return self._kitsEnLista

    def getIdentificador(self):
        return self._identificador

    def getItemsTotalesEnCanasta(self):
        return self._itemsTotalesEnCanasta

    def getItemsTotalesEnLista(self):
        return self._itemsTotalesEnLista

    def getCostoTotalEnLista(self):
        return self._costoTotalEnLista

    def getCostoTrasDescuentoEnLista(self):
        return self._costoTrasDescuentoEnLista

    def getDescuentoEnLista(self):
        return self._descuentoEnLista

    def getProductos(self):
        return self._productos

    def getIngredientes(self):
        return self._ingredientes

    def getKits(self):
        return self._kits

    def getCalificacion(self):
        return self._calificacion

    def getComentario(self):
        return self._comentario

    def getPagada(self):
        return self._pagada

    def getEstadoOrden(self):
        return self._estadoOrden

    # Setters
    def setProductosEnLista(self, productosEnLista):
        self._productosEnLista = productosEnLista

    def setIngredientesEnLista(self, ingredientesEnLista):
        self._ingredientesEnLista = ingredientesEnLista

    def setKitsEnLista(self, kitsEnLista):
        self._kitsEnLista = kitsEnLista

    def setIdentificador(self, identificador):
        self._identificador = identificador

    def setItemsTotalesEnCanasta(self, itemsTotalesEnCanasta):
        self._itemsTotalesEnCanasta = itemsTotalesEnCanasta

    def setItemsTotalesEnLista(self, itemsTotalesEnLista):
        self._itemsTotalesEnLista = itemsTotalesEnLista

    def setCostoTotalEnLista(self, costoTotalEnLista):
        self._costoTotalEnLista = costoTotalEnLista

    def setCostoTrasDescuentoEnLista(self, costoTrasDescuentoEnLista):
        self._costoTrasDescuentoEnLista = costoTrasDescuentoEnLista

    def setDescuentoEnLista(self, descuentoEnLista):
        self._descuentoEnLista = descuentoEnLista

    def setProductos(self, productos):
        self._productos = productos

    def setIngredientes(self, ingredientes):
        self._ingredientes = ingredientes

    def setKits(self, kits):
        self._kits = kits

    def setCalificacion(self, calificacion):
        self._calificacion = calificacion

    def setComentario(self, comentario):
        self._comentario = comentario

    def setPagada(self, pagada):
        self._pagada = pagada

    def setEstadoOrden(self, estadoOrden):
        self._estadoOrden = estadoOrden


    # Metodos que gestionan correctamente la modificacion de los maps
    # Verifican que efectivamente el elemento no exista en el map antes de
    # agregarlo, en el caso de que si, simplemente agrega la cantidad indicada a la que ya había

    #Para productos en lista
    def gestionAgregarP(self,prdct,elementNum=1):
        if elementNum!=0:
            if ((prdct != None) & (not (prdct in self._productosEnLista))):
                self._productosEnLista[prdct] = elementNum
            elif ((prdct != None)):
                self._productosEnLista[prdct] = self._productosEnLista[prdct] + elementNum
            self.calcularElementosLista()
            self.generarCostoDeOrden()

        else:
            for p in prdct:
                if p != None:
                    self._productos[p] += 1
                self.calcularElementosCanasta()

    #Para ingredientes en lista
    def gestionAgregarI(self,ingr,elementNum=1):
        if elementNum!=0:
            if ((ingr != None) & (not (ingr in self._ingredientesEnLista))):
                self._ingredientesEnLista[ingr] = elementNum
            elif ((ingr != None)):
                self._ingredientesEnLista[ingr] = self._ingredientesEnLista[ingr] + elementNum
            self.calcularElementosLista()
            self.generarCostoDeOrden()
        else:
            for i in ingr:
                if i != None:
                    self._ingredientes[i] += 1
            self.calcularElementosCanasta()

    #Para kits en lista
    def gestionAgregarK(self,kit,elementNum=1):
        if elementNum!=0:
            if ((kit != None) & (not (kit in self._kitsEnLista))):
                self._kitsEnLista[kit] = elementNum
            elif ((kit != None)):
                self._kitsEnLista[kit] = self._kitsEnLista[kit] + elementNum
            self.calcularElementosLista()
            self.generarCostoDeOrden()
        else:
            for k in kit:
                if k is not None:
                    self._kits.add(kit)
            self.calcularElementosCanasta()

    #Para agregar strings a una lista enviada
    def gestionAgregar(ingrd, elementNum, lista):
        if ingrd != None and ingrd not in lista:
            lista[ingrd] = elementNum
        elif ingrd != None:
            lista[ingrd] = lista[ingrd] + elementNum
        return lista
    
    #Para productos en lista
    def gestionEliminarP(self, prdct, cantidad):
        if (prdct is not None) and (self._productosEnLista.has_key(prdct)):
            if self._productosEnLista.get(prdct)+cantidad > 0:
                self._productosEnLista.update(prdct, self._productosEnLista.get(prdct)+cantidad)
                self.calcularElementosLista()
                self.generarCostoDeOrden()
                return True
            elif self._productosEnLista.get(prdct)+cantidad == 0:
                self._productosEnLista.pop(prdct)
                self.calcularElementosLista()
                self.generarCostoDeOrden()
                return True
            elif self._productosEnLista.get(prdct)+cantidad < 0:
                return False
    
    #Para ingredientes en lista
    def gestionEliminarI(self, ingr, cantidad):
        if (ingr is not None) and (self._ingredientesEnLista.has_key(ingr)):
            if self._ingredientesEnLista.get(ingr)+cantidad > 0:
                self._ingredientesEnLista.update(ingr, self._ingredientesEnLista.get(ingr)+cantidad)
                self.calcularElementosLista()
                self.generarCostoDeOrden()
                return True
            elif self._ingredientesEnLista.get(ingr)+cantidad == 0:
                self._ingredientesEnLista.pop(ingr)
                self.calcularElementosLista()
                self.generarCostoDeOrden()
                return True
            elif self._ingredientesEnLista.get(ingr)+cantidad < 0:
                return False
        else:
            return False
        return False
    
    #Para kits en lista
    def gestionEliminarK(self, kit, cantidad):
        if (kit is not None) and (self._kitsEnLista.has_key(kit)):
            if self._kitsEnLista.get(kit)+cantidad > 0:
                self._kitsEnLista.update(kit, self._kitsEnLista.get(kit)+cantidad)
                self.calcularElementosLista()
                self.generarCostoDeOrden()
                return True
            elif self._kitsEnLista.get(kit)+cantidad == 0:
                self._kitsEnLista.pop(kit)
                self.calcularElementosLista()
                self.generarCostoDeOrden()
                return True
            elif self._kitsEnLista.get(kit)+cantidad < 0:
                return False
        else:
            return False
        return False
    

    """
    * Calcula el número total de elementos en la canasta sumando las cantidades de productos, ingredientes y kits.
    * Actualiza el valor de itemsTotalesEnCanasta.
    """
    def calcularElementosCanasta(self):
        elementos= len(self._productosEnLista)+len(self._ingredientesEnLista)+len(self._kitsEnLista)
        self._itemsTotalesEnCanasta=elementos


    """
    * Calcula el número total de elementos en la canasta sumando las cantidades de productosEnLista, ingredientesEnLista y kitsEnLista.
    """
    def calcularElementosLista(self):
        elementos = 0
        if(self._productosEnLista is not None):
            for productoEntry in self._productosEnLista.keys():
                elementos+=int(productoEntry)
        if(self._ingredientesEnLista is not None):
            for ingredienteEntry in self._ingredientesEnLista.keys():
                elementos+=int(ingredienteEntry)
        if(self._kitsEnLista is not None):
            for entry in self._kitsEnLista.keys():
                elementos+=int(entry)
        self._itemsTotalesEnLista=elementos

    @staticmethod
    def cuponProductos(producto, cnt):
        multiplicador_descuento = 1.0

        # Si la cantidad cumple los requisitos se le aplica el descuento del enum
        if cnt >= 8:
            multiplicador_descuento -= DescuentoPorCantidad.OCHO.value
        elif cnt >= 5:
            multiplicador_descuento -= DescuentoPorCantidad.CINCO.value
        elif cnt >= 3:
            multiplicador_descuento -= DescuentoPorCantidad.TRES.value

        # Si el producto se encuentra dentro de los productos en oferta del enum se aplica el descuento
        for producto_enum in DescuentoProducto:
            if producto_enum.get_producto() == producto.getNombre():
                multiplicador_descuento -= producto_enum.get_valor()

        return multiplicador_descuento
    

    def generarCostoDeOrden(self):
        from gestorAplicacion.comida.Ingrediente import Ingrediente
        costo_canasta = 0.0
        descuento_canasta = 0.0

        if self._productosEnLista is not None:
            for producto_id, cantidad in self._productosEnLista.items():
                producto = Producto.obtenerObjetoPorIdP(producto_id)
                descuento = self.cuponProductos(producto, cantidad)
                costo_canasta += producto.getCosto() * cantidad * descuento
                descuento_canasta += producto.getCosto() * cantidad * (1 - descuento)

        if self._ingredientesEnLista is not None:
            for ingrediente_id, cantidad in self._ingredientesEnLista.items():
                ingrediente = Ingrediente.obtenerObjetoPorIdI(ingrediente_id)
                costo_canasta += ingrediente.getPrecioDeVenta() * cantidad

        if self._kitsEnLista is not None:
            for kit_id, cantidad in self._kitsEnLista.items():
                producto = Producto.obtenerObjetoPorIdP(kit_id)
                costo_canasta += producto.getCosto() * cantidad

        self._descuentoEnLista = descuento_canasta
        self._costoTotalEnLista = costo_canasta + descuento_canasta
        self._costoTrasDescuentoEnLista = costo_canasta

    def recibir_orden(self, objeto_entrante, cantidad, receta):
        from gestorAplicacion.comida.Ingrediente import Ingrediente
        self._estado_orden = False

        if int(cantidad) < 0:
            estado = False

            if Producto.verificarExistenciaPorIdP(objeto_entrante):
                if receta:
                    estado = self.gestionEliminarK(objeto_entrante, int(cantidad))
                else:
                    estado = self.gestionEliminarP(objeto_entrante, int(cantidad))

                if estado:
                    self._estadoOrden = True
                    return "Se ha restado la cantidad del producto de la canasta"
                else:
                    return "No se ha podido restar la cantidad del producto de la canasta"

            elif Ingrediente.verificacionExistenciaPorIdI(objeto_entrante) and not receta:
                estado = self.gestionEliminarI(objeto_entrante, int(cantidad))

                if estado:
                    self._estadoOrden = True
                    return "Se ha restado la cantidad del ingrediente de la canasta"
                else:
                    return "No se ha podido restar la cantidad del ingrediente de la canasta"

            return "No se ha podido realizar el proceso, vuelva a intentarlo"
        else:
            if Producto.verificarExistenciaPorIdP(objeto_entrante):
                if receta:
                    self.gestionAgregarK(objeto_entrante, int(cantidad))
                else:
                    self.gestionAgregarP(objeto_entrante, int(cantidad))

                self._estadoOrden = True
                return "Se ha agregado la cantidad del producto a la canasta"

            elif Ingrediente.verificacionExistenciaPorIdI(objeto_entrante) and not receta:
                self.gestionAgregarI(objeto_entrante, int(cantidad))
                self._estadoOrden = True
                return "Se ha agregado la cantidad del ingrediente a la canasta"

        return "No se ha podido realizar el proceso"
    

    def recibirOrdenPersonalizada(self, objeto_entrante, ingredientes_necesarios, cantidad, receta):
        try:
            random_num = random.randint(1, 2)
            if random_num == 1:
                ProductoFrio.crearProductoPersonalizado(objeto_entrante, ingredientes_necesarios)
            else:
                ProductoCaliente.crearProductoPersonalizado(objeto_entrante, ingredientes_necesarios)
        except Exception as e:
            print("Error al crear el producto personalizado: " + str(e))
            return False

        if Producto.verificarExistenciaPorNombreP(objeto_entrante):
            if receta:
                self.gestionAgregarK(Producto.obtenerObjetoPorNombreP(objeto_entrante).getId(), int(cantidad))
            else:
                self.gestionAgregarP(Producto.obtenerObjetoPorNombreP(objeto_entrante).getId(), int(cantidad))
            return True
        else:
            return False

    def enviarOrdenCanasta(self):
        from gestorAplicacion.humanos.Cliente import Cliente
        productos_cocinados = Cliente.getSesion().getPanaderia().agregarProductosACanasta(self._productosEnLista)
        ingredientes_cocinados = Cliente.getSesion().getPanaderia().agregarIngredientesACanasta(self._ingredientesEnLista)
        kits_cocinados = Cliente.getSesion().getPanaderia().agregarKitsACanasta(self._kitsEnLista)

        self.gestionAgregarP(productos_cocinados)
        self.gestionAgregarI(ingredientes_cocinados)
        self.gestionAgregarK(kits_cocinados)

class DescuentoProducto(Enum):
    PRODUCTO_A = ("rollos de canela", 0.1)
    PRODUCTO_B = ("bunuelo", 0.1)
    PRODUCTO_C = ("brownie", 0.1)
    PRODUCTO_D = ("torta de milo", 0.1)
    PRODUCTO_E = ("cheesecake", 0.1)

    def __init__(self, producto, valor):
        self.producto = producto
        self.valor = valor

    def get_producto(self):
        return self.producto

    def get_valor(self):
        return self.valor

class DescuentoPorCantidad(Enum):
    TRES = 0.05
    CINCO = 0.1
    OCHO = 0.15

    def __init__(self, valor):
        self.valor = valor

    def get_valor(self):
        return self.valor
