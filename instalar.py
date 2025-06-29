from backend.crear_db import *
from frontend.frontend import *
from main import *
import time

def instalar_programa():
    """
    Función para instalar el programa y la base de datos en la computadora del usuario.

    Args: instalar, str

    Returns: Programa y Base de datos instalada. Caso contrario, sale de la función.
    """
    # Limpiamos la pantalla de la consola para tener una mejor experiencia de usuario
    limpiar_pantalla_consola()

    # Damos la bienvenida a la instalación del programa
    print('\nBienvenido al programa de instalación de su programa para administrar los productos de su negocio')

    # Generamos la variable instalar para saber si el usuario quiere instalar la app. Ese input lo pasa a lower y le saca los espacios
    instalar=input('\n¿Desea instalar el programa?\nEn caso afirmativo, por favor, escriba "si": ').lower().strip()

    # Si la entrada no es si lo saca del programa. De lo contrario, llama a la función crear_tabla() que le va a permitir crear la db y las tablas.
    if instalar != 'si':
        print('\n\nA continuación saldrá del programa de instalación. Hasta luego.')
        exit()
    crear_tabla()

    # Muestra mensaje de redireccionamiento al programa con una espera de 5 segundos antes de que se ejecute la función "menu_de_bienvenida()"
    print('\n\nPrograma instalado exitosamente.\nA continuación inciaremos el programa. Muchas gracias por elegirnos.')
    time.sleep(5)
    menu_de_bienvenida(menu)
