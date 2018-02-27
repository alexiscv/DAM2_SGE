# Clase con métodos genericos
class Logica():

    # Mostrar ménu, devuelve la opción elegida
    def menu():
        print "Introduce una opcion:"
        print "1 - Alta"
        print "2 - Area"
        print "3 - Perimetro"
        print "4 - Mostrar"
        print "0 - Salir"

        op = int(input())
        return op
