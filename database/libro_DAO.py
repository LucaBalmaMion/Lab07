from database.DB_connect import DBConnect
from model.libro_DTO import Libro
import mysql.connector
"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    # TODO
    def leggi_libri_dal_DB(self):
        try:
            cnx = DBConnect.get_connection()
            cursore = cnx.cursor()
            query = 'select * from libro'
            cursore.execute(query)
            result = []
            for row in cursore:
                libro = Libro(*row)
                result.append(libro)
            cnx.close()
            return result
        except mysql.connector.Error:
            raise ConnectionError


