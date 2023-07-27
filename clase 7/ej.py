
# Atributos:
# color: string
# matrícula: string
# encendido: booleano
# velocidad: int
# combustible: string
# fechaMantenimiento: list
# montoMantenimiento: list
# listaMantenimientos:list

# Metodos
# arrancar()
# ir()
# masRapido()
# masLento()
# parar()
# obtenerInformación()
# agregarMantenimiento()
# obtenerGastoMantenimiento()

class Auto():
    def __init__(self, color, matricula, encendido=False, velocidad=0, combustible=0):
        self.color = color
        self.matricula = matricula
        self.encendido = encendido
        self.velocidad = velocidad
        self.combustible = combustible
        self.listaMantenimientos = []

    def arrancar(self):
        if self.encendido == False:
            self.encendido = True
        else:
            print("El auto ya está encendido")

    def ir(self):
        if self.encendido == True:
            self.velocidad = 10
        else:
            print("El auto no está encendido")

    def masRapido(self):
        if self.encendido == True:
            self.velocidad += 10
        else:
            print("El auto no está encendido")

    def agregarMantenimiento(self, fecha, monto):
        self.listaMantenimientos.append({"fecha":fecha, "monto": monto})

    
    def imprimir(self):
        print("Color: ", self.color)
        print("Matricula: ", self.matricula)
        print("Encendido: ", self.encendido)
        print("Velocidad: ", self.velocidad)
        print("mantenimientos: ", self.listaMantenimientos)



def main():

    auto1 = Auto("rojo", "ABC123")

    auto1.imprimir()

    auto1.agregarMantenimiento("2020-01-01", 1_000_000)

    auto1.imprimir()








    
main()