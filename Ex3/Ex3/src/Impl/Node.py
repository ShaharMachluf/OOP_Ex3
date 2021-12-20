
class Node:
    def __init__(self, id, pos):
        self.id = id
        self.pos = tuple([float(x) for x in pos.split(",")])

    def dump(self):
        return {"id": self.id, "pos": ",".join([str(x) for x in self.pos])}