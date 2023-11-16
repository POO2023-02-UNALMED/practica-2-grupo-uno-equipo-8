from random import randint

from gestorAplicacion.comida.Ingrediente import Ingrediente
from gestorAplicacion.comida.Producto import Producto
from gestorAplicacion.comida.ProductoFrio import ProductoFrio
from gestorAplicacion.comida.ProductoCaliente import ProductoCaliente
from gestorAplicacion.humanos.Domiciliario import Domiciliario
from gestorAplicacion.humanos.Catastrofe import Catastrofe


class Cocinero(Domiciliario):
    nombres = ["Sergio", "Jaime", "David", "Juancho", "Will", "Kevin"]
    
    def __init__(self, nombre="",especialidad="" , panaderia=None,habilidad=0.0, calificacion=0.0, dineroEnMano=0.0):
        super().__init__(nombre,panaderia, habilidad, calificacion, dineroEnMano)
        self._especialidad = especialidad
        self._fallado = False
        self._trabajo = False
        self._nevera = False
        self._horno = False
        self._panaderia = panaderia
        if self._panaderia is not None:
            self._panaderia.getCocineros().append(self)

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

    def ingredientesCocinero(self, ingredientesNecesarios):
        ingrFaltantes = self._panaderia.getInventario().revisarCantidadIngredientes(ingredientesNecesarios)
        return ingrFaltantes

    def cocineroIdeal(self, proceso):
        chefRandom = self.nombres[randint(0, 5)]
        ideal = None
        listaCocineros = self._panaderia.getCocineros()
        
        for cocinero in listaCocineros:
            especialidad = cocinero.getEspecialidad()
            if especialidad == proceso:
                ideal = cocinero
                return ideal
        idealNew = self._panaderia.contratarCocinero(chefRandom, proceso, super().habilidad, super().calificacion, 0)
        return idealNew

    def detenerCoccion(self, producto, cantidades):
        ingredientesUsados = producto.getIngredientes()
        for ingUsado, cantidad in ingredientesUsados.items():
            ingredienteUsado = self._panaderia.getInventario().buscarIngredientePorNombre(ingUsado)
            self._panaderia.getInventario().restarIngrediente(ingredienteUsado, cantidad * cantidades)
            
    def repararCoccion(self, producto):
        ingredientesUsados = producto.getIngredientes()
        self._panaderia.comprarIngredientes(ingredientesUsados)
        
    def detenerCoccion2(self, producto):
        ingredientesUsados = producto.getIngredientes()
        for ingUsado, cantidad in ingredientesUsados.items():
            ingredienteUsado = self._panaderia.getInventario().buscarIngredientePorNombre(ingUsado)
            self._panaderia.getInventario().restarIngrediente(ingredienteUsado, cantidad)


    def procesoCocinar(self, producto):
        # Obtiene la lista de procesos de cocina necesarios para el producto.
        procesosProducto = producto.seleccionProcesosDeCocina()

        # Asigna la lista de procesos al producto.
        producto.setProcesoDeCocina(procesosProducto)

        # Crea una instancia de la clase Catastrofe para gestionar la dificultad.
        dificultad = Catastrofe()

        # Obtiene la lista de procesos a realizar.
        procesoCook = producto.getProcesoDeCocina()
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
                Cocinero._fallosCocinando +=1
                chefIdeal.detenerCoccion(producto)
                chefIdeal.repararCoccion(producto)
                i = -1
            # Establece el cocinero como ocupado.
            chefIdeal.trabajo = True
        Cocinero._procesosDeProductosCocinados.append(procesoCook)


        # Devuelve False si todos los procesos se completaron con éxito.
        return False

    def unirMapasIngredientesId(listaDeMapas):
        mapaAcumulativo = {}
        for mapa in listaDeMapas:
            for clave, valor in mapa.items():
                mapaAcumulativo[clave] = mapaAcumulativo.get(clave, 0) + valor
        return mapaAcumulativo
    
    def multiplicarValoresEnMapa(mapa, multiplicador):
        nuevoMapa = {}
        
        for ingredienteId, valorOriginal in mapa.items():
            nuevoValor = valorOriginal * multiplicador
            nuevoMapa[ingredienteId] = nuevoValor

        return nuevoMapa

    def laborParticular(self, canastaTrabajar):
        productos = canastaTrabajar.getProductosEnLista()
        listaDeMapas = []

        for productoId, cantidad in productos.items():
            producto = Producto.obtenerObjetoPorId(productoId)
            ingredientesAUsar = producto.ingredientes

            for ingredienteIdVerificar, cantidad in ingredientesAUsar.items():
                ingrediente = Ingrediente.obtenerObjetoPorNombre(ingredienteIdVerificar)
                ingrediente.revisarCaducidad(cantidad, self._panaderia)

        for productoId, cantidad in productos.items():
            producto = Producto.obtenerObjetoPorId(productoId)
            ingredientesNecesarios = producto.ingredientes
            ingredientesAbsolutos = self.multiplicarValoresEnMapa(ingredientesNecesarios, cantidad)
            listaDeMapas.append(ingredientesAbsolutos)

        listaIngredientesTotales = self.unirMapasIngredientesId(listaDeMapas)

        ingrFaltantes = self.ingredientesCocinero(listaIngredientesTotales)

        if not ingrFaltantes:
            Cocinero._fallosCocinando +=1
            self._panaderia.comprarIngredientes(ingrFaltantes)
            ingrFaltantes.clear()
            return False

        for productoId, cantidad in productos.items():
            producto = self._panaderia.getInventario().buscarProductoPorId(productoId)
            productoNew = self.crearProducto(productoId)
            cocinero = self._panaderia.cocineroAleatorio()

            for i in range(cantidad):
                fallado = cocinero.procesoCocinar(productoNew)
                self._panaderia.getInventario().agregarProducto(productoNew)
                if fallado:
                    continue

        for productoId, cantidad in productos.items():
            producto = self._panaderia.getInventario().buscarProductoPorId(productoId)
            cocinero = self._panaderia.cocineroAleatorio()
            cocinero.detenerCoccion(producto, cantidad)

        return True