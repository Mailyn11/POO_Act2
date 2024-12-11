class NumberComparator:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def find_largest_number(self):
        if self.a > self.b and self.a > self.c:
            largest = self.a
        elif self.b > self.a and self.b > self.c:
            largest = self.b
        else:
            largest = self.c
        return largest

    def display_largest_number(self):
        largest = self.find_largest_number()
        print(f"El número más grande es: {largest}")


