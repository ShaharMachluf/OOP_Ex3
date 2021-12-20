import unittest

from Ex3.Ex3.src.DiGraph import DiGraph
from Ex3.Ex3.src.Impl.Edge import Edge
from Ex3.Ex3.src.Impl.Node import Node

g = DiGraph()
g.add_node(0, (0, 1, 2))
g.add_node(1, (1, 2, 3))
g.add_node(2, (3, 4, 5))
g.add_edge(1, 0, 3.5)
g.add_edge(0, 1, 2)

class TestDiGraph(unittest.TestCase):
    def test_v_size(self):
        self.assertEquals(g.v_size(), 3)

    def test_e_size(self):
        self.assertEquals(g.e_size(), 2)

    def test_get_mc(self):
        self.assertEquals(g.get_mc(), 4)

    def test_add_edge(self):
        before = g.e_size()
        g.add_edge(0, 3, 5.6)
        self.assertEquals(g.e_size(), before)
        g.add_edge(0, 2, 3.6)
        self.assertNotEquals(before, g.e_size())

    def test_add_node():
        assert False


    def test_remove_node():
        assert False


    def test_remove_edge():
        assert False


    def test_get_all_v():
        assert False


    def test_all_in_edges_of_node():
        assert False


    def test_all_out_edges_of_node():
        assert False
