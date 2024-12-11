import math

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        if not self.is_valid_triangle():
            raise ValueError("Los lados proporcionados no forman un triángulo válido.")

    def is_valid_triangle(self):
        return self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a

    def calculate_perimeter(self):
        return self.a + self.b + self.c

    def calculate_semiperimeter(self):
        return self.calculate_perimeter() / 2

    def calculate_area(self):
        s = self.calculate_semiperimeter()
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def display_properties(self):
        perimeter = self.calculate_perimeter()
        semiperimeter = self.calculate_semiperimeter()
        area = self.calculate_area()

        print(f"Perímetro: {perimeter}")
        print(f"Semiperímetro: {semiperimeter}")
        print(f"Área: {area}")


