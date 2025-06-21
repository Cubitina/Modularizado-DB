
from backend.mostrar_listado import *
from backend.validar_op_menu import *
from backend.conectar_db import *
from main import *

# Importar para poder utilizar datos de fecha y hora
import datetime
# Importamos colorama para poder utilizar colores en la terminal
from colorama import Fore, Back, init, Style
# Inicializa colorama para que los colores se reinicien automáticamente después de cada impresión
init(autoreset=True)

# Nombre de la base de datos
productos_db = "productos.db"

# Función Nº1 del Menú. Esta permite ingresar productos a la lista de productos.
def agregar_productos():
    """
    Función Nº1 del Menú. Esta permite ingresar productos a la tabla productos de la base de datos.
    Luego de incorporado, muestra al usuario el producto incorporado.
    Al terminar el proceso de incorporación, muestra un listado general de los productos.
    
    Args: nombre: str, categoria: str, precio: int, fecha_incorporacion: str

    Returns: Mensaje de error en caso de no poder agregar el producto. Mensaje mostrando el producto incorporado
    """
    # Creamos la variable productos_incorporados para almacenar los productos registrados por el usuario en la sesión actual
    productos_incorporados = []
    # Conectar a la base de datos
    conexion = conectar_db(productos_db)
    cursor = conexion.cursor()
    #print(f'Se ha conectado a la base de datos exitosamente')
        # Bucle para agregar productos y precios
    try:
        while True:
            # Texto explicativo para el usuario
            print(Style.RESET_ALL + Style.BRIGHT +
                  '\nPor favor, ingrese los datos del producto o escriba "fin" para finalizar. ')

            # Creamos la variable "nombre" y llama a la función "validar_dato_ingresado()" para solicitar al usuario el nombre del producto y devolverlo validado
            nombre = validar_dato_ingresado('nombre')
            # Si el texto ingresado por el usuario es "fin" sale del bucle y vuelve al menú principal
            if nombre == 'fin':
                break

            # Creamos la variable "categoria" para ingresar el tipo de producto y llama a la función "validar_dato_ingresado()" para devolverlo validado
            categoria = validar_dato_ingresado('tipo')
            # Si el texto ingresado por el usuario es "fin" sale del bucle y vuelve al menú principal
            if categoria == 'fin':
                break

            # Creamos la variable "precio" para ingresar el precio de producto llamando a la función "validar_dato_num_ingresado()" para devolverlo validado
            precio = validar_dato_num_ingresado('valor')
            # Si el texto ingresado por el usuario es "fin" sale del bucle y vuelve al menú principal
            if precio == 'fin':
                break
            fecha_incorporacion = datetime.date.today().strftime("%d/%m/%Y")
            
            # Insertar el producto en la base de datos
            cursor.execute('''
            INSERT INTO productos (nombre, categoria, precio, fecha_incorporacion)
            VALUES (?, ?, ?, ?)
            ''', (nombre, categoria, precio, fecha_incorporacion))
            # Confirmar la operación con la base de datos
            conexion.commit()
            print(f'\nEl producto {nombre} fue registrado exitosamente. \U0001F600')
            
            # Muestra al usuario la incorporación realizada
            cursor.execute('''SELECT * FROM productos ORDER BY id DESC LIMIT 1;''')
            ult_inc= cursor.fetchone()
            if ult_inc:
                print(
                    Back.GREEN + f'\n\nA continuación le mostramos la incorporación realizada: \n\tCódigo del producto: Nº{ult_inc[0]} \n\tProducto:  {ult_inc[1].capitalize()} \n\tCategoría: {ult_inc[2].capitalize()}\n\tPrecio:\t   ${ult_inc[3]}\n\tFecha de incorporación: {ult_inc[4]}.\n')
            
            # Si esta lista está vacía, no imprime el listado completo de productos al final de la función.
            productos_incorporados.append(ult_inc)


    # Excepciones
    except sqlite3.IntegrityError:
        print('\n\U0001F632 Error: el producto con ese nombre ya se encuentra registrado.')
        # Revertimos lo realizado
        conexion.rollback()
    

    finally:
        # Cerramos la conexión para evitar problemas futuros
        if conexion:
            conexion.close()
            #print('Base de datos cerrada.')

    # Llama a la función mostrar_listado_de_productos para imprimir el listado completo de los productos en caso de haber incorporado alguno.
    if len(productos_incorporados) >= 1:
        print('\nEstado actual del listado de Productos:')
        mostrar_listado_de_productos()




# Función para buscar productos en la lista. Esta se encontrará dentro de la Función Nº2 (buscador de producto) y Función Nº 4 (eliminar producto) del Menú principal.
def buscador_de_productos():
    """
    Función para buscar productos en la lista. Esta se encontrará dentro de la Función Nº2 (buscador de producto), Función Nº 4 (editar producto) y Nº5 (eliminar producto) del Menú principal.
    Se solicita al usuario que ingrese un dato del producto y lo buscamos en la base de dato.
    Si no hay ningún producto, lo informa al usuario.
    Cuando lo encuentra, imprime todos los elementos encontrados.

    Args: buscar_producto, str.

    Returns: Mensaje si no encontró o imprime todos los productos encontrados
    """
    # Conectar a la base de datos
    conexion = conectar_db(productos_db)
    cursor = conexion.cursor()
    try:
        while True:
            # Crea la variable para iterar la lista y buscar el producto deseado
            buscar_producto = input(Fore.BLUE +
                                    '\nPor favor, ingrese algún dato del producto a buscar o presione "Enter" para finalizar: \n').strip().lower()
        
            # Si el usuario no ingresa un dato, se sale del bucle
            if buscar_producto == '':
                break
            
            cursor.execute("SELECT * FROM productos WHERE id = ? OR nombre = ? OR categoria = ? OR precio = ?", (buscar_producto, buscar_producto, buscar_producto, buscar_producto))
            productos = cursor.fetchall()
            if not productos:
                print(Fore.RED + '\U0001F614 No se encontró ningún producto.\n')
                return
            # Texto que encabezará los resultados de la búsqueda
            print(Style.RESET_ALL +
                    f'\n\U0001F600 La búsqueda "{buscar_producto}" fue encontrada en el/los siguiente/s producto/s:')
            # Imprime los productos encontrados
            for producto in productos:
                print(Back.YELLOW +
                    f'\n\n\tCódigo:\t   {producto[0]}\n\tNombre:\t   {producto[1].capitalize()}\n\tCategoría: {producto[2].capitalize()}\n\tPrecio:    ${producto[3]}.\n\tFecha de incorporación: {producto[4]}\n')

    finally:
        # Cerramos la conexión para evitar problemas futuros
        if conexion:
            conexion.close()
            #print('Base de datos cerrada.')

# Función Nº4 del menú principal para editar productos
def modificar_producto():
    """
    Función Nº 4 del menú principal para editar los productos cargados en la base de datos
    
    args: cod_prod_a_modificar: int, key_a_modificar: str, nuevo_valor: str o int
    
    returns: producto modificado. Se confirma al usuario con una impresión de pantalla de los detalles del producto
    """
   
    # Texto de bienvenida a la función para modificar productos
    print(Style.RESET_ALL + Style.BRIGHT +
          '\nBienvenido a la función para editar productos. \nA continuación le solicitamos que busque el producto a editar del listado.')
    # Lo derivamos a la función buscador_de_productos para que el usuario encuentre los datos corresponidentes del producto que desea modificar
    buscador_de_productos()

    # Con el dato del producto, le pedimos que ingrese el código del mismo para poder acceder y modificarlo
     # Conectar a la base de datos
    conexion = conectar_db(productos_db)
    cursor = conexion.cursor()
    try:

        while True:
            # Creamos la variable para ingresar el código del producto a modificar y llama a la función "solicitar_dogido_prod()" que valida la entrada
            cod_prod_a_modificar = solicitar_codigo_prod('modificar')
            # Si el usuario presiona "Enter" se sale del bucle
            if not cod_prod_a_modificar:
                break

            # Solicita el key a modificar llamando a la función "validar_opcion_menu()":
            print(Style.RESET_ALL + f'Por favor, ingrese qué valor desea modificar. \nPresione 1 si desea modificar el nombre. \nPresione 2 si desea modificar el tipo de producto. \nPresione 3 si desea modificar el precio.\nPresione 4 si desea regresar al menú de inicio.')

            key_a_modificar = validar_opcion_menu()

            # Asociamos el valor ingresado a las keys de nuestros productos (diccionarios)
            match key_a_modificar:
                case 1:
                    llave = 'nombre'
                case 2:
                    llave = 'categoria'
                case 3:
                    llave = 'precio'
                case 4:
                    break
                case _:
                    print(Fore.RED + "\U0001F620 No ingresó una opción válida.")

            # Sacamos las comillas a llave para que pueda utilizarlo cuando modifico la base de datos
            llave_sc= llave.replace("'", "")
            
            producto_modificado = []
            # Solicita al usuario el valor (diccionario) a moficiar
            nuevo_valor = input(
                '\nPor favor, ingrese la modificación a realizar: ').strip()
            # Si es de tipo string lo usamos para modificar el 'nombre' o 'categoría' (de acuerdo a lo que solicitó el usuario)
            if type(nuevo_valor) == str:
                # Pasa el dato ingresado a lower para poder almacenarlo
                nuevo_valor = nuevo_valor.lower()
                # Realizamos la modificación en la base de datos
                cursor.execute(f"UPDATE productos SET {llave_sc} = ? WHERE id = ?", (nuevo_valor,cod_prod_a_modificar))
            if nuevo_valor.isdigit():
                # Pasa el input a type int
                nuevo_valor_int = int(nuevo_valor)
                # Realizamos la modificación en la base de datos
                cursor.execute(f'UPDATE productos SET {llave_sc} = ? WHERE id = ?', (nuevo_valor_int, cod_prod_a_modificar))
                
            # Confirmar los cambios en la db
            conexion.commit()

            # Muestra al usuario cómo quedó el producto modificado
            cursor.execute(f'SELECT * FROM productos WHERE id = ?', (cod_prod_a_modificar,))
            producto_modificado = cursor.fetchone()
            print(
                    Style.RESET_ALL + Back.YELLOW + f'\n\n\U0001F600 A continuación le mostramos la modificación realizada: \n\tCódigo:\t   {producto_modificado[0]}\n\tNombre:    {producto_modificado[1].capitalize()}\n\tCategoría: {producto_modificado[2].capitalize()}\n\tPrecio:    ${producto_modificado[3]}.\n\tFecha de incorporación: {producto_modificado[4]}\n')
            # Una vez finalizado, sale del bucle
            break
    finally:
        # Cerramos la conexión para evitar problemas futuros
        if conexion:
            conexion.close()
            #print('Base de datos cerrada.')

# Función Nº 4 del menú, la cual elimina productos del listado general.
def eliminar_producto():
    """
    Función Nº 4 del menú, la cual elimina productos de la base de datos.

    Args: codigo del producto a eliminar: int

    Returns: Producto eliminado y el listado actualizado al momento
    """
    # Creamos variable para sumar el producto borrado cuando encuentra un producto con el código que da el cliente y, de ser necesario, poder recuperarlo si el usuario se arrepiente. Si ingresa un código inexistente la lista queda en 0
    producto_eliminado = []
    # Texto de bienvenida a la función para eliminar_productos
    print(Style.RESET_ALL + Style.BRIGHT +
          '\nBienvenido a la función para eleminar productos.')
    print('A continuación le solicitamos que busque el producto a eliminar del listado.')
    # Lo derivamos a la función buscador_de_productos para que el usuario encuentre los datos corresponidentes del producto que desea modificar
    buscador_de_productos()
    try:
        conexion=conectar_db("productos.db")
        cursor=conexion.cursor()
            
        while True:
        # Creamos la variable para ingresar el código del producto a eliminar y llama a la función "solicitar_codigo_prod()" que valida la entrada
            producto_a_eliminar_int = solicitar_codigo_prod('eliminar')

            # Si el usuario no ingresa el código, se sale del bucle
            if producto_a_eliminar_int == None:
                break

            # Bucle para buscar y acceder al código del producto en el listado de productos
            cursor.execute("SELECT * FROM productos WHERE id = ?", (producto_a_eliminar_int,))
            producto = cursor.fetchone()

            # Pedimos al usuario una confirmación para eliminar el producto
            confirmacion_del= input(Fore.RED +f'\n¿Está seguro que desea eliminar el producto "{producto[1].capitalize()}"? Tenga en cuenta que una vez eliminado, esta acción no podrá ser revertida. \nIngrese "si" para eliminar: ').strip().lower()

            if confirmacion_del != "si":
                print(Style.RESET_ALL +f'\nSe ha cancelado la eliminación.')
                return
            else:
                # Procede a eliminar al alumno
                cursor.execute("DELETE FROM productos WHERE id = ?", (producto_a_eliminar_int,))
                conexion.commit()
                # Muestra mensaje del producto eliminado
                print(Back.LIGHTRED_EX +f'\nEl producto "{producto[1].capitalize()}", {producto[2]}, de precio ${producto[3]}, incorporado el día {producto[4]}, con el código {producto[0]} ya no pertenece a su base de datos. Bye Bye "{producto[1].capitalize()}", fuiste debidamente eliminado/a.\U0001F629\n')
                producto_eliminado.append(producto)

            # Una vez finalizado, sale del bucle
            break
    finally:
        # Cerramos la conexión para evitar problemas futuros
        if conexion:
            conexion.close()
            #print('Base de datos cerrada.')

    # Imprime el listado de productos luego de la modificación, si es que se eliminó al menos uno.
    if len(producto_eliminado) >= 1:
        print('\nA continuación imprimiremos el listado completo luego de la modificación realizada.')
        mostrar_listado_de_productos()


def solicitar_codigo_prod(funcion):
    """
    Función para solicitar y validar el código de un producto. Chequea que esté en la base de datos, si no existe, regresa al menú principal. Se encuentra dentro de la función Nº4 Modificar producto y Función Nº5 Eliminar producto

    Args: cod_producto: str 

    Returns: cod_producto_int: int
    """
    # Con el dato del producto, le pedimos que ingrese el código del mismo para poder acceder y modificarlo
    conexion = conectar_db("productos.db")
    cursor= conexion.cursor()
    try:
        while True:
            # Creamos la variable para ingresar el código del producto a modificar
            cod_producto = input(
                f'\nPor favor, ingrese el código del producto a {funcion} o presione "Enter" para salir: ').strip()

            # Si el usuario no ingresa el código, se sale del bucle
            if len(cod_producto) == 0:
                break
            elif cod_producto == '':
                return cod_producto
            # Si el usuario ingresó un texto se le notifica y vuelve a pedirle que ingrese el código
            elif cod_producto.isalpha():
                print('\U0001F620 Ingresó un texto.')

            # Pasa el input a type int para poder modificar.
            if cod_producto.isdigit():
                cod_producto_int = int(cod_producto)
                cursor.execute("SELECT id FROM productos WHERE id = ?", (cod_producto_int,))
                producto= cursor.fetchone()
                # Imprime mensaje de código inexistente cuando sqlite3 no encuentra el id ya que no se encontró ningún producto con ese código
                if not producto:
                    print(Fore.RED + '\U0001F620 Ingresó un código inexistente.')
                    # Nos saca de este menú y regresa al menú principal
                    break
                return cod_producto_int
                
    finally:
        # Cerramos la conexión para evitar problemas futuros
        if conexion:
            conexion.close()
            #print('Base de datos cerrada.')


def validar_dato_ingresado(key_producto):
    """
    Función para validar información de tipo str ingresada por el usuario en agregar_producto() para el campo nombre y tipo
    
    Agrs: dato:str

    Returns: dato validado en minúsculas y sin espacios para poder ser almacenado en la db
    """
    while True:
        # Solicita al usuario el nombre o el tipo de producto en formato string
        dato = input(
            f'Por favor, ingrese el {key_producto} del producto: ').lower().strip()
        # Si el usuario no ingresa un dato le muestra mensaje de error.
        if dato == '':
            print(Fore.RED + '\U0001F620 Error. Por favor, ingrese un dato válido.')
        # Si ingresó un contenido sigue con el código
        if dato.isalpha():
            return dato


def validar_dato_num_ingresado(key_producto):
    """
    Función para validar información de tipo int ingresada por el usuario en agregar_producto() para el campo precio
    
    Agrs: dato:str

    Returns: dato validado convertido en int positivo para poder ser almacenado en la db
    """
    while True:
        # Solicita el precio del producto en formato string
        dato = input(
            f"Por favor, ingrese el {key_producto} del producto: $").lower().strip()
        # Chequea si el usuario dejó en blanco o si ingresó un texto
        if dato.isdigit():
            # Pasa el string ingresado a type int
            precio = int(dato)
            # Si el precio es mayor a 0, lo devuelve
            if precio > 0:
                # salimos del bucle con el dato validado
                return precio
            # Si el usuario ingresa un valor menor o igual a 0, le muestra mensaje de error
            print(Fore.RED + '\U0001F620 Por favor, ingrese un valor mayor a 0.')
        # Si el usuario ingresa "fin", sale del bucle
        elif dato == 'fin':
            return dato
        # Mensaje cuando el usuario no ingresó el valor o ingresó un texto
        print(Fore.RED + '\U0001F620 Ingresó un dato no válido. Por favor, ingrese un valor.')


