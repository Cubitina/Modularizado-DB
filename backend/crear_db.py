# Importamos función para conectar a la db
from conectar_db import *

# Nombre de la base de datos
productos_db = "productos.db"
# Intentar conectar a la base de datos.
conexion= conectar_db(productos_db)

try:
    cursor= conexion.cursor()
    conexion.execute("PRAGMA foreign_keys = 1")
    
    # Crea la base de datos "productos" si no existe
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS productos (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nombre TEXT UNIQUE NOT NULL,
                   categoria TEXT NOT NULL,
                   precio INTEGER NOT NULL CHECK (precio >= 1),
                   fecha_incorporacion TEXT NOT NULL);
                ''')
    print('La tabla productos fue creada exitosamente')

    # Tablas creadas para practicar y probar las interrelaciones entre tablas.
    # Crea la base de datos "carrito" si no existe. Tiene dos valores interrelacionados a otras tablas.
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS carrito (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   cliente_id INTERGER NOT NULL,
                   producto_id INTERGER NOT NULL,
                   cantidad INTERGER NOT NULL,
                   fecha_compra TEXT NOT NULL,
                   FOREIGN KEY(producto_id) REFERENCES productos(id),
                   FOREIGN KEY(cliente_id) REFERENCES cliente(id));
                ''')
    print('La tabla carrito fue creada exitosamente')

    # Crea la base de datos "cliente" si no existe
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS cliente (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nombre TEXT NOT NULL,
                   appelido TEXT NOT NULL,
                   dni INTEGER NOT NULL,
                   fecha_nac TEXT NOT NULL,
                   fecha_ingreso TEXT NOT NULL,
                   email TEXT NOT NULL);
                ''')
    print('La tabla usuario fue creada exitosamente')

    # Confirmar la operación con la base de datos
    conexion.commit()
    
finally:
    #Cerramos la conexión para evitar problemas futuros
    if conexion:
        conexion.close()
        print('Base de datos cerrada.')