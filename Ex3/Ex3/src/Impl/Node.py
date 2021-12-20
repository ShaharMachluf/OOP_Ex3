
class Node:
    def __init__(self, id, pos):
        self.id = id
        self.pos = tuple([float(x) for x in pos.split(",")])
