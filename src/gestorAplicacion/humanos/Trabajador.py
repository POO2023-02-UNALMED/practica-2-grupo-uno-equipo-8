import random
from abc import ABC, abstractmethod
from gestorAplicacion.gestion.Canasta import Canasta

class Trabajador(ABC):
    def __init__(self, panaderia, nombre="John Doe", calificacion=0, dinero_en_mano=0, salario=1000):
        self.nombre = nombre
        self.habilidad = random.randint(9, 19)  # 9 <= habilidad <= 19
        self.calificacion = calificacion
        self.dinero_en_mano = dinero_en_mano
        self.salario = salario
        self.robado = True
        self.panaderia = panaderia
        if panaderia:
            panaderia.getTrabajadores().append(self)

    @abstractmethod
    def laborParticular(self, canasta: Canasta):
        pass

    @abstractmethod
    def conseguirIngredientes(self, listingredientes):
        pass


    # Getters y setters
    def getNombre(self):
        return self.nombre

    def getHabilidad(self):
        return self.habilidad

    def getCalificacion(self):
        return self.calificacion

    def getDineroEnMano(self):
        return self.dinero_en_mano

    def getSalario(self):
        return self.salario

    def setNombre(self, nombre):
        self.nombre = nombre

    def setHabilidad(self, habilidad):
        self.habilidad = habilidad

    def setCalificacion(self, calificacion):
        self.calificacion = calificacion

    def setDineroEnMano(self, dinero_en_mano):
        self.dinero_en_mano = dinero_en_mano

    def setSalario(self, salario):
        self.salario = salario

    def isRobado(self):
        return self.robado

    def setRobado(self, robado):
        self.robado = robado