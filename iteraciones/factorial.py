print("=== Calculadora de Factorial ===")

numero = int(input("Ingresa un número entero mayor o igual a 0: "))

if numero < 0:
    print("El número debe ser mayor o igual a 0.")
else:
    resultado = 1
    contador = 1

    while contador <= numero:
        resultado *= contador
        contador += 1

    print(f"El factorial de {numero} es: {resultado}")