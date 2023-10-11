#inicio
#   inicio = int(input("dame el numero de inicio de la serie:"))
#   incremento = int(input("dame el numero de incremento de la serie:"))
#   total = int(input("dame el numero total de la serie:"))
#   if incremento < 0:
#       while (incremento < 0):
#           incremento = int(input("dame un numero POSITIVO de incremento de la serie:"))
#   if total < 0:
#       while (total < 0):
#           total = int(input("dame un numero POSITIVO de total de la serie:"))
#   serie = str("serie=>" + str(inicio) + "-")
#   cont = inicio
#   while( cont <= total):
#       inicio = inicio + incremento
#       cont = cont + incremento
#       if cont < (total-1):
#           serie =str(serie + str(inicio) + "..")
#       else:
#           if cont == (total - 1):
#               serie =str(serie + str(inicio))
#               inicio = inicio + incremento
#               serie= str(serie) + "-" + str(inicio)
#               print(serie)
# final

inicio = int(input("dame el numero de inicio de la serie:"))
incremento = int(input("dame el numero de incremento de la serie:"))
total = int(input("dame el numero total de la serie:"))
if incremento < 0:
    while (incremento < 0):
        incremento = int(input("dame un numero POSITIVO de incremento de la serie:"))
if total < 0:
    while (total < 0):
        total = int(input("dame un numero POSITIVO de total de la serie:"))

#while incremento < 0 or total < 0: posible mejora  
#    print("funciona")
serie = str("serie=>" + str(inicio) + "-")
cont = 1
while( cont < total):
    inicio = inicio + incremento
    cont = cont + 1
    if cont < (total-1):
        serie =str(serie + str(inicio) + "..")
    else:
        if cont == (total - 1):
            serie =str(serie + str(inicio))
            inicio = inicio + incremento
            serie= str(serie) + "-" + str(inicio)
            print(serie)