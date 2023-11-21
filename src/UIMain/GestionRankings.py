
from operator import attrgetter

def ordenarCocinerosPorRanking(panaderia):
    cocineros_ordenados = sorted(panaderia.getCocineros(), key=attrgetter('calificacion'), reverse=True)
    return cocineros_ordenados

def ordenarDomiciliariosPorRanking(panaderia):
    domiciliarios_ordenados = sorted(panaderia.getDomiciliarios(), key=attrgetter('calificacion'), reverse=True)
    return domiciliarios_ordenados

def imprimirCocinerosPorRanking(self):
        cocineros_ordenados = ordenarCocinerosPorRanking(self)
        for cocinero in cocineros_ordenados:
            print(f"{cocinero.getNombre()} - Calificación: {cocinero.getCalificacion()}")
def imprimirDomiciliariosPorRanking(self):
    domiciliarios_ordenados = ordenarDomiciliariosPorRanking(self)
    for domiciliario in domiciliarios_ordenados:
        print(f"{domiciliario.getNombre()} - Calificación: {domiciliario.getCalificacion()}")