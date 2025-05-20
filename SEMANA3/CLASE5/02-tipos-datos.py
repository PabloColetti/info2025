edad = 27  # int
print(f"Edad: {edad}, Tipo: {type(edad)}")

altura = 1.75  # float
print(f"Altura: {altura}, Tipo: {type(altura)}")

z = 2+5j  # complex
print(f"Complejo: {z}, Tipo: {type(z)}")

cadena = "Juan"  # str
print(f"Nombre: {cadena}, Tipo: {type(cadena)}")

verdadero = True  # bool
print(f"Bool: {verdadero}, Tipo: {type(verdadero)}")

valor = None  # NoneType
print(f"None: {valor}, Tipo: {type(valor)}")

empty_string = ""  # str
print(f"None: {empty_string}, Tipo: {type(empty_string)}")

infinito = float("inf")
print(f"Infinito: {infinito}, Tipo: {type(infinito)}")

nan = float("nan")
print(f"Not a Number: {nan}, Tipo: {type(nan)}")

# LIsta (arrays) -> Coleccion de elementos ordenados y mutables
      #     0     1   2             3
lista = ["algo", 17, 0.5, ["otra lista", True]] # list
print(f"Lista: {lista}, Tipo: {type(lista)}")

# Tupla (tuple) -> Coleccion de elementos ordenados inmutable y que tiene una longitud fija (no se puede agregar ni eliminar)
tupla = (10.5, 48.5) # tuple
print(f"Tupla: {tupla}, Tipo: {type(tupla)}")

# Set -> Coleccion de elementos unicos (no se pueden repetir), y no tienen un orden definido, sin embargo si son mutables (se puede agregar o eliminar elementos)
colores = {"rojo", "verde", "azul"} # set
print(f"Set: {colores}, Tipo: {type(colores)}")

# Diccionarios -> Coleccion de elementos que tienen pares clave-valor (key-value)
estudiante = {
  "nombre": "Andres",
  "edad": 29,
  "curso": {
    "nombre": "Programacion web",
    "iniciales": ["PW", "WP"]
  }
}
