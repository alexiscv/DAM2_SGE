# Solitamos un número
print("Introduce un numero")
n=int(input())

# Creamos un bucle de 1 a n
for i in range(1,n+1):
    # Sumamos el valor de i + n
    suma = i+n;

    # Los mostramos
    print("La suma de "+str(i)+"+"+str(n)+"="+str(suma))
