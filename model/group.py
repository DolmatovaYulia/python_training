from sys import maxsize


class Group:
    def __init__(self, group_name=None, header=None, footer=None, id=None):
        self.group_name = group_name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.group_name, self.header, self.footer)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.group_name == other.group_name

    def id_or_max(gr):
        if gr.id:
            return int(gr.id)
        else:
            return maxsize

