import bookscanner


def get_filename(test="test"):
    if test == "test":
        return "./data/BNBBasic_sample_rdf/BNBBasic_sample.rdf"
    elif test == "reduced":
        return "./data/reduced_rdf.rdf"
    else:
        return "./data/BNBBasic_201601_rdf/BNBBasic_201601_f01.rdf"

if __name__ == "__main__":
    books = bookscanner.scan_file(get_filename("test"))

    print books