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
print(j.load().edges)
