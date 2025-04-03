a=["matematicas", "fisica"]
b= a + ["web"]

def agragar_asignatura(lista,asig):
    return lista+[asig]

rspuesta= agragar_asignatura(a,input("agrega una materia: "))

print(rspuesta)