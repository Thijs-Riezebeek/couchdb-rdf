import book
import couch

import couchbook

try:
    import xml.etree.cElementTree as ET

    print "Using faster c elementree version\n"
except ImportError:
    import xml.etree.ElementTree as ET


def scan_file(filename):
    """
    :type filename: str
    :rtype: couch.CouchCollection
    """
    books = couch.CouchCollection()
    events = ("start", "end")
    description_counter = 0

    for event, elem in ET.iterparse(filename, events=events):
        if elem.tag == book.BookBuilder.TAG_RDF_DESCRIPTION:
            description_counter += 1 if event == "start" else -1

            if description_counter == 0:
                books.add_item(couchbook.CouchBookBuilder.from_book(book.BookBuilder.from_rdf_description(elem)))

    return books