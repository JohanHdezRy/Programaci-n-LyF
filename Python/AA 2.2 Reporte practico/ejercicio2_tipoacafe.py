def preparar_cafe_ame():
    return "cafe americano"

def preparar_cafe_olla():
    return "cafe olla"

def ordenar_cafe(preparar_cafe, numero_tazas):
    tazas_cafe = [preparar_cafe() for _ in range(numero_tazas)]
    return tazas_cafe

cafe_grupoa =ordenar_cafe(preparar_cafe_olla ,(int(input("ingresa las tazas que quieres: "))))
cafe_grupob =ordenar_cafe(preparar_cafe_ame, (int(input("ingresa las tazas que quieres: "))))

print(cafe_grupoa)
print(cafe_grupob)