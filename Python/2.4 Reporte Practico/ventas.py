from functools import reduce

ventas = [1500,2500,3200,4500,6000,1200,8000]

conversion = list(map(lambda x: x * 0.049, ventas))

ventas_mayores = list(filter(lambda x:x > 150,conversion))

total_ventas = reduce(lambda acumulador , x: acumulador + x,ventas_mayores,0)
prom= total_ventas/len(ventas_mayores)

total_pesos= reduce(lambda acumulador, x: acumulador + x, ventas,0)

print("Total de ventas en pesos mexicanos: ",total_pesos)
print("Ventas en dolares: ",conversion)
print("ventas mayores a 150 dolares: ",ventas_mayores)
print("Promedio de ventas en dolares: ",prom)