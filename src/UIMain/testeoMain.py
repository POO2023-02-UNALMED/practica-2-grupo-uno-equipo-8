import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from gestorAplicacion.gestion.Panaderia import Panaderia
from gestorAplicacion.comida.Ingrediente import Ingrediente
from gestorAplicacion.comida.Producto import Producto
from gestorAplicacion.humanos.Cliente import Cliente
from gestorAplicacion.humanos.Domiciliario import Domiciliario
from gestorAplicacion.humanos.Cocinero import Cocinero
from gestorAplicacion.comida.ComidaDefault import ComidaDefault
from gestorAplicacion.gestion.Inventario import Inventario
from baseDatos.Serializador import Serializador

class SerializationTest:
    def main(self, args):
        print("Test de funcionamiento")
        panaderia = Panaderia()
        panaderia = Serializador.cargarPanaderia()
        Cliente.setPanaderia(panaderia)
        print("panaderia cargada")
        
        Ingrediente.crearIngrediente("leche")
        Ingrediente.crearIngrediente("harina")
        Ingrediente.crearIngrediente("azucar")
        Ingrediente.crearIngrediente("huevos")
        Ingrediente.crearIngrediente("mantequilla")
        Ingrediente.crearIngrediente("sal")
        Ingrediente.crearIngrediente("levadura")
        Ingrediente.crearIngrediente("chocolate")
        Ingrediente.crearIngrediente("canela")
        Ingrediente.crearIngrediente("queso")
        Ingrediente.crearIngrediente("milo")
        Ingrediente.crearIngrediente("miga de galleta")

        
        #print(Ingrediente.crearIngrediente("meme"))
        #Producto.crearProductoPersonalizado("marmota", {"meme": 1, "carnita": 1, "hormiga": 1, "azucar": 1, "mantequilla": 1})
        
        print("ingredientes creados")

        
        ingredientes_bunuelo = {
            "harina": 2,
            "huevos": 2,
            "queso": 1
        }
        ingredientes_rollos_canela = {
            "harina": 2,
            "huevos": 2,
            "canela": 1,
            "azucar": 1,
            "mantequilla": 1,
            "leche": 1
        }
        ingredientes_brownie = {
            "harina": 1,
            "huevos": 2,
            "chocolate": 1,
            "leche": 1,
            "mantequilla": 1
        }
        ingredientes_torta_milo = {
            "harina": 1,
            "huevos": 2,
            "milo": 1,
            "leche": 1
        }
        ingredientes_cheesecake = {
            "queso": 1,
            "huevos": 2,
            "miga de galleta": 1,
            "azucar": 1,
            "mantequilla": 1
        }
        
        Producto.crearProductoPersonalizado("bunuelo", ingredientes_bunuelo)
        Producto.crearProductoPersonalizado("rollos de canela", ingredientes_rollos_canela)
        Producto.crearProductoPersonalizado("brownie", ingredientes_brownie)
        Producto.crearProductoPersonalizado("torta de milo", ingredientes_torta_milo)
        Producto.crearProductoPersonalizado("cheesecake", ingredientes_cheesecake)
        
        for i in Ingrediente._baseDatosIngredientes:
            print(i.getId() , i.getNombre(), i.getPrecioDeCompra(), i.getPrecioDeVenta())

        for i in Producto.baseDatosProductos:
            print(i.getId() , i.getNombre(), i.getCosto(), i.getIngredientes())

        
        print("productos creados")
        
        cliente1 = Cliente()
        cliente1.crearCuenta("Sahely", 1123433775, "123")
        cliente1.crearCuenta("Richard", 202, "qwerty")
        Cliente.getSesion().setPresupuesto(30000)
        
        domiciliario1 = Domiciliario("Nico", panaderia)
        domiciliario2 = Domiciliario("Sasha", panaderia)
        domiciliario2.setHabilidad(9)
        cocinero1 = Cocinero("Samuel", "Decoracion", panaderia)
        
        for i in panaderia.getTrabajadores():
            print(i.getNombre())

        print("trabajadores creados")

        for i in panaderia.getDomiciliarios():
            print(i.getNombre())
        print("domiciliarios creados")

        for i in panaderia.getCocineros():
            print(i.getNombre())

        print("cocineros creados")
    
        ingredientes_cocinar = {
            "13": 2,
            "14": 6,
            "15": 4,
            "16": 5,
            "17": 3
        }
        
        Cliente.getSesion().crearCanastaNueva()
        
        cliente1 = Cliente.inicioSesionId(202)
        Cliente.inicioSesionContrasena(cliente1, "qwerty")
        print("Cliente en sesion: " + Cliente.getSesion().getNombre())
        print("clientes creados")

        a=Cliente.getSesion().getCanastaOrden()
        
        print(a.recibir_orden("13", "3",False))
        a.recibir_orden("14", "2",False)
        a.recibir_orden("15", "1",True)
        a.recibir_orden("3", "3",False)
        a.recibir_orden("13", "3",False)
        print("canasta creada")
        
        print(a.getProductosEnLista())
        print(a.getIngredientesEnLista())
        print(a.getKitsEnLista())
    
        print("Elementos existentes añadidos correctamente a la canasta")
        ingredientes_marmota = {
            "carnita": 1,
            "meme": 2,
            "hormiga": 1,
            "azucar": 1,
            "mantequilla": 1
        }

        #print(a.recibirOrdenPersonalizada("marmota", ingredientes_marmota, "3",False))

        print(a.getProductosEnLista())
        print(a.getIngredientesEnLista())
        print(a.getKitsEnLista())
        
        print("Elementos personalizados añadidos correctamente a la canasta")
        #panaderia.cocinar(ingredientes_cocinar)
        
        for i in Ingrediente._baseDatosIngredientes:
            print(i.getId() , i.getNombre(), i.getPrecioDeCompra(), i.getPrecioDeVenta())

        for i in Producto.baseDatosProductos:
            print(i.getId() , i.getNombre(), i.getCosto(), i.getIngredientes())
        
        #a.enviarOrdenCanasta()
        #panaderia.cocinar(ingredientes_cocinar)
        for i in panaderia.getInventario()._invIngredientes:
            print(i.getNombre())
        for i in panaderia.getInventario()._invProductos:
            print(i.getNombre())

        #Serializador.guardarPanaderia(panaderia)
        print("panaderia guardada")

if __name__ == "__main__":
    test = SerializationTest()
    test.main(None)


