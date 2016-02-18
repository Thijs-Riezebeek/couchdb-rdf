import couch


class Book(couch.CouchItem):
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

    def add_language(self, language):
        self._list_append_item(self.languages, language)

    def add_description(self, description):
        self._list_append_item(self.descriptions, description)

    def add_subject(self, subject):
        self._list_append_item(self.subjects, subject)

    def add_contributor(self, contributor):
        self._list_append_item(self.contributors, contributor)

    def add_type(self, _type):
        self._list_append_item(self.types, _type)

    def add_isbn10(self, isbn10):
        self._list_append_item(self.isbn10s, isbn10)

    def add_isbn13(self, isbn13):
        self._list_append_item(self.isbn13s, isbn13)

    def add_identifier(self, identifier):
        self._list_append_item(self.identifiers, identifier)

    @staticmethod
    def _list_append_item(_list, item):
        if item != "":
            _list.append(item)

    def __repr__(self):
        try :
            return ("Book: {}\n"
                    "\tCreator              -> {}\n"
                    "\tContributors         -> {}\n"
                    "\tPublication Location -> {}\n"
                    "\tPublication County   -> {}\n"
                    "\tPublisher            -> {}\n"
                    "\tYear Issued          -> {}\n"
                    "\tLanguages            -> {}\n"
                    "\tDescriptions         -> {}\n"
                    "\tSubjects             -> {}\n"
                    "\tTypes                -> {}\n"
                    "\tIdentifiers          -> {}\n"
                    "\tIsbn10s              -> {}\n"
                    "\tIsbn13s              -> {}\n"
                    ).format(self.title, self.creator, self.contributors, self.publicationLocation, self.publicationCountry,
                             self.publisher, self.issuedYear, self.languages, self.descriptions, self.subjects, self.types,
                             self.identifiers, self.isbn10s, self.isbn13s)
        except UnicodeEncodeError:
            return "Cannot print book with Unicode Errors"


TAG_RDF_DESCRIPTION = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description"
TAG_RDF_LABEL = "{http://www.w3.org/2000/01/rdf-schema#}label"

TAG_DCTERMS_TITLE = "{http://purl.org/dc/terms/}title"
TAG_DCTERMS_CONTRIBUTOR = "{http://purl.org/dc/terms/}contributor"
TAG_DCTERMS_TYPE = "{http://purl.org/dc/terms/}type"
TAG_DCTERMS_LANGUAGE = "{http://purl.org/dc/terms/}language"
TAG_DCTERMS_PUBLISHER = "{http://purl.org/dc/terms/}publisher"
TAG_DCTERMS_ISSUED = "{http://purl.org/dc/terms/}issued"
TAG_DCTERMS_IDENTIFIER = "{http://purl.org/dc/terms/}identifier"
TAG_DCTERMS_SUBJECT = "{http://purl.org/dc/terms/}subject"
TAG_DCTERMS_DESCRIPTION = "{http://purl.org/dc/terms/}description"
TAG_DCTERMS_CREATOR = "{http://purl.org/dc/terms/}creator"

TAG_RDVOCAB_PLACEOFPUBLICATION = "{http://rdvocab.info/Elements/}placeOfPublication"

TAG_ISDB_P1016 = "{http://iflastandards.info/ns/isbd/elements/}P1016"

TAG_BIBO_ISBN10 = "{http://purl.org/ontology/bibo/}isbn10"
TAG_BIBO_ISBN13 = "{http://purl.org/ontology/bibo/}isbn13"


class BookBuilder():
    def __init__(self):
        pass

    @staticmethod
    def from_rdf_description(elem):
        """
        :type elem: xml.etree.ElementTree.Element
        :rtype: Book
        """
        book = Book()

        # self.isbn10s, self.isbn13s = [], []

        for child in elem:
            if child.tag == TAG_DCTERMS_TITLE:
                book.title = elem.text
            elif child.tag == TAG_DCTERMS_CONTRIBUTOR:
                book.add_contributor(BookBuilder._get_inner_description_label(elem))
            elif child.tag == TAG_DCTERMS_TYPE:
                book.add_type(BookBuilder._get_inner_description_label(elem))
            elif child.tag == TAG_DCTERMS_LANGUAGE:
                book.add_language(BookBuilder._get_inner_description_label(elem))
            elif child.tag == TAG_RDVOCAB_PLACEOFPUBLICATION:
                book.publicationCountry = BookBuilder._get_inner_description_label(elem)
            elif child.tag == TAG_ISDB_P1016:
                book.publicationLocation = BookBuilder._get_inner_description_label(elem)
            elif child.tag == TAG_DCTERMS_PUBLISHER:
                book.publisher = BookBuilder._get_inner_description_label(elem)
            elif child.tag == TAG_DCTERMS_ISSUED:
                book.issuedYear = elem.text
            elif child.tag == TAG_DCTERMS_IDENTIFIER:
                book.add_identifier(BookBuilder._get_inner_description_label(elem))
            elif child.tag == TAG_DCTERMS_SUBJECT:
                book.add_subject(BookBuilder._get_inner_description_label(elem))
            elif child.tag == TAG_DCTERMS_DESCRIPTION:
                book.add_description(BookBuilder._get_inner_description_label(elem))
            elif child.tag == TAG_DCTERMS_CREATOR:
                book.creator = BookBuilder._get_inner_description_label(elem)
            elif child.tag == TAG_BIBO_ISBN10:
                book.add_isbn10(BookBuilder._get_inner_description_label(elem))
            elif child.tag == TAG_BIBO_ISBN13:
                book.add_isbn13(BookBuilder._get_inner_description_label(elem))

        return book

    @staticmethod
    def _get_inner_description_label(elem):
        """
        :type elem: xml.etree.ElementTree.Element
        :rtype : str
        """
        description = elem.find(TAG_RDF_DESCRIPTION)

        if description is None:
            return elem.text

        label = description.find(TAG_RDF_LABEL)

        if label is None:
            return ""

        return label.text
