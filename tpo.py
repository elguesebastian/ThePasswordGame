from reglas import regla1, regla2, regla3, regla4, regla5, regla6
from funciones import jugar

# Llamado a las reglas
reglas = [
    ("Debe tener más de 8 caracteres y al menos una letra mayúscula", regla1),
    ("Debe contener al menos un número y un símbolo (!, @, etc.)", regla2),
    ("La suma de los números debe ser mayor a 20", regla3),
    ("Contener el apellido de un campeón del mundo de la "
     "selección argentina", regla4),
    ("Debe tener una secuencia de tres letras iguales seguidas", regla5),
    ("El doble de 3 más la mitad de 8, menos 5", regla6)
]

# Inicia el juego
jugar(reglas)
