# Importamos pandas para poder trabajar la información de la base de datos
import pandas as pd
# Importamos matplotlib para gráficos
import matplotlib.pyplot as plt
# Importamos seaborn para colores aesthetic
import seaborn as sns
from backend.conectar_db import *
from backend.mostrar_listado import *

# Nombre de la base de datos
productos_db = "productos.db"

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


def graf_barras_prod(dato):
    """
    Función Nº 7 del menú de visualización de datos de la db. 
    Muestra un gráfico historiograma con los productos y sus precios relacionados. También hay un promedio de precio marcado con la línea roja

    Args: key 'nombre', 'precio' y 'stock' de la tabla productos de acuerdo a lo ingresado en el menú por el usuario a través de la variable "dato".

    Returns: gráfico historiograma emergente en una ventana nueva.
    """
    # Sacamos las comillas a la variabe "dato" para que pueda utilizarlo para acceder a la base de datos
    dato_sc = dato.replace("'", "")
    try:
        # Intentar conectar a la base de datos. Si no existe, la crea.
        conexion = conectar_db("productos.db")
        
        # Consulta SQL para obtener datos
        query = f'SELECT nombre, {dato_sc} FROM productos;'
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
        if dato =='precio':
            sns.barplot(data= df, x='nombre', y='precio', hue= 'nombre', palette='viridis', legend=False)
        else:
            sns.barplot(data= df, x='nombre', y='stock', hue= 'nombre', palette='magma', legend=False)
        # Creamos línea vertical que muestra el precio o stock promedio de los productos de la lista
        if dato == 'precio':
            plt.axhline(df['precio'].mean(), color='tomato', label='Precio promedio')
        else:
            plt.axhline(df['stock'].mean(), color='tomato', label='Stock promedio')
        # Títutlo de la tabla
        plt.title(f'Gráfico de productos y {dato_sc}\n')
        # Títulos de vectrices
        plt.xlabel("Producto")
        plt.ylabel(f"{dato_sc.capitalize()}")
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





