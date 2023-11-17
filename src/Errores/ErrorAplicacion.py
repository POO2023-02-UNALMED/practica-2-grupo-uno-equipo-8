class ErrorAplicacion(Exception):
    def __init__(self, message="Error de Aplicación: "):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"Manejo de errores de la Aplicación: {self.message}"

class ErrorTipoA(ErrorAplicacion):
    def __init__(self, message="Error de Tipo A: "):
        super().__init__(message)

    def __str__(self):
        return super().__str__()

class CamposVaciosError(ErrorTipoA):
    def __init__(self, campos_faltantes):
        self.campos_faltantes = campos_faltantes
        super().__init__("Campos faltantes: {}".format(", ".join(campos_faltantes)))
        
""""
def verificar_campos_llenos(campos):
    campos_vacios = [campo for campo in campos if len(campo.get()) == 0]
    if campos_vacios:
        raise CamposVaciosError(campos_vacios)
        

# Ejemplo de uso
try:
    # Supongamos que "campos" es una lista que contiene los Entry de la interfaz
    campos = [entry1, entry2, entry3]  # Aquí deberías definir los Entry de tu interfaz
    verificar_campos_llenos(campos)
    # Si todos los campos están llenos, continuar con el resto de la lógica
    # ...
except CamposVaciosError as e:
    campos_faltantes = e.campos_faltantes
    mensaje = "Faltan los campos: {}".format(", ".join(campos_faltantes))
    messagebox.showerror("Error", mensaje)  # Muestra una ventana de error con los campos faltantes
""" #Este metodo o una logica parecida debe ir en la clase de la ventana

class ErrorSinPresupuesto(ErrorTipoA):
    def __init__(self, presupuesto_faltante):
        self.presupuesto_faltante = presupuesto_faltante
        super().__init__("Sin presupuesto suficiente")

""""
def verificar_presupuesto_suficiente(presupuesto_actual, gasto):
    if presupuesto_actual < gasto:
        raise ErrorSinPresupuesto(gasto - presupuesto_actual)

# Ejemplo de uso
presupuesto_disponible = 1000  # Aquí se simula un presupuesto
gasto_realizado = 1200  # Aquí se simula un gasto que supera el presupuesto

try:
    verificar_presupuesto_suficiente(presupuesto_disponible, gasto_realizado)
    # Si el presupuesto es suficiente, continuar con la lógica
    # ...
except ErrorSinPresupuesto as e:
    presupuesto_faltante = e.presupuesto_faltante
    mensaje = "Presupuesto insuficiente. Faltan: {}".format(presupuesto_faltante)
    messagebox.showwarning("Advertencia", mensaje)  # Muestra una ventana de advertencia
"""#Este metodo o una logica parecida debe ir en la clase de la ventana

class ErrorTipoA3(ErrorTipoA):
    def __init__(self, message="Error de Tipo A - 3: "):
        super().__init__(message)
        
class ErrorTipoB(ErrorAplicacion):
    def __init__(self, message="Error de Tipo B: "):
        super().__init__(message)

    def __str__(self):
        return super().__str__()
    
class UsuarioNoEncontradoError(ErrorTipoB):
    def __init__(self, usuario):
        self.usuario = usuario
        super().__init__("Usuario no encontrado")
        
""""
def verificar_existencia_usuario(usuario_ingresado, lista_usuarios):
    if usuario_ingresado not in lista_usuarios:
        raise UsuarioNoEncontradoError(usuario_ingresado)

# Ejemplo de uso
lista_usuarios_guardados = ["usuario1", "usuario2", "usuario3"]  # Simula la lista de usuarios guardados

usuario_ingresado = "usuario5"  # Simula el usuario ingresado en el Entry

try:
    verificar_existencia_usuario(usuario_ingresado, lista_usuarios_guardados)
    # Si el usuario existe, continuar con la lógica
    # ...
except UsuarioNoEncontradoError as e:
    usuario_no_encontrado = e.usuario
    mensaje = "El usuario '{}' no está guardado".format(usuario_no_encontrado)
    messagebox.showwarning("Error", mensaje)  # Muestra una ventana de advertencia
"""#Este metodo o una logica parecida debe ir en la clase de la ventana
    
class ErrorTipoB2(ErrorTipoB):
    def __init__(self, message="Error de Tipo B - 2: "):
        super().__init__(message)
        
class ErrorTipoB3(ErrorTipoB):
    def __init__(self, message="Error de Tipo B - 3: "):
        super().__init__(message)