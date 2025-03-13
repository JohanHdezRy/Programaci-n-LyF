#funcion con dato de entrada
def ordena_comida(x):
    if x == 1:
        return "Hamburguesa"
    elif x == 2:
        return "Papas Fritas"
    elif x == 3:
        return "Coca Cola"
    elif x == 4:
        return "Helado"
    elif x == 5:
        return "Galletas"
    else:
        return "Opcion no valida"

def bienvenido():
    print("Bienvenido al menu de comida")
    print("1. Hamburguesa")
    print("2. Papas Fritas")
    print("3. Coca Cola")
    print("4. Helado")
    print("5. Galletas")

bienvenido()

opcion = int(input("Ingrese la opcion de comida que desea: "))
print(ordena_comida(opcion))
    