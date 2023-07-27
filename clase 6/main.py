
diccionario_ingles_espanhol = {"frutilla": "strawberry", "manzana": "apple"}
# descripcion_persona = {"nombre": "stefan", "edad": 24, "lista": [1,2,3]}
x = 100
x = x + 1
try:
    x = x / 0
    kiwi = diccionario_ingles_espanhol['kiwi']
    print(kiwi)
except KeyError:
    print("no encontrado")
except ZeroDivisionError:
    print("se intento dividir por 0")
except Exception as e:
    print("paso esto:")
    print(e)
finally:
    print("fin :)")



# diccionario_ingles_espanhol.update({"frutilla": "banana", "sandia":"watermelon"})
# diccionario_ingles_espanhol["frutilla"] = "banana"
# diccionario_ingles_espanhol['sandia'] = "watermelon"

# print(diccionario_ingles_espanhol)


# lista_valores_ingles = list(diccionario_ingles_espanhol.values())
# lista_valores_espanhol = list(diccionario_ingles_espanhol.keys())
# print(lista_valores_espanhol)

# print(descripcion_persona.items())

# for key, value in descripcion_persona.items():
#     print(value)
