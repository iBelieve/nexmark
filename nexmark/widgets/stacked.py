from gi.repository import Gtk


class Stacked(Gtk.Fixed):
    def __init__(self, count, offset):
        super().__init__()
        self.count = count
        self.offset = offset

    def add(self, widget):
        index = len(self.get_children())
        offset = self.offset * index
        self.put(widget, offset, self.offset * self.count - offset)
