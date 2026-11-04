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
        cnx = None
        cursore = None
        try:
            cnx = DBConnect.get_connection()
            if cnx is None:
                raise ConnectionError
            cursore = cnx.cursor()
            query = 'select * from biblioteca'
            cursore.execute(query)
            result = []
            for row in cursore:
                biblioteca = Biblioteca(*row)
                result.append(biblioteca)
            return result
        except mysql.connector.Error:
            raise ConnectionError
        finally:
            if cursore is not None:
                cursore.close()
            if cnx is not None:
                cnx.close()
