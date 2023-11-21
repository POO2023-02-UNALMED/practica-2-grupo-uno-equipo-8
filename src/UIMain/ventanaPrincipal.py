import random
import time
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from FieldFrame import FieldFrame
from Texto import centrar
from ErrorAplicacion import CamposVaciosError, CantidadInvalidaError, ProductoNoEncontradoError, UsuarioNoEncontradoError, usuarioExistenteError
import os
import sys
import copy
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from gestorAplicacion.gestion.Canasta import Canasta
from gestorAplicacion.humanos.Cliente import Cliente
from gestorAplicacion.comida.Producto import Producto
from gestorAplicacion.comida.Ingrediente import Ingrediente
from baseDatos.Serializador import Serializador
#from gestorAplicacion.gestion.Recibo import Recibo
from UIMain.GestionCocinar import GestionCocinar
from UIMain.GestionRankings import imprimirCocinerosPorRanking
from UIMain.GestionRankings import imprimirDomiciliariosPorRanking
from UIMain.GestionRankings import imprimirIngredientesPorVecesVendidos
from UIMain.GestionRankings import imprimirProductosPorVecesVendidos

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

        # Diccionario para la funcionalidad 4
        self.diccionarioFuncionalidad4 = {}

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
        self.menu_procesos.add_command(label = "Func. Facturar", state="disabled", command=lambda: self.cambiarFrame(self.frameFacturacion))
        self.menu_procesos.add_command(label = "Func. Cocinar",command=lambda:self.cambiarFrame(self.frameCocinar), state="disabled")
        self.menu_procesos.add_command(label = "Func. Ingredientes e inventario", command=lambda:self.cambiarFrame(self.frameComprarIngredientes), state="disabled")
        self.menu_procesos.add_command(label = "Func. Domicilio", state="disabled", command=lambda:self.cambiarFrame(self.frameDomicilio))
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
        self.labelBienvenida3 = Label(self.framePrincipal, text="""
¡Bienvenido a nuestra aplicación!

En el menú de "Procesos y Consultas", podrás iniciar tu compra. Elige "Crear canasta de compras" y haz tu pedido ya.

Pasos a seguir:
1. 🖱️ Selecciona en el menú el apartado "Procesos y Consultas".
2. 🚪 Inicia sesión o regístrate en caso de no tener cuenta.
3. 🔁 Después de iniciar sesión, vuelve al apartado de procesos y consultas y selecciona "Función: crear canasta de compras".
4. 🛒 Aquí puedes ver el catálogo, elegir productos, determinar la cantidad y añadirlos a la canasta.
5. 📝 Continúa con el proceso de compra y luego llena un formulario para realizar el domicilio.
6. 💳 Procede a "Ir a pagar". Puedes visualizar tu factura actual y, si lo deseas, las pasadas.
7. 🔥 Después de pagar, comenzará el proceso de cocinar.
8. 🛒 Si faltan ingredientes, puedes mandar a comprarlos.
9. 🚚 Una vez cocinados, los productos se enviarán a tu domicilio.
10. ⭐ Al finalizar el proceso, puedes dar calificaciones.

¡Disfruta tu experiencia de compra!
""", font=("Arial", 10))  # Cambiar la fuente a Arial y el tamaño a 12 puntos
        self.labelBienvenida3.pack()


        self.fotoRatonCalificacion = tk.PhotoImage(file="src/resources/ratonCalificacionP.png")

        # frameSesion inicio de sesion
        self.fotoInicioSesion = tk.PhotoImage(file="src/resources/ratonInicioSesion.png")
        self.frameSesion = Frame(self.root, bd=1, relief=FLAT, padx=1, pady=1) 
        self.frames.append(self.frameSesion) #agregando a la lista de frames, necesaria para cambiar entre frames metodo cambiarFrame
        self.labelFotoInicioSesion = Label(self.frameSesion, image = self.fotoInicioSesion)
        self.labelFotoInicioSesion.pack()

        self.frameSesion2 = Frame(self.frameSesion, bd=1, relief=RAISED, borderwidth=2, padx=1, pady=1)
        self.frameSesion2.pack()
        self.labelTituloInicioSesion = Label(self.frameSesion2, text="INICIO DE SESION")
        self.labelTituloInicioSesion.pack(pady=20)
        
        self.descripTituloInicioSesion = Label(self.frameSesion2, text="Aquí podrá iniciar sesión, por favor ingrese su id y contraseña en los campos correspondientes, posteriormente presione Aceptar")
        self.descripTituloInicioSesion.pack(pady=20)

        self.fieldFrameInicioSesion = FieldFrame("Datos Pedidos", ["Id:", "Contraseña:"], "Ingreselos Aquí")
        self.fieldFrameInicioSesion.defRoot(self.frameSesion2)
        self.fieldFrameInicioSesion.defFunc(self.iniciarSesion)

        #frameActual = self.frameSesion



        # frameRegistro registro
        self.frameRegistro = Frame( #Esto esta pendiente de ser adaptado con fieldFrames
        self.root, bd=1, relief=FLAT, padx=1, pady=1)
        self.frames.append(self.frameRegistro)

        self.frameRegistro2 = Frame(self.frameRegistro, bd=1, relief=RAISED, borderwidth=2, padx=1, pady=1)
        self.frameRegistro2.pack()
        self.labelFotoRegistro = Label(self.frameRegistro2, image = self.fotoInicioSesion)
        self.labelFotoRegistro.pack()
        self.labelTituloRegistro = Label(self.frameRegistro2, text="REGISTRO")
        self.labelTituloRegistro.pack(pady=20)
        
        self.descripRegistro = Label(self.frameRegistro2, text="En este apartado podrá registarse como cliente, por favor ingrese su nombre, id y contraseña en los campos correspondientes, posteriormente presione Aceptar")
        self.descripRegistro.pack(pady=20)

        self.fieldRegistro = FieldFrame("Datos Pedidos", ["Nombre:", "Id:", "Contraseña:"], "Ingreselos Aquí")
        self.fieldRegistro.defRoot(self.frameRegistro2)
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
        self.LabelDireccionDes2 = Label(self.frameDireccion2, text="En este apartado podrá cambiar su direccion de domicilio, primero escoja la ciudad donde está ubicado en el menú desplegable, luego ingrese su direccion especifica en los campos correspondientes, posteriormente presione Aceptar")
        self.LabelDireccion2.pack(pady=20)
        self.LabelDireccionDes2.pack(pady=20)
        self.comboBoxDireccion2 = ttk.Combobox(self.frameDireccion2, values = ["Medellin", "Bogota", "Envigado","Itagui"])
        self.comboBoxDireccion2.pack(pady = 10)
        self.fieldFrameDireccion2 = FieldFrame("Datos", ["Direccion específica:"], "Ingrese aqui")
        self.fieldFrameDireccion2.defRoot(self.frameDireccion2)
        self.fieldFrameDireccion2.defFunc(self.cambiarDireccion2)

        ## frameDireccion Modificar direccion
        #self.frameDireccion = Frame(self.frameModificarDatos, bd=1, relief=FLAT, padx=1, pady=1)
        #self.frameDireccion.grid(row=2, column=1, sticky="nsew")
        #self.LabelDireccion = Label(self.frameDireccion, text="Cambiar direccion")
        #self.LabelDireccionDes = Label(self.frameDireccion, text="Descripcion")
        #self.LabelDireccion.pack(pady=20)
        #self.LabelDireccionDes.pack(pady=20)
        #self.comboBoxDireccion = ttk.Combobox(self.frameDireccion, values = ["Medellin", "Bogota", "Envigado","Itagui"])
        #self.comboBoxDireccion.pack(pady = 10)
        ##usar fieldframe aqui ...
        #self.fieldFrameDireccion = FieldFrame("Datos", ["Direccion específica:"], "Ingrese aqui")
        #self.fieldFrameDireccion.defRoot(self.frameDireccion)
        #self.fieldFrameDireccion.defFunc(self.cambiarDireccion)

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

        # Configura la vinculación del evento de la rueda del mouse al Canvas
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)


        # Crear un frame dentro del canvas para colocar los botones
        self.frameCatalogo3 = tk.Frame(self.canvas)
        self.canvas.create_window((200, 0), window = self.frameCatalogo3, anchor="center")

        # Crear una variable para contar los botones
        self.contadorCatalogo = tk.IntVar()
        self.contadorCatalogo.set(0)

        self.iconoDefault = tk.PhotoImage(file="src/resources/iconoManzana1.png")
        
        #Empaquetar el canvas y el scrollbar
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

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
        self.fotoRatonFactura = PhotoImage(file="src/resources/ratonFactura.png")
        self.fotoFacturacion = Label(self.frameFacturacion, image = self.fotoRatonFactura)
        self.fotoFacturacion.pack(pady = 5)
        self.labelFacturacion = Label(self.frameFacturacion, text="Su factura")
        self.labelFacturacion.pack(pady=5)
        self.labelFacturacion2 = Label(self.frameFacturacion, text = "")
        self.labelFacturacion2.pack()

        #Botones
        self.botonPagar = Button(self.frameFacturacion, text = "Pagar", command = lambda: self.pasarAlPago())
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
        
        # frameHistorial Historial de facturas
        self.frameHistorial = Frame(self.root, bd=1, relief=FLAT, padx=1, pady=1)
        self.LabelHistorial = Label(self.frameHistorial, text="Historial de facturas")
        self.LabelHistorial.pack()
        self.frames.append(self.frameHistorial)

        # frameMeterPlata Meter plata a mi cuenta
        self.frameMeterPlata = Frame(self.root, bd=1, relief=FLAT, padx=1, pady=1)
        self.frames.append(self.frameMeterPlata)
        self.imagenPlata = Label(self.frameMeterPlata, image = self.fotoRatonFactura)
        self.imagenPlata.pack()
        self.frameMeterPlata_2 = Frame(self.frameMeterPlata, bd=1, relief=RAISED, borderwidth=2, padx=1, pady=1)
        self.frameMeterPlata_2.pack()
        self.LabelPlata2 = Label(self.frameMeterPlata_2, text="Meter plata")
        self.LabelPlataDes2 = Label(self.frameMeterPlata_2, text="En este apartado podrá ingresar dinero a su cuenta de cliente, por favor ingrese la cantidad que desea ingresar en el campo correspondiente, posteriormente presione Aceptar")
        self.LabelPlata2.pack(pady=20)
        self.LabelPlataDes2.pack(pady=20)
        #usar fieldframe aqui ...
        self.fieldFramePlata2 = FieldFrame("Valor", ["Cantidad a ingresar:"], "Ingrese aqui")
        self.fieldFramePlata2.defRoot(self.frameMeterPlata_2)
        self.fieldFramePlata2.defFunc(self.meterPlata)
        self.botonAtrasmp = Button(self.frameMeterPlata, text = "Volver atras", command = self.volverAtras)
        self.botonAtrasmp.pack(pady = 15)

        # frameFacturasPasadas
        self.frameFacturasPasadas = Frame(self.root, padx= 2, pady= 2)
        self.frames.append(self.frameFacturasPasadas)
        self.fotoFacturasPasadas = Label(self.frameFacturasPasadas, image = self.fotoRatonFactura)
        self.fotoFacturasPasadas.pack(pady = 10)
        self.labelFPasadas = Label(self.frameFacturasPasadas, text="Sus facturas pasadas \n Seleccione el id de la orden para copiar la canasta asociada")
        self.labelFPasadas.pack(pady=10)
        self.idsFacturasPasadas = []
        self.comboBoxClonar = ttk.Combobox(self.frameFacturasPasadas, values = self.idsFacturasPasadas)
        self.comboBoxClonar.pack(pady=5)
        self.BotonClonar = Button(self.frameFacturasPasadas, text="Copiar canasta", command = lambda: self.copiarOrden(self.comboBoxClonar.get()))
        self.BotonClonar.pack(pady = 5)
        self.botonAtrasFp = Button(self.frameFacturasPasadas, text="Volver a facturacion", command = lambda: self.cambiarFrame(self.frameFacturacion))
        self.botonAtrasFp.pack(pady=15)
        self.botonInicioFp = Button(self.frameFacturasPasadas, text="Volver al inicio", command = lambda: self.cambiarFrame(self.framePrincipal))
        self.botonInicioFp.pack(pady=15)

        # Agregar un Scrollbar
        scrollbarfp = Scrollbar(self.frameFacturasPasadas)
        scrollbarfp.pack(side=tk.RIGHT, fill=tk.Y)

        # Agregar un widget de Texto
        self.textoFacturasPasadas = Text(self.frameFacturasPasadas, wrap=tk.WORD, yscrollcommand=scrollbarfp.set)
        self.textoFacturasPasadas.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # frameModificarDatos
        self.frameModificarDatos = Frame(self.root, bd=1, relief=FLAT, padx=1, pady=1)
        self.frames.append(self.frameModificarDatos)
        self.LabelModificarDatos = Label(self.frameModificarDatos, text="Modificar datos")
        self.LabelModificarDatos.grid(row=0, column=0, columnspan=2)
        
        tk.Grid.rowconfigure(self.frameModificarDatos, 0, weight=1)
        tk.Grid.rowconfigure(self.frameModificarDatos, 1, weight=1)
        tk.Grid.rowconfigure(self.frameModificarDatos, 2, weight=1)
        tk.Grid.columnconfigure(self.frameModificarDatos, 0, weight=1)
        tk.Grid.columnconfigure(self.frameModificarDatos, 1, weight=1)

        # frameContrasena cambiar contraseña
        self.frameContrasena = Frame(self.frameModificarDatos, bd=1, relief=FLAT, padx=1, pady=1)
        self.frameContrasena.grid(row=1, column=0, sticky="nsew")
        self.LabelContrasena = Label(self.frameContrasena, text="Cambiar contraseña")
        self.LabelContrasenaDes = Label(self.frameContrasena, text="En este apartado podrá cambiar su contraseña, por favor ingrese su nueva contraseña en el apartado correspondiente y posteriormente presione Aceptar")
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
        self.LabelPlataDes = Label(self.framePlata, text="En este apartado podrá ingresar dinero a su cuenta de cliente, por favor ingrese la cantidad que desea ingresar en el campo correspondiente, posteriormente presione Aceptar")
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
        self.LabelValidarTipoDes = Label(self.frameValidarTipo, text="En este apartado podrá validar su tipo de cliente, por favor seleccione el tipo de cliente que desea validar en el menú desplegable, posteriormente presione Aceptar")
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
        self.LabelDireccionDes = Label(self.frameDireccion, text="En este apartado podrá cambiar su direccion de domicilio, primero escoja la ciudad donde está ubicado en el menú desplegable, luego ingrese su direccion especifica en los campos correspondientes, posteriormente presione Aceptar")
        self.LabelDireccion.pack(pady=20)
        self.LabelDireccionDes.pack(pady=20)
        self.comboBoxDireccion = ttk.Combobox(self.frameDireccion, values = ["Medellin", "Bogota", "Envigado","Itagui"])
        self.comboBoxDireccion.pack(pady = 10)
        #usar fieldframe aqui ...
        self.fieldFrameDireccion = FieldFrame("Datos", ["Direccion específica:"], "Ingrese aqui")
        self.fieldFrameDireccion.defRoot(self.frameDireccion)
        self.fieldFrameDireccion.defFunc(self.cambiarDireccion)

        # FrameCocinar Frame funcionalidad 4 
        
        self.frameCocinar = Frame(self.root, bd=1, relief=FLAT, padx=1, pady=1)
        self.frames.append(self.frameCocinar)
        self.tituloCocinar = Label(self.frameCocinar, text="COCINAR PRODUCTOS")
        self.descipCocinar = Label(self.frameCocinar, text="En este apartado podrá enviar a cocinar Productos que se añadirán al inventario de la panadería, lo primero que debe hacer es crear su listado de productos, esto lo podrá hacer con ayuda del menú desplegable en el cuál podrá escoger el ingrediente que desea enviar a comprar, si ingresa un producto que no manejamos se le generará un error, posteriormente debe digitar la cantidad que desea donde se le indica, debe ser una cantidad entera positiva menor que 15 y distinta de 0, luego para agregar el ingrediente con su respectiva cantidad debe presionar el botón Aceptar, podrá visualizar la lista de ingredientes que lleva hasta el momento en la parte inferior de la pantalla, cuando considere que ya ha llenado su lista por completo por favor presione el botón Cocinar para continuar con el proceso, adicionalmente podrá crear productos nuevos presionando el botón Cocinar Producto Personalizado, los productos que cree en este apartado se añadiran a la lista de ingredientes para enviar a cocinar, las instrucciones de ese proceso se mostrará en su respectivo apartado, cada paso del proceso se le irá informando en la parte inferior de la ventana", wraplength=800, pady=10)
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
        self.ffCocinar.defFunc(self.valoresDiccionarioCocina)

        #Boton para cocinar
        self.botonCocinar = Button(self.frameCocinar, text="Cocinar", command= self.ejecucionCocinarProductos)
        self.botonCocinar.pack(pady = 5)

        #Boton para cocinar Porducto personalizado
        self.botonCocinarProductoPersonalizado = Button(self.frameCocinar, text="Cocinar producto personalizado", command= self.cargarProductoPersonalizado2) 
        self.botonCocinarProductoPersonalizado.pack()
        
        #Frame de resultados de la ejecuion de Cocinar
        self.frameCocinar2 = Frame(self.frameCocinar, bd=1, relief=FLAT, padx=1, pady=1)
        self.textEjecCocinar= Text(self.frameCocinar2)
        self.textEjecCocinar.pack(fill=tk.BOTH, expand=True)
        self.frameCocinar2.pack(fill=tk.BOTH, expand=True)

        if self.diccionarioFuncionalidad4 != []:
            for ingredienteNombre, cantidad in self.diccionarioFuncionalidad4.items():
                    self.textEjecCocinar.insert(tk.END, "Producto: " + Producto.obtenerObjetoPorIdP(ingredienteNombre).getNombre() + " - Cantidad: " + str(cantidad) + "\n")

        #Frame funcionalidad 5
        
        self.frameComprarIngredientes = Frame(self.root, bd=1, relief=FLAT, padx=1, pady=1)
        self.frames.append(self.frameComprarIngredientes)
        self.tituloComprarIngredientes = Label(self.frameComprarIngredientes, text="COMPRAR INGREDIENTES")
        self.descipComprarIngredientes = Label(self.frameComprarIngredientes, text="En este apartado podrá enviar a comprar ingredientes que se añadirán al inventario de la panadería, los primero que debe hacer es crear su listado de ingredientes, esto lo podrá hacer con ayuda del menú desplegable en el cuál podrá escoger el ingrediente que desea enviar a comprar, si ingresa un ingrediente que no manejamos se le generará un error, posteriormente debe digitar la cantidad que desea donde se le indica, debe ser una cantidad entera positiva menor que 50 y distinta de 0, luego para agregar el ingrediente con su respectiva cantidad debe presionar el botón Aceptar, podrá visualizar la lista de ingredientes que lleva hasta el momento en la parte inferior de la pantalla, cuando considere que ya ha llenado su lista por completo por favor presione el botón Comprar para continuar con la compra de los ingrdientes, cada paso del proceso se le irá informando en la parte inferior de la ventana", wraplength=800, pady=10)
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
        self.botonComprarIngredientes = Button(self.frameComprarIngredientes, text="Comprar", command=self.ejecucionComprarIngredientes)
        self.botonComprarIngredientes.pack(pady = 5)
        
        self.frameComprarIngredientes2 = Frame(self.frameComprarIngredientes, bd=1, relief=FLAT, padx=1, pady=1)
        self.textEjecComprarIngredientes = Text(self.frameComprarIngredientes2)
        self.textEjecComprarIngredientes.config(state=tk.DISABLED)
        self.textEjecComprarIngredientes.pack(fill=tk.BOTH, expand=True)
        self.frameComprarIngredientes2.pack(fill=tk.BOTH, expand=True)

        # frameLoMejor (Frames lo mejor de nuestra Panaderia) 
        self.frameLoMejor = Frame(self.root, bd=1, relief=FLAT, padx=1, pady=1)
        self.frames.append(self.frameLoMejor)
        self.imagenLoMejor = Label(self.frameLoMejor, image = self.fotoRatonCalificacion)
        self.imagenLoMejor.pack()
        self.tituloLoMejor = Label(self.frameLoMejor, text="LO MEJOR DE NUESTRA PANADERIA", pady=10)
        self.infoLoMejor = Label(self.frameLoMejor, text="Aquí puede ver los rankings de lo mejor de nuestra panadería, las opciones que puede escoger son, los mejores cocineros, los mejores domiciliarios, los mejores productos y los mejores ingredientes, para verlas escriba, cocineros, domiciliarios, productos o ingredientes respectivamente y posteriormente presione el botón Aceptar.", wraplength=380, pady=10)
        self.tituloLoMejor.pack()
        self.infoLoMejor.pack()

        # Field Frame Lo Mejor 
        self.ffLoMejor = FieldFrame("Rankings", ["Escriba qué ranking desea ver:"], "Ingrese aquí el nombre")
        self.ffLoMejor.defRoot(self.frameLoMejor)
        self.ffLoMejor.defFunc(self.mostrarRankingCorrespondiente)

        # Frame de ejecucion Lo mejor 
        self.frameLoMejor2 = Frame(self.frameLoMejor, bd=1, relief=FLAT, padx=1, pady=1)
        self.textEjecLoMejor = Text(self.frameLoMejor2)
        self.textEjecLoMejor.pack(fill=tk.BOTH, expand=True)
        self.frameLoMejor2.pack(fill=tk.BOTH, expand=True)

        # Frame Domicilio

        self.frameDomicilio = Frame(self.root, bd=1, relief=FLAT, padx=1, pady=1)
        self.frames.append(self.frameDomicilio)
        self.tituloDomicilio = Label(self.frameDomicilio, text="DOMICILIO")
        self.infoDomicilio = Label(self.frameDomicilio, text="", wraplength=380, pady=10)
        self.tituloDomicilio.pack()
        self.infoDomicilio.pack()
        
        self.botonDomicilio = Button(self.frameDomicilio, text="Enviar domicilio", command=self.ejecucionDomicilio)
        self.botonDomicilio.pack(pady = 5)

        self.textEjecDomicilio = Text(self.frameDomicilio, wrap=tk.WORD)
        self.textEjecDomicilio.pack(fill=tk.BOTH, expand=True)



        self.frameComprar1 = Frame(self.frameComprar)
        self.frameComprar1.pack()
        self.labelfc1 = Label(self.frameComprar1, text="CREAR CANASTA DE COMPRAS", wraplength=300)
        self.labelfc1.pack(pady=5)
        self.labelDescripcion = Label(self.frameComprar1, text="En este apartado se pueden hace varias cosas, se pueden añadir cosas a la canasta, esto con la ayuda de la lista de opciones depleglable donde se podrá escoger el producto o ingrediente que desea adquirir, si es un producto y desea el kit presione el checkbox de kit, posteriormente deberá añadir la cantidad que desea de lo que se haya seleccionado y darle click en aceptar, de esta manera se irán añadiendo los productos a canasta. Debe tener en cuenta que hay un limíte el cual sera de 15 unidades, si desea quitar cosas a la canasta deberá seleccionar en la lista de opciones deplegable el producto, ingrediente o kit que desea eliminar y posteriormente debe añadir una cantidad negativa para quitar esa cantidad de unidades, el listado de productos con su respectiva cantidad escogida apareceran en la parte inferior de la pantalla, cuando tenga su canasta como la desea debe presionar el boton Continuar con proceso de compra para seguir con la compra de su canasta, además de eso se puede añadir productos personalizados a la canasta haciendo uso del boton Añadir producto personalizado y con ayuda del botón Catálogo se podrá ingresar al catálogo de productos.", wraplength=800, pady=10)
        self.labelDescripcion.pack(pady=5)

        self.botonIrCatalogo = tk.Button(self.frameComprar1, text="Ir al catalogo", command = lambda: self.cambiarFrame(self.frameCatalogo))
        self.botonIrCatalogo.pack( pady=10)

        self.botonCocinar = tk.Button(self.frameComprar1, text="Agregar un producto personalizado", command=self.cargarProductoPersonalizado)
        self.botonCocinar.pack(pady=10)

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

        #checkbox
        self.var = tk.BooleanVar()
        self.var.set(False)
        self.checkButton = ttk.Checkbutton(self.frameComprar1, text="Desea el kit?", variable=self.var) 
        self.checkButton.pack(pady=5)

        self.ffCarrito = FieldFrame("Valores", ["Cantidad a comprar:"], "Ingrese aquí")
        self.ffCarrito.defRoot(self.frameComprar1)
        self.ffCarrito.defFunc(self.registrarPedidoCanasta)

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



        self.frameCocinar1 = Frame(self.root, bd=1, relief=FLAT, padx=1, pady=1)
        self.frames.append(self.frameCocinar1)
        self.tituloCocinar1 = Label(self.frameCocinar1, text="COCINAR PRODUCTOS")
        self.descipCocinar1 = Label(self.frameCocinar1, text="Se procede a cocinar los productos añadidos a su canasta, por favor continue el proceso dandole al botón Cocinar")

        self.tituloCocinar1.pack(pady = 5)
        self.descipCocinar1.pack(pady = 5)
        self.botonCocinar1 = Button(self.frameCocinar1, text="Cocinar", command=self.procesoDeCocina)
        self.botonCocinar1.pack(pady = 5)
        

        self.textEjecCocinar1 = Text(self.frameCocinar1)
        self.textEjecCocinar1.config(state=tk.DISABLED)
        self.textEjecCocinar1.pack(fill=tk.BOTH, expand=True)

        # frameCalificar
        self.frameCalificar = Frame(self.root, bd=1, relief=FLAT, padx=1, pady=1)
        self.fotoCalificar = Label(self.frameCalificar, image = self.fotoRatonCalificacion)
        self.fotoCalificar.pack()
        self.frames.append(self.frameCalificar)
        #self.labelFC1 = Label(self.frame, text = "Te invitamos a que califiques nuestros productos y a el personal que atendio tu orden\n puedes elegir entre calificar cocinero, domiciliario, productos, ingredientes")
        self.frameCalificar2 = Frame(self.frameCalificar, bd=1, relief = "raise", borderwidth = 2, padx=1, pady=1)
        self.frameCalificar2.pack()
        self.comboBoxCalificar = ttk.Combobox(self.frameCalificar2, values = ["Domiciliario", "Cocinero","Producto","Ingredientes"], state = "readOnly")
        self.comboBoxCalificar.pack(pady=10)
        # fieldframe aqui con raiz frameCalificar2...
        
        self.ffCalificar = FieldFrame("Calificaciónes", ["Calificacion:"], "Ingrese Aquí su valor")
        self.ffCalificar.defRoot(self.frameCalificar2)
        self.ffCalificar.defFunc(self.calificar)
        
    def ejecucionDomicilio(self):
        self.textEjecDomicilio.delete("1.0", tk.END)
        Cliente.getSesion().getPanaderia().enviar_domicilio(Cliente.getSesion().getCanastaOrden(), Cliente.getSesion(),self.textEjecDomicilio)
        messagebox.showinfo("Domicilio", "Su domicilio ha sido realizado")
        time.sleep(2)
        Cliente.getSesion().crearCanastaNueva()
        self.chequeoDeEstados()
        self.cambiarFrame(self.frameCalificar)

    # funcion calificar
    def calificar(self, values):
        #self.comboBoxCalificar.get() #este es el valor del combobox
        try:
            if self.comboBoxCalificar.get() == None or self.comboBoxCalificar.get() == "":
                raise CamposVaciosError([self.comboBoxCalificar.get()])
            elif not self.esNumero(values[0]):
                raise ValueError
            elif int(values[0]) < 1 or 5 < int(values[0]): 
                raise CantidadInvalidaError(values[0])
            else:
                if self.comboBoxCalificar.get() == "Domiciliario":
                    Cliente.getSesion().calificarDomiciliario(self.facturaTemp.getDomiciliario(), values[0])
                elif self.comboBoxCalificar.get() == "Cocinero":
                    Cliente.getSesion().notaCocineros(self.facturaTemp.get(),values[0])
                elif self.comboBoxCalificar.get() == "Producto":
                    Cliente.getSesion().calificarProducto(Producto.obtenerObjetoPorNombreP, values[0])
                elif self.comboBoxCalificar.get() == "Ingredientes":
                    Cliente.getSesion().calificarDomiciliario(Ingrediente.obtenerObjetoPorNombreI, values[0])

        except CamposVaciosError as e:
            messagebox.showwarning("Error", "Completa los campos vacíos")
        except ValueError:
            messagebox.showwarning("Error", "La cantidad debe ser un entero")
        except CantidadInvalidaError as e:
            messagebox.showwarning("Error", "Debes ingresar una cantidad menor a 5 y mayor a 1")
    # frameComprar
    def cargarFrameCarrito(self):
        if Cliente.getSesion().getCanastaOrden() is None:
            Cliente.getSesion().crearCanastaNueva()
        
        self.texto_widget.delete("1.0", tk.END)
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

        self.cargarCatalogo()

    def cargarCatalogo(self):
        for element in Producto.baseDatosProductos:
            self.agregarAlCatalogo(element.getNombre())
        for element in Ingrediente._baseDatosIngredientes:
            self.agregarAlCatalogo(element.getNombre())


    #Frame agregarProductoPersonalizado
    def cargarProductoPersonalizado(self):
        self.diccionarioParaProductoPersonalizado = {}
        self.frameCrearPersonalizado = Frame(self.root, bd=1, relief=FLAT, padx=1, pady=1)
        self.frames.append(self.frameCrearPersonalizado)
        self.tituloCrearPersonalizado = Label(self.frameCrearPersonalizado, text="AGREGAR PRODUCTO PERSONALIZADO", pady=10)
        self.infoCrearPersonalizado = Label(self.frameCrearPersonalizado, text="Aquí puede crear un producto personalizado, para hacerlo debe ingresar el nombre del producto, la cantidad de ingredientes que desea que tenga y posteriormente presionar el botón Aceptar.", wraplength=380, pady=10)
        self.tituloCrearPersonalizado.pack()
        self.infoCrearPersonalizado.pack()
        self.botonIrAtras = Button(self.frameCrearPersonalizado, text = "Volver Atrás", command = lambda: self.cambiarFrame(self.frameCompra))
        self.botonIrAtras.pack(pady=10)
        
        def botonIngredientes(val):
            if val[0] in self.diccionarioParaProductoPersonalizado:
                self.diccionarioParaProductoPersonalizado[val[0]] += int(val[1])
            else:
                self.diccionarioParaProductoPersonalizado[val[0]] = int(val[1])
            self.texto_widget2.config(state=tk.NORMAL)
            self.texto_widget2.delete(1.0, "end")
            self.texto_widget2.insert(1.0, "Ingredientes necesarios para cocinar " + self.ffCrearPersonalizado.getValores()[0] + ":\n")
            for elements, cantidad in self.diccionarioParaProductoPersonalizado.items():
                self.texto_widget2.insert(tk.END, "Ingrediente: " + elements + " - Cantidad: " + str(cantidad) + "\n")

            self.texto_widget2.tag_configure("center", justify="center")

            # Aplicar el tag al texto
            self.texto_widget2.tag_add("center", "1.0", "end")

        self.ffCrearPersonalizado = FieldFrame("Producto deseado", ["Nombre del producto:", "Cantidad del producto:"], "Ingrese aquí")
        self.ffCrearPersonalizado.defRoot(self.frameCrearPersonalizado)
        
        self.ffCrearPersonalizado2 = FieldFrame("Ingredientes necesarios", ["Nombre del ingrediente:", "Cantidad del ingrediente:"], "Ingrese aquí")
        self.ffCrearPersonalizado2.defRoot(self.frameCrearPersonalizado)
        self.ffCrearPersonalizado2.defFunc(botonIngredientes)

        def anadirProductoPersonalizado():
            Cliente.getSesion().getCanastaOrden().recibirOrdenPersonalizada(self.ffCrearPersonalizado.getValores()[0], self.diccionarioParaProductoPersonalizado, self.ffCrearPersonalizado.getValores()[1], self.var2.get())
            self.texto_widget2.config(state=tk.NORMAL)
            self.texto_widget2.delete(1.0, "end")

            for elements, cantidad in Cliente.getSesion().getCanastaOrden().getProductosEnLista().items():
                self.texto_widget2.insert(tk.END, "Producto: " + Producto.obtenerObjetoPorIdP(elements).getNombre() + " - Cantidad: " + str(cantidad) + "\n")
            for elements, cantidad in Cliente.getSesion().getCanastaOrden().getIngredientesEnLista().items():
                self.texto_widget2.insert(tk.END, "Ingrediente: " + Ingrediente.obtenerObjetoPorIdI(elements).getNombre() + " - Cantidad: " + str(cantidad) + "\n")
            for elements, cantidad in Cliente.getSesion().getCanastaOrden().getKitsEnLista().items():
                self.texto_widget2.insert(tk.END, "Kits: " + Producto.obtenerObjetoPorIdP(elements).getNombre() + " - Cantidad: " + str(cantidad) + "\n")

            # Tag para centrar texto
            self.texto_widget2.tag_configure("center", justify="center")

            # Aplicar el tag al texto
            self.texto_widget2.tag_add("center", "1.0", "end")
            self.texto_widget2.config(state=tk.DISABLED)

        self.var2 = tk.BooleanVar()
        self.var2.set(False)
        self.checkButton2 = ttk.Checkbutton(self.frameCrearPersonalizado, text="Desea el kit?", variable=self.var2) 
        self.checkButton2.pack(pady=5)

        self.botonCrearPersonalizado = Button(self.frameCrearPersonalizado, text="Agregar Producto", command=anadirProductoPersonalizado)
        self.botonCrearPersonalizado.pack(pady = 5)

        # Agregar un Scrollbar
        scrollbar = Scrollbar(self.frameCrearPersonalizado)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Agregar un widget de Texto
        self.texto_widget2 = Text(self.frameCrearPersonalizado, wrap=tk.WORD, yscrollcommand=scrollbar.set)
        self.texto_widget2.pack(fill=tk.BOTH, expand=True)
        for elements, cantidad in Cliente.getSesion().getCanastaOrden().getProductosEnLista().items():
            self.texto_widget2.insert(tk.END, "Producto: " + Producto.obtenerObjetoPorIdP(elements).getNombre() + " - Cantidad: " + str(cantidad) + "\n")
        for elements, cantidad in Cliente.getSesion().getCanastaOrden().getIngredientesEnLista().items():
            self.texto_widget2.insert(tk.END, "Ingrediente: " + Ingrediente.obtenerObjetoPorIdI(elements).getNombre() + " - Cantidad: " + str(cantidad) + "\n")
        for elements, cantidad in Cliente.getSesion().getCanastaOrden().getKitsEnLista().items():
            self.texto_widget2.insert(tk.END, "Kits: " + Producto.obtenerObjetoPorIdP(elements).getNombre() + " - Cantidad: " + str(cantidad) + "\n")
        self.texto_widget2.config(state=tk.DISABLED)

        # Tag para centrar texto
        self.texto_widget2.tag_configure("center", justify="center")

        # Aplicar el tag al texto
        self.texto_widget2.tag_add("center", "1.0", "end")
        
        self.cambiarFrame(self.frameCrearPersonalizado)



    def cargarProductoPersonalizado2(self):
        self.diccionarioParaProductoPersonalizado = {}
        self.frameCrearPersonalizado = Frame(self.root, bd=1, relief=FLAT, padx=1, pady=1)
        self.frames.append(self.frameCrearPersonalizado)
        self.tituloCrearPersonalizado = Label(self.frameCrearPersonalizado, text="AGREGAR PRODUCTO PERSONALIZADO", pady=10)
        self.infoCrearPersonalizado = Label(self.frameCrearPersonalizado, text="Aquí puede mandar a cocinar un producto personalizado, para hacerlo debe ingresar el nombre del producto y la cantidad que desea en el primer apartado (FieldFrame), posteriormente dele click al primer botón de Aceptar, luego añada el nombre del ingrediente que usa y la cantidad en el segundo apartado (FieldFrame), luego persione el segundo botón Aceptar, podrá agregar cuántos ingredientes desee, solo haga el mismo proceso en el segundo apartado las veces necesarias, cuando ingrese el primer ingrediente en el apartado inferior se le irá mostrando la lista de ingredientes que ha añadido a la receta hasta el momento, cuando considere que ha terminado su receta por favor presione Agregar Producto, este se añadira a la lista de productos a cocinar, finalmente para mandar a cocinar toda la lista dele al bóton Cocinar, si desea seguir agregando productos para enviar a cocinar presione el botón Volver Atrás, la lista de productos para cocinar no se reiniciará hasta que se envíen a Cocinar.", wraplength=800, pady=10)
        self.tituloCrearPersonalizado.pack()
        self.infoCrearPersonalizado.pack()
        
        def botonIngredientes(val):
            try:
                if self.ffCrearPersonalizado.getValores() == [] or self.ffCrearPersonalizado.getValores()[0] == None or self.ffCrearPersonalizado.getValores()[0] == "" or self.ffCrearPersonalizado.getValores()[1] == None or self.ffCrearPersonalizado.getValores()[1] == "":
                    raise CamposVaciosError(self.ffCrearPersonalizado.getValores()[0])
                else:
                    if val[0] in self.diccionarioParaProductoPersonalizado:
                        self.diccionarioParaProductoPersonalizado[val[0]] += int(val[1])
                        self.textEjecCocinar2.config(state=tk.NORMAL)
                        self.textEjecCocinar2.delete(1.0, "end")
                        self.textEjecCocinar2.insert(1.0, "Ingredientes necesarios para cocinar " + self.ffCrearPersonalizado.getValores()[0] + ":\n")
                        self.textEjecCocinar2.config(state=tk.DISABLED)
                    else:
                        self.diccionarioParaProductoPersonalizado[val[0]] = int(val[1])
                        self.textEjecCocinar2.config(state=tk.NORMAL)
                        self.textEjecCocinar2.delete(1.0, "end")
                        self.textEjecCocinar2.insert(1.0, "Ingredientes necesarios para cocinar " + self.ffCrearPersonalizado.getValores()[0] + ":\n")
                        self.textEjecCocinar2.config(state=tk.DISABLED)
            
                    for elements, cantidad in self.diccionarioParaProductoPersonalizado.items():
                        self.textEjecCocinar2.config(state=tk.NORMAL)
                        self.textEjecCocinar2.insert(tk.END, "Ingrediente: " + elements + " - Cantidad: " + str(cantidad) + "\n")
                        self.textEjecCocinar2.config(state=tk.DISABLED)

                    self.textEjecCocinar2.tag_configure("center", justify="center")

                    # Aplicar el tag al texto
                    self.textEjecCocinar2.tag_add("center", "1.0", "end")
            
            except CamposVaciosError as e:
                messagebox.showwarning("Error", "Completa primero el nombre y la cantidad del producto")

        def botonAnadido(values):
            messagebox.showinfo("Añadido exitoso", "Su producto ha sido añadido con éxito")
            self.textEjecCocinar2.config(state=tk.NORMAL)
            self.textEjecCocinar2.delete(1.0, "end")
            self.textEjecCocinar2.insert(1.0, "Creando Producto" + " " + values[0] + "\n")
            self.textEjecCocinar2.tag_configure("center", justify="center")
            self.textEjecCocinar2.tag_add("center", "1.0", "end")
            self.textEjecCocinar2.config(state=tk.DISABLED)

        self.ffCrearPersonalizado = FieldFrame("Producto deseado", ["Nombre del producto:", "Cantidad del producto:"], "Ingrese aquí")
        self.ffCrearPersonalizado.defRoot(self.frameCrearPersonalizado)
        self.ffCrearPersonalizado.defFunc(botonAnadido)
        
        self.ffCrearPersonalizado2 = FieldFrame("Ingredientes necesarios", ["Nombre del ingrediente:", "Cantidad del ingrediente:"], "Ingrese aquí")
        self.ffCrearPersonalizado2.defRoot(self.frameCrearPersonalizado)
        self.ffCrearPersonalizado2.defFunc(botonIngredientes)

        def anadirProductoPersonalizado():
            self.textEjecCocinar2.config(state=tk.NORMAL)
            self.textEjecCocinar2.delete(1.0, "end")

            Producto.crearProductoPersonalizado(self.ffCrearPersonalizado.getValores()[0], self.diccionarioParaProductoPersonalizado)
            self.diccionarioFuncionalidad4[Producto.obtenerObjetoPorNombreP(self.ffCrearPersonalizado.getValores()[0]).getId()] = int(self.ffCrearPersonalizado.getValores()[1])

            for ingredienteNombre, cantidad in self.diccionarioFuncionalidad4.items():
                    self.textEjecCocinar2.insert(tk.END, "Producto: " + Producto.obtenerObjetoPorIdP(ingredienteNombre).getNombre() + " - Cantidad: " + str(cantidad) + "\n")

            # Tag para centrar texto
            self.textEjecCocinar2.tag_configure("center", justify="center")

            # Aplicar el tag al texto
            self.textEjecCocinar2.tag_add("center", "1.0", "end")
            self.textEjecCocinar2.config(state=tk.DISABLED)

        def ejecucionCocinarProductos2():
            Cliente.getSesion().getPanaderia().cocinar(self.diccionarioFuncionalidad4)
            self.diccionarioFuncionalidad4 = {}

        self.var2 = tk.BooleanVar()
        self.var2.set(False)
        
        self.botonCrearPersonalizado = Button(self.frameCrearPersonalizado, text="Agregar Producto", command=anadirProductoPersonalizado)
        self.botonCrearPersonalizado.pack(pady = 5)

        self.botonCocinar = Button(self.frameCrearPersonalizado, text="Cocinar", command= ejecucionCocinarProductos2)
        self.botonCocinar.pack(pady = 5)

        self.botonIrAtras = Button(self.frameCrearPersonalizado, text = "Volver Atrás", command = lambda: self.cambiarFrame(self.frameCocinar))
        self.botonIrAtras.pack(pady= 5)

        self.frameCocinarPersonalizadot = Frame(self.frameCrearPersonalizado, bd=1, relief=FLAT, padx=1, pady=5)
        self.textEjecCocinar2 = Text(self.frameCocinarPersonalizadot) 
        self.frameCocinarPersonalizadot.pack(fill=tk.BOTH, expand=True)
        self.textEjecCocinar2.pack(fill=tk.BOTH, expand=True)
        
        if self.diccionarioFuncionalidad4 != []:
            for ingredienteNombre, cantidad in self.diccionarioFuncionalidad4.items():
                    self.textEjecCocinar2.insert(tk.END, "Producto: " + Producto.obtenerObjetoPorIdP(ingredienteNombre).getNombre() + " - Cantidad: " + str(cantidad) + "\n")

        # Agregar un Scrollbar
        scrollbar = Scrollbar(self.frameCrearPersonalizado)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Tag para centrar texto
        self.textEjecCocinar2.tag_configure("center", justify="center")

        # Aplicar el tag al texto
        self.textEjecCocinar2.tag_add("center", "1.0", "end")
        
        self.cambiarFrame(self.frameCrearPersonalizado)

    # frameFacturacion
    def cargarFrameFacturacion(self):
        from gestorAplicacion.gestion.Recibo import Recibo #importo esto aqui para evitar el error de importacion circular
        #Cliente.getSesion().getCanastaOrden().setPagada(True)
        #self.chequeoDeEstados()
        #No borrar esas lineas, las comenté para que no te aparezca la alerta

        if Cliente.getSesion().getTipoDescuento() == None:
            Cliente.getSesion().establecerDescuentoPorTipoValido("NINGUNO")


        self.labelFacturacion2.config(text = "Su saldo es de "+ str(Cliente.getSesion().getPresupuesto())+"$$$")

        # Implementacion logica widget de texto

        #Creacion de la factura
        Cliente.getSesion().setDomiciliario(Cliente.getSesion().getPanaderia().domiciliarioAleatorio())
        self.facturaTemp = Recibo(Cliente.getSesion(), Cliente.getSesion().getCanastaOrden(), Cliente.getSesion().getDomiciliario())
        


        self.textoFacturacion.config(state="normal")
        self.textoFacturacion.delete(1.0, "end")
        self.varFactura = self.facturaTemp.imprimir_factura()
        self.textoFacturacion.insert(1.0, self.varFactura)

        # Configurar el tag para centrar el texto
        self.textoFacturacion.tag_configure("center", justify="center")

        # Aplicar el tag al texto
        self.textoFacturacion.tag_add("center", "1.0", "end")
        self.textoFacturacion.config(state="disabled")
    
    # cargarFrameFacturasPasadas
    def cargarFrameFacturasPasadas(self):
        self.idsFacturasPasadas = []
        for i in Cliente.getSesion().getRecibos():
            self.idsFacturasPasadas.append(str(i.getIdRecibo()))
        print(self.idsFacturasPasadas)
        self.comboBoxClonar.config(values=self.idsFacturasPasadas)

        self.textoFacturasPasadas.config(state = tk.NORMAL) #permitir edicion del campo de texto
        self.textoFacturasPasadas.delete("1.0", tk.END) #borrar todo lo que tenia el campo de texto antes

        for i in Cliente.getSesion().getRecibos(): #imprimir todas las facturas en el historial
            self.textoFacturasPasadas.insert(tk.END,i.imprimir_factura()+"\n")
        
        self.textoFacturasPasadas.tag_configure("center", justify = "center")
        self.textoFacturasPasadas.tag_add("center", "1.0", "end")
        self.textoFacturasPasadas.config(state = tk.DISABLED)

    def procesoDeCocina(self):
            self.menu_procesos.entryconfigure("Func. Cocinar", state="disabled")
            self.menu_procesos.entryconfigure("Func. Ingredientes e inventario", state="normal")
            self.textEjecCocinar1.config(state=tk.NORMAL)
            self.textEjecCocinar1.delete(1.0, "end")
            messagebox.showinfo("Información", "Parece que faltan ingredientes para cocinar sus productos, se accede a conseguir ingredientes")
            self.cargarFrameIngredientesDesdeClienteNormal(self.frameCocinar1)
            self.textEjecCocinar1.config(state=tk.DISABLED)



    def cargarFrameIngredientesDesdeClienteNormal(self,frame):
        self.frameIngredientes1 = Frame(self.root, bd=1, relief=FLAT, padx=1, pady=1)
        self.frames.append(self.frameIngredientes1)
        self.cambiarFrame(self.frameIngredientes1)
        self.tituloIngredientes1 = Label(self.frameIngredientes1, text="COMPRAR INGREDIENTES")
        self.descipIngredientes1 = Label(self.frameIngredientes1, text="Se procede a comprar los ingredientes añadidos a su canasta, por favor continue el proceso dandole al botón Comprar Ingredientes")

        def ejecucionComprarIngredientes():
            from gestorAplicacion.humanos.Cocinero import Cocinero
            self.textEjecIngredientes1.config(state=tk.NORMAL)
            Cliente.getSesion().getCanastaOrden().enviarOrdenCanasta(self.textEjecIngredientes1)
            self.textEjecIngredientes1.config(state=tk.DISABLED)
            time.sleep(3)
            messagebox.showinfo("Información", "Ingredientes comprados, se procede a cocinar")
            self.chequeoDeEstados()
            self.cambiarFrame(self.frameCocinar1)
            self.textEjecCocinar1.config(state=tk.NORMAL)
            self.textEjecCocinar1.delete(1.0, "end")
            for i in range(len(Cocinero._procesosDeProductosCocinados)-1):
                for element in Cocinero._procesosDeProductosCocinados[i]:
                    num = random.randint(0, 10)
                    if num<=3:
                        self.textEjecCocinar1.insert(tk.END, Cocinero._fallosCocinando[random.randint(0, len(Cocinero._fallosCocinando))-1] + "\n")
                    else:
                        self.textEjecCocinar1.insert(tk.END,"Se ha completado el proceso de " + element + "\n")
                self.textEjecCocinar1.insert(tk.END,"Se ha cocinado el producto " + Cocinero._productosCocinados[i] + "\n")
                
            self.textEjecCocinar1.tag_configure("center", justify="center")
            self.textEjecCocinar1.tag_add("center", "1.0", "end")
            self.textEjecCocinar1.config(state=tk.DISABLED)
            Cocinero._procesosDeProductosCocinados = []
            Cocinero._productosCocinados = []
            Cocinero._fallosCocinando= []
            
            self.textEjecCocinar1.config(state=tk.DISABLED)
            
            messagebox.showinfo("Información", "Productos cocinados, se procede a enviarlos a su domicilio")
            time.sleep(3)
            self.cambiarFrame(self.frameDomicilio)
            Cliente.getSesion().getCanastaOrden().setCocinada(True)
            self.chequeoDeEstados()
            self.cambiarFrame(self.frameDomicilio)

        self.tituloIngredientes1.pack(pady = 5)
        self.descipIngredientes1.pack(pady = 5)
        self.botonIngredientes1 = Button(self.frameIngredientes1, text="Comprar Ingredientes", command=ejecucionComprarIngredientes)
        self.botonIngredientes1.pack(pady = 5)
        
        self.textEjecIngredientes1 = Text(self.frameIngredientes1)
        self.textEjecIngredientes1.config(state=tk.DISABLED)
        self.textEjecIngredientes1.pack(fill=tk.BOTH, expand=True)



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
        Serializador.guardarPanaderia(self.panaderia)
        self.root.destroy()

    def cambiarFrame(self, frame, guardarComoFrameAnterior = True):
        #if Cliente.getSesion() == None:
            if guardarComoFrameAnterior == True:
                self.frameAnterior = self.frameActual
            if frame == self.frameFacturacion:
                self.cargarFrameFacturacion()
            if frame == self.frameFacturasPasadas:
                self.cargarFrameFacturasPasadas()
            if frame == self.frameComprar:
                self.cargarFrameCarrito() 

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
        self.textoDescripcion.delete(1.0, tk.END)
        nutrientes = (
            "_______________________________________________________\n"
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
        self.textoDescripcion.config(state = "normal")
        self.textoDescripcion.delete("1.0", "end")
        self.textoDescripcion.insert(tk.END, nutrientes)
        # Configurar el tag para centrar el texto
        self.textoDescripcion.tag_configure("center", justify="center")

        # Aplicar el tag al texto
        self.textoDescripcion.tag_add("center", "1.0", "end")
        self.textoDescripcion.config(state = "disabled")

    @staticmethod
    def esNumero(valor):
        try:
            int(valor)  # Intenta convertir la cadena a un número de punto flotante
            return True
        except ValueError:
            return False

    def registrarPedidoCanasta(self,val):
        try:
            if val[0] == "":
                raise CamposVaciosError([val[0]])
            elif not(Ingrediente.verificacionExistenciaPorNombreI(self.comboboxfc1.get()) or Producto.verificarExistenciaPorNombreP(self.comboboxfc1.get())):
                raise ProductoNoEncontradoError(self.comboboxfc1.get())
            elif not self.esNumero(val[0]):
                raise ValueError()
            elif int(val[0]) < -15 or int(val[0])>15 or int(val[0]) == 0:
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
                self.chequeoDeEstados()

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
        self.chequeoDeEstados()
        self.cambiarFrame(self.framePrincipal)

    def iniciarSesion(self, val):
        while True:
            try:
                cliente1 = Cliente.inicioSesionId(int(val[0]))
                if cliente1 is None:
                    raise UsuarioNoEncontradoError(int(val[0]))

                if Cliente.inicioSesionContrasena(cliente1, val[1]) == "Contraseña incorrecta":
                    raise UsuarioNoEncontradoError(int(val[0]))
                
                self.chequeoDeEstados()
                messagebox.showinfo("Inicio de sesion", "Inicio de sesion exitoso")
                self.cambiarFrame(self.framePrincipal)
                break  # Sale del bucle si el inicio de sesión fue exitoso

            except UsuarioNoEncontradoError as e:
                messagebox.showwarning("Error", "El usuario o la contraseña son incorrectos")
                break  # Sale del bucle si se encuentra un error en el inicio de sesión
            except ValueError:
                messagebox.showwarning("Error", "El usuario debe ser un numero")
                break  # Sale del bucle si se encuentra un error en el inicio de sesión


    def chequeoDeEstados(self):
        if Cliente.getSesion() is not None:
            self.menu_procesos.entryconfigure("Iniciar sesion", state="disabled")
            self.menu_procesos.entryconfigure("Registrarse", state="disabled")
            self.menu_procesos.entryconfigure("Cerrar sesion", state="normal")
            self.menu_procesos.entryconfigure("Lo mejor de nuestra panaderia", state="normal")
            self.menu_procesos.entryconfigure("Modificar datos", state="normal")

            cliente=Cliente.getSesion()
            if Cliente.getSesion().getId()==202:
                canasta=cliente.getCanastaOrden()
                if canasta.getPagada() and not canasta.getCocinada():
                    #messagebox.showinfo("Info", "Ha comenzado un proceso de compra, continue con el proceso de compra, al finalizar se desbloquearan el resto de opciones")
                    self.menu_procesos.entryconfigure("Func. Crear Canasta de Compras", state="disabled", command= lambda: self.cambiarFrame(self.frameComprar))
                    self.menu_procesos.entryconfigure("Func. Facturar", state="disabled")
                    self.menu_procesos.entryconfigure("Func. Cocinar", state="normal", command= lambda: self.cambiarFrame(self.frameCocinar1))
                    self.menu_procesos.entryconfigure("Func. Ingredientes e inventario", state="disabled", command = lambda: self.cambiarFrame(self.frameIngredientes1))
                    self.menu_procesos.entryconfigure("Func. Domicilio", state="disabled")
    
                elif canasta.getCocinada() and not canasta.getEntregada():
                    self.menu_procesos.entryconfigure("Func. Crear Canasta de Compras", state="disabled", command= lambda: self.cambiarFrame(self.frameComprar))
                    self.menu_procesos.entryconfigure("Func. Facturar", state="disabled")
                    self.menu_procesos.entryconfigure("Func. Cocinar", state="disabled", command= lambda: self.cambiarFrame(self.frameCocinar1))
                    self.menu_procesos.entryconfigure("Func. Ingredientes e inventario", state="disabled", command = lambda: self.cambiarFrame(self.frameIngredientes1))
                    self.menu_procesos.entryconfigure("Func. Domicilio", state="normal")

                elif canasta.getEntregada():
                    self.menu_procesos.entryconfigure("Func. Crear Canasta de Compras", state="normal", command= lambda: self.cambiarFrame(self.frameComprar))
                    self.menu_procesos.entryconfigure("Func. Facturar", state="normal")
                    self.menu_procesos.entryconfigure("Func. Cocinar", state="normal", command= lambda: self.cambiarFrame(self.frameCocinar1))
                    self.menu_procesos.entryconfigure("Func. Ingredientes e inventario", state="normal", command = lambda: self.cambiarFrame(self.frameIngredientes1))
                    self.menu_procesos.entryconfigure("Func. Domicilio", state="normal")
                else:
                    self.menu_procesos.entryconfigure("Func. Crear Canasta de Compras", state="normal", command= lambda: self.cambiarFrame(self.frameComprar))
                    self.menu_procesos.entryconfigure("Func. Facturar", state="normal")
                    self.menu_procesos.entryconfigure("Func. Cocinar", state="normal", command= lambda: self.cambiarFrame(self.frameCocinar))
                    self.menu_procesos.entryconfigure("Func. Ingredientes e inventario", state="normal", command = lambda: self.cambiarFrame(self.frameComprarIngredientes))
                    self.menu_procesos.entryconfigure("Func. Domicilio", state="disabled", command= lambda: self.cambiarFrame(self.frameDomicilio))
            else:
                canasta=cliente.getCanastaOrden()
                if (canasta is None) or (canasta.getProductosEnLista()=={} and canasta.getIngredientesEnLista()=={} and canasta.getKitsEnLista()=={}):
                    self.menu_procesos.entryconfigure("Func. Crear Canasta de Compras", state="normal", command= lambda: self.cambiarFrame(self.frameComprar))
                    self.menu_procesos.entryconfigure("Func. Facturar", state="normal")
                    self.menu_procesos.entryconfigure("Func. Cocinar", state="disabled", command= lambda: self.cambiarFrame(self.frameCocinar1))
                    self.menu_procesos.entryconfigure("Func. Ingredientes e inventario", state="disabled", command = lambda: self.cambiarFrame(self.frameIngredientes1))
                    self.menu_procesos.entryconfigure("Func. Domicilio", state="disabled")

                elif (not canasta.getPagada()) and (not(canasta.getProductosEnLista()=={} and canasta.getIngredientesEnLista()=={} and canasta.getKitsEnLista()=={})):
                    self.menu_procesos.entryconfigure("Func. Crear Canasta de Compras", state="normal", command= lambda: self.cambiarFrame(self.frameComprar))
                    self.menu_procesos.entryconfigure("Func. Facturar", state="normal")
                    self.menu_procesos.entryconfigure("Func. Cocinar", state="disabled", command= lambda: self.cambiarFrame(self.frameCocinar1))
                    self.menu_procesos.entryconfigure("Func. Ingredientes e inventario", state="disabled", command = lambda: self.cambiarFrame(self.frameIngredientes1))
                    self.menu_procesos.entryconfigure("Func. Domicilio", state="disabled")

                elif canasta.getPagada() and not canasta.getCocinada():
                    self.menu_procesos.entryconfigure("Func. Crear Canasta de Compras", state="disabled", command= lambda: self.cambiarFrame(self.frameComprar))
                    self.menu_procesos.entryconfigure("Func. Facturar", state="disabled")
                    self.menu_procesos.entryconfigure("Func. Cocinar", state="normal", command= lambda: self.cambiarFrame(self.frameCocinar1))
                    self.menu_procesos.entryconfigure("Func. Ingredientes e inventario", state="disabled", command = lambda: self.cambiarFrame(self.frameIngredientes1))
                    self.menu_procesos.entryconfigure("Func. Domicilio", state="disabled")

                elif canasta.getCocinada() and not canasta.getEntregada():
                    self.menu_procesos.entryconfigure("Func. Crear Canasta de Compras", state="disabled", command= lambda: self.cambiarFrame(self.frameComprar))
                    self.menu_procesos.entryconfigure("Func. Facturar", state="disabled")
                    self.menu_procesos.entryconfigure("Func. Cocinar", state="disabled", command= lambda: self.cambiarFrame(self.frameCocinar1))
                    self.menu_procesos.entryconfigure("Func. Ingredientes e inventario", state="disabled", command = lambda: self.cambiarFrame(self.frameIngredientes1))
                    self.menu_procesos.entryconfigure("Func. Domicilio", state="normal")
                elif canasta.getEntregada():
                    self.menu_procesos.entryconfigure("Func. Crear Canasta de Compras", state="normal", command= lambda: self.cambiarFrame(self.frameComprar))
                    self.menu_procesos.entryconfigure("Func. Facturar", state="normal")
                    self.menu_procesos.entryconfigure("Func. Cocinar", state="disabled", command= lambda: self.cambiarFrame(self.frameCocinar1))
                    self.menu_procesos.entryconfigure("Func. Ingredientes e inventario", state="disabled", command = lambda: self.cambiarFrame(self.frameIngredientes1))
                    self.menu_procesos.entryconfigure("Func. Domicilio", state="disabled")
        else:
            self.menu_procesos.entryconfigure("Iniciar sesion", state="normal")
            self.menu_procesos.entryconfigure("Registrarse", state="normal")
            self.menu_procesos.entryconfigure("Cerrar sesion", state="disabled")
            self.menu_procesos.entryconfigure("Func. Crear Canasta de Compras", state="disabled")
            self.menu_procesos.entryconfigure("Func. Facturar", state="disabled")
            self.menu_procesos.entryconfigure("Func. Cocinar", state="disabled")
            self.menu_procesos.entryconfigure("Func. Ingredientes e inventario", state="disabled")
            self.menu_procesos.entryconfigure("Func. Domicilio", state="disabled")
            self.menu_procesos.entryconfigure("Lo mejor de nuestra panaderia", state="disabled")
            self.menu_procesos.entryconfigure("Modificar datos", state="disabled")


    def registrarUsuario(self,val):
        try:
            if Cliente.crearCuenta(val[0], int(val[1]), val[2]) == "Ya existe una cuenta con ese ID":
                raise usuarioExistenteError
            messagebox.showinfo("Registro", "Usuario registrado correctamente")
            self.chequeoDeEstados()
            self.cambiarFrame(self.framePrincipal)
        except usuarioExistenteError as e:
            messagebox.showwarning("Error", "El usuario ya existe")

    def cambiarContrasena(self, val):
        Cliente.getSesion().setContrasena(val[0])
        messagebox.showinfo("Cambio de contraseña", "Contraseña cambiada correctamente")

    def meterPlata(self, val):
        Cliente.getSesion().setPresupuesto(Cliente.getSesion().getPresupuesto() + int(val[0]))
        messagebox.showinfo("Meter plata", "Plata ingresada correctamente, su nuevo saldo es de "+ str(Cliente.getSesion().getPresupuesto())+"$$$")


    # Métodos funcionalidad 4
    
    def valoresDiccionarioCocina(self, values):

        try:
            if self.comboboxCocinar.get() == None or self.comboboxCocinar.get() == "":
                raise CamposVaciosError(self.comboboxCocinar.get())
            elif not (Producto.verificarExistenciaPorNombreP(self.comboboxCocinar.get())):
                raise ProductoNoEncontradoError(self.comboboxCocinar.get())
            elif not self.esNumero(values[0]):
                raise ValueError()
            elif int(values[0]) < 0 or 15 < int(values[0]) or int(values[0]) == 0:
                raise CantidadInvalidaError(int(values[0]))
            else:
                if not (Producto.obtenerObjetoPorNombreP(self.comboboxCocinar.get()).getId() in self.diccionarioFuncionalidad4):
                    self.diccionarioFuncionalidad4[Producto.obtenerObjetoPorNombreP(self.comboboxCocinar.get()).getId()] = int(values[0])
                else:
                    
                    if int(self.diccionarioFuncionalidad4[Producto.obtenerObjetoPorNombreP(self.comboboxCocinar.get()).getId()]) + int(values[0]) <= 15:
                        self.diccionarioFuncionalidad4[Producto.obtenerObjetoPorNombreP(self.comboboxCocinar.get()).getId()] = int(self.diccionarioFuncionalidad4[Producto.obtenerObjetoPorNombreP(self.comboboxCocinar.get()).getId()]) + int(values[0])
                    else:
                        raise CantidadInvalidaError(int(self.diccionarioFuncionalidad4[Producto.obtenerObjetoPorNombreP(self.comboboxCocinar.get()).getId()]) + int(values[0]))

                self.textEjecCocinar.config(state=tk.NORMAL)
                self.textEjecCocinar.delete(1.0, tk.END)
                for ingredienteNombre, cantidad in self.diccionarioFuncionalidad4.items():
                    self.textEjecCocinar.insert(tk.END, "Produco: " + Producto.obtenerObjetoPorIdP(ingredienteNombre).getNombre() + " - Cantidad: " + str(cantidad) + "\n")
                self.textEjecCocinar.config(state=tk.DISABLED)
                
                self.comboboxCocinar.delete(0, "end")
                self.textEjecCocinar.tag_configure("center", justify="center")
                self.textEjecCocinar.tag_add("center", "1.0", "end")

        except CamposVaciosError as e:
            messagebox.showwarning("Error", "Completa los campos vacíos")
        except ProductoNoEncontradoError as e:
            messagebox.showwarning("Error", "El producto ingresado no existe")
        except ValueError:
            messagebox.showwarning("Error", "La cantidad debe ser un entero")
        except CantidadInvalidaError as e:
            messagebox.showwarning("Error", "Debes ingresar una cantidad no negativa, menor o igual a 15 y diferente de 0")

    def ejecucionCocinarProductos(self):
        from gestorAplicacion.humanos.Cocinero import Cocinero
        Cliente.getSesion().getPanaderia().cocinar(self.diccionarioFuncionalidad4)
        self.textEjecCocinar.config(state=tk.NORMAL)
        self.textEjecCocinar.delete(1.0, "end")
        for i in range(len(Cocinero._procesosDeProductosCocinados)-1):
            for element in Cocinero._procesosDeProductosCocinados[i]:
                num = random.randint(0, 10)
                if num<=3:
                    self.textEjecCocinar.insert(tk.END, Cocinero._fallosCocinando[random.randint(0, len(Cocinero._fallosCocinando))-1] + "\n")
                else:
                    self.textEjecCocinar.insert(tk.END,"Se ha completado el proceso de " + element + "\n")
            self.textEjecCocinar.insert(tk.END,"Se ha cocinado el producto " + Cocinero._productosCocinados[i] + "\n")
            
        self.textEjecCocinar.tag_configure("center", justify="center")
        self.textEjecCocinar.tag_add("center", "1.0", "end")
        self.textEjecCocinar.config(state=tk.DISABLED)
        Cocinero._procesosDeProductosCocinados = []
        Cocinero._productosCocinados = []
        Cocinero._fallosCocinando= []
        self.diccionarioFuncionalidad4 = {}

    # Métodos para la funcionalidad 5

    def valoresdiccionarioCompra(self, values):
        
        try:
            if self.comboboxComprarIngredientes.get() == None or self.comboboxComprarIngredientes.get() == "":
                raise CamposVaciosError(self.comboboxComprarIngredientes.get())
            elif not (Ingrediente.verificacionExistenciaPorNombreI(self.comboboxComprarIngredientes.get())):
                raise ProductoNoEncontradoError(self.comboboxComprarIngredientes.get())
            elif not self.esNumero(values[0]):
                raise ValueError()
            elif int(values[0]) < 0 or 50 < int(values[0]) or int(values[0]) == 0:
                raise CantidadInvalidaError(int(values[0]))
            else:
                if not (self.comboboxComprarIngredientes.get() in self.diccionarioFuncionalidad5):
                    self.diccionarioFuncionalidad5[self.comboboxComprarIngredientes.get()] = int(values[0])
                else:
                    
                    if int(self.diccionarioFuncionalidad5[self.comboboxComprarIngredientes.get()]) + int(values[0]) <= 50:
                        self.diccionarioFuncionalidad5[self.comboboxComprarIngredientes.get()] = int(self.diccionarioFuncionalidad5[self.comboboxComprarIngredientes.get()]) + int(values[0])
                    else:
                        raise CantidadInvalidaError(int(self.diccionarioFuncionalidad5[self.comboboxComprarIngredientes.get()]) + int(values[0]))

                self.textEjecComprarIngredientes.config(state=tk.NORMAL)
                self.textEjecComprarIngredientes.delete(1.0, tk.END)
                for ingredienteNombre, cantidad in self.diccionarioFuncionalidad5.items():
                    self.textEjecComprarIngredientes.insert(tk.END, "Ingrediente: " + ingredienteNombre + " - Cantidad: " + str(cantidad) + "\n")
                self.textEjecComprarIngredientes.config(state=tk.DISABLED)
                
                self.comboboxComprarIngredientes.delete(0, "end")
                self.textEjecComprarIngredientes.tag_configure("center", justify="center")
                self.textEjecComprarIngredientes.tag_add("center", "1.0", "end")
        
        except CamposVaciosError as e:
            messagebox.showwarning("Error", "Completa los campos vacíos")
        except ProductoNoEncontradoError as e:
            messagebox.showwarning("Error", "El ingrediente ingresado no existe")
        except ValueError:
            messagebox.showwarning("Error", "La cantidad debe ser un entero")
        except CantidadInvalidaError as e:
            messagebox.showwarning("Error", "Debes ingresar una cantidad no negativa, menor a 50 y diferente de 0")

    def ejecucionComprarIngredientes(self):
        Cliente.getSesion().getPanaderia().comprarIngredientes(self.diccionarioFuncionalidad5, self.textEjecComprarIngredientes)
        self.diccionarioFuncionalidad5 = {}

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

    def cambiarDireccion2(self, val):
        try:
            if val[0] == "":
                raise CamposVaciosError([val[0]])
            elif not Cliente.getSesion().establecerDomicilioValido(val[0],self.comboBoxDireccion2.get()):
                raise CamposVaciosError([self.comboBoxDireccion2.get()])
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

    def pasarAlPago(self):
        if Cliente.getSesion().getCanastaOrden().getProductosEnLista() == {} and Cliente.getSesion().getCanastaOrden().getIngredientesEnLista() == {} and Cliente.getSesion().getCanastaOrden().getKitsEnLista() == {}:
            messagebox.showwarning("Error", "No hay productos en la canasta")
        elif Cliente.getSesion().getPresupuesto()<self.facturaTemp.getTotal():
            messagebox.showinfo("Información", "No se ha podido pagar su factura, su saldo es de "+str(Cliente.getSesion().getPresupuesto())+"$$$ Lo cual es insuficiente")
            self.cambiarFrame(self.frameMeterPlata)
        else:
            Cliente.getSesion().setPresupuesto(Cliente.getSesion().getPresupuesto()-self.facturaTemp.getTotal())
            Cliente.getSesion().getPanaderia().setDinero(Cliente.getSesion().getPanaderia().getDinero()+self.facturaTemp.getTotal())
            Cliente.getSesion().appendRecibos(self.facturaTemp)
            Cliente.getSesion().getCanastaOrden().setPagada(True)
            self.chequeoDeEstados()
            messagebox.showinfo("Información", "El pago de su factura ha sido exitoso, su nuevo saldo es de "+str(Cliente.getSesion().getPresupuesto())+"$$$")
            self.cambiarFrame(self.frameCocinar1)


    #Esto es para que el scroll funcione con la rueda del mouse
    def on_mousewheel(self, event):
        # Implementa la lógica de desplazamiento vertical
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def copiarOrden(self, id):
        id = int(id)
        for x in Cliente.getSesion().getRecibos():
            if x.getIdRecibo() == id:
                Cliente.getSesion().setCanastaOrden(copy.deepcopy(x.getCanasta())) #se crea una canasta exactamente igual y se asocia a la orden
                messagebox.showinfo("Informacion", "La canasta ha sido copiada con exito")
        

    def mostrarRankingCorrespondiente(self, values):
        try:
            
            if values[0].upper() == "COCINEROS" or values[0].upper() == "DOMICILIARIOS" or values[0].upper() == "PRODUCTOS" or values[0].upper() == "INGREDIENTES":
                
                if values[0].upper() == "COCINEROS":
                    imprimirCocinerosPorRanking(self.textEjecLoMejor, Cliente.getSesion().getPanaderia())

                elif values[0].upper() == "DOMICILIARIOS":
                    imprimirDomiciliariosPorRanking(self.textEjecLoMejor, Cliente.getSesion().getPanaderia())

                elif values[0].upper() == "PRODUCTOS":
                    imprimirProductosPorVecesVendidos(self.textEjecLoMejor, Cliente.getSesion().getPanaderia())

                elif values[0].upper() == "INGREDIENTES":
                    imprimirIngredientesPorVecesVendidos(self.textEjecLoMejor, Cliente.getSesion().getPanaderia())
            
            else:
                raise ProductoNoEncontradoError(values[0].upper)
            
        except ProductoNoEncontradoError as e:
            messagebox.showwarning("Error", "El Ranking ingresado no es válido, por favor ingrese alguna de las opciones indicadas")

# Codigo que produce la ejecucion de la ventana cuando se ejecuta desde este archivo
def main():
    root = Tk()
    app = VentanaPrincipal(root)
    root.mainloop()


if __name__ == "__main__":
    main()
