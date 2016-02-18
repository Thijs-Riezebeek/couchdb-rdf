import copy


class CouchCollection():
    def __init__(self):
        """:type : list[CouchItem] """
        self.items = []

    def add_item(self, item):
        """
        :type item: CouchItem
        """
        self.items.append(item)

    def len(self):
        return len(self.items)

    def __repr__(self):
        result = "[ "

        for item in self.items:
            result += "\t{}".format(item)

        return result + " ]"


class CouchItem:
    def __init__(self):
        pass

    def to_dict(self):
        """
        :rtype: dict
        """
        return copy.deepcopy(self.__dict__)

    def __repr__(self):
        result = ""

        for key, value in self.to_dict().iteritems():
            try:
                result += "{0:20} -> {1}\n".format(key, value)
            except UnicodeEncodeError:
                result += "UnicodeEncodeError\n"

        return result

