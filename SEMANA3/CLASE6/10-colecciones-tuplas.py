# Se definen con parentesis () y pueden contener cualquier tipo de elementos, incluso otras tuplas, o colecciones.
# Son ordenadas (sus elementos tienen indices) y son inmutables (no se pueden agregar, eliminar o modificar)

#  0  1  2  3  4
numeros_tupla = (5, 3, 2, 4, 5)
print(f"Numeros (tupla): {numeros_tupla}, tipo: {type(numeros_tupla)}")

# primer elemento
print(numeros_tupla[0])

# ultimo elemento
print(numeros_tupla[-1])

# sublista (slicing)
print(f"Primeros 3 elementos: {numeros_tupla[:3]}")
print(f"Ultimos 2 elementos: {numeros_tupla[-2:]}")
print(f"Elementos del medio: {numeros_tupla[1:-1]}")

# longitud
print(f"Longitud de la tupla: {len(numeros_tupla)}")

# No se puede hacer, son inmutable
# numeros_tupla[0] = 0
# print(f"Despues de modificar: {numeros_tupla}")

# Desempaquetado de tuplas
var1, var2, var3, var4, var5 = numeros_tupla
print(f"Desempaquetado: a={var1} b={var2} c={var3} d={var4} e={var5}")

primer_elemento, *resto_elementos = numeros_tupla
print(f"Desempaquetado: Primero={primer_elemento}\nResto={resto_elementos}")

_, segundo_elemento, *resto_elementos = numeros_tupla
print(f"Desempaquetado: Segundo={segundo_elemento}\nResto={resto_elementos}")

matriz = (
    #  0  1  2
    (1, 2, 3),  # 0
    (4, 5, 6),  # 1
    (7, 8, 9)  # 2
)

print(f"Matriz: {matriz}")
print(f"Elemento [2][2]: {matriz[1][1]}")

persona = ("Juan", 23, 1.85, True)
print(f"Persona: {persona}")

print(
    f"Elemento con valor 'Juan' esta en la tupla?: {"SI" if "Juan" in persona else "NO"}")
print(
    f"Elemento con valor '10' esta en la tupla numeros_tupla?: {"SI" if 10 in numeros_tupla else "NO"}")

print(f"Tupla original: {numeros_tupla}")

lista_numeros = list(numeros_tupla)
print(f"Tupla convertida a lista: {lista_numeros}")

lista_numeros.append(88)
print(f"Lista luego del append: {lista_numeros}")

tupla_numeros = tuple(lista_numeros)
print(f"Lista convertida a tupla: {tupla_numeros}")
