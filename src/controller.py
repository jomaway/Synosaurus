# controller.py
#
# Copyright 2021 jomaway

from .api import OpenthesaurusAPI
from .views import WordView, SeperatorView
from gi.repository import Gtk

class Controller:

    def __init__(self, app, win):
        self.app = app
        self.win = win
        self.win.ctr = self  # pass ctr to win

        self.api = OpenthesaurusAPI()
        self.store = []  # list for ResultEntryView
        self.hist = []

        self.fetch("Test")

    def set_win(self, win):
        self.win = win

    def update_results_view(self):
        for entry in results:
            self.win.results_listbox.add(entry)

    def fetch(self, string):
        result = self.api.query(string)

        self.store_result(result)

        # update result listbox in view
        self.win.update_list(self.store)

    def get_model(self):
        return self.store

    def store_result(self, data):
        if data is None:
            return
        self.store.clear()
        for entry in data['synsets']:
            id = entry['id']
            terms = entry['terms']
            for term in terms:
                word = term['term']
                level = term.get('level','')
                self.store.append(WordView(word, level))
            self.store.append(SeperatorView())





