# Se definen con [] y pueden contener cualquier tipo de elementos, incluso otras listas, o coleccion.
# Son ordenadas (sus elementos tiene indice) y son mutables (podemos agregar, eliminar o modificar)

#  0  1  2  3  4
numeros = [3, 2, 3, 1, 5, 4, 8, 7]

# primer elemento
print(numeros[0])

# ultimo elemento
print(numeros[-1])

# sublista (slicing)
print(f"Primeros 3 elementos: {numeros[:3]}")
print(f"Ultimos 2 elementos: {numeros[-2:]}")
print(f"Elementos del medio: {numeros[1:-1]}")

print(f"Longitud de la lista: {len(numeros)}")


print(f"### METODOS ###")

print(f"Cuantas veces aparece el elemento con valor 3: {numeros.count(3)}")

print(f"Cual es el indice del elemento con valor 4: {numeros.index(4)}")

numeros[0] = 0
print(f"Despues de modificar: {numeros}")

numeros.append(6)
print(f"Lista luego del append: {numeros}")

numeros.insert(2, 8)
print(f"Lista luego del insert: {numeros}")

numeros.pop()
print(f"Lista luego del pop: {numeros}")

numeros.remove(8)
print(f"Lista luego del remove: {numeros}")

numeros.sort()
print(f"Lista luego del sort: {numeros}")

numeros.sort(reverse=True)
print(f"Lista luego del sort invertido: {numeros}")

matriz = [
#  0  1  2
  [1, 2, 3], # 0
  [4, 5, 6], # 1
  [7, 8, 9]  # 2
]

print(f"Matriz: {matriz}")
print(f"Elemento [2][2]: {matriz[2][2]}")

print(f"Elemento con valor 5 esta en la lista?: {"SI" if 5 in numeros else "NO"}")

