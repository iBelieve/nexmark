from gi.repository import Gepub


class EPUBView(Gepub.Widget):
    def __init__(self):
        super().__init__()

    def set_book(self, book):
        self.epub = Gepub.Doc(path=book.filename(format='EPUB'))
        self.epub.init(None)
        self.props.doc = self.epub
