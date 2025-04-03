juagdores = [
    {"nombre":"Brandon","edad":22},
    {"nombre":"Alana","edad":23},
    {"nombre":"oso","edad":24},
    {"nombre":"kafai","edad":25}
]

nombres_jugadores = list(map(lambda jugador: jugador["nombre"],juagdores))
print(nombres_jugadores)