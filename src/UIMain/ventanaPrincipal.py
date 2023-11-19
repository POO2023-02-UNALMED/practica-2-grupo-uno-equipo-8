from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from FieldFrame import FieldFrame

from ErrorAplicacion import CamposVaciosError, UsuarioNoEncontradoError, usuarioExistenteError

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from gestorAplicacion.humanos.Cliente import Cliente
from gestorAplicacion.comida.Producto import Producto
from gestorAplicacion.comida.Ingrediente import Ingrediente
from baseDatos.Serializador import Serializador

#Esta clase la cree yo (Richard), diganme si van a hacer algun cambio o si tienen alguna sugerencia
#Los errores los esta manejando samuel

class VentanaPrincipal:
    def __init__(self, root):

        #creando la ventana
        self.root = root
        self.root.title("Ventana principal")
        self.root.geometry("1000x800")

        self.panaderia = Serializador.cargarPanaderia()
        Cliente.setPanaderia(self.panaderia)

        #Menu superior
        self.menu_principal = tk.Menu(self.root)

        menu_archivo = tk.Menu(self.menu_principal, tearoff=0)
        menu_archivo.add_command(label="Aplicación", command=self.mostrar_info)
        menu_archivo.add_command(label="Salir", command=self.salir)
        self.menu_principal.add_cascade(label="Archivo", menu=menu_archivo)

        self.menu_procesos = tk.Menu(self.menu_principal, tearoff=0)
        self.menu_procesos.add_command(label = "Ventana principal", command = lambda: self.cambiarFrame(self.framePrincipal))
        self.menu_procesos.add_command(label = "Iniciar sesion", command= lambda: self.cambiarFrame(self.frameSesion))
        self.menu_procesos.add_command(label = "Registrarse", command= lambda: self.cambiarFrame(self.frameRegistro))
        self.menu_procesos.add_command(label = "Cerrar sesion", state="disabled",command = self.cerrarSesion)
        self.menu_procesos.add_command(label = "Func. Crear Canasta de Compras", state="disabled",command = lambda: self.cambiarFrame(self.frameComprar))
        self.menu_procesos.add_command(label = "Func. Facturar", state="disabled")
        self.menu_procesos.add_command(label = "Func. Cocinar", state="disabled")
        self.menu_procesos.add_command(label = "Func. Conseguir Ingredientes", state="disabled")
        self.menu_procesos.add_command(label = "Func. Domicilio", state="disabled")
        self.menu_procesos.add_command(label = "Lo mejor de nuestra panaderia", state="disabled",command = lambda: self.cambiarFrame(self.frameRanking))
        self.menu_procesos.add_command(label = "Ver facturas pasadas", state="disabled",command = lambda: self.cambiarFrame(self.frameHistorial))
        self.menu_procesos.add_command(label = "Modificar datos", state="disabled",command = lambda: self.cambiarFrame(self.frameModificarDatos))
        """
        self.menu_procesos.add_command(label = "Cambiar contraseña", state="disabled",command = lambda: self.cambiarFrame(self.frameContrasena))
        self.menu_procesos.add_command(label = "Meter plata a mi cuenta", state="disabled",command = lambda: self.cambiarFrame(self.framePlata))
        self.menu_procesos.add_command(label = "Validar tipo de cliente", state="disabled",command = lambda: self.cambiarFrame(self.frameValidarTipo))
        self.menu_procesos.add_command(label = "Modificar direccion", state="disabled",command = lambda: self.cambiarFrame(self.frameDireccion))
        """

        self.menu_principal.add_cascade(label="Procesos y Consultas", menu=self.menu_procesos)
        menu_ayuda = tk.Menu(self.menu_principal, tearoff=0)
        menu_ayuda.add_command(label="Acerca de", command=self.mostrar_autores)
        self.menu_principal.add_cascade(label="Ayuda", menu=menu_ayuda)

        self.root.config(menu=self.menu_principal)

        # Lista que va a contener todos los frames para facilitar el cambio entre estos
        self.frames = [] #lista de todos los frames necesaria para el metodo cambiarFrame

        # Creacion de los frames:



        # framePrincipal menu principal
        self.framePrincipal = Frame(self.root, bd=1, relief=FLAT, padx=1, pady=1)
        self.framePrincipal.pack()
        self.frameActual = self.framePrincipal
        self.frames.append(self.framePrincipal)
        #self.labelp1 = Label(self.framePrincipal, text="Entra a procesos y consultas para empezar a comprar")
        #self.labelp1.pack()
        self.imagen_1tk = tk.PhotoImage(file='src/resources/logoBienvenida.png')
        self.labelBienvenida = Label(self.framePrincipal, image = self.imagen_1tk)
        self.labelBienvenida.pack()




        # frameSesion inicio de sesion
        self.frameSesion = Frame(self.root, bd=1, relief=FLAT, padx=1, pady=1) 
        self.frames.append(self.frameSesion) #agregando a la lista de frames, necesaria para cambiar entre frames metodo cambiarFrame

        self.labelTituloInicioSesion = Label(self.frameSesion, text="INICIO DE SESION")
        self.labelTituloInicioSesion.pack(pady=20)
        
        self.descripTituloInicioSesion = Label(self.frameSesion, text="Descripcion")
        self.descripTituloInicioSesion.pack(pady=20)

        self.fieldFrameInicioSesion = FieldFrame("Datos Pedidos", ["Id:", "Contraseña:"], "Ingreselos Aquí")
        self.fieldFrameInicioSesion.defRoot(self.frameSesion)
        self.fieldFrameInicioSesion.defFunc(self.iniciarSesion)

        #frameActual = self.frameSesion



        # frameRegistro registro
        self.frameRegistro = Frame( #Esto esta pendiente de ser adaptado con fieldFrames
        self.root, bd=1, relief=FLAT, padx=1, pady=1)
        self.frames.append(self.frameRegistro)

        self.labelTituloRegistro = Label(self.frameRegistro, text="REGISTRO")
        self.labelTituloRegistro.pack(pady=20)
        
        self.descripRegistro = Label(self.frameRegistro, text="Descripcion")
        self.descripRegistro.pack(pady=20)

        self.fieldRegistro = FieldFrame("Datos Pedidos", ["Nombre:", "Id:", "Contraseña:"], "Ingreselos Aquí")
        self.fieldRegistro.defRoot(self.frameRegistro)
        self.fieldRegistro.defFunc(self.registrarUsuario)

        #frameActual = self.frameRegistro



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
        tk.Grid.columnconfigure(self.frameComprar,0, weight=1)
       # tk.Grid.columnconfigure(self.frameComprar,1, weight=1)
        tk.Grid.rowconfigure(self.frameComprar, 1, weight = 1)



        #El frame del carrito lo volví una funcion



        # frameCatalogo Catalogo de opciones disponibles para comprar
        self.frameCatalogo = Frame(self.root, bd=1, relief=FLAT, padx=1, pady=1)
        self.LabelCatalogo = Label(self.frameCatalogo, text="Catalogo de productos")
        self.LabelCatalogo.pack()

        self.frames.append(self.frameCatalogo)
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
        self.BotonAtrasCatalogo.pack(pady = 10)

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
        self.botonAtrasDescripcion = Button(self.frameDescripcion, text = "Volver al catalogo", command = lambda: self.cambiarFrame(self.frameCatalogo, False))
        self.botonAtrasDescripcion.pack(side="bottom", pady=15)

        self.frameDescripcion2 = Frame(self.frameDescripcion)
        self.frameDescripcion2.pack(fill = tk.BOTH, expand=True)
        self.labelfc1 = Label(self.frameDescripcion2, text="Lista de compras y factura")

        
        # Agregar un Scrollbar
        scrollbar = Scrollbar(self.frameDescripcion2)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Agregar un widget de Texto
        self.textoDescripcion = Text(self.frameDescripcion2, wrap=tk.WORD, yscrollcommand=scrollbar.set)
        self.textoDescripcion.pack(fill=tk.BOTH, expand=True)
        #self.textoDescripcion.insert()

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
        

        self.frameModificarDatos = Frame(self.root, bd=1, relief=FLAT, padx=1, pady=1)
        self.frames.append(self.frameModificarDatos)
        self.LabelModificarDatos = Label(self.frameModificarDatos, text="Modificar datos")
        self.LabelModificarDatos.pack()

        # frameContrasena cambiar contraseña
        self.frameContrasena = Frame(self.frameModificarDatos, bd=1, relief=FLAT, padx=1, pady=1)
        self.LabelContrasena = Label(self.frameContrasena, text="Cambiar contraseña")
        self.LabelContrasenaDes = Label(self.frameContrasena, text="Descripcion")
        self.LabelContrasena.pack(pady=20)
        self.LabelContrasenaDes.pack(pady=20)
        #usar fieldframe aqui ...
        self.fieldFrameContrasena = FieldFrame("Cambio", ["Contraseña nueva:"], "Ingrese aqui") #Ver ejemplo de uso en FieldFrame.py
        self.fieldFrameContrasena.defRoot(self.frameContrasena)
        self.frames.append(self.frameContrasena)
        
        # framePlata Meter plata a mi cuenta
        self.framePlata = Frame(self.frameModificarDatos, bd=1, relief=FLAT, padx=1, pady=1)
        self.LabelPlata = Label(self.framePlata, text="Meter plata")
        self.LabelPlataDes = Label(self.framePlata, text="Descripcion")
        self.LabelPlata.pack(pady=20)
        self.LabelPlataDes.pack(pady=20)
        #usar fieldframe aqui ...
        self.fieldFramePlata = FieldFrame("Valor", ["Cantidad a ingresar:"], "Ingrese aqui")
        self.fieldFramePlata.defRoot(self.framePlata)
        self.frames.append(self.framePlata)
        
        # frameValidarTipo Validar tipo de cliente
        self.frameValidarTipo = Frame(self.frameModificarDatos, bd=1, relief=FLAT, padx=1, pady=1)
        self.LabelValidarTipo = Label(self.frameValidarTipo, text="Validar tipo de cliente")
        self.LabelValidarTipo.pack()
        #usar fieldframe aqui ...
        self.frames.append(self.frameValidarTipo)
        
        # frameDireccion Modificar direccion
        self.frameDireccion = Frame(self.frameModificarDatos, bd=1, relief=FLAT, padx=1, pady=1)
        self.LabelDireccion = Label(self.frameDireccion, text="Cambiar direccion")
        self.LabelDireccionDes = Label(self.frameDireccion, text="Descripcion")
        self.LabelDireccion.pack(pady=20)
        self.LabelDireccionDes.pack(pady=20)
        #usar fieldframe aqui ...
        self.fieldFrameDireccion = FieldFrame("Datos", ["Ciudad", "Direccion específica:"], "Ingrese aqui")
        self.fieldFrameDireccion.defRoot(self.frameDireccion)
        self.frames.append(self.frameDireccion)

        #frame de conseguir ingredientes



    def cargarFrameCarrito(self):
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
        self.opcionesCompra = [] #IMPORTANTE despues de configurar serializacion colocar lista aqui
        for producto in Producto.baseDatosProductos:
            self.opcionesCompra.append(producto.getNombre())
        for ingrediente in Ingrediente._baseDatosIngredientes:
            self.opcionesCompra.append(ingrediente.getNombre())
        
        self.comboboxfc1 = ttk.Combobox(self.frameComprar1, values = self.opcionesCompra)
        self.comboboxfc1.pack(pady = 10)

        #Label para el segundo comboBo
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
        self.botonfc1 = Button(self.frameComprar1, text="Agregar a la canasta", command= self.registrarPedidoCanasta)
        self.botonfc1.pack(pady = 10)

        self.frameComprar2 = Frame(self.frameComprar)
        self.frameComprar2.grid(row =1 , column = 0, padx = 1, pady=1, sticky="nsew")
        self.labelfc1 = Label(self.frameComprar2, text="Lista de compras y factura")

        
        # Agregar un Scrollbar
        scrollbar = Scrollbar(self.frameComprar2)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Agregar un widget de Texto
        self.texto_widget = Text(self.frameComprar2, wrap=tk.WORD, yscrollcommand=scrollbar.set)
        self.texto_widget.pack(fill=tk.BOTH, expand=True)
        for elements, cantidad in Cliente.getSesion().getCanastaOrden().getProductosEnLista().items():
            self.texto_widget.insert(tk.END, "Producto: " + Producto.obtenerObjetoPorIdP(elements).getNombre() + " - Cantidad: " + str(cantidad) + "\n")
        for elements, cantidad in Cliente.getSesion().getCanastaOrden().getIngredientesEnLista().items():
            self.texto_widget.insert(tk.END, "Ingrediente: " + Ingrediente.obtenerObjetoPorIdI(elements).getNombre() + " - Cantidad: " + str(cantidad) + "\n")
        for elements, cantidad in Cliente.getSesion().getCanastaOrden().getKitsEnLista().items():
            self.texto_widget.insert(tk.END, "Kits: " + Producto.obtenerObjetoPorIdP(elements).getNombre() + " - Cantidad: " + str(cantidad) + "\n")

        #Frame funcionalidad 5
        self.frameComprarI



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
        #if Cliente.getSesion() == None:
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

    def registrarPedidoCanasta(self):
        producto = self.comboboxfc1.get()
        cantidad = self.comboboxfc1_2.get()
        self.texto_widget.insert(tk.END, "Producto: " + producto + " - Cantidad: " + cantidad + "\n")
        self.comboboxfc1.delete(0, 'end')
        self.comboboxfc1_2.delete(0, 'end')
        Cliente.getSesion().getCanastaOrden().recibir_orden(producto, cantidad, False)
        
    def cerrarSesion(self):
        Cliente.setSesion(None)
        self.menu_procesos.entryconfigure("Iniciar sesion", state="normal")
        self.menu_procesos.entryconfigure("Registrarse", state="normal")
        self.menu_procesos.entryconfigure("Cerrar sesion", state="disabled")
        
        self.menu_procesos.entryconfigure("Func. Crear Canasta de Compras", state="disabled")
        self.menu_procesos.entryconfigure("Func. Facturar", state="disabled")
        self.menu_procesos.entryconfigure("Func. Cocinar", state="disabled")
        self.menu_procesos.entryconfigure("Func. Conseguir Ingredientes", state="disabled")
        self.menu_procesos.entryconfigure("Func. Domicilio", state="disabled")

        self.menu_procesos.entryconfigure("Lo mejor de nuestra panaderia", state="disabled")
        self.menu_procesos.entryconfigure("Ver facturas pasadas", state="disabled")
        self.menu_procesos.entryconfigure("Modificar datos", state="disabled")
        #self.menu_procesos.entryconfigure("Cambiar contraseña", state="disabled")
        #self.menu_procesos.entryconfigure("Meter plata a mi cuenta", state="disabled")
        #self.menu_procesos.entryconfigure("Validar tipo de cliente", state="disabled")
        #self.menu_procesos.entryconfigure("Modificar direccion", state="disabled")
        self.cambiarFrame(self.framePrincipal)

    def iniciarSesion(self, val):
        while True:
            try:
                cliente1 = Cliente.inicioSesionId(int(val[0]))
                if cliente1 is None:
                    raise UsuarioNoEncontradoError(int(val[0]))

                if Cliente.inicioSesionContrasena(cliente1, val[1]) == "Contraseña incorrecta":
                    raise UsuarioNoEncontradoError(int(val[0]))

                self.menu_procesos.entryconfigure("Iniciar sesion", state="disabled")
                self.menu_procesos.entryconfigure("Registrarse", state="disabled")
                self.menu_procesos.entryconfigure("Cerrar sesion", state="normal")

                self.menu_procesos.entryconfigure("Func. Crear Canasta de Compras", state="normal")
                self.menu_procesos.entryconfigure("Func. Facturar", state="normal")
                self.menu_procesos.entryconfigure("Func. Cocinar", state="normal")
                self.menu_procesos.entryconfigure("Func. Conseguir Ingredientes", state="normal")
                self.menu_procesos.entryconfigure("Func. Domicilio", state="normal")
    
                self.menu_procesos.entryconfigure("Lo mejor de nuestra panaderia", state="normal")
                self.menu_procesos.entryconfigure("Ver facturas pasadas", state="normal")
                self.menu_procesos.entryconfigure("Modificar datos", state="normal")
                #self.menu_procesos.entryconfigure("Cambiar contraseña", state="normal")
                #self.menu_procesos.entryconfigure("Meter plata a mi cuenta", state="normal")
                #self.menu_procesos.entryconfigure("Validar tipo de cliente", state="normal")
                #self.menu_procesos.entryconfigure("Modificar direccion", state="normal")
                messagebox.showinfo("Inicio de sesion", "Inicio de sesion exitoso")
                self.cambiarFrame(self.framePrincipal)
                self.cargarFrameCarrito()
                break  # Sale del bucle si el inicio de sesión fue exitoso

            except UsuarioNoEncontradoError as e:
                messagebox.showwarning("Error", "El usuario o la contraseña son incorrectos")
                break  # Sale del bucle si se encuentra un error en el inicio de sesión
            except ValueError:
                messagebox.showwarning("Error", "El usuario debe ser un numero")
                break  # Sale del bucle si se encuentra un error en el inicio de sesión

    def registrarUsuario(self,val):
        try:
            if Cliente.crearCuenta(val[0], int(val[1]), val[2]) == "Ya existe una cuenta con ese ID":
                raise usuarioExistenteError
            messagebox.showinfo("Registro", "Usuario registrado correctamente")
            self.menu_procesos.entryconfigure("Iniciar sesion", state="disabled")
            self.menu_procesos.entryconfigure("Registrarse", state="disabled")
            self.menu_procesos.entryconfigure("Cerrar sesion", state="normal")
            
            self.menu_procesos.entryconfigure("Func. Crear Canasta de Compras", state="normal")
            self.menu_procesos.entryconfigure("Func. Facturar", state="normal")
            self.menu_procesos.entryconfigure("Func. Cocinar", state="normal")
            self.menu_procesos.entryconfigure("Func. Conseguir Ingredientes", state="normal")
            self.menu_procesos.entryconfigure("Func. Domicilio", state="normal")

            self.menu_procesos.entryconfigure("Lo mejor de nuestra panaderia", state="normal")
            self.menu_procesos.entryconfigure("Ver facturas pasadas", state="normal")
            self.menu_procesos.entryconfigure("Modificar datos", state="normal")
            #self.menu_procesos.entryconfigure("Cambiar contraseña", state="normal")
            #self.menu_procesos.entryconfigure("Meter plata a mi cuenta", state="normal")
            #self.menu_procesos.entryconfigure("Validar tipo de cliente", state="normal")
            #self.menu_procesos.entryconfigure("Modificar direccion", state="normal")
            self.cambiarFrame(self.framePrincipal)
        except usuarioExistenteError as e:
            messagebox.showwarning("Error", "El usuario ya existe")

# Codigo que produce la ejecucion de la ventana cuando se ejecuta desde este archivo
def main():
    root = Tk()
    app = VentanaPrincipal(root)
    root.mainloop()


if __name__ == "__main__":
    main()
