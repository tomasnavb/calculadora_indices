"""
Este módulo proporciona funciones para el cálculo del índice de masa corporal (IMC), el porcentaje de grasa corporal,
las calorías en reposo, las calorías según la actividad y el consumo de calorías recomendado para adelgazar.

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
"""


def calcular_IMC(peso: float, altura: float) -> float:
    """
    Calcula el Índice de Masa Corporal (IMC) dado el peso y la altura.
    :param peso: Peso en kilogramos.
    :param altura: Altura en metros.
    :return: Valor del IMC redondeado a dos decimales.
    """
    imc = round(peso / altura ** 2, 2)
    return imc


def calcular_porcentaje_grasa(peso: float, altura: float, edad: int, valor_genero: float) -> float:
    """
    Calcula el porcentaje de grasa corporal (%GC) basado en el IMC, edad y valor de género.
    :param peso: Peso en kilogramos.
    :param altura: Altura en metros.
    :param edad: Edad en años.
    :param valor_genero: Valor correspondiente al género (10.8 para masculino, 0 para femenino, 5 para masculino alternativo, -161 para femenino alternativo).
    :return: Valor del porcentaje de grasa corporal (%GC) redondeado a dos decimales.
    """
    imc = calcular_IMC(peso, altura)
    gc = round(1.2 * imc + 0.23 * edad - 5.4 - valor_genero, 2)
    return gc


def calcular_calorias_en_reposo(peso: float, altura: float, edad: int, valor_genero: int) -> float:
    """
    Calcula las calorías en reposo o Tasa Metabólica Basal (TMB) según el peso, altura, edad y valor de género.
    :param peso: Peso en kilogramos.
    :param altura: Altura en metros.
    :param edad: Edad en años.
    :param valor_genero: Valor correspondiente al género (10.8 para masculino, 0 para femenino, 5 para masculino alternativo, -161 para femenino alternativo).
    :return: Valor de las calorías en reposo o Tasa Metabólica Basal (TMB) redondeado a dos decimales.
    """
    tmb = round((10 * peso) + (6.25 * altura) - (5 * edad) + valor_genero, 2)
    return tmb


def calcular_calorias_en_actividad(peso: float, altura: float, edad: int, valor_genero: int,
                                   valor_actividad: float) -> float:
    """
    Calcula las calorías según la actividad física considerando la TMB y el valor de actividad.
    :param peso: Peso en kilogramos.
    :param altura: Altura en metros.
    :param edad: Edad en años.
    :param valor_genero: Valor correspondiente al género (10.8 para masculino, 0 para femenino, 5 para masculino alternativo, -161 para femenino alternativo).
    :param valor_actividad: Valor correspondiente al nivel de actividad física.
    :return: Valor de las calorías según la actividad redondeado a dos decimales.
    """
    tmb = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    tmb_segun_actividad = round(tmb * valor_actividad, 2)
    return tmb_segun_actividad


def consumo_calorias_recomendado_para_adelgazar(peso: float, altura: float, edad: int, valor_genero: int) -> str:
    """
    Calcula el rango de consumo de calorías recomendado para adelgazar en base a la TMB.
    :param peso: Peso en kilogramos.
    :param altura: Altura en metros.
    :param edad: Edad en años.
    :param valor_genero: Valor correspondiente al género (10.8 para masculino, 0 para femenino, 5 para masculino alternativo, -161 para femenino alternativo).
    :return: Mensaje que indica el rango de consumo de calorías recomendado para adelgazar.
    """
    tmb = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    rango_inferior = round(tmb - (tmb * 20 / 100), 2)
    rango_superior = round(tmb - (tmb * 15 / 100), 2)
    return f"Para adelgazar es recomendado que consumas entre {rango_inferior} y {rango_superior} calorías al día"


# Funciones auxiliares
def valor_segun_actividad(opcion: int) -> float:
    """
    Retorna el valor de actividad correspondiente a una opción dada.
    :param opcion: Opción de actividad (1 para poca actividad, 2 para actividad ligera, 3 para actividad moderada, 4 para actividad de deportista, 5 para actividad de atleta).
    :return: Valor de actividad correspondiente a la opción.
    """
    poca_actividad = 1.2
    ligera_actividad = 1.375
    moderada_actividad = 1.55
    deportista_actividad = 1.725
    atleta_actividad = 1.9

    match opcion:
        case 1:
            return poca_actividad
        case 2:
            return ligera_actividad
        case 3:
            return moderada_actividad
        case 4:
            return deportista_actividad
        case 5:
            return atleta_actividad
        case _:
            raise ValueError("Opción inválida. Por favor, seleccione una opción válida.")


def imprimir_mensaje_rectangular(mensaje: str) -> None:
    """
    Imprime un mensaje rodeado de un borde rectangular hecho de asteriscos.
    :param mensaje: El mensaje a imprimir.
    :return: None
    """
    lineas_mensaje = mensaje.split('\n')
    longitud_maxima = max(len(linea) for linea in lineas_mensaje)

    print('*' * (longitud_maxima + 4))
    for linea in lineas_mensaje:
        print(f'* {linea.ljust(longitud_maxima)} *')
    print('*' * (longitud_maxima + 4))
