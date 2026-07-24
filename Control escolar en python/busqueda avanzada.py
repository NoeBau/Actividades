def busqueda_avanzada():
    print("\n========== BÚSQUEDA AVANZADA ==========")
    print("1. Buscar por matrícula")
    print("2. Buscar por nombre")
    print("3. Buscar por carrera")
    print("4. Buscar por semestre")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        criterio = "matricula"
        valor = input("Ingrese la matrícula: ").strip()

    elif opcion == "2":
        criterio = "nombre"
        valor = input("Ingrese el nombre o una parte: ").strip()

    elif opcion == "3":
        criterio = "carrera"
        valor = input("Ingrese la carrera o una parte: ").strip()

    elif opcion == "4":
        criterio = "semestre"
        valor = input("Ingrese el semestre: ").strip()

    else:
        print("Opción no válida.")
        return

    resultados = []

    for estudiante in estudiantes:
        dato = str(estudiante.get(criterio, ""))

        if valor.lower() in dato.lower():
            resultados.append(estudiante)

    if not resultados:
        print("\nNo se encontraron estudiantes.")
        return

    print(f"\nSe encontraron {len(resultados)} estudiante(s):")

    for numero, estudiante in enumerate(resultados, start=1):
        print(f"\nResultado {numero}")
        print("Matrícula :", estudiante["matricula"])
        print("Nombre    :", estudiante["nombre"])
        print("Carrera   :", estudiante["carrera"])
        print("Semestre  :", estudiante["semestre"])
        print("Promedio  :", estudiante["promedio"])