def alinear(a1, a2, a3):
    textos = [str(a1), str(a2), str(a3)]
    espaciados = [35, 10, 10]
    s = ""
    
    for i in range(3):
        if espaciados[i] - len(textos[i]) > 0:
            s += textos[i] + " " * (espaciados[i] - len(textos[i]))
        else:
            s += textos[i] + " "
    
    return

def centrar(a1):
    s = ""
    espaciado = 55
    
    if (espaciado - len(a1)) / 2 > 0:
        s += " " * int((espaciado - len(a1)) / 2) + str(a1) + " " * int((espaciado - len(a1)) / 2)
        return s
    else:
        return a1