productos = ["Frijoles Refritos","Coca cola","Zumo de naranja","Cafe de olla","Gorditas de chicarron","Huevos revueltos"]

orden= sorted(productos)

cadena = ",".join(orden)
slug = list(map(lambda producto: producto.replace(" ","-").lower(), orden))


print(cadena)
print(slug)