# graph_test.py
import unittest
from graph import DirectedGraph


class TestDirectedGraoh(unittest.TestCase):

    def test_addEdge_two_node_not_exists(self):
        newGraph = DirectedGraph()
        newGraph.add_edge("1", "2")
        self.assertTrue(("1", "2") in newGraph.links)
        self.assertTrue("1" in newGraph.nodes)
        self.assertTrue("2" in newGraph.nodes)

    def test_addEdge_one_node_not_exist(self):
        newGraph = DirectedGraph()
        newGraph.nodes.append("1")
        newGraph.add_edge("1", "2")
        self.assertTrue(("1", "2") in newGraph.links)
        print(newGraph)

    def test_get_neighbours_for_empty(self):
        newGraph = DirectedGraph()
        newGraph.add_edge("1", "2")
        self.assertEqual([], newGraph.get_neighbours_for("2"))

    def test_get_neighbours_for_not_empty(self):
        newGraph = DirectedGraph()
        newGraph.add_edge("1", "2")
        newGraph.add_edge("1", "3")
        self.assertEqual(["2", "3"], newGraph.get_neighbours_for("1"))

    def test_path_between_false(self):
        newGraph = DirectedGraph()
        newGraph.add_edge("1", "2")
        newGraph.add_edge("1", "3")
        self.assertFalse(newGraph.path_between("2", "3"))

    def test_path_between_true(self):
        newGraph = DirectedGraph()
        newGraph.add_edge("1", "2")
        newGraph.add_edge("2", "3")
        newGraph.add_edge("3", "4")
        self.assertTrue(newGraph.path_between("1", "4"))


if __name__ == '__main__':
    unittest.main()
