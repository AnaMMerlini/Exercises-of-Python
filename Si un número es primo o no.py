divisor = 2
numero = int (input ("Ingrese un número natural: "))
if numero <=0:
    print ("error")
esPrimo = True
while divisor < numero and esPrimo == True:
    resto = numero % divisor
    if resto == 0:
        esPrimo = False 
    divisor = divisor + 1
if esPrimo == False:
    print ("número no primo")
else:
    print ("número primo")