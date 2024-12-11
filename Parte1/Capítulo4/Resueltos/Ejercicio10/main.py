from student import Student

# Solicitar datos por teclado
def main():
        registration_number = input("Ingrese el número de inscripción del estudiante: ")
        name = input("Ingrese el nombre del estudiante: ")
        patrimony = float(input("Ingrese el patrimonio del estudiante: "))
        social_stratum = int(input("Ingrese el estrato social del estudiante: "))
        
        student_instance = Student(registration_number, name, patrimony, social_stratum)
        student_instance.display_information()
        print("Por favor, ingrese valores válidos para el patrimonio y el estrato social.")

if __name__ == "__main__":
    main()
