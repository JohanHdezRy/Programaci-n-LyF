# Definición de zonas con sus límites de humedad
zonas = {
    1: {'nombre': 'jardin_m', 'min_humedad': 30, 'max_humedad': 50},
    2: {'nombre': 'jardin_p', 'min_humedad': 40, 'max_humedad': 60},
    3: {'nombre': 'flores', 'min_humedad': 25, 'max_humedad': 45},
    4: {'nombre': 'huerto', 'min_humedad': 45, 'max_humedad': 65},
}

# Variables iniciales
hora_actual = 20
probabilidad_lluvia = False
velocidad_viento = 5

# Humedad por zona
humedad_zona = {
    1: 25,
    2: 38,
    3: 20,
    4: 50,
}

# Temperatura por zona
temperatura_zona = {
    1: 35,
    2: 32,
    3: 30,
    4: 28,
}

def hora_adecuada():
    H = hora_actual
    return (5 <= H <= 9) or (18 <= H <= 22)

def condiciones_climaticas_adecuadas():
    return (probabilidad_lluvia == False) and (velocidad_viento < 15)

def necesita_riego(zona):
    humedad = humedad_zona.get(zona, None)
    if humedad is None:
        return False
    min_humedad = zonas[zona]['min_humedad']
    return humedad < min_humedad

def activar_riego(zona):
    return necesita_riego(zona) and condiciones_climaticas_adecuadas() and hora_adecuada()

def estado_riego(zona):
    if activar_riego(zona):
        return 'Activado'
    else:
        return 'No activado'

def alerta_temperatura(zona):
    T = temperatura_zona.get(zona, None)
    if T is None:
        return
    if T >= 35:
        print('ALERTA: Temperatura extremadamente alta en zona', zona)
    elif T >= 32:
        print('Advertencia: Temperatura alta en zona', zona)

def recomendacion(zona):
    if activar_riego(zona):
        T = temperatura_zona.get(zona, 0)
        tipo = zonas[zona]['nombre']
        if T >= 32:
            print(f'Recomendación: Regar zona {zona} ({tipo}) en horas de la tarde/noche. Evitar riego al mediodía por alta temperatura.')
        else:
            print(f'Recomendación: Regar zona {zona} ({tipo}) según programa establecido.')
    else:
        humedad = humedad_zona.get(zona, 0)
        min_humedad = zonas[zona]['min_humedad']
        if humedad > min_humedad:
            print(f'Recomendación: Zona {zona} tiene suficiente humedad. No se requiere riego.')
        elif not condiciones_climaticas_adecuadas():
            print(f'Recomendación: Zona {zona} necesita riego pero las condiciones climáticas no son óptimas.')
        else:
            print('Sin recomendaciones especiales.')

def diagnostico_general():
    for zona in zonas:
        print(f'Estado riego zona {zona}: {estado_riego(zona)}')
        alerta_temperatura(zona)
        recomendacion(zona)
        print('-' * 50)

if __name__ == '__main__':
    diagnostico_general()

