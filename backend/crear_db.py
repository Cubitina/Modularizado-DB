# Importamos función para conectar a la db
from conectar_db import *

# Nombre de la base de datos
productos_db = "productos.db"
# Intentar conectar a la base de datos.
conexion= conectar_db(productos_db)

try:
    cursor= conexion.cursor()
    
    # Crea la base de datos si no existe
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS productos (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nombre TEXT UNIQUE NOT NULL,
                   categoria TEXT NOT NULL,
                   precio INTEGER NOT NULL CHECK (precio >= 1),
                   fecha_incorporacion TEXT NOT NULL)
                ''')
    print('La tabla productos fue creada exitosamente')

    # Confirmar la operación con la base de datos
    conexion.commit()
    
finally:
    #Cerramos la conexión para evitar problemas futuros
    if conexion:
        conexion.close()
        print('Base de datos cerrada.')