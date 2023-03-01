# -*- coding: utf-8 -*-
import sqlite3


conn = sqlite3.connect('userdata.db')


conn.execute('CREATE TABLE IF NOT EXISTS users ('
             'id INTEGER PRIMARY KEY AUTOINCREMENT,'
             'user TEXT UNIQUE,'
             'password TEXT,'
             'account_number TEXT UNIQUE,'
             'balance INTEGER DEFAULT 0)')


conn.commit()


conn.close()