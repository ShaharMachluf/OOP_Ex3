import unittest

from Ex3.Ex3.src.DiGraph import DiGraph

g = DiGraph()


class TestDiGraph(unittest.TestCase):

    def setUp(self):
        global g
        g = DiGraph()
        g.add_node(0, (0, 1, 2))
        g.add_node(1, (1, 2, 3))
        g.add_node(2, (3, 4, 5))
        g.add_edge(1, 0, 3.5)
        g.add_edge(0, 1, 2)

    def test_v_size(self):
        self.assertEqual(g.v_size(), 3)

    def test_e_size(self):
        self.assertEqual(g.e_size(), 2)

    def test_get_mc(self):
        count = g.get_mc()
        g.add_node(10)
        self.assertEqual(g.get_mc(), count + 1)

    def test_add_edge(self):
        before = g.e_size()
        g.add_edge(0, 3, 5.6)
        self.assertEqual(g.e_size(), before)
        g.add_edge(0, 2, 3.6)
        self.assertNotEqual(before, g.e_size())

    def test_add_node(self):
        before = g.v_size()
        g.add_node(0, (4, 6, 7))
        self.assertEqual(g.v_size(), before)
        g.add_node(4, (5, 6, 7))
        self.assertNotEqual(before, g.v_size())

    def test_remove_node(self):
        before = g.v_size()
        g.remove_node(7)
        self.assertEqual(g.v_size(), before)
        g.remove_node(0)
        self.assertNotEqual(before, g.v_size())

    def test_remove_edge(self):
        g.add_edge(1, 2, 5.6)
        before = g.e_size()
        g.remove_edge(0, 4)
        self.assertEqual(g.e_size(), before)
        g.remove_edge(1, 2)
        self.assertNotEqual(before, g.e_size())

    def test_get_all_v(self):
        self.assertEqual(g.get_all_v(), g.nodes)

    def test_all_in_edges_of_node(self):
        self.assertEqual(g.inverse[1], g.all_in_edges_of_node(1))

    def test_all_out_edges_of_node(self):
        self.assertEqual(g.edges[1], g.all_out_edges_of_node(1))
