import logging
from copy import deepcopy
from typing import List, Set
from unittest import TestCase

import numpy as np
import pandas as pd

from ev_path.edges import StreetEdge, EdgeABC
from ev_path.graph import Graph
from ev_path.nodes import Node, NodeABC
from utils import problem02


class TestGraph(TestCase):
    log = logging.getLogger(__name__)

    def test_nodes(self):
        logging.basicConfig(level=logging.DEBUG)
        e = [
            StreetEdge(Node('a'), Node('b'), 10.0),
            StreetEdge(Node('a'), Node('c'), 15),
            StreetEdge(Node('b'), Node('a'), 10),
            StreetEdge(Node('b'), Node('e'), 8),
            StreetEdge(Node('b'), Node('f'), 5),
            StreetEdge(Node('c'), Node('a'), 15),
            StreetEdge(Node('c'), Node('d'), 20),
            StreetEdge(Node('c'), Node('e'), 4),
            StreetEdge(Node('d'), Node('c'), 20),
            StreetEdge(Node('d'), Node('e'), 6),
            StreetEdge(Node('e'), Node('c'), 4),
            StreetEdge(Node('e'), Node('d'), 6),
            StreetEdge(Node('e'), Node('b'), 10),
            StreetEdge(Node('e'), Node('z'), 12),
            StreetEdge(Node('f'), Node('b'), 13),
            StreetEdge(Node('f'), Node('z'), 15),
            StreetEdge(Node('z'), Node('f'), 7),
            StreetEdge(Node('z'), Node('e'), 9),
        ]
        # Expected set with all nodes from e
        expected = {Node('a'), Node('b'), Node('c'), Node('d'), Node('e'), Node('f'), Node('z')}

        instance = Graph(e)

        result = instance.nodes

        self.log.info('Expected: %s', expected)
        self.log.info('Result: %s', result)
        self.assertEqual(expected, result)

    def test_nodes_problem02(self):
        e = problem02.graph_edges
        # Expected set with all nodes from e
        expected = {Node('a'), Node('b'), Node('c'), Node('d'), Node('e'), Node('f'), Node('g'), Node('h'), Node('i'),
                    Node('j')}

        instance = Graph(e)

        result = instance.nodes

        self.assertEqual(expected, result)

    def test_edges(self):
        e = [
            StreetEdge(Node('a'), Node('b'), 10.0),
            StreetEdge(Node('a'), Node('c'), 15),
            StreetEdge(Node('b'), Node('a'), 10),
            StreetEdge(Node('b'), Node('e'), 8),
            StreetEdge(Node('b'), Node('f'), 5),
            StreetEdge(Node('c'), Node('a'), 15),
            StreetEdge(Node('c'), Node('d'), 20),
            StreetEdge(Node('c'), Node('e'), 4),
            StreetEdge(Node('d'), Node('c'), 20),
            StreetEdge(Node('d'), Node('e'), 6),
            StreetEdge(Node('e'), Node('c'), 4),
            StreetEdge(Node('e'), Node('d'), 6),
            StreetEdge(Node('e'), Node('b'), 10),
            StreetEdge(Node('e'), Node('z'), 12),
            StreetEdge(Node('f'), Node('b'), 13),
            StreetEdge(Node('f'), Node('z'), 15),
            StreetEdge(Node('z'), Node('f'), 7),
            StreetEdge(Node('z'), Node('e'), 9),
        ]
        # Expected list with all edges from e, without weights
        expected = deepcopy(e)

        instance = Graph(e)
        result = instance.edges

        self.assertListEqual(expected, result)

    def test_edges_problem02(self):
        e = problem02.graph_edges
        # Expected list with all edges from e, without weights
        expected = deepcopy(e)

        instance = Graph(e)

        result = instance.edges

        self.assertListEqual(expected, result)

    def test_matrix_adj(self):
        logging.basicConfig(level=logging.DEBUG)
        e = [
            StreetEdge(Node('a'), Node('c'), 15),
            StreetEdge(Node('b'), Node('a'), 10),
            StreetEdge(Node('b'), Node('e'), 8),
            StreetEdge(Node('b'), Node('f'), 5),
            StreetEdge(Node('c'), Node('a'), 15),
            StreetEdge(Node('c'), Node('d'), 20),
            StreetEdge(Node('c'), Node('e'), 4),
            StreetEdge(Node('d'), Node('c'), 20),
            StreetEdge(Node('d'), Node('e'), 6),
            StreetEdge(Node('e'), Node('c'), 4),
            StreetEdge(Node('e'), Node('d'), 6),
            StreetEdge(Node('e'), Node('b'), 10),
            StreetEdge(Node('e'), Node('z'), 12),
            StreetEdge(Node('f'), Node('b'), 13),
            StreetEdge(Node('f'), Node('z'), 15),
            StreetEdge(Node('z'), Node('e'), 9),
        ]
        # Get nodes from e
        nodes = {Node('a'), Node('b'), Node('c'), Node('d'), Node('e'), Node('f'), Node('z')}
        # Expected matrix with all edges from e, with weights
        expected = self._extract_matrix(e, nodes)

        instance = Graph(e)
        result = instance.matrix_adj

        self.log.info(f'Expected:\n{expected}')
        self.log.info(f'Result:\n{result}')
        pd.testing.assert_frame_equal(result, expected, check_dtype=False, check_like=True)

    def test_matrix_adj_problem02(self):
        e = problem02.graph_edges
        # Get nodes from e
        nodes = {Node('a'), Node('b'), Node('c'), Node('d'), Node('e'), Node('f'), Node('g'), Node('h'), Node('i'),
                 Node('j')}
        # Expected matrix with all edges from e, with weights
        expected = self._extract_matrix(e, nodes)

        instance = Graph(e)
        result = instance.matrix_adj

        print('Expected:')
        print(expected)
        print('Result:')
        print(result)

        pd.testing.assert_frame_equal(result, expected, check_dtype=False, check_like=True)

    def test_extract_nodes(self):
        e = [
            StreetEdge(Node('a'), Node('c'), 0),
            StreetEdge(Node('b'), Node('a'), 0),
            StreetEdge(Node('b'), Node('e'), 0),
            StreetEdge(Node('b'), Node('f'), 0),
            StreetEdge(Node('c'), Node('a'), 0),
            StreetEdge(Node('c'), Node('d'), 0),
            StreetEdge(Node('c'), Node('e'), 0),
            StreetEdge(Node('d'), Node('c'), 0),
            StreetEdge(Node('d'), Node('e'), 0),
            StreetEdge(Node('e'), Node('c'), 0),
            StreetEdge(Node('e'), Node('d'), 0),
            StreetEdge(Node('e'), Node('b'), 0),
            StreetEdge(Node('e'), Node('z'), 0),
            StreetEdge(Node('f'), Node('b'), 0),
            StreetEdge(Node('f'), Node('z'), 0),
            StreetEdge(Node('z'), Node('e'), 0),
        ]
        # Get nodes from e
        expected = {Node('a'), Node('b'), Node('c'), Node('d'), Node('e'), Node('f'), Node('z')}

        result = Graph.extract_nodes(e)

        self.assertEqual(expected, result)

    def test_extract_weights(self):
        e = [
            StreetEdge(Node('a'), Node('c'), 15),
            StreetEdge(Node('b'), Node('a'), 10),
            StreetEdge(Node('b'), Node('e'), 8),
            StreetEdge(Node('b'), Node('f'), 5),
            StreetEdge(Node('c'), Node('a'), 15),
            StreetEdge(Node('c'), Node('d'), 20),
            StreetEdge(Node('c'), Node('e'), 4),
            StreetEdge(Node('d'), Node('c'), 20),
            StreetEdge(Node('d'), Node('e'), 6),
            StreetEdge(Node('e'), Node('c'), 4),
            StreetEdge(Node('e'), Node('d'), 6),
            StreetEdge(Node('e'), Node('b'), 10),
            StreetEdge(Node('e'), Node('z'), 12),
            StreetEdge(Node('f'), Node('b'), 13),
            StreetEdge(Node('f'), Node('z'), 15),
            StreetEdge(Node('z'), Node('e'), 9),
        ]
        expected = {edge: edge.weight for edge in e}

        result = Graph.extract_weights(e)

        self.assertEqual(expected, result)

    def test_get_nodes_by_single_name(self):
        e = [
            StreetEdge(Node('a'), Node('b'), 10.0),
            StreetEdge(Node('a'), Node('c'), 15),
            StreetEdge(Node('b'), Node('a'), 10),
            StreetEdge(Node('b'), Node('e'), 8),
            StreetEdge(Node('b'), Node('f'), 5),
            StreetEdge(Node('c'), Node('a'), 15),
            StreetEdge(Node('c'), Node('d'), 20),
            StreetEdge(Node('c'), Node('e'), 4),
            StreetEdge(Node('d'), Node('c'), 20),
            StreetEdge(Node('d'), Node('e'), 6),
            StreetEdge(Node('e'), Node('c'), 4),
            StreetEdge(Node('e'), Node('d'), 6),
            StreetEdge(Node('e'), Node('b'), 10),
            StreetEdge(Node('e'), Node('z'), 12),
            StreetEdge(Node('f'), Node('b'), 13),
            StreetEdge(Node('f'), Node('z'), 15),
            StreetEdge(Node('z'), Node('f'), 7),
            StreetEdge(Node('z'), Node('e'), 9),
        ]
        node_name = 'z'
        expected = Node(node_name)

        instance = Graph(e)
        result = instance.get_nodes_by_name(node_name)

        self.assertEqual(1, len(result))
        self.assertTrue(expected in result)

    @staticmethod
    def _extract_matrix(edges: List[EdgeABC], nodes: Set[NodeABC]) -> pd.DataFrame:
        names = set(map(lambda x: x.name, nodes))
        expected = pd.DataFrame(np.zeros((len(nodes), len(nodes))), index=names, columns=names)
        for edge in edges:
            expected.loc[edge.node_1.name, edge.node_2.name] = edge.weight
        return expected
