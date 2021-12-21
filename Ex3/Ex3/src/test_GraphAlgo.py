import unittest
from GraphAlgo import GraphAlgo

a = GraphAlgo()


class test_GraphAlgo(unittest.TestCase):

    def test_load_from_json(self):
        self.assertTrue(a.load_from_json("C:/Users/shaha/PycharmProjects/OOP_Ex3/Ex3/Ex3/data/A0.json"))


    def test_save_to_json(self):
        a.load_from_json("C:/Users/shaha/PycharmProjects/OOP_Ex3/Ex3/Ex3/data/A0.json")
        self.assertTrue(a.save_to_json("test.json"))

    def test_get_graph(self):
        self.assertEquals(a.graph, a.get_graph())


    def test_shortest_path(self):
        a.load_from_json("C:/Users/shaha/PycharmProjects/OOP_Ex3/Ex3/Ex3/data/A0.json")


    def test_tsp(self):
        assert False


    def test_center_point(self):
        assert False


    def test_plot_graph():
        assert False
