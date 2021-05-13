# main.py
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

import sys
import gi
import json

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gio

from .window import SynosaurusWindow
from .controller import Controller

class Application(Gtk.Application):
    def __init__(self, v):
        super().__init__(application_id='de.jomaway.Synosaurus',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)
        self.version = v
        self.controller = None

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = SynosaurusWindow(application=self)
        win.present()
        if self.controller is None:
            self.controller = Controller(self, win)

def main(version):
    print(f"Running version: {version}")
    app = Application(version)
    return app.run(sys.argv)
