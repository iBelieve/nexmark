from gi.repository import Gtk
from .epub import EPUBView
from .evince import EvinceView

class ReaderScreen(Gtk.Stack):
    def __init__(self):
        super().__init__()
        self.epub_view = EPUBView()
        self.evince_view = EvinceView()
        self.add(self.epub_view)
        self.add(self.evince_view)

    def show_book(self, book):
        formats = book.formats
        if 'EPUB' in formats:
            self.epub_view.set_book(book)
            self.set_visible_child(self.epub_view)
        elif 'PDF' in formats:
            self.evince_view.set_book(book)
            self.set_visible_child(self.evince_view)
        else:
            print('WARNING: No supported formats: ' + ', '.join(formats))
