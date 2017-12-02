from gi.repository import Gtk, Gdk


class SettingsWindow(Gtk.Window):
    def __init__(self, parent):
        super().__init__(title='Settings')
        self.set_transient_for(parent)
        self.set_modal(True)
        self.set_type_hint(Gdk.WindowTypeHint.DIALOG)

        self.header = Gtk.HeaderBar(title='Settings', show_close_button=True)
        self.set_titlebar(self.header)

        screen = Gdk.Screen.get_default()

        self.set_size_request(min(screen.get_width() - 100, 500),
                              min(screen.get_height() - 100, 700))
