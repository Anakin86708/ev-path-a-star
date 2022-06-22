from unittest import TestCase
from unittest.mock import Mock

from ev_path.heuristics import EuclideanHeuristic, ManhattanHeuristic


class TestEuclideanHeuristic(TestCase):
    def test_heuristic(self):
        end_node = Mock()
        end_node.x = 1
        end_node.y = 1
        end_node.height = 3

        node = Mock()
        node.x = 0
        node.y = 0
        node.height = 0
        expected = 11 ** 0.5

        instance = EuclideanHeuristic(end_node)
        result = instance.heuristic(node)

        self.assertAlmostEqual(expected, result, places=5)


class TestManhattanHeuristic(TestCase):
    def test_heuristic(self):
        end_node = Mock()
        end_node.x = 1
        end_node.y = 1
        end_node.height = 3

        node = Mock()
        node.x = 0
        node.y = 0
        node.height = 0
        expected = abs(1 - 0) + abs(1 - 0) + abs(3 - 0)

        instance = ManhattanHeuristic(end_node)
        result = instance.heuristic(node)

        self.assertEqual(expected, result)
