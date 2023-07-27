from modu import utilidades
# 4- Hallar la suma de los términos de la serie: 1/1! + 1/2! + 1/3! + ... + 1/N!

# recibimos el numero de iteraciones
N = input("N: ")

# transformamos a entero
n_entero = int(N)

suma = 0

for i in range(n_entero):
    numero_a_dividir = utilidades.factorial(i + 1)

    suma += 1 / numero_a_dividir

print(suma)


