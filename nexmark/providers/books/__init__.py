from . import calibre
from .calibre import CalibreBook


def get_books():
    return calibre.get_books()
