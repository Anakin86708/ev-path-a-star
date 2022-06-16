import logging
from logging import DEBUG
from queue import PriorityQueue
from unittest import TestCase
from unittest.mock import Mock

from ev_path.astar import AStar
from ev_path.graph import Graph
from utils import romenia, problem02, robot, problem01


class TestAStar(TestCase):
    def test_graph(self):
        graph_mock = Graph([('a', 'b', 10.0), ('a', 'c', 15), ('b', 'a', 10), ('b', 'e', 8), ('b', 'f', 5)])

        instance = AStar(graph_mock, None)

        self.assertIsInstance(instance.graph, Graph)

    def test_path_from_to_romenia(self):
        logging.basicConfig(level=DEBUG)
        e = romenia.graph_cities
        expected = romenia.expected
        expected_cost = romenia.expected_cost
        heuristic = romenia.heuristic
        graph = Graph(e)

        instance = AStar(graph, heuristic)
        result_cost, result = instance.path_from_to(romenia.start_city, romenia.end_city)

        self.assertIsInstance(result, list)
        self.assertEqual(expected, result)
        self.assertEqual(expected_cost, result_cost)

    def test_path_from_to_problem01(self):
        logging.basicConfig(level=DEBUG)
        e = problem01.edges
        expected = problem01.expected
        expected_cost = problem01.expected_cost
        heuristic = problem01.heuristic
        graph = Graph(e)

        instance = AStar(graph, heuristic)
        result_cost, result = instance.path_from_to(problem01.start_node, problem01.end_node)

        self.assertIsInstance(result, list)
        self.assertEqual(expected, result)
        self.assertEqual(expected_cost, result_cost)

    def test_path_from_to_problem02(self):
        logging.basicConfig(level=DEBUG)
        e = problem02.graph_edges
        expected = problem02.expected
        expected_cost = problem02.expected_cost
        heuristic = problem02.heuristic
        graph = Graph(e)

        instance = AStar(graph, heuristic)
        result_cost, result = instance.path_from_to(problem02.start_node, problem02.end_node)

        self.assertIsInstance(result, list)
        self.assertEqual(expected, result)
        self.assertEqual(expected_cost, result_cost)

    def test_path_from_to_robot(self):
        logging.basicConfig(level=DEBUG)
        e = robot.graph
        expected = robot.expected
        heuristic = robot.heuristic
        graph = Graph(e)

        instance = AStar(graph, heuristic)
        result_cost, result = instance.path_from_to(robot.start_node, robot.end_node)

        self.assertIsInstance(result, list)
        self.assertEqual(expected, result)

    def test_real_cost(self):
        mock_graph = Mock()
        mock_graph.weights = {
            ('5', '3'): 4,
            ('3', '4'): 2,
            ('4', '10'): 3,
            ('3', '11'): 5,
        }
        path = {
            '5': None,
            '3': '5',
            '4': '3',
            '10': '4'
        }
        start_node = '5'
        end_node = '10'
        expected = 9

        instance = AStar(mock_graph, lambda _: 0)
        result = instance.real_cost(start_node, end_node, path)

        self.assertEqual(expected, result)

    def test_recreate_path_to_start(self):
        path = {
            '5': None,
            '3': '5',
            '4': '3',
            '10': '4'
        }
        start_node = '5'
        end_node = '10'
        expected = ['5', '3', '4', '10']

        result = AStar.recreate_path_to_start(start_node, end_node, path)

        self.assertEqual(expected, result)

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

        with self.assertRaises(ValueError, msg=f'Node "{end_node}" not in graph'):
            instance.are_nodes_present_on_graph(start_node, end_node)

    def test_node_already_in_opened(self):
        node = 'x'
        itens = {'a', 'x', 'b', 'y'}
        opened = PriorityQueue()
        for item in itens:
            opened.put((0, item))

        instance = AStar(None, None)
        result = instance._node_already_in_opened(node, opened)

        self.assertTrue(result)
