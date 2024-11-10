def tiene_simbolo_y_numero(contraseña):
    tiene_simbolo = False
    tiene_numero = False
    simbolos = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"

    for char in contraseña:
        if char in simbolos:
            tiene_simbolo = True

        if char.isdigit():
            tiene_numero = True

    return tiene_simbolo and tiene_numero
