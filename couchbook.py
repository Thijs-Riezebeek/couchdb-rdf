import copy

import couch
import book


class CouchBook(couch.CouchItem):
    def __init__(self):
        couch.CouchItem.__init__(self)
        self.title = None
        self.creator = None
        self.languages = []
        self.descriptions = []
        self.subjects = []

        self.contributors = []
        self.types = []

        self.isbn10s, self.isbn13s = [], []
        self.identifiers = []

        self.publicationLocation = None
        self.publicationCountry = None

        self.publisher = None
        self.issuedYear = None


class CouchBookBuilder:
    def __init__(self):
        pass

    @staticmethod
    def from_book(book):
        """
        :type book: book.Book
        :rtype: CouchBook
        """
        couch_book = CouchBook()

        couch_book.title = book.title
        couch_book.creator = book.creator
        couch_book.publicationLocation = book.publicationLocation
        couch_book.publicationCountry = book.publicationCountry
        couch_book.publisher = book.publisher
        couch_book.issuedYear = book.issuedYear

        couch_book.languages = copy.deepcopy(book.languages)
        couch_book.descriptions = copy.deepcopy(book.descriptions)
        couch_book.subjects = copy.deepcopy(book.subjects)
        couch_book.contributors = copy.deepcopy(book.contributors)
        couch_book.types = copy.deepcopy(book.types)
        couch_book.isbn10s = copy.deepcopy(book.isbn10s)
        couch_book.isbn13s = copy.deepcopy(book.isbn13s)
        couch_book.identifiers = copy.deepcopy(book.identifiers)

        return couch_book
