import pickle

from gestorAplicacion.comida.Ingrediente import Ingrediente
from gestorAplicacion.comida.Producto import Producto
from gestorAplicacion.gestion.Panaderia import Panaderia
from gestorAplicacion.gestion.Recibo import Recibo

class Serializador:
    @staticmethod
    def guardarPanaderia(panaderia):
        try:
            with open("panaderia.pickle", "wb") as file:
                pickle.dump(panaderia, file)
                Serializador.guardarValoresEstaticos(file)

            print("La información de la panadería se ha guardado en panaderia.pickle")
        except IOError as e:
            print(f"Error al guardar la información de la panadería: {e}")

    @staticmethod
    def cargarPanaderia():
        panaderia = None
        try:
            with open("panaderia.pickle", "rb") as file:
                panaderia = pickle.load(file)
                Serializador.cargarValoresEstaticos(file)

            print("La información de la panadería se ha cargado desde panaderia.pickle")
        except IOError as e:
            print(f"Error al cargar la información de la panadería: {e}")

        return panaderia

    @staticmethod
    def guardarValoresEstaticos(file):
        pickle.dump(Panaderia.getCanastaDelDia(), file)
        pickle.dump(Ingrediente.getBaseDatosIngredientes(), file)
        file.write(Ingrediente.getCantidadIngredientesUnicos().to_bytes(4, byteorder='big'))
        pickle.dump(Ingrediente.getTopMasVendidos(), file)
        pickle.dump(Producto.getBaseDatosProductos(), file)
        file.write(Producto.getCantidadProductosUnicos().to_bytes(4, byteorder='big'))
        pickle.dump(Producto.getTopMasVendidos(), file)
        file.write(Recibo.getTotalFacturas().to_bytes(4, byteorder='big'))

    @staticmethod
    def cargarValoresEstaticos(file):
        Panaderia.setCanastaDelDia(pickle.load(file))
        Ingrediente.setBaseDatosIngredientes(pickle.load(file))
        Ingrediente.setCantidadIngredientesUnicos(int.from_bytes(file.read(4), byteorder='big'))
        Ingrediente.setTopMasVendidos(pickle.load(file))
        Producto.setBaseDatosProductos(pickle.load(file))
        Producto.setCantidadProductosUnicos(int.from_bytes(file.read(4), byteorder='big'))
        Producto.setTopMasVendidos(pickle.load(file))
        Recibo.setTotalFacturas(int.from_bytes(file.read(4), byteorder='big'))
