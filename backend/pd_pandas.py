# Importamos pandas para poder trabajar la información de la base de datos
import pandas as pd
# Importamos sqlite3 para poder trabajar con bases de datos
import sqlite3
# Importamos matplotlib para gráficos
import matplotlib.pyplot as plt
# Importamos seaborn para colores aesthetic
import seaborn as sns

# Nombre de la base de datos
productos_db = "productos.db"

def conectar_db(db):
    """
    Función para conectar a la base de datos.

    Args:
    db: Nombre del archivo de la base de datos.

    Returns:
    Conexion si la conexión es exitosa, mensaje de error si no lo logra.
    """

    try:
    # Intentar conectar a la base de datos. Si no existe, la crea.
        conexion = sqlite3.connect(db)
        #print(f'Se ha conectado a {db} exitosamente')
        return conexion
    # Excepciones
    except sqlite3.Error as e:
        # Si hay un error muestra un mensaje al usuario
        print(f'Error en la base de datos: {e}.')
        # Si ocurre un error, revertimos los cambios
        conexion.rollback()
        return None

def grafico_tipo_productos():
    """
    Función Nº 6 del menú de visualización de datos de la db. 
    Muestra un gráfico de torta con los porcentajes de los diferentes tipos de productos en el listado

    Args: key 'categoria' de la tabla productos

    Returns: gráfico de torta emergente en una ventana nueva.
    """
    try:
        # Intentar conectar a la base de datos. Si no existe, la crea.
        conexion = conectar_db("productos.db")
        
        # Consulta SQL para obtener datos
        query = 'SELECT categoria FROM productos;'

        # Leer datos a un DataFrame de Pandas
        df = pd.read_sql_query(query, conexion)

        # Mostrar el DataFrame
        #print(df)
    
    finally:
            #Cerramos la conexión para evitar problemas futuros
            if conexion:
                conexion.close()
                #print(f'Base de datos {productos_db} cerrada.')    

    try:
        # Agrupa por la columna y cuenta las ocurrencias
        counts = df['categoria'].value_counts()

        # Creación del gráfico de torta
        # Ajusta el tamaño del gráfico
        plt.figure(figsize=(7,7))
        # Creamos el gráfico de torta. En colores, usamos la paleta de seaborn
        plt.pie(counts.values, labels=counts.index.str.capitalize(), autopct='%1.1f%%', startangle=140, colors = sns.color_palette('viridis_r'))
        # Títutlo de la tabla
        plt.title(f'Tipos de productos de su listado\n')
        # Hace que el gráfico de torta sea circular
        plt.axis('equal')
        # Muestra el gráfico de torta
        plt.show()

    except KeyError as e:
        print(f'Error, no se encontró la información solicitada: {e}')
    except Exception as e:
        print(f'Ocurrió un error inexperado: {e}.')
    finally:
        if conexion:
            conexion.close()


def graf_barras_prod_prec():
    """
    Función Nº 7 del menú de visualización de datos de la db. 
    Muestra un gráfico historiograma con los productos y sus precios relacionados. También hay un promedio de precio marcado con la línea roja

    Args: key 'nombre' y 'precio' de la tabla productos

    Returns: gráfico historiograma emergente en una ventana nueva.
    """
    try:
        # Intentar conectar a la base de datos. Si no existe, la crea.
        conexion = conectar_db("productos.db")
        
        # Consulta SQL para obtener datos
        query = 'SELECT nombre, precio FROM productos;'
        # Leer datos a un DataFrame de Pandas
        df = pd.read_sql_query(query, conexion)
        # Capitalizar las referencias
        df['nombre'] = df['nombre'].str.capitalize()

        # Mostrar el DataFrame
        #print(df)
    
    finally:
            #Cerramos la conexión para evitar problemas futuros
            if conexion:
                conexion.close()
                #print(f'Base de datos {productos_db} cerrada.')    

    try:
        # Ajusta el tamaño del gráfico
        plt.figure(figsize=(10,7))
        #Creación del historiograma. plt.bar() se utiliza para crear el gráfico de barras. Utilizamos seaborn porque tiene colores más agradables a la vista del usuario.
        #plt.bar(df['nombre'], df['precio'])
        sns.barplot(data= df, x='nombre', y='precio', hue= 'nombre', palette='viridis', legend=False)
        # Creamos línea vertical que muestra el precio promedio de los productos de la lista
        plt.axhline(df['precio'].mean(), color='tomato', label='Precio promedio')
        # Títutlo de la tabla
        plt.title(f'Gráfico de productos y precios\n')
        # Títulos de vectrices
        plt.xlabel("Producto")
        plt.xlabel("Precio")
        # Tamaño letra
        plt.xticks(fontsize=14)
        # Rota las etiquetas del eje x para mejor legibilidad
        plt.xticks(rotation=45, ha="right")
        # Ajusta el diseño para evitar que las etiquetas se superpongan
        plt.tight_layout() 
        # Mostrar la leyenda
        plt.legend()
        # Muestra el gráfico de torta
        plt.show()

    except KeyError as e:
        print(f'Error, no se encontró la información solicitada: {e}')
    except Exception as e:
        print(f'Ocurrió un error inexperado: {e}.')
    finally:
        if conexion:
            conexion.close()





