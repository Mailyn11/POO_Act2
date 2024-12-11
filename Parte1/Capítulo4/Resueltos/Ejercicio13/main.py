#aqui se ejecutara el codigo principal


from compra import Compra

def main():
    # Obtener los datos de la compra
    valor_compra = float(input("Ingrese el valor total de la compra: "))
    color_bolita = input("Ingrese el color de la bolita (blanca, verde, amarilla, azul, roja): ")

    # Crear instancia de la compra
    compra = Compra(valor_compra, color_bolita)

    # Mostrar el total a pagar después de aplicar el descuento
    compra.mostrar_total()

if __name__ == "__main__":
    main()
