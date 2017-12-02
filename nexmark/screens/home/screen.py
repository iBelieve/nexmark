import sys
import threading
import time
from datetime import datetime

from gi.repository import GLib, Gtk
from .books import BooksList
from nexmark.utils import icon


class HomeScreen(Gtk.Box):
    def __init__(self, window):
        super().__init__(orientation=Gtk.Orientation.VERTICAL)
        self.get_style_context().add_class('home')

        self.window = window

        self.setup_header()
        self.setup_content()
        self.setup_footer()

        self.update_datetime()

        thread = threading.Thread(target=self.timer, daemon=True)
        thread.start()

    def on_book_clicked(self, list, book):
        self.window.show_book(book)

    def setup_header(self):
        self.header = Gtk.HeaderBar(
            title="7:30 PM", subtitle="Thursday, Oct 30")

        self.settings_button = Gtk.Button(
            image=icon('preferences-system-symbolic'))
        self.settings_button.connect('clicked', self.on_settings_clicked)
        self.header.pack_end(self.settings_button)

        self.exit_button = Gtk.Button(label='Quit')
        self.exit_button.connect('clicked', self.on_quit)
        self.header.pack_end(self.exit_button)

        self.add(self.header)

    def setup_footer(self):
        self.pack_end(Footer(), expand=False, fill=False, padding=0)

    def setup_content(self):
        self.content = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL, vexpand=True)
        self.add(self.content)

        books_list = BooksList()
        books_list.connect('cell-clicked', self.on_book_clicked)

        self.add_subheader('Books')
        self.content.add(books_list.scrolled())
        self.add_subheader('Saved for Later')

    def timer(self):
        while True:
            GLib.idle_add(self.update_datetime)
            time.sleep(1)

    def on_quit(self, button):
        print('Quitting...')
        sys.exit(0)

    def on_settings_clicked(self, button):
        self.window.show_settings()

    def add_subheader(self, text):
        label = Gtk.Label(label=text, xalign=0)
        label.get_style_context().add_class('subheader')
        self.content.add(label)

    def update_datetime(self):
        now = datetime.now()
        self.header.props.title = now.strftime('%l:%M %p')
        self.header.props.subtitle = now.strftime('%A, %b %e')


class Footer(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL)
        self.get_style_context().add_class('footer')

        box = Gtk.Box(halign=Gtk.Align.CENTER, homogeneous=True)
        box.set_size_request(600, -1)
        self.add(box)

        box.add(FooterItem('Home', 'user-home-symbolic', selected=True))
        box.add(FooterItem('Books', 'ebook-reader-app'))
        box.add(FooterItem('Documents', 'documents-app'))
        box.add(FooterItem('Web', 'webbrowser-app'))
        box.add(FooterItem('Settings', 'system-settings'))


class FooterItem(Gtk.Box):
    def __init__(self, name, iconname, selected=False):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.get_style_context().add_class('footer-item')
        if selected:
            self.get_style_context().add_class('active')
        self.add(icon(iconname, size=Gtk.IconSize.DIALOG))
        self.add(Gtk.Label(label=name))
