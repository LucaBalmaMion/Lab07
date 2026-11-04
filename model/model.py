from database import libro_DAO
from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO
from model.biblioteca_DTO import Biblioteca
from model.libro_DTO import Libro

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di BibliotecaDAO e LibroDAO)
'''

class Model:
    def __init__(self):
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()

    # --- LIBRI ---
    def get_libri_filtrati(self, biblioteca:str, genere:str):
        """Restituisce la lista di tutti i libri filtrati per biblioteca e/o genere (filtri opzionali)."""
        # TODO
        try:
            lista_libri = self._libro_dao.leggi_libri_dal_DB()
        except ConnectionError:
            raise ConnectionError
        if biblioteca is None and genere is None:
            return lista_libri
        lista_biblioteche = self._biblioteca_dao.leggi_biblioteca_dal_DB()
        result = []
        for libro in lista_libri:
            for biblio in lista_biblioteche:
                if libro.id_biblioteca == biblio.id:
                    libro.nome_biblioteca = biblio.nome
            if libro.nome_biblioteca == (biblioteca or None) and libro.genere == (genere or None):
                 result.append(libro)

        return result






    def get_generi(self):
        """Restituisce la lista di tutti i generi."""
        # TODO
        try:
            lista_libri = self._libro_dao.leggi_libri_dal_DB()
        except ConnectionError:
            raise ConnectionError
        generi = set()
        for libro in lista_libri:
            generi.add(libro.genere)
        return list(generi)


    # --- BIBLIOTECHE ---
    def get_biblioteche(self):
        """ Restituisce la lista di tutte le biblioteche."""
        # TODO
        try:
            lista_biblioteche = self._biblioteca_dao.leggi_biblioteca_dal_DB()
        except ConnectionError:
            raise ConnectionError
        result = []
        for el in lista_biblioteche:
            result.append(el.nome)
        return result

