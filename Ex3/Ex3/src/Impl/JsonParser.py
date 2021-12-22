import json

from DiGraph import DiGraph
# from Node import Node


class JsonParser:
    def __init__(self, filename):
        self.filename = filename

    def save(self, graph):
        parsed = {"Nodes": [], "Edges": []}
        for v in graph.get_all_v().values():
            parsed["Nodes"].append(v.dump())
            parsed["Edges"].append([{"dest": v.id, "src": k, "w": w} for k, w in graph.all_in_edges_of_node(v.id).items()])
        with open(self.filename, "w+") as f:
            f.write(json.dumps(parsed, indent=4, sort_keys=True))

    def load(self):
        with open(self.filename, "r") as f:
            js = json.loads(f.read())
            return DiGraph(**js)


# j = JsonParser("/Users/ofirrubin/PycharmProjects/OOP_Ex3/Ex3/Ex3/src/old data/A5_edited")
# g = j.load()

