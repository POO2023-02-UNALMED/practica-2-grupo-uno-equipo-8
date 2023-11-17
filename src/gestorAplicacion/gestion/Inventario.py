from gestorAplicacion.comida.Producto import Producto


class Inventario:
    def __init__(self):
        self._invIngredientes = []
        self._invProductos = []
        self._maxCantidad = 20

    # Getter y setter para panaderia
    def getPanaderia(self):
        return self._panaderia

    def setPanaderia(self, panaderia):
        self._panaderia = panaderia

    # Getter y setter para invIngredientes
    def getInvIngredientes(self):
        return self._invIngredientes

    def setInvIngredientes(self, invIngredientes):
        self._invIngredientes = invIngredientes

    # Getter y setter para invProductos
    def getInvProductos(self):
        return self._invProductos

    def setInvProductos(self, invProductos):
        self._invProductos = invProductos

    # Getter y setter para maxCantidad
    def getMaxCantidad(self):
        return self._maxCantidad

    def setMaxCantidad(self, maxCantidad):
        self._maxCantidad = maxCantidad
        

    def verificarCantidadIngredientePorNombre(self, ingrd):
        contador = 0
        for ingrediente in self._invIngredientes:
            if ingrediente.getNombre() == ingrd:
                contador += 1
        return contador

    def verificarCantidadIngredientePorId(self,ingrd):
        contador = 0
        for ingrediente in self._invIngredientes:
            if ingrediente.getId() == ingrd:
                contador += 1
        return contador

    def verificarCantidadProductoPorId(self,prdct):
        contador = 0
        for producto in self._invProductos:
            if producto.getId() == prdct:
                contador += 1
        return contador

    def verificarCantidadProductoPorNombre(self,prdct):
        contador = 0
        for producto in self._invProductos:
            if producto.getNombre() == prdct:
                contador += 1
        return contador

    def buscarProductoPorId(self,id):
        for producto in self._invProductos:
            if producto.getId() == id:
                return producto
        return None
    
    def buscarProductoPorNombre(self,nombre):
        for producto in self._invProductos:
            if producto.getNombre() == nombre:
                return producto
        return None

    def buscarIngredientePorId(self,id):
        for ingrediente in self._invIngredientes:
            if ingrediente.getId() == id:
                return ingrediente
        return None
    
    def ingredientePorNombreBuscar(self,nombre):
        print(self._invIngredientes)
        for ingrediente in self._invIngredientes:
            if ingrediente.getNombre() == nombre:
                return ingrediente
        return None

    def revisarCantidadIngredientes(self, ingredientesNecesarios):
        ingredientesFaltantes = {}
        for ingrediente, cantidad in ingredientesNecesarios.items():
            cantidadExistente = self.verificarCantidadIngredientePorNombre(ingrediente)
            if cantidadExistente - cantidad < 0:
                ingredientesFaltantes[ingrediente] = (cantidadExistente - cantidad) * (-2)
        return ingredientesFaltantes

    # Método para agregar un ingrediente al inventario
    def agregarIngrediente(self,ingrediente):
        self._invIngredientes.append(ingrediente)

    def agregarProducto(self,producto):
        self._invProductos.append(producto)

    def restarIngrediente(self,ingrediente, cantidad):
        if isinstance(ingrediente, str):
            if self.verificarCantidadIngredientePorId(ingrediente) >= cantidad:
                for i in range(cantidad):
                    for ingrediente1 in self._invIngredientes:
                        if ingrediente1.getId() == ingrediente:
                            self._invIngredientes.remove(ingrediente1)
                            break
        else:
            if self.verificarCantidadIngredientePorId(ingrediente.getId()) >= cantidad:
                for i in range(cantidad):
                    for ingrediente1 in self._invIngredientes:
                        if ingrediente1.getId() == ingrediente.getId():
                            self._invIngredientes.remove(ingrediente1)
                            break

    def restarProducto(self, producto, cantidad):
        if isinstance(producto, str):
            if self.verificarCantidadProductoPorId(producto) >= cantidad:
                for i in range(cantidad):
                    for producto1 in self._invProductos:
                        if producto1.getId() == producto:
                            self._invProductos.remove(producto1)
                            producto_obtenido = Producto.obtenerObjetoPorId(producto)
                            producto_obtenido.setVecesVendido(producto_obtenido.getVecesVendido() + 1)
                            Producto.organizarTopMasVendidos()
                            break
        else:
            if self.verificarCantidadProductoPorId(producto.getId()) >= cantidad:
                for i in range(cantidad):
                    for producto1 in self._invProductos:
                        if producto1.getId() == producto.getId():
                            self._invProductos.remove(producto1)
                            producto_obtenido = Producto.obtenerObjetoPorId(producto.getId())
                            producto_obtenido.setVecesVendido(producto_obtenido.getVecesVendido() + 1)
                            Producto.organizarTopMasVendidos()
                            break