from GraphInterface import GraphInterface
from Impl.Edge import Edge
from Impl.Node import Node


class DiGraph(GraphInterface):
   # dict [src] => dict<dest, edge>
   # dict [dest] => dict<src, edge> src =1 => dict<5, edge>,6,9] | dest =9 [1,2]
    def __init__(self, Nodes, Edges):
        self.nodes = {}
        self.edges = {}  # dict[src] of (dict[dest] of edges)
        self.inverse = {}  # dict[dest] of (dict[src] of None)
        self.mc = 0

        self.node_parser(Nodes)
        self.edge_parser(Edges)

    def node_parser(self, nodes):
        for n in nodes:
            self.nodes[n["id"]] = Node(**n)

    def edge_parser(self, edges):
        for e in edges:
            edg = Edge(**e)
            self.edges[e["src"]][e["dest"]] = edg
            self.inverse[e["dest"]][e["src"]] = edg.w

    def v_size(self) -> int:
        return len(self.nodes)

    def e_size(self) -> int:
        return len(self.edges)

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 in self.nodes and id2 in self.nodes:
            self.edges[id1][id2] = Edge(id1, id2, weight)
            self.inverse[id2][id1] = weight
            return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.nodes:
            return False
        else:
            self.nodes[node_id] = Node(node_id, pos)
            return True

    def remove_node(self, node_id: int) -> bool:
        if node_id in self.nodes:
            for dest in self.edges[node_id]:
                self.inverse[dest].pop(node_id)
            self.nodes.pop(node_id)
            self.edges.pop(node_id)
            return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        self.edges[node_id1].pop(node_id2)
        self.inverse[node_id2].pop(node_id1)

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.inverse[id1]

    def all_out_edges_of_node(self, id1: int) -> dict:
        pass
