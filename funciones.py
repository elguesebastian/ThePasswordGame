from colorama import init
from mensajes import (
    BIENVENIDA, INTRODUCCION, REGLA_CORRECTA, NUEVA_REGLA,
    VICTORIA, ERROR_CONTRASENA, REINTENTO, RONDA, mostrar_error_regla
)

init(autoreset=True)


def verificar_reglas(contraseña, reglas_aplicadas):
    errores = []
    for descripcion, regla in reglas_aplicadas:
        if not regla(contraseña):
            errores.append(descripcion)
    return errores


def jugar(reglas):
    reglas_aplicadas = [reglas[0]]  # Arranca con la primera regla
    ronda = 1
    juego_terminado = False

    print(BIENVENIDA)
    print(INTRODUCCION)
    print(f"\nRegla: {reglas_aplicadas[-1][0]}")

    while not juego_terminado:
        print(RONDA.format(ronda))
        contraseña = input("Introduce una contraseña: ")

        errores = verificar_reglas(contraseña, reglas_aplicadas)

        if not errores:
            print(REGLA_CORRECTA)

            # Agrega una nueva regla
            if len(reglas_aplicadas) < len(reglas):
                reglas_aplicadas.append(reglas[len(reglas_aplicadas)])
                print(NUEVA_REGLA, reglas_aplicadas[-1][0], "\n")
                ronda += 1
            else:
                print(VICTORIA)
                juego_terminado = True
        else:
            print(ERROR_CONTRASENA)
            for error in errores:
                print(mostrar_error_regla(error))
            print(REINTENTO)
