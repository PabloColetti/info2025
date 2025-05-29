# def saludo(nombre):
#     print(f"Hola {nombre}")

# saludo("Pablo")
# saludo("Elias")
# saludo("Edu")

# notas = [10, 5, 7, 8, 10, 6]
# suma = 0

# for nota in notas:
#   suma += nota

# promedio = suma / len(notas)

# print(f"Suma: {suma}")
# print(f"Cantidad de notas: {len(notas)}")
# print(f"Promedio: {promedio}")


# def promedio(notas):
#     return sum(notas) / len(notas)

# promedio_pablo = promedio([5, 6, 8, 9])
# promedio_juan = promedio([10, 5, 6, 9])

# print(f"promedio_pablo: {promedio_pablo}")
# print(f"promedio_juan: {promedio_juan}")


contador = 0
contador = 10

def prueba():
  global contador 
  contador = 20
  print(contador)

prueba()
print(contador)


