pesoPayaso = 112
pesoMuneca = 75
numeroPayaso= float(input("cuantos payasos habia en el ultimo pedido: "))
numeroMuneca= float(input("cuantos muñecas habia en el ultimo pedido: "))
pesoTotalmunecas = numeroMuneca * pesoMuneca
pesoTotalPayasos = numeroPayaso * pesoPayaso
pesoTotalTotal = pesoTotalmunecas + pesoTotalPayasos
print(f"el peso total del ultimo pedido es: {pesoTotalTotal}")