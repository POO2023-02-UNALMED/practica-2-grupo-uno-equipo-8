from random import randint

from gestorAplicacion.humanos.Trabajador import Trabajador
from gestorAplicacion.comida.Ingrediente import Ingrediente
from gestorAplicacion.comida.Producto import Producto
from gestorAplicacion.comida.ProductoFrio import ProductoFrio
from gestorAplicacion.comida.productoCaliente import ProductoCaliente
from gestorAplicacion.gestion.Canasta import Canasta
from gestorAplicacion.gestion.Panaderia import Panaderia
from gestorAplicacion.humanos.Domiciliario import Domiciliario
from gestorAplicacion.humanos.Catastrofe import Catastrofe


class Cocinero(Domiciliario):
    nombres = ["Sergio", "Jaime", "David", "Juancho", "Will", "Kevin"]
    
    def __init__(self, nombre="", habilidad=0.0, calificacion=0.0, dineroEnMano=0.0, especialidad="", panaderia=None):
        super().__init__(nombre, habilidad, calificacion, dineroEnMano, panaderia, True)
        self._especialidad = especialidad
        self._fallado = False
        self._trabajo = False
        self._nevera = False
        self._horno = False
        self._panaderia = panaderia
        if self._panaderia is not None:
            self._panaderia.get_cocineros().append(self)

    def get_especialidad(self):
        return self._especialidad

    def set_especialidad(self, especialidad):
        self._especialidad = especialidad

    def is_fallado(self):
        return self._fallado

    def set_fallado(self, quemado):
        self._fallado = quemado

    def is_trabajo(self):
        return self._trabajo

    def set_trabajo(self, trabajo):
        self._trabajo = trabajo

    def is_nevera(self):
        return self._nevera

    def set_nevera(self, nevera):
        self._nevera = nevera

    def is_horno(self):
        return self._horno

    def set_horno(self, horno):
        self._horno = horno

    def get_panaderia(self):
        return self._panaderia

    def set_panaderia(self, panaderia):
        self._panaderia = panaderia

    def ingredientesCocinero(self, ingredientesNecesarios):
        ingrFaltantes = self.panaderia.getInventario().revisarCantidadIngredientes(ingredientesNecesarios)
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
        idealNew = self._panaderia.contratarCocinero(chefRandom, habilidad=0, calificacion=0, dineroEnMano=0, proceso=proceso)
        return idealNew

    def detenerCoccion(self, producto, cantidades):
        ingredientesUsados = producto.getIngredientes()
        for ingUsado, cantidad in ingredientesUsados.items():
            ingredienteUsado = self._panaderia._inventario.buscarIngredientePorNombre(ingUsado)
            self._panaderia._inventario.restarIngrediente(ingredienteUsado, cantidad * cantidades)
            
    def repararCoccion(self, producto):
        ingredientesUsados = producto.getIngredientes()
        self.panaderia.comprarIngredientes(ingredientesUsados)
        
    def detenerCoccion2(self, producto):
        ingredientesUsados = producto.getIngredientes()
        for ingUsado, cantidad in ingredientesUsados.items():
            ingredienteUsado = self._panaderia._inventario.buscarIngredientePorNombre(ingUsado)
            self._panaderia._inventario.restarIngrediente(ingredienteUsado, cantidad)


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
                #GestionCocinar.fallosCocinando(procesoCook, longitud)
                chefIdeal.detenerCoccion(producto)
                chefIdeal.repararCoccion(producto)
                i = -1
            #GestionCocinar.barrasCocinando(procesoCook, longitud)
            # Establece el cocinero como ocupado.
            chefIdeal.trabajo = True

        # Devuelve False si todos los procesos se completaron con éxito.
        return False

    def unirMapasIngredientesId(listaDeMapas):
        mapaAcumulativo = {}
        for mapa in listaDeMapas:
            for clave, valor in mapa.items():
                mapaAcumulativo[clave] = mapaAcumulativo.get(clave, 0) + valor
        return mapaAcumulativo
    
    def multiplyValuesInMap(map, multiplier):
        newMap = {}
        
        for ingredientId, originalValue in map.items():
            newValue = originalValue * multiplier
            newMap[ingredientId] = newValue

        return newMap

    def laborParticular(self, canastaTrabajar):
        productos = canastaTrabajar.productosEnLista()
        listaDeMapas = []

        for productoId, cantidad in productos.items():
            producto = Producto.obtenerObjetoPorId(productoId)
            ingredientesAUsar = producto.ingredientes

            for ingredienteIdVerificar, cantidad in ingredientesAUsar.items():
                ingrediente = Ingrediente.obtenerObjetoPorNombre(ingredienteIdVerificar)
                ingrediente.revisarCaducidad(cantidad, self.panaderia)

        for productoId, cantidad in productos.items():
            producto = Producto.obtenerObjetoPorId(productoId)
            ingredientesNecesarios = producto.ingredientes
            ingredientesAbsolutos = self.multiplicarValoresEnMapa(ingredientesNecesarios, cantidad)
            listaDeMapas.append(ingredientesAbsolutos)

        listaIngredientesTotales = self.unirMapasIngredientesId(listaDeMapas)

        ingrFaltantes = self.ingredientesCocinero(listaIngredientesTotales)

        if not ingrFaltantes:
            #GestionCocinar.fallosCocinando()
            self.panaderia.comprarIngredientes(ingrFaltantes)
            ingrFaltantes.clear()
            return False

        for productoId, cantidad in productos.items():
            producto = self.panaderia.inventario.buscarProductoPorId(productoId)
            productoNew = self.crearProducto(productoId)
            cocinero = self.panaderia.cocineroAleatorio()

            for i in range(cantidad):
                fallado = cocinero.procesoCocinar(productoNew)
                self.panaderia.inventario.agregarProducto(productoNew)
                if fallado:
                    continue

        for productoId, cantidad in productos.items():
            producto = self.panaderia.inventario.buscarProductoPorId(productoId)
            cocinero = self.panaderia.cocineroAleatorio()
            cocinero.detenerCoccion(producto, cantidad)

        return True