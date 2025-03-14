def pan():
    return "🧇"

def numero_p(piezas_p):
    piezas_p = [pan() for _ in range(piezas_p)]
    return piezas_p

numero_p = numero_p(int(input("ingreas el num de piezas: ")))
print(numero_p)