def menu():
    participantes = []
    op = 0
    while op != 4:
        print("\n--- MENÚ DE OPCIONES ---")
        print("1. Agregar participante")
        print("2. Mostrar participantes ordenados por nombre")
        print("3. Mostrar participantes ordenados por edad")
        print("4. Salir")
        opcion = int(input("Seleccione una opción: "))

        match op:
            case 1:
                agregar_participante(participantes)
            case 2:
                break
            case 3:
                break
            case 4:
                 print("Nos  vemos")
            case _:
                print("Ingrese una opción válida")

def ordenar_participantesedad(lista):
    if len(lista) <= 1:
        return lista[:]
    pivote = lista[0]
    menores = [x for x in lista[1:] if x < pivote]
    iguales = [x for x in lista if x == pivote]  # incluye el pivote y otras iguales
    mayores = [x for x in lista[1:] if x > pivote]
    return ordenar_participantesedad(menores) + iguales + ordenar_participantesedad(mayores)


def agregar_participante(participantes):
    ingreso = int(input("¿Cuantos participantes desea ingresar? : "))
    for i in range (ingreso):
        while True:
            dorsal = int(input("Ingrese número de dorsal:   "))
            if dorsal in participantes:
                print(f"El dorsal {dorsal} ya está registrado. Intente con otro.")
            else:
                break
        nombre = input("Ingrese nombre completo: ")
        while True:
            edad = int(input("Ingrese edad: "))
            if edad < 0 or edad > 100:
                print("El edad debe ser entre 0 y 100")
            else:
                break
        while True:
            categorias = {"juvenil": "Juvenil", "adulto": "Adulto", "máster": "Máster"}
            categoria = input("Ingrese categoría (juvenil, adulto, máster): ")
            if categoria not in categorias:
                print("Categoría inválida. Use: juvenil, adulto o máster.")
            else:
                break
        categoria = categorias[categoria]
        participante = {
            "dorsal": dorsal,
            "nombre": nombre,
            "edad": edad,
            "categoria": categoria
        }
        participantes.append(participante)

