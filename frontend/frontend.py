# Importación para poder limpiar la pantalla de la app
import os
# Importamos colorama para poder utilizar colores en la terminal
from colorama import Fore, Back, init, Style
init(autoreset=True) # Inicializa colorama para que los colores se reinicien automáticamente después de cada impresión
from backend.backend import *
from backend.mostrar_listado import *
from backend.validar_op_menu import *
from backend.pd_pandas import *

# Función del menú principal del programa. 
def menu():
    """
    Función principal de la app, donde está el menú principal de opciones para interactuar con el usuario.

    Args: opciones_menu: str => valida por validar_opcion_menu() y se convierte en int

    Returns: Ejecuta la opción/función seleccionada por el usuario
    """

    while True:
        # Opciones del menú principal
        print(Style.BRIGHT + Fore.BLUE +f'\nPor favor, indique la opción deseada: ')
        print(f'\nSi desea agregar un producto, presione 1.\nSi desea visualizar el listado de sus productos, presione 2.\nSi desea buscar un producto, presione 3.\nSi desea modificar un producto, presione 4.\nSi desea eliminar un producto, presione 5.\nSi desea limpiar la consola para una mejor visualización, presion 6.\nSi desea salir del programa, presione 7.')
        
        # Llama  a la función "validar_opcion_menu()" para que el usuario ingrese una opción y valide la entrada.
        opciones_menu= validar_opcion_menu()

        # Redirecciona a la función del menú deseada de acuerdo al input del usuario.
        match opciones_menu:
            case 1:
                # Llama a la función "agregar_productos" para que se ejecute
                agregar_productos()
            case 2:
                # Llama a la función "mostrar_listado_menu()" para que se ejecute
                mostrar_listado_menu()
            case 3:
                # Llama a la función "buscador_de_productos_menu()" para que se ejecute
                buscador_de_productos_menu()
            case 4:
                # Llama a la función "modificar_producto()" para que se ejecute
                modificar_producto()
            case 5:
                # Llama a la función "eliminar_producto()" para que se ejecute
                eliminar_producto()
            case 6:
                # Llama a la función "limpiar_pantalla_consola" para que se ejecute
                limpiar_pantalla_consola()
            case 7:
                # Se despide del usuario con estilo y sale de la app
                print(Style.RESET_ALL +  Fore.LIGHTYELLOW_EX +'\nHasta la vista, baby \U0001F60E')
                exit()
            case _:
                # Por si el usuario flashea
                print(Fore.RED + "\U0001F620 No ingresó una opción válida.")
            
        
# Función Menú de Bienvenida
def menu_de_bienvenida(menu):
    """
    Función menú_de_bienvenida(). Primer pantalla que ve el usuario donde se le da una bienvenida y llama a la función menu() para que el usuario elija qué realizar en la app.
    """
    # Limpia la pantalla de la consola para iniciar el programa y tener una visual limpia
    limpiar_pantalla_consola()
    # Damos la bienvenida al programa.
    print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX +'\n¡Bienvenidos al progama de administración de productos de su negocio!')
    menu()
    
# Función para limpiar la pantalla de la consola y tener un usuario feliz
def limpiar_pantalla_consola():
    """
    Función para limpiar la pantalla de la consola de acuerdo al sistema operativo en donde se está utilizando la app.
    """
    # verifica si el sistema operativo es windows
    if os.name== 'nt':
        #ejecuta el comando cls para limpiar la pantalla
        os.system('cls')
    else:
        # Para Linux y macOs ejecuta el comando clear para limpiar la pantalla
        os.system('clear')


# Función Nº 2 del menú. Llama a la función "mostrar_listado_de_productos" la cual muestra el listado completo del productos en la terminal desde el menú del inicio
def mostrar_listado_menu():
    """
    Función Nº2 del menú mostrar_listado_menu() de la app, ofrece un menú de opciones de visualización de datos: listado completo, listado ordenado por precio o nombre ascendente o descendente.

    Args: opciones_menu: str => valida por validar_opcion_menu() y se convierte en int

    Returns: Ejecuta la opción/función mostrar_listado_de_productos() o mostrar_listado_ord() seleccionada por el usuario y devuelve llave y modo de acuerdo a lo elegido por el usuario en el menú.
    """
    while True:
        # Opciones del menú principal
        print(Style.BRIGHT + Fore.BLUE +f'\nPor favor, indique la opción deseada: ')
        print(f'\nSi desea ver el listado completo de productos, presione 1.\nSi desea visualizar el listado de productos por precio ascendente, presione 2.\nSi desea visualizar el listado de productos por precio descendente, presione 3.\nSi desea visualizar el listado de productos por orden alfabético ascendente, presione 4.\nSi desea visualizar el listado de productos por orden alfabético descendente, presione 5.\nSi desea ver un gráfico de qué tipo de productos tiene en su lista, presione 6. \nSi desea ver un gráfico de barras de sus productos y precios, precione 7.\nSi desea regrear al menú principal, presione 8.')
        
        # Llama  a la función "validar_opcion_menu()" para que el usuario ingrese una opción y valide la entrada.
        opciones_menu= validar_opcion_menu()

        # Redirecciona a la función del menú deseada de acuerdo al input del usuario.
        match opciones_menu:
            case 1:
                # Llama a la función "mostrar_listado_de_productos" para que se ejecute
                mostrar_listado_de_productos()
            case 2:
                # Llama a la función "mostrar_listado_ord()" 
                llave = 'precio'
                modo='ASC'
                mostrar_listado_ord(llave, modo)
            case 3:
                # Llama a la función "mostrar_listado_ord()" 
                llave = 'precio'
                modo = 'DESC'
                mostrar_listado_ord(llave, modo)
                
            case 4:
                # Llama a la función "mostrar_listado_ord()" 
                llave = 'nombre'
                modo='ASC'
                mostrar_listado_ord(llave, modo)
                
            case 5:
                # Llama a la función "mostrar_listado_ord()" 
                llave = 'nombre'
                modo = 'DESC'
                mostrar_listado_ord(llave, modo)

            case 6:
                # Llama a la función "grafico_tipo_productos()"
                grafico_tipo_productos()

            case 7:
                # Regresa al menú principal
                graf_barras_prod_prec()
            
            case 8:
                # Regresa al menú principal
                break

            case _:
                # Por si el usuario flashea
                print(Fore.RED + "\U0001F620 No ingresó una opción válida.")
        #return llave
    

# Función Nº 3 del Menú principal, llama a la función "buscador_de_productos" para buscar productos en el listado general
def buscador_de_productos_menu():
    """
    Función Nº3 del Menú principal, llama a la función buscador_de_productos()
    """
    # Texto de bienvenida a la función del buscador desde el menú principal
    print(Style.RESET_ALL + Style.BRIGHT +'\nBienvenido al buscador de productos.\n')
    buscador_de_productos()