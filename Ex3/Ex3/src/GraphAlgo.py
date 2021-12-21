import json
from typing import List
import heapq

from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
from Impl.JsonParser import JsonParser


class GraphAlgo(GraphAlgoInterface):
    def load_from_json(self, file_name: str) -> bool:
        try:
            self.graph = JsonParser(file_name).load()
        except (OSError, json.JSONDecodeError):
            return False
        return True

    def save_to_json(self, file_name: str) -> bool:
        try:
            JsonParser(file_name).save(self.graph)
            return True
        except (OSError, json.JSONDecodeError):
            return False

    def get_graph(self) -> GraphInterface:
        return self.graph

    def build_path(self, src, dest, prvs):
        nds = []
        # v = self.graph.nodes[dest]
        v = dest #v.d
        while v != src:
            nds.insert(0, v) #v.id)
            v = prvs[v]
        nds.insert(0, src)
        return self.graph.nodes[dest].d, nds

    def relax(self, u, v, w, q, parents):
        if v.d > u.d + w:
            q.remove((v.d, v))
            v.d = u.d + w
            heapq.heappush(q, (self.sort_by(v), v))
            parents[v] = u
            # v.pi = u

    def shortest_path_pointer(self, src, dest):
        if src not in self.graph.nodes.keys() or dest not in self.graph.nodes.keys():
            return None
        q = [(0.0, self.graph.nodes[src])]
        visited = []
        parents = {}
        # self.graph.nodes[src].visited = True
        visited.append(src)
        while len(q) != 0:
            u = heapq.heappop(q)[1]
            if u.id == dest:
                return parents
            for v, w in self.graph.all_out_edges_of_node(u.id).items():
                node = self.graph.nodes[v]
                #if not node.visited:
                if v not in visited:
                    node.d = float("inf")
                    heapq.heappush(q, (self.sort_by(node), node))
                    # node.visited = True
                    visited.append(v)
                    self.relax(u, node, w, q, parents)
        return None


    def shortest_path(self, src, dest):
        prvs = self.shortest_path_pointer(src, dest)
        return self.build_path(src, dest, prvs) if prvs is not None else None

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        pass

    def centerPoint(self) -> (int, float):
        pass

    def plot_graph(self) -> None:
        pass

    def __init__(self):
        self.graph = None
        self.sort_by = lambda n: n.d