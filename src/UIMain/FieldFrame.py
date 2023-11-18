from tkinter import *
from ErrorAplicacion import CamposVaciosError
from tkinter import messagebox
class FieldFrame(Frame):

    # Esta clase sirve para crear frames genericos, se debe crear un objeto field frame y en el contructor se le debe ingresar como primer parametro el nombre que desea que 
    # tenga las etiquetas del parte izuquierda, por ejemplo "Valores" luego se le debera pasar una lista de strings con las etiquetas que se quieran llenar, por ejemplo ["Nombre:", "Cantidad:"]
    # luego se debe ingresar otro string que sera el titulo que ira encima de los entrys por ejemplo "Entradas", finalmente el constructor acepta dos parametros adicionales y opcionales,
    # se puede ingresar una lista con los vaalores que sean obligatorios en el inicio, por ejemplo, si en la lista de etiquetas se puso ["Nombre:", "Cantidad:"], en este parametro se 
    # podria pasar una lista ["string", "int"] esto indicara el tipo de valor que se puede ingresar en cada casilla, esto sirve para los errores, y el ultimo parametro que acepta es una lista
    # la cual contiene strings con el nombre de las etiquetas que desea inhabilitadas

    def __init__(self, tituloCriterios, criterios, tituloValores, valores = None, habilitado = None ):
        
        self.valores = []
        self.funcionAsociada = None
        self.entradas = []
        self.frame = Frame()
        self.frame.pack(anchor="c", ipadx=10, ipady=10)
        tituloC = Label(self.frame, text=tituloCriterios)
        tituloC.grid(row=0, column=0, padx=10, pady=10)
        tituloV = Label(self.frame, text=tituloValores)
        tituloV.grid(row=0, column=1, padx=10, pady=10)

        def eliminar():
            for p in self.entradas:
                p.delete(0, END)

        def adicionValida():
            
            entriesValues = []
            for l in self.entradas:
                entriesValues.append(l.get())
            self.valores = entriesValues

            try:
                self.verificar_campos_llenos(entriesValues)
            except CamposVaciosError as e:
                mensaje = f"Por favor, complete los campos: {len(e.campos_faltantes)}"
                messagebox.showwarning("Campos Vacíos", mensaje)
                eliminar()

        for k in criterios:
            cont = criterios.index(k)

            texto = Label(self.frame, text=k)
            texto.grid(row=cont+1, column=0, padx=10, pady=10)

            if valores != None:
                entrada = Entry(self.frame, textvariable=valores[k])
                entrada.grid(row=cont+1, column=1, padx=10, pady=10)
                self.entradas.append(entrada)

            else:
                entrada = Entry(self.frame)
                entrada.grid(row=cont+1, column=1, padx=10, pady=10)
                self.entradas.append(entrada)

            if habilitado != None:
                if k in habilitado:
                    entrada.config(state="disabled")

            if k == "Codigo" or k == "codigo":
                entrada.config(state="disabled")

        botonA = Button(self.frame, text="Aceptar", command=adicionValida)
        botonA.grid(row=len(criterios)+1, column=0, padx=10, pady=10)
        botonT = Button(self.frame, text="Borrar", command=eliminar)
        botonT.grid(row=len(criterios)+1, column=1, padx=10, pady=10)

    def defRoot(self, frame):
        self.frame.pack(in_=frame)

    def defFunc(self, funcion):
        self.funcionAsociada = funcion 

    def getFrame(self):
        return self.frame
    
    def getValores(self):
        if self.valores != []:
            return self.valores
        else:
            print("No hay valores")
    
    def verificar_campos_llenos(self, campos):
        campos_vacios = [campo for campo in campos if len(campo) == 0]
        if campos_vacios:
            raise CamposVaciosError(campos_vacios)