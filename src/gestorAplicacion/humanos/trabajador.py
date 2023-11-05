from ABC import ABC, abstractmethod
import random

class Trabajador(ABC):
    
    def __init__(self):
        self.nombre = "John Doe"
        self.habilidad = random.randint(1, 10)
        self.calificacion = 0
        self.dineroEnMano = 0
        self.salario = 1_000
        self.robado = False
        self.panaderia = None

    def getNombre(self):
        return self.nombre
    
    def getHabilidad(self):
        return self.habilidad
    
    def getCalificacion(self):
        return self.calificacion
    
    def getDineroEnMano(self):
        return self.dineroEnMano
    
    def getSalario(self):
        return self.salario
    
    def getRobado(self):
        return self.robado
    
    def getPanaderia(self):
        return self.panaderia
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def setHabilidad(self, habilidad):
        self.habilidad = habilidad

    def setCalificacion(self, calificacion):
        self.calificacion = calificacion

    def setDineroEnMano(self, dineroEnMano):
        self.dineroEnMano = dineroEnMano

    def setSalario(self, salario):
        self.salario = salario
    
    def setRobado(self, robado):
        self.robado = robado
    
    def setPanaderia(self, panaderia):
        self.panaderia = panaderia
    
    @abstractmethod
    def laborParticular(self, canasta):
        pass

    @abstractmethod
    def conseguir_ingredientes(self, listingredientes):
        pass


