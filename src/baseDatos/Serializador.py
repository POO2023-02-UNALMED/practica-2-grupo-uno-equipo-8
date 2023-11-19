import os
import pickle

# Obtener la ruta del directorio donde se encuentra este script
directorio_actual = os.path.dirname(os.path.abspath(__file__))

# Nombre del archivo pickle
nombre_archivo_pickle = "panaderia.pickle"

# Crear la ruta al archivo pickle utilizando os.path.join()
ruta_al_pickle = os.path.join(directorio_actual, nombre_archivo_pickle)

class Serializador:
    @staticmethod
    def guardarPanaderia(panaderia):
        try:
            with open(ruta_al_pickle, "wb") as file:
                pickle.dump(panaderia, file)
                Serializador.guardarValoresEstaticos(file)

            print("La información de la panadería se ha guardado en panaderia.pickle")
        except IOError as e:
            print(f"Error al guardar la información de la panadería: {e}")

    @staticmethod
    def cargarPanaderia():
        panaderia = None
        try:
            with open(ruta_al_pickle, "rb") as file:
                panaderia = pickle.load(file)
                Serializador.cargarValoresEstaticos(file)

            print("La información de la panadería se ha cargado desde panaderia.pickle")
        except IOError as e:
            print(f"Error al cargar la información de la panadería: {e}")

        return panaderia

    @staticmethod
    def guardarValoresEstaticos(file):

        from gestorAplicacion.comida.Ingrediente import Ingrediente
        from gestorAplicacion.comida.Producto import Producto
        from gestorAplicacion.gestion.Panaderia import Panaderia
        from gestorAplicacion.gestion.Recibo import Recibo
        from gestorAplicacion.comida.ComidaDefault import ComidaDefault

        pickle.dump(Panaderia.getCanastaDelDia(), file)
        pickle.dump(Ingrediente.getBaseDatosIngredientes(), file)
        file.write(ComidaDefault.getContador().to_bytes(4, byteorder='big'))
        pickle.dump(Ingrediente.getTopMasVendidos(), file)
        pickle.dump(Producto.getBaseDatosProductos(), file)
        pickle.dump(Producto.getTopMasVendidos(), file)
        file.write(Recibo.getTotalFacturas().to_bytes(4, byteorder='big'))

    @staticmethod
    def cargarValoresEstaticos(file):
        from gestorAplicacion.comida.Ingrediente import Ingrediente
        from gestorAplicacion.comida.Producto import Producto
        from gestorAplicacion.gestion.Panaderia import Panaderia
        from gestorAplicacion.gestion.Recibo import Recibo
        from gestorAplicacion.comida.ComidaDefault import ComidaDefault

        Panaderia.setCanastaDelDia(pickle.load(file))
        Ingrediente.setBaseDatosIngredientes(pickle.load(file))
        ComidaDefault.setContador(int.from_bytes(file.read(4), byteorder='big'))

        Ingrediente.setTopMasVendidos(pickle.load(file))
        Producto.setBaseDatosProductos(pickle.load(file))
        Producto.setTopMasVendidos(pickle.load(file))
        Recibo.setTotalFacturas(int.from_bytes(file.read(4), byteorder='big'))
