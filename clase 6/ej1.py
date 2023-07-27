# 1) Escribe un programa que pida un número por teclado y que cree un
# diccionario cuyas claves sean desde el número 1 hasta el número indicado, y los
# valores sean los cuadrados de las claves.

numero_de_claves = int(input("numero: "))

# resultado = {x+1 : (x+1)**2 for x in range(numero_de_claves)}

resultado = {}
for i in range(numero_de_claves):
    resultado[i+1] = (i+1)**2



print(resultado)

print('hola')