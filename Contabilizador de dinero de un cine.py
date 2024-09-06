totalfun = 0
funcióndesc = 0
funciónsindesc = 0
espectadordesc = 0
entradadesc = 3500
entradasindesc = 5000
recaudacióntotal = 0
espectadores = int (input("Ingrese la cantidad de espectadores de la función o 0 para finalizar: "))
while espectadores != 0:
    función = int (input("¿La función tenía descuento? (1 para sí y 2 para no): "))
    totalfun = totalfun + 1
    if función == 1:
        funcióndesc = funcióndesc + (entradadesc * espectadores)
        espectadordesc = espectadordesc + espectadores
    if función == 2:
        funciónsindesc = funciónsindesc + (entradasindesc * espectadores)
    espectadores = int (input("Ingrese la cantidad de espectadores de la función o 0 paara finalizar: "))
porcentaje = espectadordesc * totalfun / 100
recaudacióntotal = funcióndesc + funciónsindesc
print ("Recaudación total: ", recaudacióntotal, "Espectadores con descuentos: ", espectadordesc, "Porcentaje que representan los espectadores con descuento: ", porcentaje)