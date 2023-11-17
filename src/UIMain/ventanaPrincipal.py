from tkinter import *
import tkinter as tk

#Esta clase la cree yo (Richard), diganme si van a hacer algun cambio o si tienen alguna sugerencia

class VentanaPrincipal:
    def __init__(self, root):

        #creando la ventana
        self.root = root
        self.root.title("Ventana principal")
        self.root.geometry("1000x800")


        #Menu superior
        self.menu_principal = tk.Menu(self.root)

        menu_archivo = tk.Menu(self.menu_principal, tearoff=0)
        menu_archivo.add_command(label="Aplicación", command=self.mostrar_info)
        menu_archivo.add_command(label="Salir", command=self.salir)
        self.menu_principal.add_cascade(label="Archivo", menu=menu_archivo)

        menu_procesos = tk.Menu(self.menu_principal, tearoff=0)
        menu_procesos.add_command(label = "Ventana principal", command = lambda: self.cambiarFrame(self.framePrincipal))
        menu_procesos.add_command(label = "Iniciar sesion", command= lambda: self.cambiarFrame(self.frameSesion))
        menu_procesos.add_command(label = "Registrarse", command= lambda: self.cambiarFrame(self.frameRegistro))
        menu_procesos.add_command(label = "Cerrar sesion")
        menu_procesos.add_command(label = "Ir a comprar", command = lambda: self.cambiarFrame(self.frameComprar))
        menu_procesos.add_command(label = "Ver catalogo de productos y descripcion")
        menu_procesos.add_command(label = "Lo mejor de nuestra panaderia")
        menu_procesos.add_command(label = "Ver facturas pasadas")
        menu_procesos.add_command(label = "Cambiar contraseña")
        menu_procesos.add_command(label = "Meter plata a mi cuenta")
        menu_procesos.add_command(label = "Validar tipo de cliente")
        menu_procesos.add_command(label = "Modificar direccion")

        self.menu_principal.add_cascade(label="Procesos y Consultas", menu=menu_procesos)
        menu_ayuda = tk.Menu(self.menu_principal, tearoff=0)
        menu_ayuda.add_command(label="Acerca de", command=self.mostrar_autores)
        self.menu_principal.add_cascade(label="Ayuda", menu=menu_ayuda)

        self.root.config(menu=self.menu_principal)

        # Lista que va a contener todos los frames para facilitar el cambio entre estos
        self.frames = [] #lista de todos los frames necesaria para el metodo cambiarFrame

        # Creacion de los frames:

        # framePrincipal menu principal
        self.framePrincipal = Frame(
        self.root, bd=1, relief=FLAT, padx=1, pady=1)
        self.framePrincipal.pack()
        self.frameActual = self.framePrincipal
        self.frames.append(self.framePrincipal)
        self.labelp1 = Label(self.framePrincipal, text="Bienvenido a pooBakery, este es el menu")
        self.labelp1.pack()
        
        # frameSesion inicio de sesion
        self.frameSesion = Frame( #Esto esta pendiente de ser adaptado con fieldFrames
        self.root, bd=1, relief=FLAT, padx=1, pady=1) 
        self.frames.append(self.frameSesion) #agregando a la lista de frames, necesaria para cambiar entre frames metodo cambiarFrame
        self.root.title("Inicio de Sesión")

        self.label_usuario = Label(self.frameSesion, text="Usuario:")
        self.label_usuario.pack(pady=10)

        self.entry_usuario = Entry(self.frameSesion)
        self.entry_usuario.pack(pady=10)

        self.label_contrasena = Label(self.frameSesion, text="Contraseña:")
        self.label_contrasena.pack(pady=10)

        self.entry_contrasena = Entry(self.frameSesion, show="*")
        self.entry_contrasena.pack(pady=10)

        self.boton_iniciar_sesion = Button(self.frameSesion, text="Iniciar Sesión", command = self.iniciar_sesion)
        self.boton_iniciar_sesion.pack(pady=10)

        frameActual = self.frameSesion

        # frameRegistro registro
        self.frameRegistro = Frame( #Esto esta pendiente de ser adaptado con fieldFrames
        self.root, bd=1, relief=FLAT, padx=1, pady=1)
        self.frames.append(self.frameRegistro)

        self.root.title("Registro")

        self.label_RegistroUsuario = Label(self.frameRegistro, text="Usuario:")
        self.label_RegistroUsuario.pack(pady=10)

        self.entry_RegistroUsuario = Entry(self.frameRegistro)
        self.entry_RegistroUsuario.pack(pady=10)

        self.label_RegistroIdentificacion = Label(self.frameRegistro, text="Identificacion: ")
        self.label_RegistroIdentificacion.pack(pady=10)

        self.entry_RegistroIdentificacion = Entry(self.frameRegistro)
        self.entry_RegistroIdentificacion.pack(pady=10)

        self.label_RegistroContrasena = Label(self.frameRegistro, text="Contraseña:")
        self.label_RegistroContrasena.pack(pady=10)

        self.entry_RegistroContrasena = Entry(self.frameRegistro, show="*")
        self.entry_RegistroContrasena.pack(pady=10)

        self.boton_Registro = Button(self.frameRegistro, text="Registrarse", command = self.iniciar_sesion)
        self.boton_Registro.pack(pady=10)

        # frameInfo frame con informacion
        self.frameInfo = Frame(self.root, bd=1, relief=FLAT, padx=1, pady=1)
        self.frames.append(self.frameInfo)
        self.labelInformacion = Label(self.frameInfo, text="Informacion aqui")
        self.labelInformacion.pack()
        self.infoBoton = Button(self.frameInfo, text="Volver atras", command= self.volverAtras)
        self.infoBoton.pack(pady = 20)

        # frameComprar Ir a comprar
        self.frameComprar = Frame(root, bd = 1, relief=FLAT, padx = 1, pady = 1)
        self.frames.append(self.frameComprar)
        #self.frameComprar.pack(padx = 5, pady = 5, fill = "both", expand=True)
        tk.Grid.rowconfigure(self.frameComprar,0, weight=1)
        #tk.Grid.rowconfigure(frame,1, weight=1)
        tk.Grid.columnconfigure(self.frameComprar,0, weight=1)
        tk.Grid.columnconfigure(self.frameComprar,1, weight=1)

        #framep1 = Frame(frame, bd = 5, relief=FLAT, padx = 2, pady = 2, bg = "white").grid(row =0 , column = 0)
        #framep2 = Frame(frame, bd = 5, relief=FLAT, padx = 2, pady = 2, bg = "white").grid(row =0 , column = 1)
        self.frameComprar1 = Frame(self.frameComprar, bg = "blue").grid(row =0 , column = 0, padx = 1, pady=1, sticky="nsew")
        self.frameComprar2 = Frame(self.frameComprar, bg = "red").grid(row =0 , column = 1, padx = 1, pady=1, sticky="nsew")
        
        # frameCatalogo Catalogo de opciones disponibles para comprar
        self.frameCatalogo = Frame(self.root, bd=1, relief=FLAT, padx=1, pady=1)
        self.frames.append(self.frameCatalogo)
        
        # frameRanking Lo mejor de nuestra panaderia
        self.frameRanking = Frame(self.root, bd=1, relief=FLAT, padx=1, pady=1)
        self.frames.append(self.frameRanking)
        
        # frameHistorial Historial de facturas
        self.frameHistorial = Frame(self.root, bd=1, relief=FLAT, padx=1, pady=1)
        self.frames.append(self.frameHistorial)
        
        # frameContrasena cambiar contraseña
        self.frameContrasena = Frame(self.root, bd=1, relief=FLAT, padx=1, pady=1)
        self.frames.append(self.frameContrasena)
        
        # framePlata Meter plata a mi cuenta
        self.framePlata = Frame(self.root, bd=1, relief=FLAT, padx=1, pady=1)
        self.frames.append(self.framePlata)
        
        # frameValidarTipo Validar tipo de cliente
        self.frameValidarTipo = Frame(self.root, bd=1, relief=FLAT, padx=1, pady=1)
        self.frames.append(self.frameValidarTipo)
        
        # frameDireccion Modificar direccion
        self.frameDireccion = Frame(self.root, bd=1, relief=FLAT, padx=1, pady=1)
        self.frames.append(self.frameDireccion)
        
    #Metodos necesiarios para la interfaz de usuario
    def iniciar_sesion(self):
        #aqui deberia haber algun condicional para ver si el usuario si existe
        self.cambiarFrame(self.framePrincipal)
    
    def mostrar_info(self):
        info = '''
        ¡Bienvenido a la aplicación de POOBakery!
        
        Con nuestra aplicación, puedes realizar pedidos de postres y otros productos de nuestra panadería desde la comodidad de tu hogar. 
        Hemos creado una interfaz fácil de usar que te permite navegar por nuestros productos y agregarlos a tu carrito de compras.
        También puedes guardar tus productos favoritos para futuras compras. 
        Una vez que hayas agregado los productos que deseas comprar a tu carrito, 
        puedes realizar el pago de forma segura y sencilla a través de nuestra aplicación.
        Estamos comprometidos a ofrecerte una experiencia de compra fácil y sin problemas.
        Si tienes alguna pregunta o problema, no dudes en ponerte en contacto con nosotros a través de nuestra aplicación.
         
        ¡Gracias por elegir POOBakery!

         '''
        self.labelInformacion.config(text=info)
        self.cambiarFrame(self.frameInfo)
        pass

    def mostrar_autores(self):
        info = '''
        Este programa fue creado por:
        Mateo Builes
        Richard Muñoz Henao
        Sahely Romero
        Samuel Castaño
        Nicolas Echeverry
         '''
        self.labelInformacion.config(text=info)
        self.cambiarFrame(self.frameInfo)
        pass

    def salir(self):
        self.root.destroy()

    def cambiarFrame(self, frame):
        self.frameAnterior = self.frameActual
        for f in self.frames:
            if f == frame:
                f.pack(padx = 5, pady = 5, fill = "both", expand=True)
                self.frameActual = frame
            else:
                f.pack_forget()
    
    def volverAtras(self):
        self.cambiarFrame(self.frameAnterior)

# Codigo que produce la ejecucion de la ventana cuando se ejecuta desde este archivo
def main():
    root = Tk()
    app = VentanaPrincipal(root)
    root.mainloop()


if __name__ == "__main__":
    main()
