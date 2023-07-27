# with open("gato_copia.jpeg", "wb") as lista_copia_f:
#     with open("gato.jpeg", "rb") as lista_f:
#         for linea in lista_f.readlines():
#             print(linea)
#             lista_copia_f.write(linea)


while True:
    nombre = input("escribir nombre:")
    nombre = input("escribir apellido:")
    if nombre == "":
        break
    with open("nombres.txt", "a") as f:
        f.write(nombre + "\n")




    
# with open("/Users/ete/Documents/facu/cipython/clase 6/ej1.py", "a") as f:
#     f.write("\nprint('hola')")
