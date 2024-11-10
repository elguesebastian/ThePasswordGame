def tiene_tres_caracteres_repetidos(contraseña):
    for i in range(len(contraseña) - 2):
        if (contraseña[i] == contraseña[i + 1] ==
                contraseña[i + 2]):
            return True
    return False
