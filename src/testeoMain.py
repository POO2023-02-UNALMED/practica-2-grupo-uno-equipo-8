from gestorAplicacion.gestion.Panaderia import Panaderia
from gestorAplicacion.comida.Ingrediente import Ingrediente
from gestorAplicacion.comida.Producto import Producto
from gestorAplicacion.humanos.Cliente import Cliente
from gestorAplicacion.humanos.Domiciliario import Domiciliario
from gestorAplicacion.humanos.Cocinero import Cocinero
from baseDatos.Serializador import Serializador


class SerializationTest:
    def main(self, args):
        print("Test de funcionamiento")
        panaderia = Panaderia()
        Cliente.setPanaderia(panaderia)
        #panaderia = Serializador.cargarPanaderia()
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
    

        print("Cliente en sesion: " + Cliente.getSesion().getNombre())
        print("clientes creados")

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
        panaderia.cocinar(ingredientes_cocinar)
    
        Serializador.guardarPanaderia(panaderia)
        print("panaderia guardada")

if __name__ == "__main__":
    test = SerializationTest()
    test.main(None)
