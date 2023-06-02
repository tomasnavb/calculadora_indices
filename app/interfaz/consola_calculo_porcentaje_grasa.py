from app.modulo import calculadora_indices as calc

# Mensaje de bienvenida
MENSAJE_DE_BIENVENIDA = "Bienvenido/a a la calculadora de porcentaje de grasa (%GC)"
calc.imprimir_mensaje_rectangular(MENSAJE_DE_BIENVENIDA)

# Calculos
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
edad = int(input("Ingrese su edad: "))
valor_genero = float(input("Ingrese su valor género (10,8 para masculino, 0 para femenino): "))

# Resultados
gc = calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero)
print("RESULTADOS:")
print(f"Su porcentaje de grasa corporal es de {gc}%")




