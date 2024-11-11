from reglas.mas_8_y_mayuscula import tiene_ocho_y_mayuscula
from reglas.simbolo_y_numero import tiene_simbolo_y_numero
from reglas.suma_numeros import suma_mayor_20
from reglas.jugador_campeon import contiene_jugador_campeon
from reglas.mes_año import contiene_mes
from reglas.tres_repetidos import tiene_tres_caracteres_repetidos
from reglas.acertijo_numero import contiene_numero_acertijo
from reglas.color_hex import contiene_color_hex
from reglas.numero_romano import contiene_numero_romano
from reglas.principio_y_fin import tiene_principio_y_fin

# Llamado a las reglas
reglas = [
    ("Debe tener más de 8 caracteres y al menos una letra mayúscula",
     tiene_ocho_y_mayuscula),
    ("Debe contener al menos un número y un símbolo (!, @, etc.)",
     tiene_simbolo_y_numero),
    ("La suma de los números debe ser mayor a 20", suma_mayor_20),
    ("Contener el apellido de un campeón del mundo de la "
     "selección argentina", contiene_jugador_campeon),
    ("Debe contener algun mes del año", contiene_mes),
    ("Debe tener una secuencia de tres letras iguales seguidas",
     tiene_tres_caracteres_repetidos),
    ("Contener el color blanco o el color negro en hexadecimal",
     contiene_color_hex),
    ("Tiene que contener el 26 en numero romano", contiene_numero_romano),
    ("El doble de 3 más la mitad de 8, menos 5", contiene_numero_acertijo),
    ("La contraseña debe comenzar con un numero y finalizar con una letra",
     tiene_principio_y_fin)
]
