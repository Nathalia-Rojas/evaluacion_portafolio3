print("=== Formulario de Registro ===")

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
estatura = float(input("Ingresa tu estatura en metros (ej: 1.56): "))

respuesta = input("¿Te gusta programar? (si/no): ").strip().lower()
gusta_programar = respuesta == "si"  # True si responde 'si', False si responde cualquier otra cosa

print("\n--- Información Registrada ---")
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(f"Estatura: {estatura} m")
print(f"¿Le gusta programar?: {gusta_programar}")
