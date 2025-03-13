# Seleccionador

Redes = 0  
Base = 0  
Desarrollo = 0  
Haswer = 0  
modelado = 0
gestion = 0

print('==============')
print('Las ramas de sistemas computacionales ')
print('==============')  

#    --- Pregunta 1 ---

print('P1) ¿Qué actividad te resulta más interesante?')
print('  1) Configurar y mantener servidores y redes.')
print('  2) Diseñar y gestionar bases de datos.')
print('  3) Desarrollar aplicaciones y programas.')
print('  4) Programar y optimizar hardware.')
print('  5) Crear modelos y animaciones en 3D.')
print('  6) Planificar y dirigir proyectos de software.')

respuesta = int(input('Ingresa respuesta (1-6): '))

if respuesta == 1:
    Redes += 2
elif respuesta == 2:
    Base += 2
elif respuesta == 3:
    Desarrollo += 2
elif respuesta == 4:
    Haswer += 2
elif respuesta == 5:
    modelado += 2
elif respuesta == 6:
    gestion += 2
else:
    print('Respuesta incorrecta.')

# --- Pregunta 2 ---

print('\nP2) ¿Qué tipo de problemas te gusta resolver?')

print('  1) Problemas de conectividad y comunicación entre dispositivos.')
print('  2) Problemas de organización y recuperación de información.')
print('  3) Problemas de funcionalidad y usabilidad de software.')
print('  4) Problemas de rendimiento y eficiencia de hardware.')
print('  5) Problemas de diseño y visualización en 3D.')
print('  6) Problemas de coordinación y entrega de proyectos.')

respuesta = int(input('Ingresa respuesta (1-6): '))

if respuesta == 1:
    Redes += 2
elif respuesta == 2:
    Base += 2
elif respuesta == 3:
    Desarrollo += 2
elif respuesta == 4:
    Haswer += 2
elif respuesta == 5:
    modelado += 2
elif respuesta == 6:
    gestion += 2
else:
    print('Respuesta incorrecta.')

# --- Pregunta 3 ---

print('\n03) ¿Qué herramienta te parece más útil?')

print('  1) Herramientas de diagnóstico de redes.')
print('  2) Sistemas de gestión de bases de datos.')
print('  3) Entornos de desarrollo integrado (IDEs).')
print('  4) Herramientas de programación de microcontroladores.')
print('  5) Software de modelado 3D como Blender o Maya.')
print('  6) Herramientas de gestión de proyectos como Jira o Trello. ')

respuesta = int(input('Ingresa respuesta (1-6): '))

if respuesta == 1:
    Redes += 2
elif respuesta == 2:
    Base += 2
elif respuesta == 3:
    Desarrollo += 2
elif respuesta == 4:
    Haswer += 2
elif respuesta == 5:
    modelado += 2
elif respuesta == 6:
    gestion += 2
else:
    print('Respuesta incorrecta.')

# --- Pregunta 4 ---

print('\n04) ¿Qué tipo de proyectos te gustaría liderar?')

print('  1) Implementación de infraestructuras de red.')
print('  2) Diseño y optimización de bases de datos.')
print('  3) Desarrollo de aplicaciones móviles o web.')
print('  4) Desarrollo de dispositivos electrónicos. ')
print('  5) Creación de animaciones o juegos en 3D. ')
print('  6) Dirección de equipos para la entrega de software. ')

respuesta = int(input('Ingresa respuesta (1-6): '))

if respuesta == 1:
    Redes += 2
elif respuesta == 2:
    Base += 2
elif respuesta == 3:
    Desarrollo += 2
elif respuesta == 4:
    Haswer += 2
elif respuesta == 5:
    modelado += 2
elif respuesta == 6:
    gestion += 2
else:
    print('Respuesta incorrecta.')

# --- Pregunta 5 ---

print('\n05) ¿Qué habilidad te gustaría desarrollar más?')

print('  1) Configuración y seguridad de redes.')
print('  2) Diseño y consultas avanzadas en bases de datos.')
print('  3) Programación en múltiples lenguajes de software. ')
print('  4) Programación de bajo nivel y optimización de hardware. ')
print('  5) Creación de modelos 3D realistas y animaciones.')
print('  6) Liderazgo y gestión de equipos de desarrollo. ')

respuesta = int(input('Ingresa respuesta (1-6): '))

if respuesta == 1:
    Redes += 2
elif respuesta == 2:
    Base += 2
elif respuesta == 3:
    Desarrollo += 2
elif respuesta == 4:
    Haswer += 2
elif respuesta == 5:
    modelado += 2
elif respuesta == 6:
    gestion += 2
else:
    print('Respuesta incorrecta.')

print("Redes: ", Redes)
print("Base de datos: ", Base)
print("Desarrollo de Software: ", Desarrollo)
print("Programación Hardware: ", Haswer)
print("Modelado 3D: ", modelado)
print("Gestión de Proyectos de Software: ", gestion)

if Redes >= Desarrollo and Redes >= Base and Redes >= Haswer and Redes >= modelado and Redes >= gestion:
    print("Redes es tu rama")
elif Base >= Desarrollo and Base >= Haswer and Base >= modelado and Base >= gestion:
    print("Base de datos es tu rama")
elif Desarrollo >= Haswer and Desarrollo >= modelado and Desarrollo >= gestion:
    print("Desarrollo de Software es tu rama")
elif Haswer >= modelado and Haswer >= gestion:
    print("Programación Hardware es tu rama")
elif modelado >= gestion:
    print("Modelado 3D es tu rama")
else:
    print("Gestión de Proyectos de Software es tu rama")

