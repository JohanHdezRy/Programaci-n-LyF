from functools import reduce

juagdores = [
    {"nombre":"Brandon","edad":22},
    {"nombre":"Alana","edad":23},        
    {"nombre":"oso","edad":24},
    {"nombre":"kafai","edad":25}
]

lambda acumulador, jugador: acumulador + jugador["edad"],juagdores,0

sumaEdad=reduce(lambda acumulador, jugador: acumulador + jugador["edad"],juagdores,0)

print(sumaEdad)