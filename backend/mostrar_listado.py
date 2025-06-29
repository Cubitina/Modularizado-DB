from frontend.frontend import *
from backend.backend import *
from backend.conectar_db import *
# Importamos sqlite para poder acceder a la base de datos
import sqlite3
from colorama import init, Style, Back
# Inicializa colorama para que los colores se reinicien automáticamente después de cada impresión
init(autoreset=True)

# Nombre de la base de datos
productos_db = "productos.db"

# Función para mostrar el listado completo de productos en la terminal.


def mostrar_listado_de_productos():
    """
    Función para mostrar el listado completo de productos de la db

    Args: productos

    Returns: lista de productos
    """
    # Conectar a la base de datos
    conexion = conectar_db(productos_db)
    # conexion = sqlite3.connect("productos.db")
    cursor = conexion.cursor()
    # print(f'Se ha conectado a la base de datos exitosamente')
    try:
        # Mostrar todos los productos de la base de datos
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()

        if len(productos) == 0:
            print('\U0001F620 No hay productos registrados')
        else:
            print(Style.RESET_ALL + Style.BRIGHT + '\nProductos registrados: ')
            for producto in productos:
                if producto[4]<= 5:
                    print(Style.RESET_ALL + Back.YELLOW +f'\n---- Bajo Stock ----\nCódigo del producto: Nº{producto[0]} \nProducto:  {producto[1].capitalize()} \nCategoría: {producto[2].capitalize()}\nPrecio:\t   ${producto[3]}\nStock:\t   {producto[4]}\nFecha de incorporación: {producto[5]}.\n ')
                else:
                    print(Style.RESET_ALL +
                    f'\nCódigo del producto: Nº{producto[0]} \nProducto:  {producto[1].capitalize()} \nCategoría: {producto[2].capitalize()}\nPrecio:\t   ${producto[3]}\nStock:\t   {producto[4]}\nFecha de incorporación: {producto[5]}.\n')

    finally:
        # Cerramos la conexión para evitar problemas futuros
        if conexion:
            conexion.close()
            # print(f'Base de datos {productos_db} cerrada.')


def mostrar_listado_ord(llave, modo):
    """
    Función para mostrar listado ordenado de productos por precio o nombre y por orden ascendente o descendente según lo elegido por el usuario en el menú de la función mostrar_productos_menu()

    Args: llave: str; modo: str.

    Returns: listado de productos ordenado
    """
    # Conectar a la base de datos
    conexion = conectar_db(productos_db)
    # conexion = sqlite3.connect("productos.db")
    cursor = conexion.cursor()
    # Sacamos las comillas a llave para que pueda utilizarlo cuando modifico la base de datos
    llave_sc = llave.replace("'", "")
    modo_sc = modo.replace("'", "")

    try:
        # Mostrar todos los productos de la base de datos
        cursor.execute(
            f"SELECT * FROM productos ORDER BY {llave_sc} {modo_sc}")
        prod_prec_asc = cursor.fetchall()
        if len(prod_prec_asc) == 0:
            print('\U0001F620 No hay productos registrados')
        else:
            print(Style.RESET_ALL + Style.BRIGHT + '\nProductos registrados: ')
            for producto in prod_prec_asc:
                if producto[4]<= 5:
                    print(Style.RESET_ALL + Back.YELLOW +f'\n---- Bajo Stock ----\nCódigo del producto: Nº{producto[0]} \nProducto:  {producto[1].capitalize()} \nCategoría: {producto[2].capitalize()}\nPrecio:\t   ${producto[3]}\nStock:\t   {producto[4]}\nFecha de incorporación: {producto[5]}.\n ')
                else:
                    print(Style.RESET_ALL +
                    f'\nCódigo del producto: Nº{producto[0]} \nProducto:  {producto[1].capitalize()} \nCategoría: {producto[2].capitalize()}\nPrecio:\t   ${producto[3]}\nStock:\t   {producto[4]}\nFecha de incorporación: {producto[5]}.\n')
    finally:
        # Cerramos la conexión para evitar problemas futuros
        if conexion:
            conexion.close()
            # print(f'Base de datos {productos_db} cerrada.')


def mostrar_stock_bajo():
    """
    Función para mostrar listado de productos con stock bajo

    Args: productos.db

    Returns: Listado de productos bajos en stock
    """
    # Conectar a la base de datos
    conexion = conectar_db(productos_db)
    # conexion = sqlite3.connect("productos.db")
    cursor = conexion.cursor()

    try:
        # Mostrar todos los productos de la base de datos
        cursor.execute(f"SELECT * FROM productos WHERE stock <= 5")
        prod_bajo_stock = cursor.fetchall()
        if len(prod_bajo_stock) == 0:
            print(Style.RESET_ALL +f'\U0001F600 No hay productos bajos en stock')
        else:
            print(Style.RESET_ALL + Style.BRIGHT +
                  '\n\U0001F631 Productos bajos en stock: ')
            for producto in prod_bajo_stock:
                print(Style.RESET_ALL + Back.YELLOW + f'\nCódigo del producto: Nº{producto[0]} \nProducto:  {producto[1].capitalize()} \nCategoría: {producto[2].capitalize()}\nPrecio:\t   ${producto[3]}\nStock:\t   {producto[4]}\nFecha de incorporación: {producto[5]}.\n ')
    finally:
        # Cerramos la conexión para evitar problemas futuros
        if conexion:
            conexion.close()
            # print(f'Base de datos {productos_db} cerrada.')
