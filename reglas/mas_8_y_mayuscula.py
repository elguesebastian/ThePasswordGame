def tiene_ocho_y_mayuscula(contraseña):
    if len(contraseña) <= 8:
        return False

    tiene_mayuscula = False
    for char in contraseña:
        if char.isupper():
            tiene_mayuscula = True
    return tiene_mayuscula
