def tiempo_cocina(callback):
    print("Cocinando...")
    # Simular tarea
    resultado = "Terminado"
    callback(resultado)

def notificar(resultado):
    print(f"Notificación: {resultado}")

tiempo_cocina(notificar)