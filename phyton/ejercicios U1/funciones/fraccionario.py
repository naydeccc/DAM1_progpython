def factorialstr(numero: int):
    numerotexto = str(numero) +"! => " + str(numero) + " X "
    while numero > 2:
        numero -= 1
        numerotexto += str(numero) + " X "
    numerotexto += str(numero - 1) + " = "
    return numerotexto


def factorial(numero: int):
    total = 1
    while numero > 1:
        total *= numero
        numero -= 1
    return total
numero = int(input("introduce un numero: "))
print(str(factorialstr(numero)) ) 