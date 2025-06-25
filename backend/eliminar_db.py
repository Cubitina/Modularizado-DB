# Importamos función para conectar a la db
from conectar_db import *

# Nombre de la base de datos
productos_db = "productos.db"


# Función creada para practicar.
def eliminar_table(db_file, nombre_tabla):
    """
  Elimina una tabla de una base de datos SQLite.

  Args:
    db_file: La ruta al archivo de la base de datos SQLite.
    nombre_tabla: El nombre de la tabla a eliminar.
  """
    try:
        # Intentar conectar a la base de datos.
        conexion= conectar_db(db_file)
        cursor= conexion.cursor()
        cursor.execute(f'DROP TABLE IF EXISTS {nombre_tabla};')
        conexion.commit()
        print(f'La tabla "{nombre_tabla}" fue eliminada correctamente.')
    except sqlite3.Error as e:
        print(f'Error al eliminar la tabla: {e}')
    finally:
        if conexion:
            conexion.close()

eliminar_table(productos_db,'carrito')

