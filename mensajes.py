from colorama import Fore, Style

# Mensajes de inicio
BIENVENIDA = Fore.CYAN + Style.BRIGHT + "\nThe Password Game:"
INTRODUCCION = (
    Fore.CYAN + Style.BRIGHT +
    "\nIntroduce una contraseña que cumpla con las siguientes reglas:"
)
FINAL_JUEGO = (
    Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n{}\n"
)

# Mensajes de reglas
REGLA_CORRECTA = (
    Fore.LIGHTGREEN_EX + Style.BRIGHT +
    "\n¡Contraseña correcta!"
)
NUEVA_REGLA = (
    Fore.LIGHTBLUE_EX + Style.BRIGHT +
    "Nueva regla añadida:"
)

# Mensajes de ganar juego
VICTORIA = (
    Fore.LIGHTGREEN_EX + Style.BRIGHT +
    "¡Has ganado! Todas las reglas han sido aplicadas."
)

# Mensajes de error
ERROR_CONTRASENA = (
    Fore.LIGHTRED_EX + Style.BRIGHT +
    "\nLa contraseña no cumple con las siguientes reglas:"
)
REINTENTO = "Por favor, inténtalo de nuevo.\n"

# Mensaje para la ronda
RONDA = Fore.WHITE + Style.BRIGHT + "\nRonda {}:"

# Mensajes de estadísticas
HISTORIAL = (
    Fore.LIGHTCYAN_EX + Style.BRIGHT + "\nEstadísticas del juego:\n"
)
ESTADISTICA = (
    Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "- {}: {}"
)


# Función para mostrar el error
def mostrar_error_regla(error):
    return Fore.RED + f"- {error}"
