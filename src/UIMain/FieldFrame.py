from tkinter import *

class FieldFrame(Frame):
  
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

        def eliminar(self):
            for p in self.entradas:
                p.delete(0, END)

        for k in criterios:
            cont = criterios.index(k)

            texto = Label(self.frame, text=k)
            texto.grid(row=cont+1, column=0, padx=10, pady=10)

            entrada = Entry(self.frame)
            entrada.grid(row=cont+1, column=1, padx=10, pady=10)
            entrada.insert(0, k)
            self.entradas.append(entrada)

            if habilitado != None:
                if k in habilitado:
                    entrada.config(state="disabled")

            if k == "Codigo" or k == "codigo":
                entrada.config(state="disabled")

        botonA = Button(self.frame, text="Aceptar")
        botonA.grid(row=len(criterios)+1, column=0, padx=10, pady=10)
        botonT = Button(self.frame, text="Borrar")
        botonT.grid(row=len(criterios)+1, column=1, padx=10, pady=10)

    def defRoot(self, root):
        self.frame.pack(in_=root)

    def defFunc(self, funcion):
        self.funcionAsociada = funcion 

    def getFrame(self):
        return self.frame
    
    def getValores(self):
        if self.valores != []:
            return self.valores
        else:
            print("No hay valores")
