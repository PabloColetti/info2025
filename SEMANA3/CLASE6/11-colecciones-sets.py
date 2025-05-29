# Se definen con llaves {} y pueden contener cualquier tipo de elementos sin embargo no los unhashable (solo tuplas)
# Son desordenadas (sus elementos no tienen indice) y son mutables (agregar, eliminar o modificar), sin embargo, no pueden contenter elementos duplicados.

colores_set = {"rojo", "azul", "verde"}
print(f"Conjunto set: {colores_set}, {type(colores_set)}")

# print(f"Intento acceder al primer elemento: {colores_set[0]}") # NO SE PUEDE ACCEDER CON INDICES, PORQUE NO TIENEN (SON DESORDENADOS)

colores_set.add("amarillo")
print(f"Set luego del add: {colores_set}")

colores_set.add("amarillo")
print(f"Set luego del segundo add: {colores_set}")

colores_set.remove("verde")
print(f"Set luego del remove: {colores_set}")

colores_set.discard("verde")
print(f"Set luego del discard: {colores_set}")

elemento_eliminado = colores_set.pop()
print(f"Elemento eliminado: {elemento_eliminado}")
print(f"Set luego del pop: {colores_set}")

colores_set.clear()
print(f"Set luego del set: {colores_set}")

colores_set = {"rojo", "azul", "verde"}
print(f"El color 'rojo' esta en el set?: {"rojo" in colores_set}")
print(f"El color 'violeta' esta en el set?: {"violeta" in colores_set}")

conj1 = {1, 2, 3}
conj2 = {2, 4, 5, 6, 3}

union_conj = conj1.union(conj2)
print(f"Union: {union_conj}")

interseccion_conj = conj1.intersection(conj2)
print(f"Interseccion: {interseccion_conj}")

diferencia_conj = conj1.difference(conj2)
print(f"Diferencia: {diferencia_conj}")

lista_con_duplicados = [10, 10, 2, 4, 9, 5, 7, 9, 8]
lista_sin_duplicados = list(set(lista_con_duplicados))

print(f"Lista sin duplicados: {lista_sin_duplicados}")
