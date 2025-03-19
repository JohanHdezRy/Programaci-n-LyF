def aplicar_operacion(lista, operacion):
    return [operacion(num) for num in lista]

def duplicado(numero):
    return numero * 2

numeros = [1, 2, 3, 4]
resultado = aplicar_operacion(numeros, duplicado)