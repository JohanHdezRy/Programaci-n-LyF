#ejemplo de callback

"""def operar (n1,n2, funcion):
    return funcion(n1,n2)

def suma(a,b):
    return a+b

def resta(a,b,):
    return a-b

resultado = operar(5,3,suma)
print(resultado) """

#ejemplo de funcion primera clase

# def saludo():
#     return "Hola"

# variable = saludo()
# print(variable)

# def saludo2():
#     return "Que tal"

# variable = saludo2
# print(variable())

#ejemplo de funcion de orden superior

# def elegir_operacion(operacion):
#     def multiplicar(x):
#         return x*2
#     def dividir(X):
#         return X/2
    
#     if operacion == "multiplicar":
#         return multiplicar
#     else:
#         return dividir
    
# double = elegir_operacion("multiplicar")
# print(double(10))
# divide2 = elegir_operacion("dividir")
# print(divide2(10))

#ejemplo de funcion anonima = lambda

double = lambda x: x*2
print(double(5))

numeros = [1,2,3,4]
doubles = list(map(lambda x: x*2, numeros))
print(doubles)

almunnos =['Alejandro','Miguel','Vinicio','Rodney','Marcial']
saludar_alumnos = list(map(lambda nombre: "hola" + nombre,almunnos))
print(saludar_alumnos)

#sin lambda

def saludar(nombre):
    return "Hola " + nombre

lista_saludos = list(map(saludar,almunnos))
print(lista_saludos)

