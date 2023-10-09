PV = input("Dame el precio del producto: ")
IVA = input("dame el IVA del producto: ")
IVA = (int(IVA) / 100) + 1
PVP = float(PV) / float(IVA)

print(f"El iva es {IVA} % , el importe sin via es {round(PVP,2)}.")