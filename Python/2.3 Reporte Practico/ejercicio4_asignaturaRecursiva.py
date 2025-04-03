def agregar_asignatura(lista):
    pre=input("agrega una asignatura o escribe NO para salir: ")
    if pre == "NO":
        return lista
    return agregar_asignatura(lista + [pre])

asig= ["graficacion", "automatas", "web"]

nueva= agregar_asignatura(asig)

print(nueva)