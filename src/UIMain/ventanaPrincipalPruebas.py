from tkinter import *
import tkinter as tk

#Esta clase la cree yo (Richard), diganme si van a hacer algun cambio o si tienen alguna sugerencia

class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Ventana principal")
        self.root.geometry("1000x800")

        # Lista que va a contener todos los frames para facilitar el cambio entre estos
        self.frames = [] #lista de todos los frames necesaria para el metodo cambiarFrame

        # Creacion de los frames:

        # frameSesion inicio de sesion
        self.frameSesion = Frame(
        self.root, bd=1, relief=FLAT, padx=1, pady=1) 
        self.frames.append(self.frameSesion) #agregando a la lista de frames, necesaria para cambiar entre frames metodo cambiarFrame
        self.frameSesion.pack()
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
        self.frameRegistro = Frame(
        self.root, bd=1, relief=FLAT, padx=1, pady=1, bg="white")
        self.frames.append(self.frameRegistro)



        # frame2 menu principal
        self.framePrincipal = Frame(
        self.root, bd=1, relief=FLAT, padx=1, pady=1, bg="white")
        self.frames.append(self.framePrincipal)
        self.labelp1 = Label(self.framePrincipal, text="Bienvenido a pooBakery, este es el menu")
        self.labelp1.pack()

        # Menú superior del menu principal
        self.menu_principal = tk.Menu(self.root)

        menu_archivo = tk.Menu(self.menu_principal, tearoff=0)
        menu_archivo.add_command(label="Aplicación", command=self.mostrar_info)
        menu_archivo.add_command(label="Salir", command=self.salir)
        self.menu_principal.add_cascade(label="Archivo", menu=menu_archivo)

        menu_procesos = tk.Menu(self.menu_principal, tearoff=0)
        # Agregar procesos y consultas a menu_procesos
        # ...
        self.menu_principal.add_cascade(label="Procesos y Consultas", menu=menu_procesos)

        menu_ayuda = tk.Menu(self.menu_principal, tearoff=0)
        menu_ayuda.add_command(label="Acerca de", command=self.mostrar_autores)
        self.menu_principal.add_cascade(label="Ayuda", menu=menu_ayuda)

        self.root.config(menu=self.menu_principal)

        # frameInfo frame con informacion
        self.frameInfo = Frame(self.root, bd=1, relief=FLAT, padx=1, pady=1, bg="white")
        self.frames.append(self.frameInfo)
        informacion = ""
        self.textoInfo = tk.Text(self.frameInfo, height=10, width=50)
        self.textoInfo.insert(tk.END, informacion)
        self.textoInfo.config(state="disabled")
        self.textoInfo.pack()
        self.infoBoton = Button(self.frameInfo, text="Volver atras", command= self.volverAtras)

        # framef1 funcionalidad 1
        self.frameF1 = Frame(self.root, bd=1, relief=FLAT, padx=1, pady=1, bg="white")
        self.frames.append(self.frameF1)



        # framef2 funcionalidad 2
        self.frameF2 = Frame(self.root, bd=1, relief=FLAT, padx=1, pady=1, bg="white")
        self.frames.append(self.frameF2)



        # framef3 funcionalidad 3
        self.frameF3 = Frame(self.root, bd=1, relief=FLAT, padx=1, pady=1, bg="white")
        self.frames.append(self.frameF3)



        # framef4 funcionalidad 4
        self.frameF4 = Frame(self.root, bd=1, relief=FLAT, padx=1, pady=1, bg="white")
        self.frames.append(self.frameF4)



    #Metodos necesiarios para la interfaz de usuario
    def iniciar_sesion(self):
        #aqui deberia haber algun condicional para ver si el usuario si existe
        self.cambiarFrame(self.framePrincipal)
    
    def mostrar_info(self):
        self.informacion = "Informacion del programa"
        self.cambiarFrame(self.frameInfo)
        pass

    def mostrar_autores(self):
        self.informacion = "Los autores"
        self.cambiarFrame(self.frameInfo)
        pass

    def salir(self):
        self.root.destroy()

    def cambiarFrame(self, frame):
        self.frameActual = frame
        for f in self.frames:
            if f == frame:
                f.pack()
            else:
                f.pack_forget()
    
    def volverAtras(self):
        self.cambiarFrame(self.frameActual)


# Codigo que produce la ejecucion de la ventana cuando se ejecuta desde este archivo
def main():
    root = Tk()
    app = VentanaPrincipal(root)
    root.mainloop()


if __name__ == "__main__":
    main()
