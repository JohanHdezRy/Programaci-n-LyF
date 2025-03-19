def multiplicador(factor):
    def multiplicar(numero):
        return numero * factor
    return multiplicar

duplicar = multiplicador(2)
print(duplicar(5)) 