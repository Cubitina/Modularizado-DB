# Importamos función para conectar a la db
from backend.conectar_db import *

# Nombre de la base de datos
productos_db = "productos.db"

def crear_tabla():
    # Intentar conectar a la base de datos.
    conexion= conectar_db(productos_db)

    try:
        cursor= conexion.cursor()
        conexion.execute("PRAGMA foreign_keys = 1")
        table_name_1= "productos"
        table_name_2= "cliente"
        table_name_3= "carrito"
        
        # Crea la base de datos "productos" si no existe
        cursor.execute(f'''
                    CREATE TABLE IF NOT EXISTS {table_name_1} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT UNIQUE NOT NULL,
                    categoria TEXT NOT NULL,
                    precio INTEGER NOT NULL CHECK (precio >= 1),
                    stock INTEGER NOT NULL CHECK (stock >=1),
                    fecha_incorporacion TEXT NOT NULL
                    );
                    ''')
        print(f'La tabla {table_name_1} fue creada exitosamente')
        # Confirmar la operación con la base de datos
        conexion.commit()

        
        # Tablas creadas para practicar y probar las interrelaciones entre tablas.
        # Crea la base de datos "cliente" si no existe
        cursor.execute(f'''
                    CREATE TABLE IF NOT EXISTS {table_name_2} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    appelido TEXT NOT NULL,
                    dni INTEGER NOT NULL,
                    fecha_nac TEXT NOT NULL,
                    fecha_ingreso TEXT NOT NULL,
                    email TEXT NOT NULL);
                    ''')
        print(f'La tabla {table_name_2} fue creada exitosamente')
        # Confirmar la operación con la base de datos
        conexion.commit()

        # Crea la base de datos "carrito" si no existe. Tiene dos valores interrelacionados a otras tablas.
        cursor.execute(f'''
                    CREATE TABLE IF NOT EXISTS {table_name_3} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cliente_id INTERGER NOT NULL,
                    producto_id INTERGER NOT NULL,
                    cantidad INTERGER NOT NULL,
                    fecha_compra TEXT NOT NULL,
                    FOREIGN KEY(producto_id) REFERENCES productos(id),
                    FOREIGN KEY(cliente_id) REFERENCES cliente(id));
                    ''')
        print(f'La tabla {table_name_3} fue creada exitosamente')
        # Confirmar la operación con la base de datos
        conexion.commit()
        
    finally:
        #Cerramos la conexión para evitar problemas futuros
        if conexion:
            conexion.close()
            print('Base de datos cerrada.')