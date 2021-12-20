import json

from DiGraph import DiGraph
from Edge import Edge
from Node import Node


class JsonParser:
    def __init__(self, filename):
        self.filename = filename

    def parse(self, graph):
        pass

    def load(self):
        with open(self.filename, "r") as f:
            js = json.loads(f.read())
            return DiGraph(**js)


j = JsonParser("/Users/ofirrubin/PycharmProjects/OOP_Ex3/Ex3/Ex3/src/data/A5_edited")
g = j.load()
g.add_node(1, (0, 2, 3))
g.add_node(2, (1, 2, 3))
g.add_edge(1, 2, 3.5)
g.add_edge(2, 1, 2)
g.remove_edge(2, 1)
