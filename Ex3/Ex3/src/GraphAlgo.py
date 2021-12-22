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
        v = dest
        while v != src:
            nds.insert(0, v)
            v = prvs[v]
        nds.insert(0, src)
        return self.graph.nodes[dest].d, nds

    def relax(self, u, v, w, q, parents):
        if v.d > u.d + w:
            q.remove((v.d, v))
            v.d = u.d + w
            heapq.heappush(q, (self.sort_by(v), v))
            parents[v.id] = u.id
            # v.pi = u

    def sp(self, src, dest=None):
        # sp is used in two ways:
        # When dest is given it calculates parents dict to find shortest path if available, None otherwise
        # If dest is None then the function returns the longest distance between src to any other node.
        if src not in self.graph.nodes.keys():
            return None
        if dest is not None and dest not in self.graph.nodes.keys():
            return None

        self.graph.nodes[src].d = 0
        q = [(0.0, self.graph.nodes[src])]
        visited = []
        parents = {}
        visited.append(src)
        last = None
        while len(q) != 0:
            u = heapq.heappop(q)[1]
            for v, w in self.graph.all_out_edges_of_node(u.id).items():
                node = self.graph.nodes[v]
                if v not in visited:
                    node.d = float("inf")
                    heapq.heappush(q, (self.sort_by(node), node))
                    visited.append(v)
                    self.relax(u, node, w, q, parents)
                    if dest is None and (last is None or self.graph.nodes[last].d < self.graph.nodes[v].d):
                        last = v
                    if v == dest:
                        return parents
        return self.graph.nodes[last] if dest is None else None

    def shortest_path(self, src, dest):
        prvs = self.sp(src, dest)
        return self.build_path(src, dest, prvs) if prvs is not None else None

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        pass

    def centerPoint(self) -> (int, float):
        min_n = None
        min_dist = float("inf")
        for n in self.graph.get_all_v():
            d = self.sp(n).d
            if d <= min_dist:
                min_dist = d
                min_n = n
        return min_n, min_dist

        # distances = {}
        # for n in self.graph.get_all_v():
        #     distances[n] = 0
        #     for n2 in self.graph.get_all_v():
        #         if n == n2:
        #             continue
        #         d = self.shortest_path(n, n2)
        #         if d is None:
        #             return "The graph is not connected"
        #         else:
        #             distances[n] = max(distances[n], d[0])
        # node = None
        # dist = float("inf")
        # for n in distances:
        #     if distances[n] <= dist:
        #         node = n
        #         dist = distances[n]
        # return node, dist

    def plot_graph(self) -> None:
        pass

    def __init__(self):
        self.graph = None
        self.sort_by = lambda n: n.d