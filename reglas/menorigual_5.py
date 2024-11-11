def suma_no_mayor_5(contraseña):
    suma = 0
    for char in contraseña:
        if char.isdigit():
            suma += int(char)
    return suma <= 5
