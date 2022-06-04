from unittest import TestCase
from unittest.mock import Mock

from ev_path.astar import AStar
from ev_path.graph import Graph


class TestAStar(TestCase):
    def test_graph(self):
        graph_mock = Graph([('a', 'b', 10.0), ('a', 'c', 15), ('b', 'a', 10), ('b', 'e', 8), ('b', 'f', 5)])

        instance = AStar(graph_mock, None)

        self.assertIsInstance(instance.graph, Graph)

    def test_path_from_to(self):
        self.fail()

    def test_are_nodes_present_on_graph_valid(self):
        start_node = 'x'
        end_node = 'y'
        graph_mock = Mock()
        graph_mock.nodes = {'x', 'a', 'b', 'y'}

        instance = AStar(graph_mock, None)
        result = instance.are_nodes_present_on_graph(start_node, end_node)

        self.assertTrue(result)

    def test_are_nodes_present_on_graph_invalid(self):
        start_node = 'x'
        end_node = 'z'
        graph_mock = Mock()
        graph_mock.nodes = {'x', 'a', 'b', 'y'}

        instance = AStar(graph_mock, None)

        with self.assertRaises(ValueError, msg=f'Node {end_node} not in graph'):
            instance.are_nodes_present_on_graph(start_node, end_node)
