contactos = {}

def mostrar_menu():
    print("\n=== Agenda de Contactos ===")
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Buscar contacto")
    print("4. Salir")

def agregar_contacto():
    nombre = input("Nombre del contacto: ")
    telefono = input("Teléfono: ")
    contactos[nombre] = telefono
    print("Contacto guardado.")

def mostrar_contactos():
    if not contactos:
        print("No hay contactos.")
    else:
        for nombre, telefono in contactos.items():
            print(f"{nombre}: {telefono}")

def buscar_contacto():
    nombre = input("Nombre a buscar: ")
    if nombre in contactos:
        print(f"{nombre}: {contactos[nombre]}")
    else:
        print("Contacto no encontrado.")

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        agregar_contacto()
    elif opcion == "2":
        mostrar_contactos()
    elif opcion == "3":
        buscar_contacto()
    elif opcion == "4":
        print("Adiós.")
        break
    else:
        print("Opción no válida.")