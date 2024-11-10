def contiene_jugador_campeon(contraseña):
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
