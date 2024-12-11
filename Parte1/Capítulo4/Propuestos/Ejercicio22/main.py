from Employee import Employee

# Solicitar datos por teclado
name = input("Ingrese el nombre del empleado: ")
hourly_wage = float(input("Ingrese el salario por hora: "))
hours_worked = int(input("Ingrese el total de horas trabajadas en el mes: "))

employee = Employee(name, hourly_wage, hours_worked)
employee.display_salary_info()
