from Quadratic import QuadraticEquation

# Ejemplo de uso
a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))

quadratic = QuadraticEquation(a, b, c)
solutions = quadratic.find_solutions()

if isinstance(solutions, str):
    print(solutions)
else:
    print("Soluciones:", solutions)