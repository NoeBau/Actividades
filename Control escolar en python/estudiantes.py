import json
from pathlib import Path


ARCHIVO_ESTUDIANTES = Path(__file__).parent / "estudiantes.json"


def cargar_estudiantes():
    if not ARCHIVO_ESTUDIANTES.exists():
        return []

    try:
        with open(ARCHIVO_ESTUDIANTES, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

            if isinstance(datos, list):
                return datos

            return []

    except (json.JSONDecodeError, OSError):
        return []


estudiantes = cargar_estudiantes()


def guardar_estudiantes():
    try:
        with open(ARCHIVO_ESTUDIANTES, "w", encoding="utf-8") as archivo:
            json.dump(
                estudiantes,
                archivo,
                indent=4,
                ensure_ascii=False
            )

    except OSError as error:
        print("\nNo fue posible guardar los datos.")
        print("Error:", error)


def buscar_por_matricula(matricula):
    for estudiante in estudiantes:
        if estudiante["matricula"].lower() == matricula.lower():
            return estudiante

    return None


def solicitar_promedio():
    while True:
        promedio = input("Promedio de 0 a 10: ").strip()

        try:
            promedio_numero = float(promedio)

            if 0 <= promedio_numero <= 10:
                return promedio_numero

            print("El promedio debe estar entre 0 y 10.")

        except ValueError:
            print("Ingrese un promedio numérico válido.")


def solicitar_semestre():
    while True:
        semestre = input("Semestre de 1 a 12: ").strip()

        if semestre.isdigit():
            semestre_numero = int(semestre)

            if 1 <= semestre_numero <= 12:
                return semestre_numero

        print("Ingrese un semestre válido entre 1 y 12.")


def registrar_estudiante():
    print("\n===== REGISTRAR ESTUDIANTE =====")

    matricula = input("Matrícula: ").strip()

    if not matricula:
        print("\nLa matrícula no puede estar vacía.")
        return

    if buscar_por_matricula(matricula):
        print("\nYa existe un estudiante con esa matrícula.")
        return

    nombre = input("Nombre completo: ").strip()
    carrera = input("Carrera: ").strip()

    if not nombre or not carrera:
        print("\nEl nombre y la carrera son obligatorios.")
        return

    semestre = solicitar_semestre()
    promedio = solicitar_promedio()

    estudiante = {
        "matricula": matricula,
        "nombre": nombre,
        "carrera": carrera,
        "semestre": semestre,
        "promedio": promedio
    }

    estudiantes.append(estudiante)
    guardar_estudiantes()

    print("\nEstudiante registrado correctamente.")


def mostrar_estudiantes():
    print("\n")
    print("=" * 95)
    print("LISTA DE ESTUDIANTES".center(95))
    print("=" * 95)

    if not estudiantes:
        print("\nNo hay estudiantes registrados.")
        return

    encabezado = (
        f"{'No.':<5}"
        f"{'Matrícula':<15}"
        f"{'Nombre':<30}"
        f"{'Carrera':<25}"
        f"{'Sem.':<8}"
        f"{'Prom.':<10}"
    )

    print(encabezado)
    print("-" * 95)

    for numero, estudiante in enumerate(estudiantes, start=1):

        print(
            f"{numero:<5}"
            f"{estudiante['matricula']:<15}"
            f"{estudiante['nombre']:<30}"
            f"{estudiante['carrera']:<25}"
            f"{estudiante['semestre']:<8}"
            f"{float(estudiante['promedio']):<10.2f}"
        )

    print("=" * 95)
    print(f"Total de estudiantes: {len(estudiantes)}")


def buscar_estudiante():
    print("\n===== BUSCAR ESTUDIANTE =====")

    matricula = input("Ingrese la matrícula: ").strip()
    estudiante = buscar_por_matricula(matricula)

    if estudiante is None:
        print("\nNo se encontró ningún estudiante con esa matrícula.")
        return

    print("\n===== ESTUDIANTE ENCONTRADO =====")
    print("Matrícula :", estudiante["matricula"])
    print("Nombre    :", estudiante["nombre"])
    print("Carrera   :", estudiante["carrera"])
    print("Semestre  :", estudiante["semestre"])
    print("Promedio  :", estudiante["promedio"])


def actualizar_estudiante():
    print("\n===== ACTUALIZAR ESTUDIANTE =====")

    matricula = input("Matrícula del estudiante: ").strip()
    estudiante = buscar_por_matricula(matricula)

    if estudiante is None:
        print("\nNo se encontró ningún estudiante con esa matrícula.")
        return

    print("\nDeja el campo vacío para conservar el dato actual.")

    nombre = input(f"Nombre [{estudiante['nombre']}]: ").strip()
    carrera = input(f"Carrera [{estudiante['carrera']}]: ").strip()
    semestre = input(f"Semestre [{estudiante['semestre']}]: ").strip()
    promedio = input(f"Promedio [{estudiante['promedio']}]: ").strip()

    if nombre:
        estudiante["nombre"] = nombre

    if carrera:
        estudiante["carrera"] = carrera

    if semestre:
        if semestre.isdigit() and 1 <= int(semestre) <= 12:
            estudiante["semestre"] = int(semestre)
        else:
            print("El semestre no se actualizó porque no es válido.")

    if promedio:
        try:
            promedio_numero = float(promedio)

            if 0 <= promedio_numero <= 10:
                estudiante["promedio"] = promedio_numero
            else:
                print("El promedio no se actualizó porque debe estar entre 0 y 10.")

        except ValueError:
            print("El promedio no se actualizó porque no es numérico.")

    guardar_estudiantes()

    print("\nEstudiante actualizado correctamente.")


def eliminar_estudiante():
    print("\n===== ELIMINAR ESTUDIANTE =====")

    matricula = input("Matrícula del estudiante: ").strip()
    estudiante = buscar_por_matricula(matricula)

    if estudiante is None:
        print("\nNo se encontró ningún estudiante con esa matrícula.")
        return

    print("\nEstudiante encontrado:")
    print("Nombre    :", estudiante["nombre"])
    print("Matrícula :", estudiante["matricula"])

    confirmacion = input(
        "\n¿Está seguro de eliminar al estudiante? (s/n): "
    ).strip().lower()

    if confirmacion != "s":
        print("\nEliminación cancelada.")
        return

    estudiantes.remove(estudiante)
    guardar_estudiantes()

    print("\nEstudiante eliminado correctamente.")


def busqueda_avanzada():
    print("\n===== BÚSQUEDA AVANZADA =====")
    print("1. Buscar por matrícula")
    print("2. Buscar por nombre")
    print("3. Buscar por carrera")
    print("4. Buscar por semestre")

    opcion = input("Seleccione una opción: ").strip()

    criterios = {
        "1": "matricula",
        "2": "nombre",
        "3": "carrera",
        "4": "semestre"
    }

    criterio = criterios.get(opcion)

    if criterio is None:
        print("\nOpción no válida.")
        return

    valor = input("Ingrese el valor de búsqueda: ").strip().lower()
    resultados = []

    for estudiante in estudiantes:
        dato = str(estudiante.get(criterio, "")).lower()

        if valor in dato:
            resultados.append(estudiante)

    if not resultados:
        print("\nNo se encontraron estudiantes.")
        return

    print(f"\nSe encontraron {len(resultados)} estudiante(s).")

    for numero, estudiante in enumerate(resultados, start=1):
        print(f"\nResultado {numero}")
        print("Matrícula :", estudiante["matricula"])
        print("Nombre    :", estudiante["nombre"])
        print("Carrera   :", estudiante["carrera"])
        print("Semestre  :", estudiante["semestre"])
        print("Promedio  :", estudiante["promedio"])


def mostrar_estadisticas():
    print("\n===== ESTADÍSTICAS ESCOLARES =====")

    if not estudiantes:
        print("No hay estudiantes registrados.")
        return

    promedios = []

    for estudiante in estudiantes:
        try:
            promedios.append(float(estudiante["promedio"]))
        except (ValueError, TypeError):
            continue

    if not promedios:
        print("No existen promedios válidos.")
        return

    promedio_general = sum(promedios) / len(promedios)
    aprobados = sum(1 for promedio in promedios if promedio >= 6)
    reprobados = sum(1 for promedio in promedios if promedio < 6)
    promedio_mayor = max(promedios)
    promedio_menor = min(promedios)

    mejor_estudiante = None

    for estudiante in estudiantes:
        try:
            if float(estudiante["promedio"]) == promedio_mayor:
                mejor_estudiante = estudiante
                break
        except (ValueError, TypeError):
            continue

    print("Total de estudiantes  :", len(estudiantes))
    print(f"Promedio general      : {promedio_general:.2f}")
    print("Estudiantes aprobados :", aprobados)
    print("Estudiantes reprobados:", reprobados)
    print(f"Promedio más alto     : {promedio_mayor:.2f}")
    print(f"Promedio más bajo     : {promedio_menor:.2f}")

    if mejor_estudiante:
        print(
            "Mejor estudiante      :",
            mejor_estudiante["nombre"]
        )