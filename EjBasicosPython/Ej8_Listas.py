# Preguntamos el n de elementos a almacenar
print("¿Cuantos elementos quieres almacentar en la lista?");
n = int(input())

# Creamos nuestra lista
lista = []

# Vamos preguntando y almacenando los n elementos
for i in range(0,n):
    print("Introduce el dato...");
    lista.append(input())

# Ahora mostramos el contenido de la lista
print ("Esta es la lista de inscritos: " + str(lista))

# Imprimir en orden inverso
for i in range(0,n):
    valor = n-i
    print("Valor["+str(valor)+"] => "+str(lista[valor-1]))

# Para saber la posición de un valor
posicionPaco = lista.index("Paco")
print("Paco está en la posición "+str(posicionPaco))
