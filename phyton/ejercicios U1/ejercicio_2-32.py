# Ejercicio 1.32 - Lee dos números y crea la serie que los une de 1 en 1...
#
#
#> Introduce un número: 4
#> Introduce otro: 8
#> 4-5-6-7-8
#
#> Introduce un número: 12
#> Introduce otro: 3
#> 3-4-5-6-7-8-9-10-11-12
#
#Inicio
#
#	Escribe "Introduce un número: "
#	Lee x
#	Escribe "Introduce otro: "
#	Lee y
#	
#	Si (x >= y) entonces
#		numIni = x
#		numFin = y
#	Sino
#		numIni = y
#		numFin = x
#		
#	Mientras (numIni <= numFin) hacer
#		Escribe numIni
#		Si (numIni != numFin) entonces
#			Escribe "-"
#                numIni = numIni + 1
#
#Fin
# Ejercicio 1.32 - Lee dos números y crea la serie que los une de 1 en 1...
#

x = int(input("Introduce un número: "))
y = int(input("Introduce otro: "))
serie =""
if (x <= y):
	numIni = x
	numFin = y
else:
	numIni = y
	numFin = x
while (numIni <= numFin):
    if (numIni != numFin):
        serie = serie + str(numIni) + "-"
    numIni = numIni + 1
serie = serie + str(numFin)
print(serie)