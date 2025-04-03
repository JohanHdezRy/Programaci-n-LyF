#Ejemplo1 inmutailidad, funciones puras y sin efectos secundarios
variable_global= 10

def aumentar_variable():
    return variable_global + 1
print(aumentar_variable()) 

#Ejemplo2 inmutailidad, funciones puras y sin efectos secundarios
def contar_palabras(texto):
    return len(texto.split())

oracion = "El tema de hoy es inmutabilidad"
print(contar_palabras(oracion))

#Ejemplo3 uso incorrecto de la funcion pura
contador_global = 0

def contar_palabras_no_funcional(texto):
    global contador_global
    contador_global = len(texto.split())

texto_ejemplo = "Este es un ejemplo sencillo"
contar_palabras_no_funcional(texto_ejemplo)
print(contador_global)

#mutable
#contar_palabras_no_funcional(texto_ejemplo)