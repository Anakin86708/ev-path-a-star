from copy import deepcopy
from typing import List, Dict, Set

import networkx as nx
import numpy as np
import pandas as pd

from ev_path.edges import EdgeABC
from ev_path.nodes import NodeABC


class Graph:
    def __init__(self, edges: List[EdgeABC]):
        if not isinstance(edges, list) and not isinstance(edges[0], EdgeABC):
            raise TypeError("Edges must be a list of EdgeABC")
        self._edges = edges
        self._weights = self.extract_weights(edges)

    @property
    def nodes(self) -> Set[NodeABC]:
        """
        :return: Returns a Set of unique edges.
        """
        return Graph.extract_nodes(self.edges)

    @property
    def edges(self) -> List[EdgeABC]:
        """
        :return:  Returns a copy of edges.
        """
        return deepcopy(self._edges)

    @property
    def weights(self) -> Dict[EdgeABC, float]:
        """
        :return: Returns a copy of weights.
        """
        return deepcopy(self._weights)

    @property
    def matrix_adj(self) -> pd.DataFrame:
        """
        :return: Returns a matrix (dataframe) containing the weight between two nodes.
        """
        m = len(self.nodes)
        names = set(map(lambda x: x.name, self.nodes))
        matrix = pd.DataFrame(np.zeros((m, m)), columns=names, index=names)
        for edge, cost in self.weights.items():
            matrix.loc[edge.node_1.name, edge.node_2.name] = cost
        return matrix

    def get_nodes_by_name(self, names) -> Set[NodeABC]:
        """
        :param names: Names of the node to retrieve.
        :return: Returns a list of nodes with the given name.
        """
        return set(filter(lambda x: x.name in names, self.nodes))

    def get_weight_between(self, node_1: NodeABC, node_2: NodeABC) -> float:
        """
        :param node_1: First node.
        :param node_2: Second node.
        :return: Returns the weight between the two nodes.
        """
        edge = self.get_edge_between(node_1, node_2)
        return self.weights[edge]

    def get_edge_between(self, node_1: NodeABC, node_2: NodeABC) -> EdgeABC:
        """
        :param node_1: First node.
        :param node_2: Second node.
        :return: Returns the edge between the two nodes.
        """
        return next(filter(lambda x: x.node_1 == node_1 and x.node_2 == node_2, self.edges))

    @staticmethod
    def extract_nodes(edges: List[EdgeABC]) -> Set[NodeABC]:
        """
        :param edges: List of tuples with all edges.
        :return: Returns a Set of unique edges.
        """
        nodes = set()
        for edge in edges:
            nodes.add(edge.node_1)
            nodes.add(edge.node_2)
        return nodes

    @staticmethod
    def extract_weights(edges) -> Dict[EdgeABC, float]:
        """
        :param edges: List with all edges and its weights.
        :return: Returns a Dictionary with edges as key and weight as value.
        """
        return {x: x.weight for x in edges}

    def draw(self):
        g = nx.DiGraph(self.matrix_adj)
        pos = {}
        height = []
        weight = self._get_weight_colors(g)

        for node in g.nodes:
            node_g = self.get_nodes_by_name(node).pop()
            pos[node] = (node_g.x, node_g.y)
            height.append(node_g.height)

        return nx.draw_networkx(g, pos=pos, with_labels=False, node_size=height, edge_color=weight)

    def _get_weight_colors(self, g: nx.DiGraph):
        weight = []
        for edge in g.edges:
            nodes = self.get_nodes_by_name(edge)
            n1 = next(filter(lambda x: x.name == edge[0], nodes))
            n2 = next(filter(lambda x: x.name == edge[1], nodes))
            weight.append(self.get_weight_between(n1, n2))
        return weight
