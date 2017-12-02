from .cover import get_cover


class Book:
    def __init__(self, title):
        self.title = title

    @property
    def get_cover(self, size=None):
        return get_cover(self.title, size=size)
