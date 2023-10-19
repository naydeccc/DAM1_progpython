numero = int(input("ingresa un numero: "))
numerotexto = str(numero) +"! => " + str(numero) + " X "
numeroprincipal = 0
numerosuma = numero * (numero-1)
numero = numero - 1
while numero > 2:
    numerosuma = numerosuma * (numero-1)
    numerotexto = numerotexto + str(numero) + " X "
    numeroprincipal = numerosuma + numeroprincipal
    numero = numero - 1
numerotexto = numerotexto + str(numero) + " X "
numerotexto = numerotexto + str(numero-1)
print(numerotexto + " = " + str(numeroprincipal)) 