#!/usr/bin/env python
'''
SQL Introducción [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import json
import requests
import tinymongo as tm
import tinydb

# Bug: https://github.com/schapman1974/tinymongo/issues/58
class TinyMongoClient(tm.TinyMongoClient):
    @property
    def _storage(self):
        return tinydb.storages.JSONStorage

url = 'https://jsonplaceholder.typicode.com/todos'

db_name = 'titulos'

def clear():
    conn = TinyMongoClient()
    db = conn[db_name]
    db.database.remove({})
    conn.close()


def fill():
    conn = TinyMongoClient()
    db = conn[db_name]
    response = requests.get(url)
    contenido = response.json()
    db.database.insert_many(contenido)
    conn.close()


def show():
    conn = TinyMongoClient()
    db = conn[db_name]
    cursor = db.database.find()
    data = list(cursor)
    data_string = json.dumps(data, indent=4)
    print(data_string)
    conn.close()



def title_completed_count(userId):
    conn =TinyMongoClient()
    db = conn[db_name]
    count = db.database.find({"userId": userId, "completed": True}).count()
    print(count)
    print('')


if __name__ == '__main__':
    clear()
    fill()
    show()
    userId = 3
    title_completed_count(userId)