#inicio
#   escribe "dame el numero de inicio de la serie:"
#   lee inicio
#   escribe "dame el numero de incremento de la serie:"
#   lee incremento
#   escribe "dame el numero total de la serie:"
#   lee total
#   si incremento menor que 0 entonces
#       mientras incremento menor que 0 entonces
#           escribe "dame un numero POSITIVO de incremento de la serie:"
#           lee incremento
#   si total menor que 0 entonces
#       mientras total menor que 0 entonces
#           escribe "dame un numero POSITIVO de total de la serie"
#           lee total
#   serie = "serie=>" + inicio + "-"
#   cont = 1
#   mientras cont menor que total entonces
#       inicio = inicio + incremento
#       cont = cont + 1
#       si cont menor que (total-1) entonces
#           serie =serie + inicio + ".."
#       si no entonces
#           si cont sea igual (total - 1) entonces
#               serie = serie + inicio
#               inicio = inicio + incremento
#               serie= serie + "-" + inicio
#               escribe serie
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