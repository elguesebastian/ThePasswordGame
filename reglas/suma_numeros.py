def suma_mayor_20(contraseña):
    suma = 0
    for char in contraseña:
        if char.isdigit():
            suma += int(char)
    return suma > 20
