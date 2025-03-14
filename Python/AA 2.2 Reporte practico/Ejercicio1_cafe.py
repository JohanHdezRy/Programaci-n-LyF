def cafe():
    return "Café"

def ordenar_cafe(numero_tazas):
    tazas_cafe = [cafe() for _ in range(numero_tazas)]
    return tazas_cafe
#cadena = ["hola"+ "que hace" for _ in range(3)]

#cafe_grupo = ordenar_cafe

cafe_grupo = ordenar_cafe(int(input("ingresa las tazas de cafe: ")))
print(cafe_grupo)