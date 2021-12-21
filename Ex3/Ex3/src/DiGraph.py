from GraphInterface import GraphInterface
from Impl.Node import Node


class DiGraph(GraphInterface):
   # dict [src] => dict<dest, edge>
   # dict [dest] => dict<src, edge> src =1 => dict<5, edge>,6,9] | dest =9 [1,2]
    def __init__(self, Nodes = None, Edges = None):
        self.nodes = {}
        self.edges = {}  # dict[src] of (dict[dest] of edges)
        self.inverse = {}  # dict[dest] of (dict[src] of None)
        self.mc = 0
        self.edge_count = 0
        if Nodes is not None:
            self.node_parser(Nodes)
        if Edges is not None:
            self.edge_parser(Edges)

    def node_parser(self, nodes):
        for n in nodes:
            self.add_node(n["id"], n["pos"])

    def edge_parser(self, edges):
        for e in edges:
            self.add_edge(e["src"], e["dest"], e["w"])

    def v_size(self) -> int:
        return len(self.nodes)

    def e_size(self) -> int:
        return self.edge_count

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 in self.nodes.keys() and id2 in self.nodes.keys():
            self.edges[id1][id2] = weight
            self.inverse[id2][id1] = weight
            self.mc += 1
            self.edge_count += 1
            return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.nodes:
            return False
        else:
            self.nodes[node_id] = Node(node_id, pos)
            self.edges[node_id] = {}
            self.inverse[node_id] = {}
            self.mc += 1
            return True

    def remove_node(self, node_id: int) -> bool:
        if node_id in self.nodes:
            for dest in self.edges[node_id]:
                self.inverse[dest].pop(node_id)
            self.nodes.pop(node_id)
            self.edges.pop(node_id)
            self.mc += 1
            return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 in self.edges.keys() and node_id2 in self.edges[node_id1].keys():
            self.edges[node_id1].pop(node_id2)
            self.inverse[node_id2].pop(node_id1)
            self.edge_count -= 1
            self.mc += 1
            return True
        return False

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        if id1 in self.inverse.keys():
            return self.inverse[id1]
        return {}

    def all_out_edges_of_node(self, id1: int) -> dict:
        if id1 in self.edges.keys():
            return self.edges[id1]
        return {}

    def is_edge(self, id1, id2):
        return id2 in self.edges[id1].keys()

    def get_edge(self, id1, id2):
        return self.edges[id1][id2]

    def get_weight(self, id1: int, id2: int) -> (float, list):
        if self.graph.is_edge(id1, id2) is True:
            return self.graph.get_edge(id1, id2)


