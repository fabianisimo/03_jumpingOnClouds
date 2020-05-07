import random

def entrada_datos():
    largo_cadena = random.randint(2,20)
    cadena = []
    for i in range(largo_cadena):
        if i == 0 or i == largo_cadena-1:
            cadena.append(0)
        else:
            if i-1 > 0 and cadena[i-1] == 0:
                a = random.randint(0,1)
                cadena.append(a)
            else:
                cadena.append(0)
    return [largo_cadena, cadena]

datos = entrada_datos()
print (datos[0])
print (datos[1])

def jumpingOnClouds(c):
    saltos = 0
    i = 0
    while i < len(c):
        if i+2 < len(c) and c[i+2] == 0:
            i = i+2
        else: 
            i = i+1
        saltos = saltos + 1
    return saltos - 1

saltos = jumpingOnClouds(datos[1])
print (saltos)