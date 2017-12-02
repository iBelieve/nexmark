from nexmark import app
from gi.repository import Gtk, EvinceView as EvView, EvinceDocument as EvDocument

EvDocument.init()


class EvinceView(Gtk.ScrolledWindow):
    def __init__(self):
        super().__init__()
        self.viewer = EvView.View()
        self.add(self.viewer)

    def set_book(self, book):
        doc = EvDocument.Document.factory_get_document(
            'file://' + book.filename())
        model = EvView.DocumentModel(document=doc)
        model.set_sizing_mode(EvView.SizingMode.FIT_PAGE)
        model.set_continuous(False)
        model.set_page_layout(EvView.PageLayout.DUAL if app(
        ).is_landscape else EvView.PageLayout.SINGLE)
        self.viewer.set_model(model)
