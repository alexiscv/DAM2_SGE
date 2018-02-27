# Realizamos las importaciones de la librería random
from random import randint, uniform, random

# Generamos un número aleatorio
n = randint(0,10);

# Comenzmaos el juego
# Es un bucle que solo se rompe al adivinar el valor de n
respuesta = -1

# Contador de intento
intentos = 0

while respuesta!=n:
    print("¿Cual crees que es el número aleatorio?")
    respuesta = int(input())

    if(respuesta > n):
        print("Te has pasado!")
        intentos = intentos+1

    elif ( respuesta < n):
        print("Un poco más...")
        intentos = intentos+1

    else:
        print("HAS ACERTADO!! El número es "+str(n))

print("Lo has intentanto: "+str(intentos)+" veces")
