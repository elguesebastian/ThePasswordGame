# Definición de reglas
def regla1(contraseña):
    if len(contraseña) > 8:
        return True
    else:
        return False

def regla2(contraseña):
    tiene_numero = False
    for char in contraseña:
        if char.isdigit():
            tiene_numero = True
    return tiene_numero

def regla3(contraseña):
    tiene_simbolo = False
    simbolos = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
    
    for char in contraseña:
        if char in simbolos:
            tiene_simbolo = True
    return tiene_simbolo

def regla4(contraseña):
    tiene_mayuscula = False
    for char in contraseña:
        if char.isupper():
            tiene_mayuscula = True
    return tiene_mayuscula

def regla5(contraseña):
    suma = 0
    for char in contraseña:
        if char.isdigit():
            suma += int(char)
    if suma > 20:
        return True
    else:
        return False

def regla6(contraseña):
    jugadores = ["MESSI", "DI MARIA", "DE PAUL", "OTAMENDI", "MARTINEZ", "ALVAREZ", 
             "MAC ALLISTER", "FERNANDEZ", 
             "MOLINA", "ROMERO", "ACUÑA", "TAGLIAFICO", "PAREDES", "PEZZELLA",
             "RULLI", "ARMANI", "FOYTH", "CORREA", 
             "PALACIOS", "MONTIEL", "GOMEZ", "DYBALA", "ALMADA", "RODRIGUEZ"]
    contiene_apellido = False
    for jugador in jugadores:
        if jugador in contraseña.upper():
            contiene_apellido = True
    return contiene_apellido

def regla7(contraseña):
    tiene_secuencia = False
    for i in range(len(contraseña) - 2):
        if contraseña[i] == contraseña[i+1] == contraseña[i+2]:
            tiene_secuencia = True
    return tiene_secuencia

def regla8(contraseña):
    acierta_numero = False
    numero_acertijo = "5"
    for char in contraseña:
        if char == numero_acertijo:
            acierta_numero = True            
    return acierta_numero

# Lista de reglas
reglas = [
    ("Debe tener más de 8 caracteres.", regla1),
    ("Debe incluir al menos un número.", regla2),
    ("Debe contener al menos un símbolo (!, @, etc.).", regla3),
    ("Debe tener al menos una letra mayúscula.", regla4),
    ("La suma de los números debe ser mayor a 20.", regla5),
    ("Debe contener el apellido de un campeón del mundo de la selección argentina.", regla6),
    ("Debe tener una secuencia de tres letras iguales seguidas.", regla7),
    ("El doble de 3 más la mitad de 8, menos 5", regla8)
]

def verificar_reglas(contraseña, reglas_aplicadas):
    errores = []
    for descripcion, regla in reglas_aplicadas:
        if not regla(contraseña):
            errores.append(descripcion)
    return errores

def jugar_contraseña():
    reglas_aplicadas = [reglas[0]]  # Empieza la primera regla
    ronda = 1
    juego_terminado = False  #Variable que controla si el juego termino

    while not juego_terminado:
        print("The Password Game:")
        print(f"\nRonda {ronda}:")
        
        # Muestra siempre las reglas actuales
        for i in range(len(reglas_aplicadas)):
            print(f"Regla {i+1}: {reglas_aplicadas[i][0]}")
        
        # Pide una contraseña
        contraseña = input("Introduce una contraseña: ")
        
        # Verifica las reglas
        errores = verificar_reglas(contraseña, reglas_aplicadas)
        
        if len(errores) == 0:
            print("\n¡Contraseña correcta!")
            
            # Agrega nueva regla si quedan reglas para acertar
            if len(reglas_aplicadas) < len(reglas):
                reglas_aplicadas.append(reglas[len(reglas_aplicadas)])
                print(f"Nueva regla añadida: {reglas_aplicadas[-1][0]}\n")
                ronda += 1
            else:
                print("¡Has ganado! Todas las reglas han sido aplicadas.")
                juego_terminado = True
        else:
            print("\nLa contraseña no cumple con las siguientes reglas:")
            for error in errores:
                print(f"- {error}")
            print("Por favor, inténtalo de nuevo.\n")
            # No cambia la ronda, el juego sigue en la misma ronda hasta que se cumplan todas las reglas anteriores.

# Inicia el juego
jugar_contraseña()
