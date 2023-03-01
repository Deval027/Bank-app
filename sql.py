# -*- coding: utf-8 -*-
import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conn = sqlite3.connect('userdata.db')

# Crear la tabla de usuarios
conn.execute('CREATE TABLE IF NOT EXISTS users ('
             'id INTEGER PRIMARY KEY AUTOINCREMENT,'
             'user TEXT UNIQUE,'
             'password TEXT,'
             'account_number TEXT UNIQUE,'
             'balance INTEGER DEFAULT 0)')

# Guardar los cambios en la base de datos
conn.commit()

# Cerrar la conexión a la base de datos
conn.close()