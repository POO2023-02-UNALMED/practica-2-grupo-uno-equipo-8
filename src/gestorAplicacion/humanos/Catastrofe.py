import random

class Catastrofe:
    fallos_cocina = ["El producto se quemó", "El cocinero se cortó un dedo", "El producto se pudrió", "Hubo un incendio", "El cocinero está triste", "Encontramos un pelo en la comida"]

    def __init__(self):
        self._maldad = random.randint(1, 10)  # 1 <= maldad <= 10
        self._dinero_robado = 0
        
    def getMaldad(self):
        return self._maldad
    
    def setMaldad(self, maldad):
        self._maldad = maldad
        
    def dificultadProducto(self, cocinero):
        if cocinero._habilidad < self.maldad:
            cocinero._fallado = False
            return True
        return False
