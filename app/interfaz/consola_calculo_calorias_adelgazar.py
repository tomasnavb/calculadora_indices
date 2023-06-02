from app.modulo import calculadora_indices as calc

# Mensaje de bienvenida
MENSAJE_DE_BIENVENIDA = "Bienvenido/a a la calculadora de calorías para adelgazar"
calc.imprimir_mensaje_rectangular(MENSAJE_DE_BIENVENIDA)

# Calculos
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: ")) * 100
edad = int(input("Ingrese su edad: "))
valor_genero = int(input("Ingrese su valor género (5 para masculino, -161 para femenino): "))

# Resultados
calorias_en_reposo = calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero)
print("RESULTADOS:")
print(calorias_en_reposo)
