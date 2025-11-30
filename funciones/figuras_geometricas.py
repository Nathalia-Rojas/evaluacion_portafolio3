def area_cuadrado(lado):
    return lado * lado

def area_rectangulo(base, altura):
    return base * altura

def area_circulo(radio):
    pi = 3.14159
    return pi * radio ** 2

while True:
    print("\n=== Cálculo de Áreas ===")
    print("1. Cuadrado")
    print("2. Rectángulo")
    print("3. Círculo")
    print("4. Salir")
    
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        lado = float(input("Lado del cuadrado: "))
        print(f"Área: {area_cuadrado(lado):.2f}")
    elif opcion == "2":
        base = float(input("Base: "))
        altura = float(input("Altura: "))
        print(f"Área: {area_rectangulo(base, altura):.2f}")
    elif opcion == "3":
        radio = float(input("Radio: "))
        print(f"Área: {area_circulo(radio):.2f}")
    elif opcion == "4":
        print("Hasta la próxima.")
        break
    else:
        print("Opción no válida.")