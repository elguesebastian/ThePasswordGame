from colorama import init
from mensajes import (
    BIENVENIDA, INTRODUCCION, REGLA_CORRECTA, NUEVA_REGLA,
    VICTORIA, ERROR_CONTRASENA, REINTENTO, RONDA, mostrar_error_regla,
    FINAL_JUEGO, HISTORIAL, ESTADISTICA
)
import time

init(autoreset=True)


def verificar_reglas(contraseña, reglas_aplicadas):
    errores = []
    for descripcion, regla in reglas_aplicadas:
        if not regla(contraseña):
            errores.append(descripcion)
    return errores


def mostrar_historial(tiempo_total, errores_totales, intentos_totales, ronda):
    print(HISTORIAL)
    print(ESTADISTICA.format("Tiempo total jugado", str(round(tiempo_total, 2))
                             + " segundos"))
    print(ESTADISTICA.format("Total de errores cometidos",
                             str(errores_totales)))
    print(ESTADISTICA.format("Total de contraseñas intentadas",
                             str(intentos_totales)))
    print(ESTADISTICA.format("Rondas completadas", str(ronda)))
    print(FINAL_JUEGO)


def jugar(reglas):
    reglas_aplicadas = [reglas[0]]  # Arranca con la primera regla
    ronda = 1
    intentos_totales = 0
    errores_totales = 0
    juego_terminado = False

    print(BIENVENIDA)
    print(INTRODUCCION)
    print("Para finalizar el juego, introduce FIN.")
    print(f"\nRegla: {reglas_aplicadas[-1][0]}")

    # Registrar el tiempo de inicio
    tiempo_inicio = time.time()

    while not juego_terminado:
        print(RONDA.format(ronda))
        contraseña = input("Introduce una contraseña: ")

        if contraseña.upper() == "FIN":
            juego_terminado = True
        else:
            intentos_totales += 1
            errores = verificar_reglas(contraseña, reglas_aplicadas)

            if not errores:
                print(REGLA_CORRECTA)

                if len(reglas_aplicadas) < len(reglas):
                    reglas_aplicadas.append(reglas[len(reglas_aplicadas)])
                    print(NUEVA_REGLA, reglas_aplicadas[-1][0], "\n")
                    ronda += 1
                else:
                    print(VICTORIA)
                    juego_terminado = True
            else:
                print(ERROR_CONTRASENA)
                errores_totales += len(errores)
                for error in errores:
                    print(mostrar_error_regla(error))
                print(REINTENTO)

    # Registrar el tiempo de finalización
    tiempo_fin = time.time()
    tiempo_total = tiempo_fin - tiempo_inicio

    # Mostrar estadísticas del juego
    mostrar_historial(tiempo_total, errores_totales, intentos_totales, ronda)
