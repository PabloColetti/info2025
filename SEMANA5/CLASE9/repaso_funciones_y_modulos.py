def mostrar_info(nombre, edad, *otros_datos, actividad="Estudiante", **kwargs):
    print(f"Hola {nombre}, tiene {edad} años, y es {actividad}")
    print(f"*args: {otros_datos}")
    print(f"**kwargs: {kwargs}")


mostrar_info("Pablo", 27, "Manzana", "Banana",
             actividad="Programador", materias=["mate", "lengua", "quimica"], notas=[8, 7, 8, 5])


