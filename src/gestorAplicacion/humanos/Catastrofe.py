import random

class Catastrofe:
    """
    Clase que representa una catástrofe en el contexto de una aplicación de gestión de humanos.
    """

    fallos_cocina = ["El producto se quemó", "El cocinero se cortó un dedo", "El producto se pudrió", "Hubo un incendio", "El cocinero está triste", "Encontramos un pelo en la comida"]

    def __init__(self):
        """
        Inicializa una instancia de la clase Catastrofe.

        Atributos:
        - _maldad: nivel de maldad de la catástrofe (entero entre 1 y 10).
        - _dineroRobado: cantidad de dinero robado durante la catástrofe (entero).
        """
        self._maldad = random.randint(1, 10)  # 1 <= maldad <= 10
        self._dineroRobado = 0
        
    def getMaldad(self):
        """
        Devuelve el nivel de maldad de la catástrofe.

        Returns:
        - Nivel de maldad de la catástrofe (entero).
        """
        return self._maldad
    
    def setMaldad(self, maldad):
        """
        Establece el nivel de maldad de la catástrofe.

        Parameters:
        - maldad: nivel de maldad de la catástrofe (entero entre 1 y 10).
        """
        self._maldad = maldad
        
    def dificultadProducto(self, cocinero):
        """
        Comprueba si el cocinero puede manejar la dificultad de la catástrofe.

        Parameters:
        - cocinero: instancia de la clase Cocinero.

        Returns:
        - True si el cocinero puede manejar la dificultad de la catástrofe, False en caso contrario.
        """
        if cocinero._habilidad < self._maldad:
            cocinero._fallado = False
            return True
        return False
    
    def robarComprador(self, rival):
        """
        Intenta robar al comprador rival durante la catástrofe.

        Parameters:
        - rival: instancia de la clase Comprador.

        Returns:
        - rival: instancia de la clase Comprador actualizada después del intento de robo.
        """
        if self.getMaldad() > rival.getHabilidad():
            rival.setRobado(False)
            self._dineroRobado += rival.getDineroEnMano()
            rival.setDineroEnMano(0)
        else:
            rival.setRobado(True)
        
        return rival

    def paradaTransito(self, domiciliario):
        if self.getMaldad > domiciliario.getHabilidad():