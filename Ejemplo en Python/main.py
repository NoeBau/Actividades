from funciones import sumar, restar, multiplicar, dividir


def mostrar_menu():
    print("\n==============================")
    print("   CALCULADORA EN PYTHON")
    print("==============================")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")


def solicitar_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: escribe un número válido.")


def ejecutar_calculadora():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "5":
            print("Programa finalizado.")
            break

        if opcion not in ["1", "2", "3", "4"]:
            print("Opción incorrecta.")
            continue

        numero1 = solicitar_numero("Escribe el primer número: ")
        numero2 = solicitar_numero("Escribe el segundo número: ")

        if opcion == "1":
            resultado = sumar(numero1, numero2)
        elif opcion == "2":
            resultado = restar(numero1, numero2)
        elif opcion == "3":
            resultado = multiplicar(numero1, numero2)
        else:
            resultado = dividir(numero1, numero2)

        print(f"Resultado: {resultado}")


if __name__ == "__main__":
    ejecutar_calculadora()