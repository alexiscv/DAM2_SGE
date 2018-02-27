# Creamos un diccionario
d = {}

# Mostrar menú
def menu() :
    print("## MENÚ ##")
    print("1) Añadir término")
    print("2) Buscar definición")
    print("0) Salir")

    print("Que desea hacer:")
    opcion = int(input())
    return opcion;

# Mostramos la primera vez el menú
# y recogemos la opción seleccionada
op = menu()

# Ejecutamos hasta que queramos salir
while( op != 0 ):
    # Ejecutamos la acción seleccionada
    # Añadir
    if( op == 1):
        # Preguntamos por los datos del termino
        print("Nombre del termino:")
        termino = input()
        print("Definición:")
        definicion = input()

        # Añadimos al diccionario
        d[termino] = definicion

    # Buscar
    elif( op == 2):
        # Preguntamos por el término
        print("Nombre del termino:")
        termino = input()

        # Retornamos la Definición
        print(d[termino])

    else:
        print("ERROR: Opción no reconocida");

    # La acción ya se ha ejecutado
    # Volvemos a mostrar el menú
    op = menu()

# Cuando salgamos, mostramos todo el diccionario
print(d)
