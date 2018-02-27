import math

# Mostrar ménu, devuelve la opción elegida
def menu():
    print ("Introduce una opcion:")
    print ("1 - Alta")
    print ("2 - Area")
    print ("3 - Perimetro")
    print ("4 - Mostrar")
    print ("0 - Salir")

    op = int(input())
    return op

#########################################
#   Clase Principal
#########################################

# Clase FIGURA
class Figura():
    # Constructor
    def __init__(self, area, perimetro):
        self.area = -1
        self.perimetro = -1

    def mostrar(self):
        return "[Area="+str(self.area)+", Perimetro="+str(self.perimetro)+"]"

#########################################
#   Clases con herencia
#########################################

# Clase Triangulo, hereda de Fígura
class Triangulo(Figura):
    def __init__(self):
        Figura.__init__(self)
        self.lado1 = 0.0
        self.lado2 = 0.0
        self.lado3 = 0.0
        self.altura = 0.0

    def alta(self):
        print "Introduce la base:"


#########################################
#   PROGRAMA
#########################################

# Repetir hasta elegir Salir
op = menu()

while( op != 0 ):
    if (op == 1):
        print ("NUEVO ALTA")
