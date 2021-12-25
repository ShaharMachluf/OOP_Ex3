import json
# from collections import Iterator
from typing import List
import heapq

from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
from Impl.JsonParser import JsonParser


def dfs(graph, start):
    """
    performs the dfs algorithm on the given graph starting from node "start"
    """
    for n in graph.get_all_v().values():
        n.visited = False
    count = 0
    count = dfs_visit(count, start, graph)
    return count


def dfs_visit(count, n, graph):
    """
    visit all the neighbors of node "n" recursively and count all the visits
    """
    n.visited = True
    count += 1
    if n.id not in graph.edges.keys():
        return count
    next_e = graph.all_out_edges_of_node(n).items()
    for next_n in next_e:
        node = graph.nodes[next_n]
        if not node.visited:
            count = dfs_visit(count, node, graph)
    return count


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
        """
        helper to sp. the function "relax" from dijkstra algorithm
        """
        if v.d > u.d + w:
            q.remove((v.d, v))
            v.d = u.d + w
            heapq.heappush(q, (self.sort_by(v), v))
            parents[v.id] = u.id

    def sp(self, src, dest=None):
        # sp is used in two ways:
        # When dest is given it calculates parents dict to find shortest path if available, None otherwise (dijkstra)
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
            if u.id == dest:
                return parents
            for v, w in self.graph.all_out_edges_of_node(u.id).items():
                node = self.graph.nodes[v]
                if v not in visited or (node.d, node) in q:
                    if v not in visited:
                        node.d = float("inf")
                        heapq.heappush(q, (self.sort_by(node), node))
                        visited.append(v)
                    self.relax(u, node, w, q, parents)
                    if dest is None and (last is None or self.graph.nodes[last].d < self.graph.nodes[v].d):
                        last = v

        return self.graph.nodes[last] if dest is None else None

    def shortest_path(self, src, dest):
        prvs = self.sp(src, dest)
        return self.build_path(src, dest, prvs) if prvs is not None else (float("inf"), [])

    def is_connected(self):
        # create gTranspose
        gTranspose = DiGraph()
        for n in self.graph.nodes.values():
            gTranspose.add_node(n.id, n.pos)
        for s in self.graph.edges.keys():
            for d in self.graph.edges[s].keys():
                gTranspose.add_edge(d, s, self.graph.edges[s][d])
        # check connectivity
        start = list(self.graph.get_all_v().values())[0]
        if dfs(self.graph, start) < self.graph.v_size():
            return False
        return dfs(gTranspose, start) == self.graph.v_size

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        dist = 0.0
        ordered_list = []
        n = node_lst.pop(0)
        ordered_list.append(n)
        min_dist = float("inf")
        closest_neighbor = n
        closest_list = []  # shortest path list between n and neighbor
        while len(node_lst) > 0:
            for neighbor in node_lst:  # for every node left in node_list check if it's the closest one to n
                curr = self.shortest_path(n, neighbor)
                if curr[0] < min_dist:
                    min_dist = curr[0]
                    closest_neighbor = neighbor
                    closest_list = curr[1]
            # after finding the closest neighbor:
            n = closest_neighbor
            node_lst.remove(closest_neighbor)
            # add shortest path list between n and neighbor to the total path list
            ordered_list.extend(closest_list[1:])
            # add shortest path dist between n and neighbor to the total path dist
            dist += min_dist
            min_dist = float("inf")  # init min dist
        return ordered_list, dist

    def centerPoint(self) -> (int, float):
        if not self.is_connected():
            return -1, float("inf")
        min_n = None
        min_dist = float("inf")
        for n in self.graph.get_all_v():
            d = self.sp(n).d
            if d <= min_dist:
                min_dist = d
                min_n = n
        return min_n, min_dist

    def plot_graph(self) -> None:
        pass

    def __init__(self, g = None):
        self.graph = g
        self.sort_by = lambda n: n.d