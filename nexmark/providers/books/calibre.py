import sqlite3
import os
from pickle import Unpickler
from collections import namedtuple

from gi.repository import GdkPixbuf
from .common import Book

CALIBRE_DIR = os.path.expanduser('~/Books')

db = None
config = None


def execute(*args, **kwargs):
    if db is None:
        open_db()
    return db.execute(*args, **kwargs)


def get_books():
    return [CalibreBook(*row) for row in execute('SELECT id, title, path, has_cover from books;')]


def open_db():
    global db
    db = sqlite3.connect(os.path.join(CALIBRE_DIR, 'metadata.db'))


def load_iterator():
    global config
    with open(os.path.expanduser('~/.config/calibre/iterator.pickle'), 'rb') as f:
        config = CalibreUnpickler(f).load()


CalibreTag = namedtuple('CalibreTag', 'id name')


class CalibreConfig(dict):
        pass


class CalibreUnpickler(Unpickler):
    def find_class(self, module, name):
        if module == 'calibre.utils.config' and name == 'DynamicConfig':
            return CalibreConfig
        return super().find_class(module, name)


class CalibreBook(Book):
    def __init__(self, id, title, path, has_cover):
        super().__init__(title)
        self.id = id
        self.path = path
        self.has_cover = has_cover

        self.tags = [CalibreTag(*row) for row in execute(
            'SELECT tags.id, tags.name FROM tags JOIN books_tags_link ON books_tags_link.tag == tags.id WHERE books_tags_link.book = ?', [id])]

    @property
    def formats(self):
        return [row[0] for row in execute('SELECT format FROM data WHERE book = ?', [self.id])]

    def filename(self, format=None):
        if format is not None:
            c = execute('SELECT name, format FROM data WHERE book = ? AND format = ?', [self.id, format])
        else:
            c = execute(
                'SELECT name, format FROM data WHERE book = ?', [self.id])
        row = c.fetchone()
        if row is None:
            return None
        name, format = row
        return os.path.join(CALIBRE_DIR, self.path, name + '.' + format.lower())

    def get_cover(self, size=None):
        if self.has_cover:
            filename = os.path.join(CALIBRE_DIR, self.path, 'cover.jpg')
            if size is not None:
                return GdkPixbuf.Pixbuf.new_from_file_at_size(filename, width=size, height=size)
            else:
                return GdkPixbuf.Pixbuf.new_from_file(filename)
        else:
            return super().get_cover(size=size)

    @property
    def progress(self):
        pass
