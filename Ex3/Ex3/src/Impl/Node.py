
class Node:
    def __init__(self, id, pos):
        self.d = 0
        self.pi = -1
        self.visited = False
        self.id = id
        if type(pos) is tuple:
            self.pos = pos
        else:
            self.pos = tuple([float(x) for x in pos.split(",")])

    def dump(self):
        return {"id": self.id, "pos": ",".join([str(x) for x in self.pos])}