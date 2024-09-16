def regla1(contraseña):
    if len(contraseña) <= 8:
        return False

    tiene_mayuscula = False
    for char in contraseña:
        if char.isupper():
            tiene_mayuscula = True
    return tiene_mayuscula


def regla2(contraseña):
    tiene_simbolo = False
    tiene_numero = False
    simbolos = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"

    for char in contraseña:
        if char in simbolos:
            tiene_simbolo = True

        if char.isdigit():
            tiene_numero = True

    return tiene_simbolo and tiene_numero


def regla3(contraseña):
    suma = 0
    for char in contraseña:
        if char.isdigit():
            suma += int(char)
    return suma > 20


def regla4(contraseña):
    jugadores = [
        "MESSI", "DI MARIA", "DE PAUL", "OTAMENDI", "MARTINEZ", "ALVAREZ",
        "MAC ALLISTER", "FERNANDEZ", "MOLINA", "ROMERO", "ACUÑA",
        "TAGLIAFICO", "PAREDES", "PEZZELLA", "RULLI", "ARMANI", "FOYTH",
        "CORREA", "PALACIOS", "MONTIEL", "GOMEZ", "DYBALA", "ALMADA",
        "RODRIGUEZ"
    ]
    for jugador in jugadores:
        if jugador in contraseña.upper():
            return True
    return False


def regla5(contraseña):
    for i in range(len(contraseña) - 2):
        if (contraseña[i] == contraseña[i + 1] ==
                contraseña[i + 2]):
            return True
    return False


def regla6(contraseña):
    numero_acertijo = "5"
    return numero_acertijo in contraseña
