
def sumar(x, y):
    try:
        x/0
    except Exception as e:
        print(e)
    finally:
        print("finalizado")

    suma = x + y
    return suma


# print(sumar(2, 2))


def dividir(x, y):
    """Esta funcion hace la division de 2 numeros."""

    return x / y


def imprimirAlgo(*cosas):
    x = cosas[0]
    y = cosas[1]
    z = cosas[2]

    print(x,y,z)


def crearPersona(nombre, edad, trabajo="programador"):

    print(f"{nombre} tiene {edad} años y su trabajo es {trabajo}")




