# Importamos colorama para poder utilizar colores en la terminal
from colorama import Fore, Back, init, Style
init(autoreset=True) # Inicializa colorama para que los colores se reinicien 


def validar_opcion_menu():
    """
    Función para validar las opciones de menú

    Args: opcion_menu():str

    Returns: opcion_menu_int():int validado
    """
    while True:
        # Variable para ingresar la opción del menú
        opcion_menu= input(Fore.BLUE +'\n\nPor favor, ingrese su opción aquí: ').strip()
        # Evitamos el error de la app si el usuario ingresa un string.
        if type(opcion_menu)== str and not opcion_menu.isdigit():
            print(Fore.RED + "Error. Por favor, ingrese el número indicado.\n")
        # Evitamos el error de la app si el usuario no ingresa datos.
        elif opcion_menu == '' and not opcion_menu.isdigit():
            print(Fore.RED + "Error. Por favor, ingrese el número indicado.\n")
        # Si la entrada es un número, sale del búcle y continúa con el código
        elif opcion_menu.isdigit():
            opcion_menu_int = int(opcion_menu)
            if opcion_menu_int >0:
                return opcion_menu_int