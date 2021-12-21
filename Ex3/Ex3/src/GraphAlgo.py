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

    def build_path(self, src, dest, prev_dict):
        nds = []
        v = dest
        while v != src:
            nds.insert(0, self.graph.nodes["id"])
            v = prev_dict[v]
        nds.insert(0, self.graph.nodes["id"])
        return nds

    def shortest_path_pointer(self, src, dest):
        if src not in self.graph.nodes[src].keys() or dest not in self.graph.nodes[dest].keys():
            return False
        n = {"key": src, "w": self.graph.nodes[src]}
        weights = {}
        prvs = {}
        explored = set()
        frontier = []
        weights[src] = 0.0
        heapq.heappush(frontier, n)
        while len(frontier) != 0:
            n = heapq.heappop(frontier)
            if n["key"] == dest:
                return prvs
            explored.add(n["key"])
            for dest in self.graph.edges["key"]:
                w =
                if dest not in explored:
                    weights[dest] = weights[n["key"]]
                    prvs[dest] =

        explored.add(src)


    def shortest_path(self, src, dest):
        pvs = self.shortest_path_pointer(src, dest)
        return self.build_path(src, dest, pvs) if pvs is not None else None

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if self.graph.is_edge(id1, id2) is True:
            return self.graph.get_edge(id1, id2).w




    def TSP(self, node_lst: List[int]) -> (List[int], float):
        pass

    def centerPoint(self) -> (int, float):
        pass

    def plot_graph(self) -> None:
        pass

    def __init__(self):
        self.graph = None
