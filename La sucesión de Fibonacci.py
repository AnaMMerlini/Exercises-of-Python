número = 0
suma = 0
acumulador = 0
númerodos = 1
cantidad = 0
contador = 1
cantidad = int (input("ingresar un número: "))
print ("suma: ", número)
while (contador < cantidad):
    número = númerodos
    númerodos = suma
    suma = número + númerodos
    acumulador = acumulador + suma
    contador = contador + 1
    print ("suma: ", suma)
print ("acumulador: ", acumulador)