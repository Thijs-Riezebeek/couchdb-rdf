class CouchCollection():
    def __init__(self):
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
            result += " " + item.__repr__() + " "

        return result + " ]"


class CouchItem():
    def __init__(self):
        pass
