import math


class Node:
    def __init__(self, id, pos):
        self.d = 0
        self.pi = -1
        self.visited = False
        self.id = id
        if type(pos) is tuple:
            self.pos = pos
        elif type(pos) is str:
            self.pos = tuple([float(x) for x in pos.split(",")])
        else:
            self.pos = ()

    def distance(self, n):
        return math.sqrt(math.pow(self.pos[0] - n.pos[0], 2) + math.pow(self.pos[1] - n.pos[1], 2))

    def dump(self):
        return {"id": self.id, "pos": ",".join([str(x) for x in self.pos])}

    def __repr__(self):
        return "id: " + str(self.id) + " pos: " + ",".join([str(x) for x in self.pos])