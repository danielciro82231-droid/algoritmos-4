datos = [5, 3, 8, 1, 2, 9, 4]

import heapq

heapq.heapify(datos)
print("heap:" , datos)



heapq.heappush(datos, 6)
print("heap  despues de agregar 6:",datos)

minimo = heapq.heappop(datos)
print("elemento minimo extraido:", minimo)
print("heap  despues de extraer el minimo:", datos)



datos2 = [(2, 'A'), (1, 'B'), (3, 'C'), (2, 'B')]
heapq.heapify(datos2)
print("heap con tuplas:", datos2)


# hacer un programa para un hospital
# cada paciente tiene prioridad de 1 a 3, 1 es la mas importante
# las personas deben saber quien es el siguiente en atender e indicar su nombre y su prioridad
 