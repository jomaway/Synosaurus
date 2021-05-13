# window.py
#
# Copyright 2021 jomaway
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk, Gdk
import json

@Gtk.Template(resource_path='/de/jomaway/Synosaurus/window.ui')
class SynosaurusWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'SynosaurusWindow'

    results_listbox = Gtk.Template.Child()
    search_entry = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ctr = None

        self.results_listbox.set_activate_on_single_click(False)


        # set focus to search entry
        self.search_entry.grab_focus()

    @Gtk.Template.Callback()
    def on_search_activate(self, *args):
        query_string = self.search_entry.get_text()
        self.ctr.fetch(query_string)
        self.search_entry.grab_focus()

    @Gtk.Template.Callback()
    def on_results_listbox_row_activated(self, listbox, listboxrow):
        self.search_entry.set_text(listboxrow.word)
        self.ctr.fetch(listboxrow.word)
        self.search_entry.grab_focus()

    def create_widget_func(self, item):
        label = Gtk.Label(item.text)
        return label

    def add_to_listbox(self, item):
        self.results_listbox.add(item)

    def update_list(self, datastore):
        # remove all rows
        for row in self.results_listbox:
            self.results_listbox.remove(row)

        # add new rows
        for entry in datastore:
            self.results_listbox.add(entry)




    
