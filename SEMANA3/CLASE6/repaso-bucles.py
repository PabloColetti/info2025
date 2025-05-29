# contador = 0
# while True:
#   contador += 1
#   print(f"Hola hace frio 🥶, {contador} veces") # Ctrl + C

# flag = True
# while flag:
#     print("Hola info 🤧🥶")
#     respuesta = input("Desea continuar? s/n: ")

#     if respuesta == "n":
#         flag = False

#     print("Luego del break")


# while True:
#     print("Hola info 🤧🥶")
#     respuesta = input("Desea continuar? s/n: ")

#     if respuesta == "n":
#         break

#     print("Luego del break")


while True:
    print("Hola info 🤧🥶")
    respuesta = input("Desea continuar? s/n: ")

    # if not (respuesta == "s" or respuesta == "n"):
    #     print("Introduce una respuesta valida")
    #     continue
    
    if not respuesta == "s" and not respuesta == "n":
        print("Introduce una respuesta valida")
        continue

    if respuesta == "n":
        break

    print("Luego del break")
