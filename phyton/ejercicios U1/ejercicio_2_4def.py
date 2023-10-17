#1.4 => NO recibe parámetros y retorna la temperatura convertida en grados Celsius. Dentro de la función se pedirá al usuario los grados Farenheit.
def temp (F):
    celsius = float(input("Dame una temperatura en grado Farenheit:"))
    fah = (celsius - 32) * 5/9
    return "la temperatura en Celsius es " + str(round(fah,2))
F = 0
print(temp(F))