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

# def prueba(num1, num2):
#   global resultado
#   resultado = num1 + num2
#   print(f"Desde adentro: {resultado}")

# resultado = 0

# resultado = 10

# prueba(10, 20)

# print(f"Desde afuera: {resultado}")


# def suma(num1, num2, num3):
#   return num1 + num2 + num3

# resultado = suma(10, 10)
# print(f"El resultado es: {resultado}")


# *args: Pemiten pasar a una funcion un numero variable/indeterminado de argumentos posicionales...

# def suma(*args):
#     # print(args)
#     # print(type(args))

#     resultado = 0
#     for numero in args:
#         resultado += numero

#     return resultado


# def suma(*args):
#     # print(args)
#     # print(type(args))

#     return sum(args)


# resultado = suma(20, 50, 100, 200, 55, 1000, 7887)
# print(f"El resultado es: {resultado}")



# **kwargs: Pemiten pasar a una funcion un numero variable/indeterminado de argumentos con nombre (clave-valor)

# def ver_persona(**kwargs):
# 	print(kwargs)
# 	print(type(kwargs))

# 	for clave, valor in kwargs.items():
# 		print(f"Clave: {clave}, Valor: {valor}")

# ver_persona(nombre = "Juan", edad = 25, ciudad = "Resistencia", algo = "algo", algo_mas= "algo mas")

		# indetermidados determinados
				# posicionales      
def mostrar_info(*args, nombre, edad=0, **kwargs):
							#     nombrados
						# determinados indeterminados
    print(f"Posicionales indetermidados {args}")
    print(f"Posicionales determinados {nombre}")
    print(f"Nombrados determinados: {edad}")
    print(f"Nombrados indeterminados: {kwargs}")
    

mostrar_info(50, True, "algo", nombre="Pablo", edad=28, ciudad="Resis")


