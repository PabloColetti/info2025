# Se definen con llaves {} y estan compuestos por pares (clave-valor | key-value)
# Las claves son unicas, y lo valores puden ser cualquier tipo de dato, incluso otros diccionarios...
# Son desordenados (sus elementos no tienen indice) y son mutables (podemos agregar, eliminar, modificar...)

estudiante = {
    "nombre": "Ana",
    "edad": 23,
    "curso": "Matematicas"
}
print(f"Conjunto diccionario: {estudiante}, {type(estudiante)}")

print(f"Edad estudiante: {estudiante['edad']}")

estudiante["carrera"] = "Ing"
print(f"Estudiante: {estudiante}")

del estudiante["carrera"]
print(f"Estudiante: {estudiante}")

print(f"Claves (keys) del diccionario: {list(estudiante.keys())}")

print(f"Valores (values) del diccionario: {list(estudiante.values())}")

estudiante_dos = {
    "nombre": "Juan",
    "edad": 23,
    "curso": {
        "nombre": "Programacion web",
        "tags": ["PW", "Programacion", "Web", "Python", "Django", {
            "algo": 12
        }]
    }
}

print(f"Estudiante dos: {estudiante_dos['curso']['nombre']}")
print(f"Estudiante dos: {estudiante_dos['curso']['tags'][3]}")
print(f"Estudiante dos: {estudiante_dos['curso']['tags'][5]["algo"]}")

estudiante_dos['curso']['tags'][5]["algo"] = 99

print(f"Estudiante dos: {estudiante_dos['curso']['tags'][5]["algo"]}")

calificaciones = {
  "quimica": 10,
  "fisica": 5,
  "lengua": 7
}

for materia, nota in calificaciones.items():
  print(materia, nota)