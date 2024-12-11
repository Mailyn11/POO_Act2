class Esfera:
    def __init__(self, nombre, peso):
        self.nombre = nombre
        self.peso = peso

    def guardar_en_archivo(self):
        with open(f"{self.nombre}.txt", "w") as archivo:
            archivo.write(f"Nombre: {self.nombre}\n")
            archivo.write(f"Peso: {self.peso}\n")
