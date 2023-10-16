#1.2 => recibe horas y coste y retorna el importe total.
def trabajo (HT , CH) :
    IT = CH * HT
    return IT

HT = float(input("Horas de trabajo: "))
CH = int(input("Coste por hora: "))

print("Importe total: " + str(trabajo(HT,CH)))