def contiene_color(contraseña):
    colores = [
        "rojo", "azul", "amarillo",
        "naranja", "verde", "morado"
    ]
    for color in colores:
        if color in contraseña.lower():
            return True
    return False
