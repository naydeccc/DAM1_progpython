def precio(PV,IVA):
    VA = float(IVA) / 100 + 1
    PVP = float(PV) * float(VA)
    print ("el precio con iva es " + str(PV) + " X " + str(round(float(IVA), 2)) + "%")
    print ("el precio final es " + str(round(PVP, 2)) + " €")

PV = input("Dame el precio del producto: ")
IVA = input("dame el IVA del producto: ")
precio(PV, IVA)