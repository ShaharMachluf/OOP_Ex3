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

    def build_path(self, src, dest):
        nds = []
        v = self.graph.nodes[dest]
        w = v.d
        while v != src:
            nds.insert(0, v.id)
            v = v.pi
        nds.insert(0, src)
        return w, nds

    def relax(self, u, v, w, q):
        if v.d > u.d + w:
            q.remove((v.d, v))
            v.d = u.d + w
            heapq.heappush(q, (v.d, v))
            v.pi = u

    def shortest_path_pointer(self, src, dest):
        if src not in self.graph.nodes[src].keys() or dest not in self.graph.nodes[dest].keys():
            return False
        q = [(0.0, self.graph.nodes[src])]
        while len(q) != 0:
            u = heapq.heappop(q)[1]
            if u.id == dest:
                return True
            for v, w in self.graph.all_out_edges_of_node(u).items:
                if not v.visited:
                    heapq.heappush(q, (float("inf"), v))
                    v.visited = True
                self.relax(u, v, w, q)
        return False


    def shortest_path(self, src, dest):
        return self.build_path(src, dest) if self.shortest_path_pointer(src, dest) else None

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        pass

    def centerPoint(self) -> (int, float):
        pass

    def plot_graph(self) -> None:
        pass

    def __init__(self):
        self.graph = None
