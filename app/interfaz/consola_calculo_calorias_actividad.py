from app.modulo import calculadora_indices as calc

# Mensaje de bienvenida
MENSAJE_DE_BIENVENIDA = "Bienvenido/a a la calculadora de calorías en segun actividad"
calc.imprimir_mensaje_rectangular(MENSAJE_DE_BIENVENIDA)

# Calculos
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: ")) * 100
edad = int(input("Ingrese su edad: "))
valor_genero = int(input("Ingrese su valor género (5 para masculino, -161 para femenino): "))
valor_segun_actividad = int(input("""
A continuación se listan los valores de actividad:

- Si usted realiza poco o ningún ejercicio ingrese 1
- Si usted realiza ejercicio ligero (1 a 3 días por semana) ingrese 2
- Si usted realiza ejercicio moderado (3 a 5 días por semana) ingrese 3
- Si usted realiza ejercicio como un deportista (6 a 7 días por semana) ingrese 4
- Si usted realiza ejercicio como un atleta (entrenamientos mañana y tarde) ingrese 5

Opción: """))
valor_actividad = calc.valor_segun_actividad(valor_segun_actividad)

# Resultados
calorias_en_actividad = calc.calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad)
print("RESULTADOS:")
print(f"La cantidad de calorías que consume en actividad es de: {calorias_en_actividad} cal")
