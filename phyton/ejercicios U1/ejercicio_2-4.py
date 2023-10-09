celsius = float(input("Dame una temperatura en grado celsius:"))
print("tu numero en grado celsius es:" + str(round(celsius,2)))
fah = (celsius * 9 / 5) + 32
print("La temperatura en grados Farenheit es " + str(round(fah,2)) + " 10ºF (" + str(round(celsius,2)) + " ºC)")