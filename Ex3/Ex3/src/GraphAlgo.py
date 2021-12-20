import json
from typing import List

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

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        pass

    def centerPoint(self) -> (int, float):
        pass

    def plot_graph(self) -> None:
        pass

    def __init__(self):
        self.graph = None
