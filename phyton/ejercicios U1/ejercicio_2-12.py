KG = input("dame cuanto pesas en kg:")
AL = input("dame tu estatura en metros:")
MC = int(KG) / (float(AL)**2)
print("Tu índice de masa corporal es donde es" + str(round(MC,2)))