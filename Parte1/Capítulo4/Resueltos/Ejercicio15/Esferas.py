class Esfera:
    def __init__(self, peso):
        self.peso = peso

class CompararEsferas:
    def __init__(self, esferaA, esferaB, esferaC, esferaD):
        self.esferaA = esferaA
        self.esferaB = esferaB
        self.esferaC = esferaC
        self.esferaD = esferaD

    def comparar(self):
        if self.esferaA.peso == self.esferaB.peso == self.esferaC.peso:
            if self.esferaD.peso != self.esferaA.peso:
                print("La esfera D es la diferente")
                if self.esferaD.peso > self.esferaA.peso:
                    print("Y es de mayor peso")
                else:
                    print("Y es de menor peso")
        elif self.esferaA.peso == self.esferaB.peso == self.esferaD.peso:
            print("La esfera C es la diferente")
            if self.esferaC.peso > self.esferaA.peso:
                print("Y es de mayor peso")
            else:
                print("Y es de menor peso")
        elif self.esferaA.peso == self.esferaC.peso == self.esferaD.peso:
            print("La esfera B es la diferente")
            if self.esferaB.peso > self.esferaA.peso:
                print("Y es de mayor peso")
            else:
                print("Y es de menor peso")
        else:
            print("La esfera A es la diferente")
            if self.esferaA.peso > self.esferaB.peso:
                print("Y es de mayor peso")
            else:
                print("Y es de menor peso")


# Función principal
def main():
    # Solicitar los valores de las esferas por teclado
    print("Ingrese el peso de la esfera A: ")
    pesoA = float(input())  

    print("Ingrese el peso de la esfera B: ")
    pesoB = float(input())  

    print("Ingrese el peso de la esfera C: ")
    pesoC = float(input())  

    print("Ingrese el peso de la esfera D: ")
    pesoD = float(input())  

    # Crear instancias de la clase Esfera con los pesos proporcionados por el usuario
    esferaA = Esfera(pesoA)
    esferaB = Esfera(pesoB)
    esferaC = Esfera(pesoC)
    esferaD = Esfera(pesoD)

    # Crear una instancia de la clase CompararEsferas
    diferenciar_esferas = CompararEsferas(esferaA, esferaB, esferaC, esferaD)

    # Llamar la función o método para comparar los pesos
    diferenciar_esferas.comparar()

# Ejecutar la función principal
if __name__ == "__main__":
    main()
