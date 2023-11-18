from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from FieldFrame import FieldFrame

from ErrorAplicacion import CamposVaciosError, UsuarioNoEncontradoError

#Esta clase la cree yo (Richard), diganme si van a hacer algun cambio o si tienen alguna sugerencia
#Los errores los esta manejando samuel

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
        menu_procesos.add_command(label = "Ver catalogo de productos y descripcion", command = lambda: self.cambiarFrame(self.frameCatalogo))
        menu_procesos.add_command(label = "Lo mejor de nuestra panaderia", command = lambda: self.cambiarFrame(self.frameRanking))
        menu_procesos.add_command(label = "Ver facturas pasadas", command = lambda: self.cambiarFrame(self.frameHistorial))
        menu_procesos.add_command(label = "Cambiar contraseña", command = lambda: self.cambiarFrame(self.frameContrasena))
        menu_procesos.add_command(label = "Meter plata a mi cuenta", command = lambda: self.cambiarFrame(self.framePlata))
        menu_procesos.add_command(label = "Validar tipo de cliente", command = lambda: self.cambiarFrame(self.frameValidarTipo))
        menu_procesos.add_command(label = "Modificar direccion", command = lambda: self.cambiarFrame(self.frameDireccion))

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
        #self.labelp1 = Label(self.framePrincipal, text="Entra a procesos y consultas para empezar a comprar")
        #self.labelp1.pack()
        self.imagen_1tk = tk.PhotoImage(file='src/resources/logoBienvenida.png')
        self.labelBienvenida = Label(self.framePrincipal, image = self.imagen_1tk)
        self.labelBienvenida.pack()
        
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

        self.boton_Registro = Button(self.frameRegistro, text="Registrarse", command = self.registrarse)
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
        tk.Grid.rowconfigure(self.frameComprar,0, weight=1)
        tk.Grid.columnconfigure(self.frameComprar,0, weight=6)
        tk.Grid.columnconfigure(self.frameComprar,1, weight=1)

        #framep1 = Frame(frame, bd = 5, relief=FLAT, padx = 2, pady = 2, bg = "white").grid(row =0 , column = 0)
        #framep2 = Frame(frame, bd = 5, relief=FLAT, padx = 2, pady = 2, bg = "white").grid(row =0 , column = 1)
        self.frameComprar1 = Frame(self.frameComprar)
        self.frameComprar1.grid(row =0 , column = 0, padx = 1, pady=1, sticky="nsew")
        self.labelfc1 = Label(self.frameComprar1, text="Hola cliente, bienvenido a su canasta de compras, use el comboBox para ordenar, recuerde que en el menu procesos y consultas puede ver un catalogo mas completo de los productos que puede ordenar", wraplength=300)
        self.labelfc1.pack(pady=30)

        #Label para el primer comboBox
        self.labelfc1_2 = Label(self.frameComprar1, text="Elija un producto")
        self.labelfc1_2.pack(pady = 5)
        
        #Creando el primer comboBox
        self.opcionesCompra = ["Pandequeso", "Bonice", "Manzana podrida"] #IMPORTANTE despues de configurar serializacion colocar lista aqui
        self.comboboxfc1 = ttk.Combobox(self.frameComprar1, values = self.opcionesCompra)
        self.comboboxfc1.pack(pady = 10)

        #Label para el segundo comboBox
        self.labelfc1_3 = Label(self.frameComprar1, text="Elija una cantidad")
        self.labelfc1_3.pack(pady = 5)
        
        self.botonIrCatalogo = tk.Button(self.frameComprar1, text="Ir al catalogo", command = lambda: self.cambiarFrame(self.frameCatalogo))
        self.botonIrCatalogo.pack(side="bottom", pady=50)

        self.botonCocinar = tk.Button(self.frameComprar1, text="Cocinar producto personalizado")
        self.botonCocinar.pack(side="bottom", pady=10)

        #credando el segundo comboBox
        self.opcionesCantidad = [1,2,3,4,5,6,7,8,9,10]
        self.comboboxfc1_2 = ttk.Combobox(self.frameComprar1, values = self.opcionesCantidad)
        self.comboboxfc1_2.pack(pady = 10)
        self.botonfc1 = Button(self.frameComprar1, text="Agregar a la canasta")
        self.botonfc1.pack(pady = 10)

        self.frameComprar2 = Frame(self.frameComprar)
        self.frameComprar2.grid(row =0 , column = 1, padx = 1, pady=1, sticky="nsew")
        self.labelfc1 = Label(self.frameComprar2, text="Lista de compras y factura")

        # Agregar un Scrollbar
        scrollbar = Scrollbar(self.frameComprar2)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Agregar un widget de Texto
        self.texto_widget = Text(self.frameComprar2, wrap=tk.WORD, yscrollcommand=scrollbar.set, width = 60)
        self.texto_widget.pack(fill=tk.Y, expand=True),
        # frameCatalogo Catalogo de opciones disponibles para comprar
        self.frameCatalogo = Frame(self.root, bd=1, relief=FLAT, padx=1, pady=1)
        self.LabelCatalogo = Label(self.frameCatalogo, text="Catalogo de productos")
        self.BotonAtrasCatalogo = Button(self.frameCatalogo, text="volver atras", command= self.volverAtras)
        self.BotonAtrasCatalogo.pack(side=BOTTOM, pady=40)
        self.LabelCatalogo.pack()
    
        self.frames.append(self.frameCatalogo)
        self.LabelCatalogo = Label(self.frameCatalogo, text="Catalogo de productos")
        self.LabelCatalogo.pack()
        self.frameCatalogo2 = Frame(self.frameCatalogo, bd=1, relief=FLAT, padx=1, pady=1)
        self.frameCatalogo2.pack(fill="both", expand=True)

        #El catalogo va a ser una fila de 3 productos,

        # Crear un canvas con un scrollbar
        self.canvas = tk.Canvas(self.frameCatalogo2)
        scrollbar = tk.Scrollbar(self.frameCatalogo2, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=scrollbar.set)

        # Crear un frame dentro del canvas para colocar los botones
        self.frameCatalogo3 = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window = self.frameCatalogo3, anchor="nw")

        # Crear una variable para contar los botones
        self.contadorCatalogo = tk.IntVar()
        self.contadorCatalogo.set(0)

        self.iconoDefault = tk.PhotoImage(file="src/resources/iconoManzana1.png")
        
        #Empaquetar el canvas y el scrollbar
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.agregarAlCatalogo("Pancake con forma de manzana1")
        self.agregarAlCatalogo("Pancake con forma de manzana2")
        self.agregarAlCatalogo("Pancake con forma de manzana3")
        self.agregarAlCatalogo("Pancake con forma de manzana4")
        self.agregarAlCatalogo("Pancake con forma de manzana5")
        self.agregarAlCatalogo("Pancake con forma de manzana6")
        self.agregarAlCatalogo("Pancake con forma de manzana7")
        self.agregarAlCatalogo("Pancake con forma de manzana8")
        self.agregarAlCatalogo("Pancake con forma de manzana9")
        self.agregarAlCatalogo("Pancake con forma de manzana10")
        self.agregarAlCatalogo("Pancake con forma de manzana11")
        self.agregarAlCatalogo("Pancake con forma de manzana12")
        self.agregarAlCatalogo("Pancake con forma de manzana13")
        self.agregarAlCatalogo("Pancake con forma de manzana14")

        self.BotonAtrasCatalogo = Button(self.frameCatalogo, text="volver atras", command= self.volverAtras)
        self.BotonAtrasCatalogo.pack()

        # frameDescripcion Descripcion de los productos
        self.frameDescripcion = Frame(self.root, bd=1, relief=FLAT, padx=1, pady=1)
        self.frames.append(self.frameDescripcion)
        self.LabelDescripcion = Label(self.frameDescripcion)
        self.LabelDescripcion.pack(pady = 15)
        self.fotoDescripcion = Label(self.frameDescripcion)
        self.fotoDescripcion.pack(pady=15)
        self.LabelDescripcion2 = Label(self.frameDescripcion) #En este label va a ir la calificacion del producto
        self.LabelDescripcion2.pack(pady = 15)
        self.LabelDescripcion3 = Label(self.frameDescripcion) #En este label va a ir la descripcion del producto
        self.LabelDescripcion3.pack(pady = 15)
        self.botonAtrasDescripcion = Button(self.frameDescripcion, text = "Volver al catalogo", command= self.volverAtras)
        self.botonAtrasDescripcion.pack(side="bottom", pady=15)

        #frameRanking Lo mejor de nuestra panaderia
        self.frameRanking = Frame(self.root, bd=1, relief=FLAT, padx=1, pady=1)
        self.LabelRanking = Label(self.frameRanking, text="Lo mejor de POOBakery")
        self.LabelRanking.pack()
        #usar fieldframe aqui ...
        self.frames.append(self.frameRanking)
                
        # frameHistorial Historial de facturas
        self.frameHistorial = Frame(self.root, bd=1, relief=FLAT, padx=1, pady=1)
        self.LabelHistorial = Label(self.frameHistorial, text="Historial de facturas")
        self.LabelHistorial.pack()
        #usar fieldframe aqui ...
        self.frames.append(self.frameHistorial)
        
        # frameContrasena cambiar contraseña
        self.frameContrasena = Frame(self.root, bd=1, relief=FLAT, padx=1, pady=1)
        self.LabelContrasena = Label(self.frameContrasena, text="Cambiar contraseña")
        self.LabelContrasena.pack()
        #usar fieldframe aqui ...
        self.fieldFrameContrasena = FieldFrame("Cambio", ["Contraseña nueva:", "hola"], "Ingrese aqui") #Ver ejemplo de uso en FieldFrame.py
        self.fieldFrameContrasena.defRoot(self.frameContrasena)
        self.frames.append(self.frameContrasena)
        
        # framePlata Meter plata a mi cuenta
        self.framePlata = Frame(self.root, bd=1, relief=FLAT, padx=1, pady=1)
        self.LabelPlata = Label(self.framePlata, text="Meter plata")
        self.LabelPlata.pack()
        #usar fieldframe aqui ...
        self.frames.append(self.framePlata)
        
        # frameValidarTipo Validar tipo de cliente
        self.frameValidarTipo = Frame(self.root, bd=1, relief=FLAT, padx=1, pady=1)
        self.LabelValidarTipo = Label(self.frameValidarTipo, text="Validar tipo de cliente")
        self.LabelValidarTipo.pack()
        #usar fieldframe aqui ...
        self.frames.append(self.frameValidarTipo)
        
        # frameDireccion Modificar direccion
        self.frameDireccion = Frame(self.root, bd=1, relief=FLAT, padx=1, pady=1)
        self.LabelDireccion = Label(self.frameDireccion, text="Cambiar direccion")
        self.LabelDireccion.pack()
        #usar fieldframe aqui ...
        self.frames.append(self.frameDireccion)
        
        #Metodos necesiarios para la interfaz de usuario
    def verificar_campos_llenos(self, campos):  # Asegúrate de pasar 'self' como primer argumento
        campos_vacios = [campo for campo in campos if len(campo) == 0]
        if campos_vacios:
            raise CamposVaciosError(campos_vacios)
        
    def verificar_existencia_usuario(self, usuario):
        # Lógica para verificar si el usuario existe
        # Podrías usar alguna base de datos o alguna estructura de datos para almacenar usuarios y verificar su existencia
        # Por ejemplo, si tienes una lista de usuarios, podrías hacer algo como esto:
        # return usuario in self.lista_de_usuarios
        return False  # Aquí devolverías True si el usuario existe y False si no existe

    def iniciar_sesion(self):
        while True:
            usuario = self.entry_usuario.get()
            contrasena = self.entry_contrasena.get()

            try:
                campos = [usuario, contrasena]
                self.verificar_campos_llenos(campos)
                # Aquí podrías validar si el usuario y la contraseña son correctos antes de cambiar el frame
                # Agregar lógica para verificar la existencia del usuario
                if not self.verificar_existencia_usuario(usuario):
                    raise UsuarioNoEncontradoError(usuario)
                
                self.cambiarFrame(self.framePrincipal)
                break  # Sale del bucle si los campos son válidos y el usuario existe
            except CamposVaciosError as e:
                mensaje = f"Por favor, complete los campos: {len(e.campos_faltantes)} usuario y/o contraseña"
                messagebox.showwarning("Campos Vacíos", mensaje)
                self.entry_usuario.delete(0, 'end')
                self.entry_contrasena.delete(0, 'end')
                break  # Sale del bucle para permitir al usuario reintentar el inicio de sesión
            except UsuarioNoEncontradoError as e:
                messagebox.showwarning("Usuario no encontrado", f"El usuario '{e.usuario}' no fue encontrado.")
                self.entry_usuario.delete(0, 'end')
                self.entry_contrasena.delete(0, 'end')
                break  # Sale del bucle para permitir al usuario reintentar el inicio de sesión
        
    def registrarse(self):
        while True:
            usuario = self.entry_RegistroUsuario.get()
            contrasena = self.entry_RegistroContrasena.get()
            identificacion = self.entry_RegistroIdentificacion.get()

            try:
                campos = [usuario, contrasena, identificacion]
                self.verificar_campos_llenos(campos)
                # Aquí podrías validar si el usuario y la contraseña son correctos antes de cambiar el frame
                # Agregar lógica para verificar la existencia del usuario
                if not self.verificar_existencia_usuario(usuario):
                    raise UsuarioNoEncontradoError(usuario)
                
                self.cambiarFrame(self.framePrincipal)
                break  # Sale del bucle si los campos son válidos y el usuario existe
            except CamposVaciosError as e:
                mensaje = f"Por favor, complete los campos: {len(e.campos_faltantes)} usuario y/o contraseña y/o identificacion"
                messagebox.showwarning("Campos Vacíos", mensaje)
                self.entry_usuario.delete(0, 'end')
                self.entry_contrasena.delete(0, 'end')
                break
    
    def mostrar_info(self):
        
        info = '''Con nuestra aplicación, puedes realizar pedidos de postres y otros productos de nuestra panadería desde la comodidad de tu hogar. Hemos creado una interfaz fácil de usar que te permite navegar por nuestros productos y agregarlos a tu carrito de compras. También puedes guardar tus productos favoritos para futuras compras. Una vez que hayas agregado los productos que deseas comprar a tu carrito, puedes realizar el pago de forma segura y sencilla a través de nuestra aplicación. Estamos comprometidos a ofrecerte una experiencia de compra fácil y sin problemas. Si tienes alguna pregunta o problema, no dudes en ponerte en contacto con nosotros a través de nuestra aplicación.
        ¡Gracias por elegir POOBakery!'''
        messagebox.showinfo("Información", info)
        #self.labelInformacion.config(text=info)
        #self.cambiarFrame(self.frameInfo)
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
        messagebox.showinfo("Información", info)
        #self.labelInformacion.config(text=info)
        #self.cambiarFrame(self.frameInfo)
        pass

    def salir(self):
        self.root.destroy()

    def cambiarFrame(self, frame, guardarComoFrameAnterior = True):
        if guardarComoFrameAnterior == True:
            self.frameAnterior = self.frameActual

        for f in self.frames:
            if f == frame:
                f.pack(padx = 5, pady = 5, fill = "both", expand=True)
                self.frameActual = frame
            else:
                f.pack_forget()
    
    def volverAtras(self):
        self.cambiarFrame(self.frameAnterior)

    def agregarAlCatalogo(self, nombre, foto = None, descripcion = "Este producto aun no tiene descripcion, pero te invitamos a probarlo" , calificacion = "☆☆☆☆☆"):
        if foto == None:
            foto = self.iconoDefault

        # Incrementar el contador
        self.contadorCatalogo.set(self.contadorCatalogo.get() + 1)

        # Crear un botón con una imagen y un nombre
        boton = tk.Button(self.frameCatalogo3, text=nombre, image = foto, compound="top", command = lambda: self.mostrarDescripcion(nombre, foto, descripcion, calificacion))

        # Colocar el botón en el grid según el contador
        fila = (self.contadorCatalogo.get() - 1) // 3
        columna = (self.contadorCatalogo.get() - 1) % 3
        boton.grid(row=fila, column=columna, padx=5, pady=5)

        # Actualizar el tamaño del frame y el canvas
        self.frameCatalogo3.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def mostrarDescripcion(self, nombre, foto, descripcion, calificacion):
        self.cambiarFrame(self.frameDescripcion, False)
        self.LabelDescripcion.config(text="Descripcion de "+ nombre)
        self.fotoDescripcion.config(image = foto)
        self.LabelDescripcion2.config(text = "Calificacion de nuestros clientes: "+calificacion)
        self.LabelDescripcion3.config(text = descripcion)

        

# Codigo que produce la ejecucion de la ventana cuando se ejecuta desde este archivo
def main():
    root = Tk()
    app = VentanaPrincipal(root)
    root.mainloop()


if __name__ == "__main__":
    main()
