
# Calculadora de índices corporales

Este proyecto consta de un módulo que proporciona funciones para el cálculo del índice de masa corporal (IMC), el porcentaje de grasa corporal,
las calorías en reposo, las calorías según la actividad y el consumo de calorías recomendado para adelgazar.
Además, cuenta con una interfaz de usuario simple por consola, realizada a modo de test para probar las funciones del módulo.
Este es un proyecto simple realizado para la materia Python, haciendo foco en conocer el uso de módulos, funciones y buenas prácticas del lengüaje.

Funciones disponibles:
- `calcular_IMC(peso, altura)`: Calcula el índice de masa corporal dado el peso y la altura.
- `calcular_porcentaje_grasa(peso, altura, edad, valor_genero)`: Calcula el porcentaje de grasa corporal (%gc) basado
   en el IMC, edad y valor de género.
- `calcular_calorias_en_reposo(peso, altura, edad, valor_genero)`: Calcula las calorías en reposo o tasa metabólica
   basal (TMB) según el peso, altura, edad y valor de género.
- `calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad)`: Calcula las calorías según la
   actividad física considerando la TMB y el valor de actividad.
- `consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero)`: Calcula el rango de consumo de
   calorías recomendado para adelgazar en base a la TMB.
- `valor_segun_actividad(opcion)`: Retorna el valor de actividad correspondiente a una opción dada.

La función `imprimir_mensaje_rectangular(mensaje)` se utiliza para imprimir un mensaje envuelto en un rectángulo de
asteriscos.

Las funciones auxiliares y constantes internas están incluidas para apoyar el cálculo y la lógica de las funciones
principales.

Este módulo puede ser utilizado para realizar cálculos relacionados con la salud y el bienestar personal.


## Modo de uso

Para hacer uso de este proyecto:

- Clonar en repositorio
- Ejecutar individualmente cada uno de los archivos que se encuentran situados en el directorio "interfaz".


## Lengüaje

* Python


## Autor

- [@Tomás Navarro](https://www.github.com/tomasnavb)

