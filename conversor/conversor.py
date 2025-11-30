def convertir_temperatura():
    print("\n--- Conversor de Temperatura (°C ↔ °F) ---")
    valor = float(input("Ingresa el valor de la temperatura: "))
    tipo = input("¿Está en Celsius (C) o Fahrenheit (F)? ").strip().upper()

    if tipo == "C":
        resultado = (valor * 9/5) + 32
        print(f"{valor}°C equivalen a {resultado:.2f}°F")
    elif tipo == "F":
        resultado = (valor - 32) * 5/9
        print(f"{valor}°F equivalen a {resultado:.2f}°C")
    else:
        print("Unidad no válida. Usa C o F.")


def convertir_monedas():
    print("\n--- Conversor de Monedas (USD ↔ CLP) ---")
    valor = float(input("Ingresa la cantidad de dinero: "))
    tipo = input("¿Es USD o CLP? ").strip().upper()

    tasa = 950.0  # Ejemplo de tasa de cambio

    if tipo == "USD":
        resultado = valor * tasa
        print(f"{valor} USD equivalen a {resultado:.2f} CLP")
    elif tipo == "CLP":
        resultado = valor / tasa
        print(f"{valor} CLP equivalen a {resultado:.2f} USD")
    else:
        print("Moneda no válida. Usa USD o CLP.")


def menu():
    while True:
        print("\n=== Conversor de Unidades ===")
        print("1. Temperatura")
        print("2. Monedas")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            convertir_temperatura()
        elif opcion == "2":
            convertir_monedas()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")


# Inicio del programa
menu()
