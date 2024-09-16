from colorama import Fore, Back, Style, init
from reglas import regla1, regla2, regla3, regla4, regla5, regla6

init(autoreset=True)


# Llamado a las reglas
reglas = [
    ("Debe tener contener más de 8 caracteres y al menos una letra mayúscula",
     regla1),
    ("Debe contener al menos un número y un símbolo (!, @, etc.).", regla2),
    ("La suma de los números debe ser mayor a 20.", regla3),
    ("Contener el apellido de un campeón del mundo de la selección argentina.",
     regla4),
    ("Debe tener una secuencia de tres letras iguales seguidas.", regla5),
    ("El doble de 3 más la mitad de 8, menos 5", regla6)
]


def verificar_reglas(contraseña, reglas_aplicadas):
    errores = []
    for descripcion, regla in reglas_aplicadas:
        if not regla(contraseña):
            errores.append(descripcion)
    return errores


def jugar():
    reglas_aplicadas = [reglas[0]]  # Arranca con la primer regla
    ronda = 1
    juego_terminado = False

    print(Fore.CYAN + Back.BLACK + Style.BRIGHT + "\nThe Password Game:")
    print(Fore.CYAN + Back.BLACK + Style.BRIGHT +
          "\nIntroduce una contraseña que cumpla con las siguientes reglas:")
    print(f"\nRegla: {reglas_aplicadas[-1][0]}")

    while not juego_terminado:
        print(Fore.WHITE + Style.BRIGHT + f"\nRonda {ronda}:")

        # Pedir contraseña
        contraseña = input("Introduce una contraseña: ")

        # Verifica las reglas
        errores = verificar_reglas(contraseña, reglas_aplicadas)

        if len(errores) == 0:
            print(Fore.LIGHTGREEN_EX + Back.BLACK +
                  Style.BRIGHT + "\n¡Contraseña correcta!")

            # Agrega nueva regla si quedan reglas por ganar
            if len(reglas_aplicadas) < len(reglas):
                reglas_aplicadas.append(reglas[len(reglas_aplicadas)])
                print(Fore.LIGHTBLUE_EX + Back.BLACK + Style.BRIGHT +
                      f"Nueva regla añadida: {reglas_aplicadas[-1][0]}\n")
                ronda += 1
            else:
                print(Fore.LIGHTGREEN_EX + Back.BLACK + Style.BRIGHT +
                      "¡Has ganado! Todas las reglas han sido aplicadas.")
                juego_terminado = True
        else:
            print(Fore.LIGHTRED_EX + Back.BLACK + Style.BRIGHT +
                  "\nLa contraseña no cumple con las siguientes reglas:")
            for error in errores:
                print(Fore.RED + f"- {error}")
            print("Por favor, inténtalo de nuevo.\n")


# Inicia el juego
jugar()
