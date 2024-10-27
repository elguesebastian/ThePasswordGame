from colorama import Fore, Back, Style

# Mensajes de inicio y bienvenida
BIENVENIDA = Fore.CYAN + Back.BLACK + Style.BRIGHT + "\nThe Password Game:"
INTRODUCCION = Fore.CYAN + Back.BLACK + Style.BRIGHT + (
    "\nIntroduce una contraseña que cumpla con las siguientes reglas:"
)

# Mensajes de reglas
REGLA_CORRECTA = Fore.LIGHTGREEN_EX + Back.BLACK + Style.BRIGHT + "\n¡Contraseña correcta!"
NUEVA_REGLA = Fore.LIGHTBLUE_EX + Back.BLACK + Style.BRIGHT + "Nueva regla añadida:"

# Mensajes de ganar juego
VICTORIA = Fore.LIGHTGREEN_EX + Back.BLACK + Style.BRIGHT + "¡Has ganado! Todas las reglas han sido aplicadas."

# Mensajes de error
ERROR_CONTRASENA = Fore.LIGHTRED_EX + Back.BLACK + Style.BRIGHT + "\nLa contraseña no cumple con las siguientes reglas:"
REINTENTO = "Por favor, inténtalo de nuevo.\n"

# Mensajes de ronda
RONDA = Fore.WHITE + Style.BRIGHT + "\nRonda {}:"

# Función para mostrar el error específico de reglas
def mostrar_error_regla(error):
    return Fore.RED + f"- {error}"
