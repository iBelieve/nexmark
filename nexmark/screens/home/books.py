# from math import ceil, sqrt

from cairo import Context
from gi.repository import Gtk, GObject
from nexmark.providers.books import get_books
# from nexmark.widgets import Stacked
from nexmark.drawing import rounded_rect


class BooksList(Gtk.Box):
    __gsignals__ = {
        'cell-clicked': (GObject.SignalFlags.RUN_FIRST, None, (object,))
    }

    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.HORIZONTAL)
        for book in get_books():
            cell = BookCell(book)
            cell.connect('clicked', self.cell_clicked)
            self.add(cell)
        # for name, books in get_collections().items():
        #     self.add(CollectionCell(name, books))

    def cell_clicked(self, cell):
        self.emit('cell-clicked', cell.book)

    def scrolled(self):
        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.NEVER)
        scrolled.add(self)
        return scrolled


# class CollectionCell(Gtk.Box):
#     def __init__(self, name, books):
#         super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=10)
#         highlighted_books = books[:3]
#         stacked = Stacked(count=len(highlighted_books), offset=10)
#         for book in highlighted_books:
#             image = Gtk.Image.new_from_pixbuf(
#                 book.get_cover(size=BookCell.image_height))
#             stacked.add(image)
#         self.add(stacked)
#         self.add(Gtk.Label(label=name))

# x * y = a
# x = 2/3 * y
# 2/3 * y^2 = a
# y = sqrt(3/2 * a)

# class CollectionCell(Gtk.Box):
#         def __init__(self, name, books):
#             super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=10)
#             self.get_style_context().add_class('collection')

#             grid = Gtk.Grid(column_spacing=5, row_spacing=5)

#             columns = round(sqrt(3 / 2 * len(books)))
#             rows = ceil(len(books) / columns)

#             image_height = (BookCell.image_height -
#                             (rows - 1) * grid.props.row_spacing - 16) / rows

#             for index, book in enumerate(books):
#                 image = Gtk.Image.new_from_pixbuf(
#                     book.get_cover(size=image_height))
#                 image.props.halign = Gtk.Align.CENTER
#                 grid.attach(image, index % columns, index // columns, 1, 1)
#             self.add(grid)
#             self.add(Gtk.Label(label=name))


class BookCell(Gtk.EventBox):
    __gsignals__ = {
        'clicked': (GObject.SignalFlags.RUN_FIRST, None, ())
    }

    image_height = 160

    def __init__(self, book):
        super().__init__()
        self.book = book

        self.connect('button-press-event', self.on_mouse_pressed)
        self.connect('button-release-event', self.on_mouse_released)

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.box.get_style_context().add_class('book')
        self.add(self.box)

        fixed = Gtk.Fixed()

        self.pixbuf = book.get_cover(size=BookCell.image_height)
        self.image = Gtk.Image.new_from_pixbuf(self.pixbuf)
        fixed.add(self.image)

        drawingarea = Gtk.DrawingArea()
        drawingarea.set_size_request(self.pixbuf.get_width(),
                                     self.pixbuf.get_height())
        drawingarea.connect('draw', self.draw_progress)

        fixed.add(drawingarea)
        self.box.add(fixed)

        # self.label = Gtk.Label(label=title, wrap=True)
        # self.add(self.label)

    def draw_progress(self, da, ctx: Context):
        if not self.book.progress:
            return

        padding = 10

        width = self.pixbuf.get_width() - 2 * padding
        height = 10
        x = 10
        y = self.pixbuf.get_height() - height - padding

        rounded_rect(ctx, x, y, width, height, height / 2)
        ctx.set_source_rgb(1, 1, 1)
        ctx.fill()
        rounded_rect(ctx, x, y, width, height, height / 2)
        ctx.set_source_rgb(233 / 255, 84 / 255, 32 / 255)  # E95420
        # ctx.set_source_rgb(19/255, 124/255, 189/255)
        ctx.set_line_width(1.5)
        ctx.stroke()
        rounded_rect(ctx, x + 2, y + 2, self.book.progress * (width - 4), height - 4, (height - 4) / 2)
        ctx.fill()

    def on_mouse_pressed(self, button, event):
        print(event.button)
        print('Button')

    def on_mouse_released(self, button, event):
        print('Released')
        self.emit('clicked')
