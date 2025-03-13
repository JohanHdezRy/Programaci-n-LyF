#programa que simula el lanzamiento de una moneda
import random
num = random.randint(0,1)
if num == 0:
    print('Cara')
else:
    print('Cruz')

#promgrama que simula la bola magica
import random

pregunta = input("pregunta: ")
numero_aleratorio = random.randint(1, 9)

if numero_aleratorio ==1:
    respuesta = "si - definitivamente"
elif numero_aleratorio ==2:
    respuesta = "Esta decidido"
elif numero_aleratorio ==3:
    respuesta = "sin duda"
elif numero_aleratorio ==4:
    respuesta = "Respuesta confusa, intenta de nuevo"
elif numero_aleratorio ==5:
    respuesta = "Pregunta mas tarde"
elif numero_aleratorio ==6:
    respuesta = "Mejor no te digo"
elif numero_aleratorio ==7:
    respuesta = "mis fuentes dicen que no"
elif numero_aleratorio ==8:
    respuesta = "No parece bueno"
elif numero_aleratorio ==9:
    respuesta = "Muy dudoso"
else:
    respuesta = "Error"

print("Bola magica dice: ", respuesta)