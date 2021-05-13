# views.py
#
# Copyright 2021 jomaway


from gi.repository import Gtk


class ResultEntryView(Gtk.ListBoxRow):

    def __init__(self, text):
        super().__init__()

        self.hbox = Gtk.HBox()

        self.title_label = Gtk.Label()
        #self.title_label.set_ellipsize(Pango.EllipsizeMode.END)

        self.count_label = Gtk.Label()
        self.count_label.get_style_context().add_class('group-count')

        self.hbox.pack_start(self.title_label, True, True, 0)
        self.hbox.pack_end(self.count_label, False, False, 0)
        self.add(self.hbox)

        self.update(text)

        self.show_all()

    def update(self, text):
        self.title_label.set_text(text)

class WordView(Gtk.ListBoxRow):

    def __init__(self, word, info=None):
        super().__init__()

        self.hbox = Gtk.HBox()

        self.word_label = Gtk.Label()
        self.word_label.set_xalign(0)
        self.word_label.set_margin_top(6)
        self.word_label.set_margin_bottom(6)
        self.word_label.set_margin_start(10)
        self.word_label.set_margin_end(6)
        self.word_label.set_text(word)

        self.info_label = Gtk.Label()
        if info is not None:
            self.info_label.set_text(info)

        # pack
        self.hbox.pack_start(self.word_label, True, True, 0)
        self.hbox.pack_start(self.info_label, False, False, 0)

        self.add(self.hbox)
        self.show_all()

    @property
    def word(self):
        return self.word_label.get_text()

    def update(self, word):
        self.word_label.set_text(word)

class SeperatorView(Gtk.ListBoxRow):

    def __init__(self):
        super().__init__()

        sep = Gtk.Separator()
        sep.set_margin_top(20)
        sep.set_margin_bottom(20)
        self.set_selectable(False)
        self.set_activatable(False)

        self.add(sep)
        self.show_all()
