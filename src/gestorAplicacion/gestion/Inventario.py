from gestorAplicacion.comida.Producto import Producto


class Inventario:
    def __init__(self):
        """
        Inicializa una instancia de la clase Inventario.

        El inventario se compone de una lista de ingredientes y una lista de productos.
        La cantidad máxima de elementos en el inventario está limitada a 20.

        """
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
        """
        Verifica la cantidad de ingredientes con el nombre especificado en el inventario.

        Args:
            ingrd (str): El nombre del ingrediente a verificar.

        Returns:
            int: La cantidad de ingredientes con el nombre especificado.
        """
        contador = 0
        for ingrediente in self._invIngredientes:
            if ingrediente.getNombre() == ingrd:
                contador += 1
        return contador

    def verificarCantidadIngredientePorId(self, ingrd):
        """
        Verifica la cantidad de ingredientes por su ID en el inventario.

        Parámetros:
        - ingrd: El ID del ingrediente a verificar.

        Retorna:
        - contador: La cantidad de ingredientes con el ID especificado en el inventario.
        """
        contador = 0
        for ingrediente in self._invIngredientes:
            if ingrediente.getId() == ingrd:
                contador += 1
        return contador

    def verificarCantidadProductoPorId(self, prdct):
        """
        Verifica la cantidad de productos en el inventario que coinciden con el ID dado.

        Args:
            prdct (int): El ID del producto a verificar.

        Returns:
            int: El número de productos en el inventario que coinciden con el ID dado.
        """
        contador = 0
        for producto in self._invProductos:
            if producto.getId() == prdct:
                contador += 1
        return contador

    def verificarCantidadProductoPorNombre(self, prdct):
        """
        Verifica la cantidad de productos con el nombre especificado en el inventario.

        Args:
            prdct (str): El nombre del producto a verificar.

        Returns:
            int: La cantidad de productos con el nombre especificado.
        """
        contador = 0
        for producto in self._invProductos:
            if producto.getNombre() == prdct:
                contador += 1
        return contador

    def buscarProductoPorId(self, id):
        """
        Busca un producto en el inventario por su ID.

        Parámetros:
        - id: El ID del producto a buscar.

        Retorna:
        - El producto encontrado, si existe.
        - None, si no se encuentra ningún producto con el ID especificado.
        """
        for producto in self._invProductos:
            if producto.getId() == id:
                return producto
        return None
    
    def buscarProductoPorNombre(self, nombre):
        """
        Busca un producto en el inventario por su nombre.

        Parámetros:
        - nombre: El nombre del producto a buscar.

        Retorna:
        - El producto encontrado si existe en el inventario, o None si no se encuentra.
        """
        for producto in self._invProductos:
            if producto.getNombre() == nombre:
                return producto
        return None

    def buscarIngredientePorId(self, id):
        """
        Busca un ingrediente en el inventario por su ID.

        Parámetros:
        - id: El ID del ingrediente a buscar.

        Retorna:
        - El ingrediente encontrado, si existe.
        - None si no se encuentra ningún ingrediente con el ID especificado.
        """
        for ingrediente in self._invIngredientes:
            if ingrediente.getId() == id:
                return ingrediente
        return None
    
    def ingredientePorNombreBuscar(self, nombre):
        """
        Busca un ingrediente en el inventario por su nombre.

        Parámetros:
        - nombre: El nombre del ingrediente a buscar.

        Retorna:
        - El objeto ingrediente si se encuentra en el inventario.
        - None si no se encuentra el ingrediente.
        """
        for ingrediente in self._invIngredientes:
            if ingrediente.getNombre() == nombre:
                return ingrediente
        return None

    def revisarCantidadIngredientes(self, ingredientesNecesarios):
        """
        Comprueba si hay suficiente cantidad de ingredientes en el inventario para satisfacer las necesidades de una receta.

        Args:
            ingredientesNecesarios (dict): Un diccionario que contiene los ingredientes necesarios para la receta y sus cantidades requeridas.

        Returns:
            dict: Un diccionario que contiene los ingredientes faltantes y la cantidad necesaria para completar la receta.
        """
        ingredientesFaltantes = {}
        for ingrediente, cantidad in ingredientesNecesarios.items():
            cantidadExistente = self.verificarCantidadIngredientePorNombre(ingrediente)
            if cantidadExistente - cantidad < 0:
                ingredientesFaltantes[ingrediente] = (cantidadExistente - cantidad) * (-2)
        return ingredientesFaltantes

    # Método para agregar un ingrediente al inventario
    def agregarIngrediente(self, ingrediente):
        """
        Agrega un ingrediente al inventario.

        Args:
            ingrediente (objeto): El ingrediente a agregar.

        Returns:
            None
        """
        self._invIngredientes.append(ingrediente)

    def agregarProducto(self, producto):
        """
        Agrega un producto al inventario.

        Parámetros:
        - producto: El producto a agregar al inventario.

        """
        self._invProductos.append(producto)

    def restarIngrediente(self, ingrediente, cantidad):
        """
        Resta la cantidad especificada de un ingrediente del inventario.

        Args:
            ingrediente (str or Ingrediente): El nombre o el objeto Ingrediente del ingrediente a restar.
            cantidad (int): La cantidad de ingrediente a restar.

        Returns:
            None
        """
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
        """
        Resta la cantidad especificada del producto dado del inventario.

        Args:
            producto (str or Producto): El producto o su identificador.
            cantidad (int): La cantidad a restar del producto.

        Returns:
            None
        """
        if isinstance(producto, str):
            if self.verificarCantidadProductoPorId(producto) >= cantidad:
                for i in range(cantidad):
                    for producto1 in self._invProductos:
                        if producto1.getId() == producto:
                            self._invProductos.remove(producto1)
                            producto_obtenido = Producto.obtenerObjetoPorIdP(producto)
                            producto_obtenido.setVecesVendido(producto_obtenido.getVecesVendido() + 1)
                            Producto.organizarTopMasVendidos()
                            break
        else:
            if self.verificarCantidadProductoPorId(producto.getId()) >= cantidad:
                for i in range(cantidad):
                    for producto1 in self._invProductos:
                        if producto1.getId() == producto.getId():
                            self._invProductos.remove(producto1)
                            producto_obtenido = Producto.obtenerObjetoPorIdP(producto.getId())
                            producto_obtenido.setVecesVendido(producto_obtenido.getVecesVendido() + 1)
                            Producto.organizarTopMasVendidos()
                            break