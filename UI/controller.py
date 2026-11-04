import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    # TODO
    def popola_dd_genere(self):
        try:
            lista_generi = self._model.get_generi()
        except ConnectionError:
            self._view.show_alert(('errore di connessione al database, lista dei generi vuota'))
            return
        for genere in lista_generi:
            self._view.dd_genere.options.append(ft.DropdownOption(key=genere, text=genere))
    def popola_dd_biblioteca(self):
        try:
            lista_biblioteche = self._model.get_biblioteche()
        except ConnectionError:
            self._view.show_alert(('errore di connessione al database, lista delle biblioteche vuota'))
            return
        for biblioteca in lista_biblioteche:
            self._view.dd_biblioteca.options.append(ft.DropdownOption(key=biblioteca, text=biblioteca))

    # CALLBACKS DROPDOWN
    # TODO
    def dd_genere_handler(self):
        self.genere_selezionato = self._view.dd_genere.value
    def dd_biblioteca_handler(self):
        self.biblioteca_selezionata = self._view.dd_biblioteca.value



    # AZIONE: MOSTRA LIBRI
    # TODO
    def btn_mostra_handler(self):
        try:
            lista_libri = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)
        except ConnectionError:
            self._view.show_alert(('errore di connessione al database'))
            self._view.listview_libri.controls.clear()

            return
        self._view.listview_libri.controls.clear()
        for libri in lista_libri:
            self._view.listview_libri.controls.append(ft.Text(f"{libri}"))
        self._view.page.update()
