from gestorAplicacion.comida import Ingrediente
from gestorAplicacion.comida import Producto
from gestorAplicacion.comida import ProductoCaliente
from gestorAplicacion.comida import ProductoFrio
from gestorAplicacion.gestion import Panaderia
from gestorAplicacion.humanos import Cliente

class Canasta:

    #Constructores Canasta
    def __init__(self):
      self._productos = []
      self._ingredientes = []
      self._kits = []
      self._productos_en_lista = {}
      self._ingredientes_en_lista = {}
      self._kits_en_lista = {}
      self._identificador = ""
      self._items_totales_en_canasta = 0
      self._items_totales_en_lista = 0
      self._costo_total_en_lista = 0
      self._costo_tras_descuento_en_lista = 0
      self._descuento_en_lista = 0
      self._calificacion = 0
      self._comentario = ""
      self._pagada = False
      self._estado_orden = False
      self.calcularElementosCanasta()

    def __init__(self, productos, ingredientes, kits):
      self._productos_en_lista = {}
      self._ingredientes_en_lista = {}
      self._kits_en_lista = {}
      self._identificador = ""
      self._items_totales_en_canasta = 0
      self._items_totales_en_lista = 0
      self._costo_total_en_lista = 0
      self._costo_tras_descuento_en_lista = 0
      self._descuento_en_lista = 0
      self._calificacion = 0
      self._comentario = ""
      self._pagada = False
      self._estado_orden = False
      self._productos = productos
      self._ingredientes = ingredientes
      self._kits = kits
      self.calcularElementosCanasta()

    def __init__(self, productos, ingredientes, kits, productosEnLista, ingredientesEnLista, kitsEnLista, identificador, itemsTotalesEnCanasta, itemsTotalesEnLista, costoTotalEnLista, costoTrasDescuentoEnLista, descuentoEnLista, calificacion, comentario, pagada):
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

    def __init__(self, productosEnLista, ingredientesEnLista, kitsEnLista, itemsTotalesEnCanasta, itemsTotalesEnLista, costoTotalEnLista, costoTrasDescuentoEnLista, descuentoEnLista) :
      self.productosEnLista = productosEnLista
      self.ingredientesEnLista = ingredientesEnLista
      self.kitsEnLista = kitsEnLista
      self.itemsTotalesEnCanasta = itemsTotalesEnCanasta
      self.itemsTotalesEnLista = itemsTotalesEnLista
      self.costoTotalEnLista = costoTotalEnLista
      self.costoTrasDescuentoEnLista = costoTrasDescuentoEnLista
      self.descuentoEnLista = descuentoEnLista

    def __init__(self, productosEnLista, ingredientesEnLista, kitsEnLista, itemsTotalesEnCanasta, itemsTotalesEnLista, costoTotalEnLista, costoTrasDescuentoEnLista, descuentoEnLista, identificador):
      self.productosEnLista = productosEnLista
      self.ingredientesEnLista = ingredientesEnLista
      self.kitsEnLista = kitsEnLista
      self.identificador = identificador
      self.itemsTotalesEnCanasta = itemsTotalesEnCanasta
      self.itemsTotalesEnLista = itemsTotalesEnLista
      self.costoTotalEnLista = costoTotalEnLista
      self.costoTrasDescuentoEnLista = costoTrasDescuentoEnLista
      self.descuentoEnLista = descuentoEnLista

    # Getters
    def get_productos(self):
        return self._productos

    def get_ingredientes(self):
        return self._ingredientes

    def get_kits(self):
        return self._kits

    def get_productos_en_lista(self):
        return self._productos_en_lista

    def get_ingredientes_en_lista(self):
        return self._ingredientes_en_lista

    def get_kits_en_lista(self):
        return self._kits_en_lista

    def get_identificador(self):
        return self._identificador

    def get_items_totales_en_canasta(self):
        return self._items_totales_en_canasta

    def get_items_totales_en_lista(self):
        return self._items_totales_en_lista

    def get_costo_total_en_lista(self):
        return self._costo_total_en_lista

    def get_costo_tras_descuento_en_lista(self):
        return self._costo_tras_descuento_en_lista

    def get_descuento_en_lista(self):
        return self._descuento_en_lista

    def get_calificacion(self):
        return self._calificacion

    def get_comentario(self):
        return self._comentario

    def get_pagada(self):
        return self._pagada

    def get_estado_orden(self):
        return self._estado_orden

    # Setters
    def set_productos(self, productos):
        self._productos = productos

    def set_ingredientes(self, ingredientes):
        self._ingredientes = ingredientes

    def set_kits(self, kits):
        self._kits = kits

    def set_productos_en_lista(self, productos_en_lista):
        self._productos_en_lista = productos_en_lista

    def set_ingredientes_en_lista(self, ingredientes_en_lista):
        self._ingredientes_en_lista = ingredientes_en_lista

    def set_kits_en_lista(self, kits_en_lista):
        self._kits_en_lista = kits_en_lista

    def set_identificador(self, identificador):
        self._identificador = identificador

    def set_items_totales_en_canasta(self, items_totales_en_canasta):
        self._items_totales_en_canasta = items_totales_en_canasta

    def set_items_totales_en_lista(self, items_totales_en_lista):
        self._items_totales_en_lista = items_totales_en_lista
      
    def set_costo_total_en_lista(self, costo_total_en_lista):
        self._costo_total_en_lista = costo_total_en_lista

    def set_costo_tras_descuento_en_lista(self, costo_tras_descuento_en_lista):
        self._costo_tras_descuento_en_lista = costo_tras_descuento_en_lista

    def set_descuento_en_lista(self, descuento_en_lista):
        self._descuento_en_lista = descuento_en_lista

    def set_calificacion(self, calificacion):
        self._calificacion = calificacion

    def set_comentario(self, comentario):
        self._comentario = comentario

    def set_pagada(self, pagada):
        self._pagada = pagada

    def set_estado_orden(self, estado_orden):
        self._estado_orden = estado_orden

    # Metodos que gestionan correctamente la modificacion de los maps
    # Verifican que efectivamente el elemento no exista en el map antes de
    # agregarlo, en el caso de que si, simplemente agrega la cantidad indicada a la que ya había

    #Para productos
    def gestionAgregarP(self, productos):
      for p in productos:
        if p != None:
          self.productos[p] += 1
      self.calcularElementosCanasta()

    def __clone__(self):
      return super.__clone__()

    #Para ingredientes
    def gestionAgregarI(self, ingredientes):
      for i in ingredientes:
        if i != None:
          self.ingredientes[i] += 1
      self.calcularElementosCanasta()

    #Para kits
    def gestionAgregarK(self,kits):
      for kit in kits:
          if kit is not None:
            self.kits.add(kit)
      self.calcularElementosCanasta()

    #Para productos en lista
    def gestionAgregar(self,prdct,elementNum,iD):
      if ((prdct != None) & (not self.productosEnLista.has_key(prdct))):
          self.productosEnLista[prdct] = elementNum
      elif ((prdct != None)):
          self.productosEnLista[prdct] = self.productosEnLista[prdct] + elementNum
      self.calcularElementosLista()
      self.generarCostoDeOrden()

    #Para ingredientes en lista
    def gestionAgregarI(self,ingr,elementNum,iD):
      if ((ingr != None) & (not self.ingredientesEnLista.has_key(ingr))):
          self.ingredientesEnLista[ingr] = elementNum
      elif ((ingr != None)):
          self.ingredientesEnLista[ingr] = self.ingredientesEnLista[ingr] + elementNum
      self.calcularElementosLista()
      self.generarCostoDeOrden()

    #Para kits en lista
    def gestionAgregarK(self,kit,elementNum,iD):
      if ((kit != None) & (not self.kitsEnLista.has_key(kit))):
          self.kitsEnLista[kit] = elementNum
      elif ((kit != None)):
          self.kitsEnLista[kit] = self.kitsEnLista[kit] + elementNum
      self.calcularElementosLista()
      self.generarCostoDeOrden()

    #Para agregar strings a una lista enviada
    def gestionAgregar(ingrd, elementNum, lista):
      if ingrd != None and ingrd not in lista:
          lista[ingrd] = elementNum
      elif ingrd != None:
          lista[ingrd] = lista[ingrd] + elementNum
      return lista
    
    #Para productos en lista
    def gestionEliminar(self, prdct, cantidad, iD):
      if (prdct is not None) and (self.productosEnLista.has_key(prdct)):
          if self.productosEnLista.get(prdct)+cantidad > 0:
              self.productosEnLista.put(prdct, self.productosEnLista.get(prdct)+cantidad)
              self.calcularElementosLista()
              self.generarCostoDeOrden()
              return True
          elif self.productosEnLista.get(prdct)+cantidad == 0:
              self.productosEnLista.remove(prdct)
              self.calcularElementosLista()
              self.generarCostoDeOrden()
              return True
          elif self.productosEnLista.get(prdct)+cantidad < 0:
              return False
      else:
          return False
      return False
    
    #Para ingredientes en lista
    def gestionEliminarI(self, ingr, cantidad, iD):
      if (ingr is not None) and (self.ingredientesEnLista.has_key(ingr)):
          if self.ingredientesEnLista.get(ingr)+cantidad > 0:
              self.ingredientesEnLista.put(ingr, self.ingredientesEnLista.get(ingr)+cantidad)
              self.calcularElementosLista()
              self.generarCostoDeOrden()
              return True
          elif self.ingredientesEnLista.get(ingr)+cantidad == 0:
              self.ingredientesEnLista.remove(ingr)
              self.calcularElementosLista()
              self.generarCostoDeOrden()
              return True
          elif self.ingredientesEnLista.get(ingr)+cantidad < 0:
              return False
      else:
          return False
      return False
    
    #Para kits en lista
    def gestionEliminarK(self, kit, cantidad, iD):
      if (kit is not None) and (self.kitsEnLista.has_key(kit)):
          if self.kitsEnLista.get(kit)+cantidad > 0:
              self.kitsEnLista.put(kit, self.kitsEnLista.get(kit)+cantidad)
              self.calcularElementosLista()
              self.generarCostoDeOrden()
              return True
          elif self.kitsEnLista.get(kit)+cantidad == 0:
              self.kitsEnLista.remove(kit)
              self.calcularElementosLista()
              self.generarCostoDeOrden()
              return True
          elif self.kitsEnLista.get(kit)+cantidad < 0:
              return False
      else:
          return False
      return False
    

    """
    * Calcula el número total de elementos en la canasta sumando las cantidades de productos, ingredientes y kits.
    * Actualiza el valor de itemsTotalesEnCanasta.
    """
    def calcularElementosCanasta(self):
      elementos= len(self.productos)+len(self.ingredientes)+len(self.kits)
      self.itemsTotalesEnCanasta=elementos


    """
    * Calcula el número total de elementos en la canasta sumando las cantidades de productosEnLista, ingredientesEnLista y kitsEnLista.
    """
    def calcularElementosLista(self):
      elementos = 0
      if(self.productosEnLista is not None):
        for productoEntry in self.productosEnLista:
          elementos+=productoEntry.getValue()
      if(self.ingredientesEnLista is not None):
        for ingredienteEntry in self.ingredientesEnLista:
          elementos+=ingredienteEntry.getValue()
      if(self.kitsEnLista is not None):
        for entry in self.kitsEnLista:
          elementos+=entry.getValue()
      self.itemsTotalesEnLista=elementos

