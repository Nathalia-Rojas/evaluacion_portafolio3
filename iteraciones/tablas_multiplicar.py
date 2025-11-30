print("=== Generador de Tabla de Multiplicar ===")

numero = int(input("Ingresa un número: "))

for i in range(1, 13):
    print(f"{numero} x {i} = {numero * i}")