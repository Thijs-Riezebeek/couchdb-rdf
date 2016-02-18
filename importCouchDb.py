import book
import couch

try:
    import xml.etree.cElementTree as ET

    print "Using faster c elementree version\n"
except ImportError:
    import xml.etree.ElementTree as ET


def get_filename(test="test"):
    if test == "test":
        return "./data/BNBBasic_sample_rdf/BNBBasic_sample.rdf"
    elif test == "reduced":
        return "./data/reduced_rdf.rdf"
    else:
        return "./data/BNBBasic_201601_rdf/BNBBasic_201601_f01.rdf"

if __name__ == "__main__":
    TEST = "test"
    FILENAME = get_filename(TEST)

    events = ("start", "end")

    description_counter = 0

    books = couch.CouchCollection()

    for event, elem in ET.iterparse(FILENAME, events=events):
        if elem.tag == book.BookBuilder.TAG_RDF_DESCRIPTION:
            description_counter += 1 if event == "start" else -1

            if description_counter == 0:
                books.add_item(book.BookBuilder.from_rdf_description(elem))

    print books
