# Función que solicita datos al usuario y llama a un callback para validarlos
def solicitar_datos(callback):
    dato = input("Ingresa un número positivo: ")
    if callback(dato): 
        print("Dato válido. Procesando...")
    else:
        print("Dato inválido. Intenta de nuevo.")

# Callback para validar si el dato es un número positivo
def validar_dato(dato):
    try:
        numero = float(dato)
        return numero > 0  # Retorna True si es un número positivo
    except ValueError:
        return False  # Retorna False si no es un número válido

# Llamar a la función solicitar_datos y pasar el callback
solicitar_datos(validar_dato)