from estudiantes import (
    actualizar_estudiante,
    buscar_estudiante,
    busqueda_avanzada,
    eliminar_estudiante,
    mostrar_estadisticas,
    mostrar_estudiantes,
    registrar_estudiante
)


def mostrar_menu():
    print("\n========================================")
    print("       SISTEMA DE CONTROL ESCOLAR")
    print("========================================")
    print("1. Registrar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Buscar estudiante por matrícula")
    print("4. Actualizar estudiante")
    print("5. Eliminar estudiante")
    print("6. Búsqueda avanzada")
    print("7. Estadísticas escolares")
    print("8. Salir")
    print("========================================")


def main():
    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_estudiante()

        elif opcion == "2":
            mostrar_estudiantes()

        elif opcion == "3":
            buscar_estudiante()

        elif opcion == "4":
            actualizar_estudiante()

        elif opcion == "5":
            eliminar_estudiante()

        elif opcion == "6":
            busqueda_avanzada()

        elif opcion == "7":
            mostrar_estadisticas()

        elif opcion == "8":
            print("\nGracias por usar el Sistema de Control Escolar.")
            break

        else:
            print("\nOpción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()