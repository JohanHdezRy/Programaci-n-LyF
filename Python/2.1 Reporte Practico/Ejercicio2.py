#tipo de datos 
#colecciones
#listas
lista = [1,2,3,4,5]
print(lista)
print(lista[0])#imprime el primer elemento de la lista
print(lista[1])

#tuplas
tupla=(1,2,3,4,5)
print(tupla)
print(tupla[0])#imprime el primer elemento de la tupla
print(tupla[1])

#diccionarios
diccionario = {'nombre':'Juan','edad':22}
print(diccionario)
print(diccionario['nombre'])#imprime el valor de la clave nombre
print(diccionario['edad'])

#conjuntos
conjunto = {1,2,3,4,5}
print(conjunto)

#convertir cadenaa enteros
numero = int("10")
print(numero)

#convertir cadenas a flotantes
numero = float("10.5")
print(numero)

#convertir enteros a cadenas
numero = str(10)
print(numero)

#convertir flotantes a cadenas
numero = str(10.5)
print(numero)

#convertir enteros a flotantes
numero = float(10)
print(numero)

#operaciones aritmeticas
num1 = int (input("Ingrese un numero: "))
num2 = int (input("Ingrese otro numero: "))
print("Suma: ", num1 + num2)
print("Resta: ", num1 - num2)
print("Multiplicacion: ", num1 * num2)
print("Division: ", num1 / num2)

#operacione relacionales
num1 = int (input("Ingrese un numero: "))
num2 = int (input("Ingrese otro numero: "))
print ("El primer numero es mayor que el segundo?: ", num1 > num2)
print ("El primer numero es menor que el segundo?: ", num1 < num2)
print ("El primer numero es mayor o igual que el segundo?: ", num1 >= num2)
print ("El primer numero es menor o igual que el segundo?: ", num1 <= num2)
print ("El primer numero es igual la segundo?: ", num1 == num2)
print ("El primer numero es diferente que el segundo?: ", num1 != num2)

#operaciones logicas
print("Operaciones logicas")
print("True and True: ", True and True)
print("True and False: ", True and False)
print("False and True: ", False and True)
print("False and False: ", False and False)
print("True or True: ", True or True)
print("True or False: ", True or False)
print("False or True: ", False or True)
print("False or False: ", False or False)
print("Not True: ", not True)
print("Not False: ", not False)

#operaciones de asignacion
num1=10
num1 +=5
print(num1)
num1 -=5
print(num1)
num1 *=5
print(num1)
num1 /=5
print(num1)
num1 %=5
print(num1)
num1 **=5 #exponente
print(num1)
num1 //=5 #division
print(num1)

#operaciones de pertenencia
lista = [1,2,3,4,5]
print(1 in lista)
print(6 in lista)
print(1 not in lista)
print(6 not in lista)

aprobado = float(input("Ingrese su calificacion: "))>=70
print("Aprobaste?: ", aprobado)