def pizza():
    return "🍕"

def hamburguesa():
    return "🍔"

def hotdog():
    return "🌭"

def bonus(num_porciones):
    if (num_porciones > 2):
        return "Coca gratis:🥤"
    else:
        return ""

def ordenar_alimento(preparar_alimento, num_porciones):
    porciones = [preparar_alimento() for _ in range(num_porciones)]
    bonuw = bonus(num_porciones)
    return porciones, bonuw

grupoa= ordenar_alimento(pizza, (int(input("ingresa las porciones de pizza: "))))
grupob= ordenar_alimento(hamburguesa, (int(input("ingresa las porciones de hamburguesa: "))))
grupoc= ordenar_alimento(hotdog, (int(input("ingresa las porciones de hotdog: "))))

print(grupoa)
print(grupob)
print(grupoc)


