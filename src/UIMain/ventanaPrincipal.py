from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from FieldFrame import FieldFrame
from Texto import centrar
from ErrorAplicacion import CamposVaciosError, CantidadInvalidaError, ProductoNoEncontradoError, UsuarioNoEncontradoError, usuarioExistenteError

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

        #Listas exclusivas para la funcionalidad 5
        self.diccionarioFuncionalidad5 = {}

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
        self.menu_procesos.add_command(label = "Func. Cocinar",command=lambda:self.cambiarFrame(self.frameCocinar), state="disabled")
        self.menu_procesos.add_command(label = "Func. Conseguir Ingredientes", command=lambda:self.cambiarFrame(self.frameComprarIngredientes), state="disabled")
        self.menu_procesos.add_command(label = "Func. Domicilio", state="disabled")
        self.menu_procesos.add_command(label = "Lo mejor de nuestra panaderia", state="disabled",command = lambda: self.cambiarFrame(self.frameLoMejor))

        self.menu_procesos.add_command(label = "Modificar datos", state="disabled",command = lambda: self.cambiarFrame(self.frameModificarDatos))
        
        

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
        #self.imagen_2tk = tk.PhotoImage(file='src/resources/ratonInicio.png')
        #self.labelBienvenida2 = Label(self.framePrincipal, image = self.imagen_2tk)
        #self.labelBienvenida2.pack()
        self.labelBienvenida3 = Label(self.framePrincipal, text="Bienvenido a nuestra aplicacion, en el menu de procesos y consultas podras iniciar tu compra, elije crear canasta de compras y haz tu pedido ya!")
        self.labelBienvenida3.pack()



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

        #El frame del carrito lo volví una funcion cargarFrameCarrito()

        # framePreguntarDomicilio preguntar al cliente si deseaDomicilio
        self.framePreguntarDomicilio = Frame(self.root, bd = 1, relief=FLAT, pady = 1)
        self.frames.append(self.framePreguntarDomicilio)
        self.imagenfpd = tk.PhotoImage(file="src/resources/ratonDomicilio.png")
        self.imagenPreguntarDomicilio = Label(self.framePreguntarDomicilio, image = self.imagenfpd)
        self.imagenPreguntarDomicilio.pack(pady=5)
        self.labelPreguntarDomicilio = Label(self.framePreguntarDomicilio, text="Desea que le entreguemos su pedido a domicilio? Haga click abajo si asi lo desea")
        self.labelPreguntarDomicilio.pack(pady=5)
        self.checkButtonFramePreguntarDomicilio = ttk.Checkbutton(self.framePreguntarDomicilio, text="Pedido a domicilio") # Logica Domicilio que cuando el checkButton este activado se envie a domicilio
        self.checkButtonFramePreguntarDomicilio.pack(pady=5)

        # fieldframe domicilio
        self.frameDireccion2 = Frame(self.framePreguntarDomicilio, bd=1, relief="raise", borderwidth=2, padx=1, pady=1)
        self.frameDireccion2.pack()
        self.LabelDireccion2 = Label(self.frameDireccion2, text="Cambiar direccion")
        self.LabelDireccionDes2 = Label(self.frameDireccion2, text="Descripcion")
        self.LabelDireccion2.pack(pady=20)
        self.LabelDireccionDes2.pack(pady=20)
        self.comboBoxDireccion2 = ttk.Combobox(self.frameDireccion2, values = ["Medellin", "Bogota", "Envigado","Itagui"])
        self.comboBoxDireccion2.pack(pady = 10)
        self.fieldFrameDireccion2 = FieldFrame("Datos", ["Direccion específica:"], "Ingrese aqui")
        self.fieldFrameDireccion2.defRoot(self.frameDireccion2)
        self.fieldFrameDireccion2.defFunc(self.cambiarDireccion)

        # botones ir a facturar
        self.botonContinuarfpd = Button(self.framePreguntarDomicilio, text = "Ir a pagar", command = lambda: self.cambiarFrame(self.frameFacturacion))
        self.botonContinuarfpd.pack(pady=5)
        self.botonAtrasfpd = Button(self.framePreguntarDomicilio, text="Volver a canasta", command=lambda: self.cambiarFrame(self.frameComprar))
        self.botonAtrasfpd.pack(pady=5)
        
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

        # frameFacturacion
        self.frameFacturacion = Frame(self.root, bd = 1, relief = FLAT)
        self.frames.append(self.frameFacturacion)
        
        # frameHistorial Historial de facturas
        self.frameHistorial = Frame(self.root, bd=1, relief=FLAT, padx=1, pady=1)
        self.LabelHistorial = Label(self.frameHistorial, text="Historial de facturas")
        self.LabelHistorial.pack()
        self.frames.append(self.frameHistorial)
        

        self.frameModificarDatos = Frame(self.root, bd=1, relief=FLAT, padx=1, pady=1)
        self.frames.append(self.frameModificarDatos)
        self.LabelModificarDatos = Label(self.frameModificarDatos, text="Modificar datos")
        self.LabelModificarDatos.grid(row=0, column=0, columnspan=2)
        
        tk.Grid.rowconfigure(self.frameModificarDatos, 0, weight=1)
        tk.Grid.rowconfigure(self.frameModificarDatos, 1, weight=1)
        tk.Grid.rowconfigure(self.frameModificarDatos, 2, weight=1)
        tk.Grid.columnconfigure(self.frameModificarDatos, 0, weight=1)
        tk.Grid.columnconfigure(self.frameModificarDatos, 1, weight=1)

        # frameFacturasPasadas
        self.frameFacturasPasadas = Frame(self.root, padx= 2, pady= 2)
        self.frames.append(self.frameFacturasPasadas)
        self.fotofp1 = PhotoImage(file="src/resources/ratonFactura.png")
        self.fotoFacturasPasadas = Label(self.frameFacturasPasadas, image = self.fotofp1)
        self.fotoFacturasPasadas.pack(pady = 10)
        self.labelFPasadas = Label(self.frameFacturasPasadas, text="Sus facturas pasadas")
        self.labelFPasadas.pack(pady=10)
        self.botonAtrasFp = Button(self.frameFacturasPasadas, text="Volver a facturacion", command = lambda: self.cambiarFrame(self.frameFacturacion))
        self.botonAtrasFp.pack(pady=10)
        self.botonInicioFp = Button(self.frameFacturasPasadas, text="Volver al inicio", command = lambda: self.cambiarFrame(self.framePrincipal))
        self.botonInicioFp.pack(pady=10)

        # Agregar un Scrollbar
        scrollbarfp = Scrollbar(self.frameFacturasPasadas)
        scrollbarfp.pack(side=tk.RIGHT, fill=tk.Y)

        # Agregar un widget de Texto
        self.textoFacturasPasadas = Text(self.frameFacturasPasadas, wrap=tk.WORD, yscrollcommand=scrollbarfp.set)
        self.textoFacturasPasadas.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # frameContrasena cambiar contraseña
        self.frameContrasena = Frame(self.frameModificarDatos, bd=1, relief=FLAT, padx=1, pady=1)
        self.frameContrasena.grid(row=1, column=0, sticky="nsew")
        self.LabelContrasena = Label(self.frameContrasena, text="Cambiar contraseña")
        self.LabelContrasenaDes = Label(self.frameContrasena, text="Descripcion")
        self.LabelContrasena.pack(pady=20)
        self.LabelContrasenaDes.pack(pady=20)
        #usar fieldframe aqui ...
        self.fieldFrameContrasena = FieldFrame("Cambio", ["Contraseña nueva:"], "Ingrese aqui") #Ver ejemplo de uso en FieldFrame.py
        self.fieldFrameContrasena.defRoot(self.frameContrasena)
        self.fieldFrameContrasena.defFunc(self.cambiarContrasena)
        
        # framePlata Meter plata a mi cuenta
        self.framePlata = Frame(self.frameModificarDatos, bd=1, relief=FLAT, padx=1, pady=1)
        self.framePlata.grid(row=1, column=1, sticky="nsew")
        self.LabelPlata = Label(self.framePlata, text="Meter plata")
        self.LabelPlataDes = Label(self.framePlata, text="Descripcion")
        self.LabelPlata.pack(pady=20)
        self.LabelPlataDes.pack(pady=20)
        #usar fieldframe aqui ...
        self.fieldFramePlata = FieldFrame("Valor", ["Cantidad a ingresar:"], "Ingrese aqui")
        self.fieldFramePlata.defRoot(self.framePlata)
        self.fieldFramePlata.defFunc(self.meterPlata)
        
        # frameValidarTipo Validar tipo de cliente
        self.frameValidarTipo = Frame(self.frameModificarDatos, bd=1, relief=FLAT, padx=1, pady=1)
        self.frameValidarTipo.grid(row=2, column=0, sticky="nsew")
        self.LabelValidarTipo = Label(self.frameValidarTipo, text="Validar tipo de cliente")
        self.LabelValidarTipoDes = Label(self.frameValidarTipo, text="Descripcion")
        self.LabelValidarTipo.pack(pady=20)
        self.LabelValidarTipoDes.pack(pady=20)
        self.comboBoxValidarTipo = ttk.Combobox(self.frameValidarTipo, values = ["Estudiante", "Profesor", "Senior","Empleado", "Ninguno"])
        self.comboBoxValidarTipo.pack(pady = 10)
        self.botonValidarTipo = Button(self.frameValidarTipo, text="Establecer",command=self.validarTipo)
        self.botonValidarTipo.pack(pady = 10)
        self.LabelValidarTipo.pack()
        
        # frameDireccion Modificar direccion
        self.frameDireccion = Frame(self.frameModificarDatos, bd=1, relief=FLAT, padx=1, pady=1)
        self.frameDireccion.grid(row=2, column=1, sticky="nsew")
        self.LabelDireccion = Label(self.frameDireccion, text="Cambiar direccion")
        self.LabelDireccionDes = Label(self.frameDireccion, text="Descripcion")
        self.LabelDireccion.pack(pady=20)
        self.LabelDireccionDes.pack(pady=20)
        self.comboBoxDireccion = ttk.Combobox(self.frameDireccion, values = ["Medellin", "Bogota", "Envigado","Itagui"])
        self.comboBoxDireccion.pack(pady = 10)
        #usar fieldframe aqui ...
        self.fieldFrameDireccion = FieldFrame("Datos", ["Direccion específica:"], "Ingrese aqui")
        self.fieldFrameDireccion.defRoot(self.frameDireccion)
        self.fieldFrameDireccion.defFunc(self.cambiarDireccion)

        # Frame funcionalidad 4 (FrameCocinar)
        
        self.frameCocinar = Frame(self.root, bd=1, relief=FLAT, padx=1, pady=1)
        self.frames.append(self.frameCocinar)
        self.tituloCocinar = Label(self.frameCocinar, text="COCINAR PRODUCTOS")
        self.descipCocinar = Label(self.frameCocinar, text="DESCRIPCION")
        self.tituloCocinar.pack(pady = 5)
        self.descipCocinar.pack(pady = 5)
        self.labelCocinar = Label(self.frameCocinar, text="Elija un producto")
        self.labelCocinar.pack(pady = 5)

        #Creando el comboBox
        self.opcionesCompra = [] 
        for producto in Producto.baseDatosProductos:
            self.opcionesCompra.append(producto.getNombre())
        
        self.comboboxCocinar= ttk.Combobox(self.frameCocinar, values = self.opcionesCompra)
        self.comboboxCocinar.pack(pady = 10)

        #Implementaion del field frame
        self.ffCocinar = FieldFrame("Elija la cantidad", ["Cantidad a comprar:"], "Ingrese aquí")
        self.ffCocinar.defRoot(self.frameCocinar)

        #Boton para cocinar
        self.botonCocinar = Button(self.frameCocinar, text="Cocinar")
        self.botonCocinar.pack(pady = 5)

        #Frame CocinarPersonalizado 

        self.frameCocinarPersonalizado = Frame(self.root, bd=1, relief=FLAT, padx=1, pady=1)
        self.frames.append(self.frameCocinarPersonalizado)
        self.ffCocinarPersonalizado1 = FieldFrame("Datos del producto", ["Nombre del producto:", "Cantidad a cocinar:"], "Ingreselos Aquí")
        self.ffCocinarPersonalizado1.defRoot(self.frameCocinarPersonalizado)
        self.ffCocinarPersonalizado1.defFunc(self.cambioAIngredientes)
        self.botonVolverPersonalizado = Button(self.frameCocinarPersonalizado, text="Volver Atras", command=lambda: self.cambiarFrame(self.frameCocinar))
        self.botonVolverPersonalizado.pack()

        #Texto de ejecucion de cocinar producto personalizado
        self.frameCocinarPersonalizado2 = Frame(self.frameCocinarPersonalizado, bd=1, relief=FLAT, padx=1, pady=1)
        self.textEjecCocinarPersonalizado= Text(self.frameCocinarPersonalizado2)
        self.textEjecCocinarPersonalizado.pack(fill=tk.BOTH, expand=True)
        self.frameCocinarPersonalizado2.pack(fill=tk.BOTH, expand=True)

        #Boton para cocinar Porducto personalizado
        self.botonCocinarProductoPersonalizado = Button(self.frameCocinar, text="Cocinar producto personalizado", command=lambda: self.cambiarFrame(self.frameCocinarPersonalizado))
        self.botonCocinarProductoPersonalizado.pack()
        
        #Frame de resultados de la ejecuion de Cocinar
        self.frameCocinar2 = Frame(self.frameCocinar, bd=1, relief=FLAT, padx=1, pady=1)
        self.textEjecCocinar= Text(self.frameCocinar2)
        self.textEjecCocinar.pack(fill=tk.BOTH, expand=True)
        self.frameCocinar2.pack(fill=tk.BOTH, expand=True)

        #Frame funcionalidad 5
        
        self.frameComprarIngredientes = Frame(self.root, bd=1, relief=FLAT, padx=1, pady=1)
        self.frames.append(self.frameComprarIngredientes)
        self.tituloComprarIngredientes = Label(self.frameComprarIngredientes, text="COMPRAR INGREDIENTES")
        self.descipComprarIngredientes = Label(self.frameComprarIngredientes, text="DESCRIPCION")
        self.tituloComprarIngredientes.pack(pady = 5)
        self.descipComprarIngredientes.pack(pady = 5)
        self.labelComprarIngredientes = Label(self.frameComprarIngredientes, text="Elija un ingrediente")
        self.labelComprarIngredientes.pack(pady = 5)
        
        #Creando el comboBox
        self.opcionesCompra = [] 
        for ingrediente in Ingrediente._baseDatosIngredientes:
            self.opcionesCompra.append(ingrediente.getNombre())
        
        self.comboboxComprarIngredientes = ttk.Combobox(self.frameComprarIngredientes, values = self.opcionesCompra)
        self.comboboxComprarIngredientes.pack(pady = 10)

        #Implementaion del field frame
        self.ffComprarIngredientes = FieldFrame("Elija la cantidad", ["Cantidad a comprar:"], "Ingrese aquí")
        self.ffComprarIngredientes.defRoot(self.frameComprarIngredientes)
        self.ffComprarIngredientes.defFunc(self.valoresdiccionarioCompra)

        #Boton 
        self.botonComprarIngredientes = Button(self.frameComprarIngredientes, text="Comprar")
        self.botonComprarIngredientes.pack(pady = 5)
        
        self.frameComprarIngredientes2 = Frame(self.frameComprarIngredientes, bd=1, relief=FLAT, padx=1, pady=1)
        self.textEjecComprarIngredientes = Text(self.frameComprarIngredientes2)
        self.textEjecComprarIngredientes.pack(fill=tk.BOTH, expand=True)
        self.frameComprarIngredientes2.pack(fill=tk.BOTH, expand=True)

        # frameLoMejor (Frames lo mejor de nuestra Panaderia) 
        self.frameLoMejor = Frame(self.root, bd=1, relief=FLAT, padx=1, pady=1)
        self.frames.append(self.frameLoMejor)
        self.tituloLoMejor = Label(self.frameLoMejor, text="LO MEJOR DE NUESTRA PANADERIA", pady=10)
        self.infoLoMejor = Label(self.frameLoMejor, text="Aquí puede ver los rankings de lo mejor de nuestra panadería, las opciones que puede escoger son, los mejores cocineros, los mejores domiciliarios, los mejores productos y los mejores ingredientes, para verlas escriba, cocineros, domiciliarios, productos o ingredientes respectivamente y posteriormente presione el botón Aceptar.", wraplength=380, pady=10)
        self.tituloLoMejor.pack()
        self.infoLoMejor.pack()
        self.ffLoMejor = FieldFrame("Rankings", ["Escriba qué ranking desea ver:"], "Ingrese aquí el nombre")
        self.ffLoMejor.defRoot(self.frameLoMejor)
        self.frameLoMejor2 = Frame(self.frameLoMejor, bd=1, relief=FLAT, padx=1, pady=1)
        self.textEjecLoMejor = Text(self.frameLoMejor2)
        self.textEjecLoMejor.pack(fill=tk.BOTH, expand=True)
        self.frameLoMejor2.pack(fill=tk.BOTH, expand=True)

    # frameComprar
    def cargarFrameCarrito(self):
        #framep1 = Frame(frame, bd = 5, relief=FLAT, padx = 2, pady = 2, bg = "white").grid(row =0 , column = 0)
        #framep2 = Frame(frame, bd = 5, relief=FLAT, padx = 2, pady = 2, bg = "white").grid(row =0 , column = 1)
        self.frameComprar1 = Frame(self.frameComprar)
        self.frameComprar1.pack()
        self.labelfc1 = Label(self.frameComprar1, text="Crear Canasta de Compras", wraplength=300)
        self.labelfc1.pack(pady=5)
        self.labelDescripcion = Label(self.frameComprar1, text="En este apartado se pueden hace varias cosas, se pueden añadir cosas a la canasta, esto con la ayuda de la lista de opciones depleglable donde se podrá escoger el producto, ingrediente o kit que desea adquirir, posteriormente deberá añadir la cantidad que desea de lo que se haya seleccionado, debe tener en cuenta que hay un limíte el cual sera de *** unidades, si desea quitar cosas a la canasta deberá seleccionar en la lista de opciones deplegable el producto, ingrediente o kit que desea eliminar y posteriormente debe añadir una cantidad negativa para quitar esa cantidad de unidades, el listado de productos con su respectiva cantidad escogida apareceran en la parte inferior de la pantalla, cuando tenga su canasta como la desea debe presionar el boton Continuar con proceso de compra para seguir con la compra de su canasta, además de eso se puede añadir productos personalizados a la canasta haciendo uso del boton Añadir producto personalizado y con ayuda del botón Catálogo se podrá ingresar al catálogo de productos.", wraplength=800, pady=10)
        self.labelDescripcion.pack(pady=5)

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
        self.comboboxfc1.pack(pady = 5)

        # FieldFrame para cantidad

        self.ffCarrito = FieldFrame("Valores", ["Cantidad a comprar:"], "Ingrese aquí")
        self.ffCarrito.defRoot(self.frameComprar1)
        self.ffCarrito.defFunc(self.registrarPedidoCanasta)

        #checkbox
        self.var = tk.BooleanVar()
        self.var.set(False)
        self.checkButton = ttk.Checkbutton(self.frameComprar1, text="Desea el kit?", variable=self.var) 
        self.checkButton.pack(pady=5)

        self.botonCocinar = tk.Button(self.frameComprar1, text="Agregar producto personalizado")
        self.botonCocinar.pack(pady=10)

        self.botonIrCatalogo = tk.Button(self.frameComprar1, text="Ir al catalogo", command = lambda: self.cambiarFrame(self.frameCatalogo))
        self.botonIrCatalogo.pack( pady=10)

        self.botonIrPreguntarDomicilio = Button(self.frameComprar1, text = "Continuar con proceso de compra", command = lambda: self.cambiarFrame(self.framePreguntarDomicilio))
        self.botonIrPreguntarDomicilio.pack(side="bottom", pady=10)

        self.frameComprar2 = Frame(self.frameComprar)
        self.frameComprar2.pack(fill=tk.BOTH, expand=True)
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

        # Tag para centrar texto
        self.texto_widget.tag_configure("center", justify="center")

        # Aplicar el tag al texto
        self.texto_widget.tag_add("center", "1.0", "end")

    # frameFacturacion
    def cargarFrameFacturacion(self):
        self.fotoff1 = PhotoImage(file="src/resources/ratonFactura.png")
        self.fotoFacturacion = Label(self.frameFacturacion, image = self.fotoff1)
        self.fotoFacturacion.pack(pady = 5)
        self.LabelFacturacion = Label(self.frameFacturacion, text="Su factura")
        self.LabelFacturacion.pack(pady=5)

        #Botones
        self.botonPagar = Button(self.frameFacturacion, text = "Pagar")
        self.botonPagar.pack(pady = 10)
        self.botonFacPasadas = Button(self.frameFacturacion, text = "Ver facturas pasadas", command=lambda: self.cambiarFrame(self.frameFacturasPasadas))
        self.botonFacPasadas.pack(pady = 10)
        self.botonAtrasFacturacion = Button(self.frameFacturacion, text = "Volver atras", command = lambda: self.cambiarFrame(self.framePreguntarDomicilio, False))
        self.botonAtrasFacturacion.pack(pady = 10)
        

        # Agregar un Scrollbar
        scrollbar = Scrollbar(self.frameFacturacion)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Agregar un widget de Texto
        self.textoFacturacion = Text(self.frameFacturacion, wrap=tk.WORD, yscrollcommand=scrollbar.set)
        self.textoFacturacion.pack(fill=tk.BOTH, expand=True, pady=20, padx=20)

        # Implementacion logica widget de texto
        self.textoFacturacion.delete(1.0, "end")
        self.varFactura = ""
        self.textoFacturacion.insert(1.0, self.varFactura)

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
                if frame == self.frameFacturacion:
                    self.cargarFrameFacturacion()
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
        self.textoDescripcion.delete(1.0, tk.END)
        nutrientes = (
            " _______________________________________________________\n"
            f"|"+centrar("Producto: "+nombre)+"|\n"
            "| Porcion: 30 g                                         |\n"
            "|_______________________________________________________|\n"
            "| Informacion nutricional por porcion                   |\n"
            "|______________________ ________ _______________________|\n"
            "| Energia              | 140 kcal| 7% del valor diario  |\n"
            "|______________________ ________ _______________________|\n"
            "| Grasa total          | 6 g     | 9% del valor diario  |\n"
            "| _ Grasa saturada     | 3 g     | 15% del valor diario |\n"
            "| _ Grasa trans        | 0 g     |                      |\n"
            "|______________________ ________ _______________________|\n"
            "| Colesterol           | 0 mg    | 0% del valor diario  |\n"
            "|______________________ ________ _______________________|\n"
            "| Sodio                | 75 mg   | 3% del valor diario  |\n"
            "|______________________ ________ _______________________|\n"
            "| Carbohidratos totales| 20 g    | 7% del valor diario  |\n"
            "| _ Fibra dietetica    | 1 g     | 4% del valor diario  |\n"
            "| _ Azucares           | 10 g    |                      |\n"
            "|______________________ ________ _______________________|\n"
            "| Proteina             | 2 g     |                      |\n"
            "|______________________ ________ _______________________|\n"
            "| Vitamina A           | 0% del valor diario            |\n"
            "| Vitamina C           | 0% del valor diario            |\n"
            "| Calcio               | 2% del valor diario            |\n"
            "| Hierro               | 6% del valor diario            |\n"
            "|_______________________________________________________|\n"
        )
        self.textoDescripcion.insert(tk.END, nutrientes)
        # Configurar el tag para centrar el texto
        self.textoDescripcion.tag_configure("center", justify="center")

        # Aplicar el tag al texto
        self.textoDescripcion.tag_add("center", "1.0", "end")

    def registrarPedidoCanasta(self,val):
        try:
            if val[0] == "":
                raise CamposVaciosError([val[0]])
            elif not(Ingrediente.verificacionExistenciaPorNombreI(self.comboboxfc1.get()) or Producto.verificarExistenciaPorNombreP(self.comboboxfc1.get())):
                raise ProductoNoEncontradoError(self.comboboxfc1.get())
            elif not val[0].isdigit():
                raise ValueError()
            elif int(val[0]) < -15 or int(val[0])>15:
                raise CantidadInvalidaError(int(val[0]))
            else:
                producto = self.comboboxfc1.get()
                elemento = ""
                if Producto.verificarExistenciaPorNombreP(producto):
                    elemento = Producto.obtenerObjetoPorNombreP(producto).getId()
                elif Ingrediente.verificacionExistenciaPorNombreI(producto):
                    elemento = Ingrediente.obtenerObjetoPorNombreI(producto).getId()
                Cliente.getSesion().getCanastaOrden().recibir_orden(elemento, val[0], self.var.get())
                self.texto_widget.delete(1.0, tk.END)
                for elements, cantidad in Cliente.getSesion().getCanastaOrden().getProductosEnLista().items():
                    self.texto_widget.insert(tk.END, "Producto: " + Producto.obtenerObjetoPorIdP(elements).getNombre() + " - Cantidad: " + str(cantidad) + "\n")
                for elements, cantidad in Cliente.getSesion().getCanastaOrden().getIngredientesEnLista().items():
                    self.texto_widget.insert(tk.END, "Ingrediente: " + Ingrediente.obtenerObjetoPorIdI(elements).getNombre() + " - Cantidad: " + str(cantidad) + "\n")
                for elements, cantidad in Cliente.getSesion().getCanastaOrden().getKitsEnLista().items():
                    self.texto_widget.insert(tk.END, "Kits: " + Producto.obtenerObjetoPorIdP(elements).getNombre() + " - Cantidad: " + str(cantidad) + "\n")
                self.comboboxfc1.delete(0, 'end')   
                self.texto_widget.tag_configure("center", justify="center")

                # Aplicar el tag al texto
                self.texto_widget.tag_add("center", "1.0", "end")

        except CamposVaciosError as e:
            messagebox.showwarning("Error", "Completa los campos vacios")
        except ProductoNoEncontradoError as e:
            messagebox.showwarning("Error", "El producto no existe")
        except ValueError:
            messagebox.showwarning("Error", "La cantidad debe ser un numero")
        except CantidadInvalidaError as e:
            messagebox.showwarning("Error", "La cantidad debe estar entre -15 y 15")

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
        self.menu_procesos.entryconfigure("Modificar datos", state="disabled")
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

                self.menu_procesos.entryconfigure("Modificar datos", state="normal")
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
            self.menu_procesos.entryconfigure("Modificar datos", state="normal")
            self.cambiarFrame(self.framePrincipal)
        except usuarioExistenteError as e:
            messagebox.showwarning("Error", "El usuario ya existe")

    def cambiarContrasena(self, val):
        Cliente.getSesion().setContrasena(val[0])
        messagebox.showinfo("Cambio de contraseña", "Contraseña cambiada correctamente")

    def meterPlata(self, val):
        Cliente.getSesion().setPresupuesto(Cliente.getSesion().getPresupuesto() + int(val[0]))
        messagebox.showinfo("Meter plata", "Plata ingresada correctamente")

    # Métodos para la funcionalidad 5
    def creaciondiccionarioCompra(self, llaves, valores):
        
        for i in range (0, len(llaves)-1):
            self.diccionarioFuncionalidad5[llaves[i]] = valores[i]
            x = (f"{llaves[i]}: {valores[i]}") 
            self.textEjecComprarIngredientes.insert(x)

    def valoresdiccionarioCompra(self, values):
        valores = []
        llaves = []

        if values != []:
            for i in values:
                valores.append(i)
        else:
            print("No se ingreso nada") #Recordar Cambiar por un exception
        
        y = self.comboboxComprarIngredientes.get()

        if y == None or y == "":
            print("No hay nada en el combobox") #Recordar Cambiar por una excepcion
        
        else:
            llaves.append(y)

        self.creaciondiccionarioCompra(llaves, valores)

        Cliente.getSesion().getPanaderia().comprarIngredientes(self.diccionarioFuncionalidad5, self.textEjecComprarIngredientes)
    
    def cambiarDireccion(self, val):
        try:
            if val[0] == "":
                raise CamposVaciosError([val[0]])
            elif not Cliente.getSesion().establecerDomicilioValido(val[0],self.comboBoxDireccion.get()):
                raise CamposVaciosError([self.comboBoxDireccion.get()])
            else:
                messagebox.showinfo("Cambio de direccion", "Direccion cambiada correctamente")
        except CamposVaciosError as e:
            messagebox.showwarning("Error", "Direccion inválida o campo vacio")

    def validarTipo(self):
        try:
            if not Cliente.getSesion().establecerDescuentoPorTipoValido(self.comboBoxValidarTipo.get()):
                raise CamposVaciosError([self.comboBoxValidarTipo.get()])
            else:
                messagebox.showinfo("Validar tipo de cliente", "Tipo de cliente validado correctamente")
        except CamposVaciosError as e:
            messagebox.showwarning("Error", "Tipo de cliente inválido o campo vacio")

    def cambioAIngredientes(self,val):
        
        # Frame para ingredientes de personalizado
        self.frameIngredientesPersonalizado = Frame(self.root, bd=1, relief=FLAT, padx=1, pady=1)
        self.frames.append(self.frameIngredientesPersonalizado)
        self.ffCocinarPersonalizado2 = FieldFrame("Ingredientes necesarios", ["Nombre del ingrediente:", "Cantidad:"], "Ingreselos Aquí")
        self.ffCocinarPersonalizado2.defRoot(self.frameIngredientesPersonalizado)
        self.botonVolverIngrediente = Button(self.frameIngredientesPersonalizado, text="Volver Atras", command=self.volverAtras)
        self.botonVolverIngrediente.pack()
        self.frameIngredientesPersonalizado2 = Frame(self.frameIngredientesPersonalizado, bd=1, relief=FLAT, padx=1, pady=1)
        self.textDescPersonalizado = Text(self.frameIngredientesPersonalizado2)
        self.textDescPersonalizado.pack(fill=tk.BOTH, expand=True)
        self.frameIngredientesPersonalizado2.pack(fill=tk.BOTH, expand=True)

        self.cambiarFrame(self.frameIngredientesPersonalizado)

# Codigo que produce la ejecucion de la ventana cuando se ejecuta desde este archivo
def main():
    root = Tk()
    app = VentanaPrincipal(root)
    root.mainloop()


if __name__ == "__main__":
    main()
