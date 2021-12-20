
class Edge:
    def __init__(self, src, dest, w):
        self.src = src
        self.dest = dest
        self.w = w

    def __repr__(self):
        return str(self.src) + "-> " + str(self.dest) + "(" + str(self.w) + ")"
