# factorial de 5 = 5 * 4 * 3 * 2 * 1
# factorial de 4 = 4 * 3 * 2 * 1
# factorial de 3 = 3 * 2 * 1

# factorial de 5 = 5 * factorial de 4


def factorial(numero_factorial):
    factorial = 1

    for i in range(numero_factorial):
        factorial = factorial * (i+1)

    return factorial

def factorial_recursivo(numero_factorial):
    print(numero_factorial)
    # caso base, caso en el 
    if numero_factorial <= 0:
        print("PARE")
        return 1
    
    return numero_factorial * factorial_recursivo(numero_factorial - 1)


if __name__ == "__main__":
    N = input("N factorial: ")

    # transformamos a entero
    n_entero = int(N)
    print(factorial_recursivo(n_entero))
    



