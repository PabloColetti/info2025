print("### STRINGS ###")

nombre = "Pablo"
edad = 27

mensaje = "Hola me llamo {} y tengo {}".format(nombre, edad)
print(mensaje)

mensaje = f"Hola me llamo {nombre} y tengo {edad}"
print(mensaje)

a = 7
b = 20
mensaje = f"Hola me llamo {nombre} y tengo {a + b}"
print(mensaje)

print("### OPERACIONES CON STRINGS ###")

cadena1 = "Hola"
cadena2 = "Info"

cadena_concatenada = cadena1 + " " + cadena2
print(cadena_concatenada)

cadena_repetida = cadena2 * 3
print(cadena_repetida)

# 0123456789
cadena = "Hola mundo"
print(cadena)

longitud = len(cadena)
print(longitud)

subcadena = cadena[0:4]
print(subcadena)

cadena_invertida = cadena[::-1]
print(cadena_invertida)

cadena_mayusculas = cadena.upper()
print(cadena_mayusculas)

cadena_minusculas = cadena_mayusculas.lower()
print(cadena_minusculas)

cadena_capitalize = cadena_minusculas.capitalize()
print(cadena_capitalize)

cadena_reemplazo = cadena.replace("Hola", "algo")
print(cadena_reemplazo)

print("Hola\nMundo")  # \ => Alt + 92
print("Hola\tMundo")
print("Hola\\Mundo")
print("Hola \"Mundo\"")


print("### ACA")
print("Hola", end="!")
# print("Hola")
print("mundo", end="\n")

print("Hola", "mundo", "info", sep="\t")
