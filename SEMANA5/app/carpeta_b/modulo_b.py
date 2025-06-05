from carpeta_a.modulo_aa import saludar_con_nombre_de_funcion_largo as saludo
from carpeta_a.modulo_ab import despedir

def ejecutar():
  mensaje = saludo("Pablo")
  print(f"desde modulo_b: {mensaje}")

  mensaje_despedida = despedir("Juan")
  print(f"desde modulo_b: {mensaje_despedida}")

if __name__ == "__main__":
  ejecutar()