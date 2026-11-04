import mysql.connector

from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    # TODO
    def leggi_biblioteca_dal_DB(self):
        try:
            cnx = DBConnect.get_connection()
            cursore = cnx.cursor()
            query = 'select * from biblioteca'
            cursore.execute(query)
            result = []
            for row in cursore:
                biblioteca = Biblioteca(*row)
                result.append(biblioteca)
            cnx.close()
            return result
        except mysql.connector.Error:
            raise ConnectionError
