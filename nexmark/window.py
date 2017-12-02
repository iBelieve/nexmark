from gi.repository import Gtk, Gdk
from .screens import HomeScreen, ReaderScreen, SettingsWindow


class Window(Gtk.ApplicationWindow):
    def __init__(self, app):
        super().__init__(application=app, title="Nexmark")

        self.home = HomeScreen(self)
        self.reader = ReaderScreen()

        self.stack = Gtk.Stack()
        self.stack.add(self.home)
        self.stack.add(self.reader)
        self.add(self.stack)

        self.fullscreen()

    def do_realize(self):
        Gtk.Window.do_realize(self)
        self.props.window.props.cursor = Gdk.Cursor(
            Gdk.CursorType.BLANK_CURSOR)

    def show_settings(self):
        window = SettingsWindow(self)
        window.show_all()

    def show_book(self, book):
        self.reader.show_book(book)
        self.stack.set_visible_child(self.reader)
