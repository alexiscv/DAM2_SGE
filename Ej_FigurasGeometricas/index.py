# Instanciamos un Obj. Logica, que contendrá métodos genericos
logica = Logica()

# Repetir hasta elegir Salir
op = logica.menu()

while( op != 0 ):
    if (op == 1):
        print "NUEVO ALTA"
