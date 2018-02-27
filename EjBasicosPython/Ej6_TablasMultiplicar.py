# Tabla de multiplicar del 1 al 12
for value in range(1,13):
    print("# TABLA DEL "+str(value))

    # Generamos la tabla del "value": 1,2,3 ...
    for n in range(1,11):
        resultado = value*n;
        print(str(value)+"*"+str(n)+"="+str(resultado))

    print("--- Fin Tabla ---")
