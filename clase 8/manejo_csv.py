import csv

f = csv.reader(open("archivos/lista.txt", "r"))

for linea in f:
    
    indice, nombre, apellido = linea
    if not indice.isdigit():
        continue
    
    print(int(indice) + 10, nombre, apellido)