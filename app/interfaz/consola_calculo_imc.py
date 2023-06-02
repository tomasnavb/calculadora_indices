from app.modulo import calculadora_indices as calc

# Mensaje de bienvenida
MENSAJE_DE_BIENVENIDA = "Bienvenido/a a la consola de calculo IMC"
calc.imprimir_mensaje_rectangular(MENSAJE_DE_BIENVENIDA)

# Cálculos
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
imc = calc.calcular_IMC(peso, altura)

# Resultados
print("RESULTADOS:")
print("Su índice de masa corporal (IMC) es de: ", imc)
