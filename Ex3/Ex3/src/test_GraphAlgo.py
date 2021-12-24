import os
import unittest
from GraphAlgo import GraphAlgo

a = GraphAlgo()
path = r"C:/Users/shaha/PycharmProjects/OOP_Ex3/Ex3/Ex3/src/data/"


class test_GraphAlgo(unittest.TestCase):

    def test_load_from_json(self):
        self.assertTrue(a.load_from_json(os.path.join(path, "A0.json")))

    def test_save_to_json(self):
        a.load_from_json(path)
        self.assertTrue(a.save_to_json("test.json"))

    def test_get_graph(self):
        self.assertEquals(a.graph, a.get_graph())

    def test_shortest_path(self):
        a.load_from_json(os.path.join(path, "A4.json"))
        # Graph 4:
        self.assertEquals(a.shortest_path(0, 3), (4.053703927458311, [0, 1, 2, 3]))

    def test_tsp(self):
        a.load_from_json(os.path.join(path, "A0.json"))
        t = a.TSP([3, 5, 7])
        self.assertTrue(t[0], [3, 4, 5, 6, 7])

    def test_center_point(self):
        a.load_from_json(os.path.join(path, "A0.json"))  # Graph 0
        p, d = a.centerPoint()
        self.assertTrue(p, 7)

    def test_plot_graph(self):
        assert True
