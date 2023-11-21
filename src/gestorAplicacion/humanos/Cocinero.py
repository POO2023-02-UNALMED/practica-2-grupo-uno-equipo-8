from random import randint, random

from gestorAplicacion.comida.Ingrediente import Ingrediente
from gestorAplicacion.comida.Producto import Producto
from gestorAplicacion.comida.ProductoFrio import ProductoFrio
from gestorAplicacion.comida.ProductoCaliente import ProductoCaliente
from gestorAplicacion.humanos.Domiciliario import Domiciliario
from gestorAplicacion.humanos.Catastrofe import Catastrofe


class Cocinero(Domiciliario):
    nombres = ["Sergio", "Jaime", "David", "Juancho", "Will", "Kevin"]
    _procesosDeProductosCocinados = []
    _productosCocinados = []
    _fallosCocinando= []
    
    def __init__(self, nombre="", especialidad="", panaderia=None, habilidad=0.0, calificacion=0.0, dineroEnMano=0.):
        """
        Inicializa un objeto Cocinero con los siguientes atributos:

        Args:
            nombre (str, opcional): El nombre del cocinero. Por defecto es una cadena vacía.
            especialidad (str, opcional): La especialidad del cocinero. Por defecto es una cadena vacía.
            panaderia (Panaderia, opcional): La panadería a la que pertenece el cocinero. Por defecto es None.
            habilidad (float, opcional): La habilidad del cocinero. Por defecto es 0.0.
            calificacion (float, opcional): La calificación del cocinero. Por defecto es 0.0.
            dineroEnMano (float, opcional): La cantidad de dinero en mano del cocinero. Por defecto es 0.0.
        """
        super().__init__(nombre, panaderia, habilidad, calificacion, dineroEnMano)
        self._especialidad = especialidad
        self._fallado = False
        self._trabajo = False
        self._nevera = False
        self._horno = False
        self._habilidad = super().getHabilidad()
        self._panaderia = panaderia
        if self._panaderia is not None:
            self._panaderia.getCocineros().append(self)

#getters y setters

    def getEspecialidad(self):
        return self._especialidad

    def setEspecialidad(self, especialidad):
        self._especialidad = especialidad

    def isFallado(self):
        return self._fallado

    def setFallado(self, quemado):
        self._fallado = quemado

    def isTrabajo(self):
        return self._trabajo

    def setTrabajo(self, trabajo):
        self._trabajo = trabajo

    def isNevera(self):
        return self._nevera

    def setNevera(self, nevera):
        self._nevera = nevera

    def isHorno(self):
        return self._horno

    def setHorno(self, horno):
        self._horno = horno

    def getPanaderia(self):
        return self._panaderia

    def setPanaderia(self, panaderia):
        self._panaderia = panaderia
        
    @classmethod
    def getProcesosDeProductosCocinados(cls):
        return cls._procesosDeProductosCocinados
    
    @classmethod
    def setProcesosDeProductosCocinados(cls, procesosDeProductosCocinados):
        cls._procesosDeProductosCocinados = procesosDeProductosCocinados
        
    @classmethod
    def getFallosCocinando(cls):
        return cls._fallosCocinando
    
    @classmethod
    def setFallosCocinando(cls, fallosCocinando):
        cls._fallosCocinando = fallosCocinando
        
    @classmethod
    def getProductosCocinados(cls):
        return cls._productosCocinados
    
    @classmethod
    def setProductosCocinados(cls, productosCocinados):
        cls._productosCocinados = productosCocinados
        

    def ingredientesCocinero(self, ingredientesNecesarios):
        """
        Devuelve una lista de ingredientes faltantes necesarios para cocinar.

        Parámetros:
        - ingredientesNecesarios: una lista de ingredientes necesarios para cocinar.

        Retorna:
        - ingrFaltantes: una lista de ingredientes faltantes necesarios para cocinar.
        """
        ingrFaltantes = self._panaderia.getInventario().revisarCantidadIngredientes(ingredientesNecesarios)
        return ingrFaltantes

    def cocineroIdeal(self, proceso):
        """
        Devuelve el cocinero ideal para un proceso de cocina dado.

        Parámetros:
        - proceso: El proceso de cocina para el cual se busca el cocinero ideal.

        Retorna:
        - El cocinero ideal para el proceso dado, si existe.
        - Si no existe un cocinero ideal, se contrata un nuevo cocinero con una especialidad aleatoria y se retorna.

        """
        chefRandom = self.nombres[randint(0, 5)]
        ideal = None
        listaCocineros = self._panaderia.getCocineros()
        
        for cocinero in listaCocineros:
            especialidad = cocinero.getEspecialidad()
            if especialidad == proceso:
                ideal = cocinero
                return ideal
        idealNew = self._panaderia.contratarCocinero(chefRandom, proceso, randint(9, 19), 0, 0)
        return idealNew

    def detenerCoccion(self, producto, cantidades):
        """
        Detiene la cocción de un producto y resta los ingredientes utilizados en la cantidad especificada.

        Parámetros:
        - producto: El producto cuya cocción se va a detener.
        - cantidades: La cantidad de veces que se va a detener la cocción del producto.

        """
        ingredientesUsados = producto.getIngredientes()
        for ingUsado, cantidad in ingredientesUsados.items():
            ingredienteUsado = self._panaderia.getInventario().ingredientePorNombreBuscar(ingUsado)
            self._panaderia.getInventario().restarIngrediente(ingredienteUsado, cantidad * cantidades)

    def repararCoccion(self, producto,texto):
        """
        Repara la cocción de un producto dado comprando los ingredientes utilizados.

        Parámetros:
        - producto: El producto cuya cocción se va a reparar.

        """
        ingredientesUsados = producto.getIngredientes()
        self._panaderia.comprarIngredientes(ingredientesUsados,texto)

    def detenerCoccion2(self, producto):
        """
        Detiene la cocción de un producto y resta los ingredientes utilizados de la panadería.

        Parámetros:
        - producto: El producto cuya cocción se desea detener.

        """
        ingredientesUsados = producto.getIngredientes()
        for ingUsado, cantidad in ingredientesUsados.items():
            ingredienteUsado = self._panaderia.getInventario().ingredientePorNombreBuscar(ingUsado)
            self._panaderia.getInventario().restarIngrediente(ingredienteUsado, cantidad)

    def procesoCocinar(self, producto,texto):
        """
        Realiza el proceso de cocinar un producto.

        Args:
            producto (Producto): El producto a cocinar.

        Returns:
            bool: False si todos los procesos se completaron con éxito.
        """
        # Obtiene la lista de procesos de cocina necesarios para el producto.
        procesosProducto = producto.seleccionProcesosDeCocina()

        # Asigna la lista de procesos al producto.
        producto.setProcesosDeCocina(procesosProducto)

        # Crea una instancia de la clase Catastrofe para gestionar la dificultad.
        dificultad = Catastrofe()

        # Obtiene la lista de procesos a realizar.
        procesoCook = producto.getProcesosDeCocina()
        longitud = len(procesoCook)
        
        # Itera a través de los procesos de cocina.
        for i in range(longitud):
            # Encuentra al cocinero ideal para el proceso actual.
            chefIdeal = self.cocineroIdeal(procesoCook[i])

            # Realiza el proceso específico para productos fríos, si corresponde.
            if isinstance(producto, ProductoFrio):
                productoF = producto
                productoF.procesoCongelamiento(chefIdeal)

            # Realiza el proceso específico para productos calientes, si corresponde.
            if isinstance(producto, ProductoCaliente):
                productoH = producto
                productoH.procesoHornear(chefIdeal)

            # Evalúa la dificultad del proceso con el cocinero seleccionado.
            cookProducto = dificultad.dificultadProducto(chefIdeal)

            if cookProducto:
                # Incrementa la habilidad del cocinero si el proceso falló.
                chefIdeal.habilidad += 1
                numero_random = randint(0, 4)
                mensaje_fallo = f"Perdón su pedido tartará un poco más porque {Catastrofe.fallos_cocina[numero_random]} cuando estaba en el proceso de {procesoCook[i]}"
                Cocinero._fallosCocinando.append(mensaje_fallo)
                chefIdeal.detenerCoccion2(producto)
                chefIdeal.repararCoccion(producto,texto)
                i = -1
            # Establece el cocinero como ocupado.
            chefIdeal.trabajo = True
        Cocinero._procesosDeProductosCocinados.append(procesoCook)
        Cocinero._productosCocinados.append(producto.getNombre())


        # Devuelve False si todos los procesos se completaron con éxito.
        return False

    @staticmethod
    def unirMapasIngredientesId(listaDeMapas):
        """
        Une varios mapas de ingredientes en uno solo, acumulando los valores de las claves comunes.

        Args:
            listaDeMapas (list): Una lista de diccionarios que representan los mapas de ingredientes.

        Returns:
            dict: Un diccionario que contiene la acumulación de los valores de las claves comunes en los mapas de ingredientes.
        """
        mapaAcumulativo = {}
        for mapa in listaDeMapas:
            for clave, valor in mapa.items():
                mapaAcumulativo[clave] = mapaAcumulativo.get(clave, 0) + valor
        return mapaAcumulativo
    
    @staticmethod
    def multiplicarValoresEnMapa(mapa, multiplicador):
        """
        Multiplica los valores en un mapa por un multiplicador dado.

        Args:
            mapa (dict): El mapa con los ingredientes y sus valores originales.
            multiplicador (int): El valor por el cual se multiplicarán los valores en el mapa.

        Returns:
            dict: Un nuevo mapa con los valores multiplicados.

        """
        nuevoMapa = {}
        
        for ingredienteId, valorOriginal in mapa.items():
            nuevoValor = valorOriginal * multiplicador
            nuevoMapa[ingredienteId] = nuevoValor

        return nuevoMapa

    def laborParticular(self, canastaTrabajar,texto):
        """
        Realiza la labor particular del cocinero con una canasta de trabajo.

        Args:
            canastaTrabajar (Canasta): La canasta de trabajo que contiene los productos a cocinar.

        Returns:
            bool: True si se completó la labor correctamente, False si hubo ingredientes faltantes.

        """
        productos = canastaTrabajar.getProductosEnLista()
        listaDeMapas = []

        for productoId, cantidad in productos.items():
            producto = Producto.obtenerObjetoPorIdP(productoId)
            ingredientesAUsar = producto.ingredientes

            for ingredienteIdVerificar, cantidad in ingredientesAUsar.items():
                ingrediente = Ingrediente.obtenerObjetoPorNombreI(ingredienteIdVerificar)
                ingrediente.revisarCaducidad(cantidad, self._panaderia)

        for productoId, cantidad in productos.items():
            producto = Producto.obtenerObjetoPorIdP(productoId)
            ingredientesNecesarios = producto.ingredientes
            ingredientesAbsolutos = self.multiplicarValoresEnMapa(ingredientesNecesarios, cantidad)
            listaDeMapas.append(ingredientesAbsolutos)

        listaIngredientesTotales = self.unirMapasIngredientesId(listaDeMapas)

        ingrFaltantes = self.ingredientesCocinero(listaIngredientesTotales)

        if ingrFaltantes:
            numero_random = randint(0, 4)
            mensaje_fallo = f"Perdón su pedido tartará un poco más porque {Catastrofe.fallos_cocina[numero_random]}"
            Cocinero._fallosCocinando.append(mensaje_fallo)
            self._panaderia.comprarIngredientes(ingrFaltantes,texto)
            ingrFaltantes.clear()
            return False

        for productoId, cantidad in productos.items():
            producto = self._panaderia.getInventario().buscarProductoPorId(productoId)
            productoNew = Producto.crearProducto(productoId)
            cocinero = self._panaderia.cocineroAleatorio()

            for i in range(cantidad):
                fallado = cocinero.procesoCocinar(productoNew,texto)
                self._panaderia.getInventario().agregarProducto(productoNew)
                if fallado:
                    continue

        for productoId, cantidad in productos.items():
            producto = self._panaderia.getInventario().buscarProductoPorId(productoId)
            cocinero = self._panaderia.cocineroAleatorio()
            cocinero.detenerCoccion(producto, cantidad)

        return True