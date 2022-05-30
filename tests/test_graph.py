from unittest import TestCase

import numpy as np
import pandas as pd

from ev_path.graph import Graph


class TestGraph(TestCase):

    def test_nodes(self):
        e = [
            ('a', 'b', 10.0),
            ('a', 'c', 15),
            ('b', 'a', 10),
            ('b', 'e', 8),
            ('b', 'f', 5),
            ('c', 'a', 15),
            ('c', 'd', 20),
            ('c', 'e', 4),
            ('d', 'c', 20),
            ('d', 'e', 6),
            ('e', 'c', 4),
            ('e', 'd', 6),
            ('e', 'b', 10),
            ('e', 'z', 12),
            ('f', 'b', 13),
            ('f', 'z', 15),
            ('z', 'f', 7),
            ('z', 'e', 9),
        ]
        # Expected set with all nodes from e
        expected = {'a', 'b', 'c', 'd', 'e', 'f', 'z'}

        instance = Graph(e)

        result = instance.nodes

        self.assertEqual(result, expected)

    def test_edges(self):
        e = [
            ('a', 'b', 10.0),
            ('a', 'c', 15),
            ('b', 'a', 10),
            ('b', 'e', 8),
            ('b', 'f', 5),
            ('c', 'a', 15),
            ('c', 'd', 20),
            ('c', 'e', 4),
            ('d', 'c', 20),
            ('d', 'e', 6),
            ('e', 'c', 4),
            ('e', 'd', 6),
            ('e', 'b', 10),
            ('e', 'z', 12),
            ('f', 'b', 13),
            ('f', 'z', 15),
            ('z', 'f', 7),
            ('z', 'e', 9),
        ]
        # Expected list with all edges from e, without weights
        expected = [
            ('a', 'b'),
            ('a', 'c'),
            ('b', 'a'),
            ('b', 'e'),
            ('b', 'f'),
            ('c', 'a'),
            ('c', 'd'),
            ('c', 'e'),
            ('d', 'c'),
            ('d', 'e'),
            ('e', 'c'),
            ('e', 'd'),
            ('e', 'b'),
            ('e', 'z'),
            ('f', 'b'),
            ('f', 'z'),
            ('z', 'f'),
            ('z', 'e'),
        ]

        instance = Graph(e)
        result = instance.edges

        self.assertListEqual(result, expected)

    def test_matrix_adj(self):
        e = [
            ('a', 'c', 15),
            ('b', 'a', 10),
            ('b', 'e', 8),
            ('b', 'f', 5),
            ('c', 'a', 15),
            ('c', 'd', 20),
            ('c', 'e', 4),
            ('d', 'c', 20),
            ('d', 'e', 6),
            ('e', 'c', 4),
            ('e', 'd', 6),
            ('e', 'b', 10),
            ('e', 'z', 12),
            ('f', 'b', 13),
            ('f', 'z', 15),
            ('z', 'e', 9),
        ]
        # Get nodes from e
        nodes = {'a', 'b', 'c', 'd', 'e', 'f', 'z'}
        # Expected matrix with all edges from e, with weights
        expected = pd.DataFrame(np.zeros((len(nodes), len(nodes))), index=nodes, columns=nodes)
        for node_1, node_2, weight in e:
            expected.loc[node_1, node_2] = weight

        instance = Graph(e)
        result = instance.matrix_adj

        pd.testing.assert_frame_equal(result, expected, check_dtype=False, check_like=True)

    def test_extract_nodes(self):
        e = [
            ('a', 'c'),
            ('b', 'a'),
            ('b', 'e'),
            ('b', 'f'),
            ('c', 'a'),
            ('c', 'd'),
            ('c', 'e'),
            ('d', 'c'),
            ('d', 'e'),
            ('e', 'c'),
            ('e', 'd'),
            ('e', 'b'),
            ('e', 'z'),
            ('f', 'b'),
            ('f', 'z'),
            ('z', 'e'),
        ]
        # Get nodes from e
        expected = {'a', 'b', 'c', 'd', 'e', 'f', 'z'}

        result = Graph.extract_nodes(e)

        self.assertEqual(result, expected)

    def test_extract_weights(self):
        e = [
            ('a', 'c', 15),
            ('b', 'a', 10),
            ('b', 'e', 8),
            ('b', 'f', 5),
            ('c', 'a', 15),
            ('c', 'd', 20),
            ('c', 'e', 4),
            ('d', 'c', 20),
            ('d', 'e', 6),
            ('e', 'c', 4),
            ('e', 'd', 6),
            ('e', 'b', 10),
            ('e', 'z', 12),
            ('f', 'b', 13),
            ('f', 'z', 15),
            ('z', 'e', 9),
        ]
        expected = {(node_1, node_2): weight for node_1, node_2, weight in e}

        result = Graph.extract_weights(e)

        self.assertEqual(result, expected)

    def test_extract_edges(self):
        e = [
            ('a', 'c', 15),
            ('b', 'a', 10),
            ('b', 'e', 8),
            ('b', 'f', 5),
            ('c', 'a', 15),
            ('c', 'd', 20),
            ('c', 'e', 4),
            ('d', 'c', 20),
            ('d', 'e', 6),
            ('e', 'c', 4),
            ('e', 'd', 6),
            ('e', 'b', 10),
            ('e', 'z', 12),
            ('f', 'b', 13),
            ('f', 'z', 15),
            ('z', 'e', 9),
        ]
        # Get nodes from e
        expected = [
            ('a', 'c'),
            ('b', 'a'),
            ('b', 'e'),
            ('b', 'f'),
            ('c', 'a'),
            ('c', 'd'),
            ('c', 'e'),
            ('d', 'c'),
            ('d', 'e'),
            ('e', 'c'),
            ('e', 'd'),
            ('e', 'b'),
            ('e', 'z'),
            ('f', 'b'),
            ('f', 'z'),
            ('z', 'e'),
        ]

        result = Graph.extract_edges(e)

        self.assertEqual(result, expected)
