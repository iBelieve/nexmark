from gi.repository import GLib, Gtk, Gio, Gdk

from .window import Window


class Application(Gtk.Application):
    window: Window = None

    def __init__(self, version, pkgdatadir, libdir):
        super().__init__(application_id='io.mspencer.Nexmark')

        self.version = version
        self.pkgdatadir = pkgdatadir
        self.libdir = libdir

        self.settings = Gio.Settings(schema_id='io.mspencer.Nexmark')

    # Signal handlers

    def do_activate(self):
        Gtk.Application.do_activate(self)
        if self.window is None:
            self.window = Window(self)
            self.window.connect('destroy', self.on_window_destroyed)
        self.window.show_all()

    def on_window_destroyed(self, window):
        self.window = None

    @property
    def is_landscape(self):
        size = self.window.get_allocation()
        print(size.width, size.height)
        return size.width > size.height
