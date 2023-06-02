from app.modulo import calculadora_indices as calc

# Mensaje de bienvenida
MENSAJE_DE_BIENVENIDA = "Bienvenido/a a la calculadora de calorías en reposo"
calc.imprimir_mensaje_rectangular(MENSAJE_DE_BIENVENIDA)

# Calculos
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: ")) * 100
edad = int(input("Ingrese su edad: "))
valor_genero = int(input("Ingrese su valor género (5 para masculino, -161 para femenino): "))

# Resultados
calorias_en_reposo = calc.calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
print("RESULTADOS:")
print(f"La cantidad de calorías que consume en reposo es de: {calorias_en_reposo} cal")
