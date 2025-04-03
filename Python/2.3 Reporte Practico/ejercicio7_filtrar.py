juagdores = [
    {"nombre":"Brandon","edad":22},
    {"nombre":"Alana","edad":23},       
    {"nombre":"oso","edad":24},
    {"nombre":"kafai","edad":25}
]
juagdores_mayores = list(filter(lambda jugador: jugador["edad"] > 23,juagdores))
print(juagdores_mayores)