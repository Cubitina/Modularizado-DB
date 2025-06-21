# Importamos sqlite3 para poder trabajar con bases de datos
import sqlite3

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


