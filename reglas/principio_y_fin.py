def tiene_principio_y_fin(contraseña):
    if contraseña[0].isdigit() and contraseña[-1].isalpha():
        return True
    else:
        return False
