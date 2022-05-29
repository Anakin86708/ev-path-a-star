from copy import deepcopy
from typing import List, Tuple, Dict

import numpy as np
import pandas as pd


class Graph:
    def __init__(self, edges: List[Tuple[str, str, float]]):
        self._edges = self.extract_edges(edges)
        self.weights = self.extract_weights(edges)

    @property
    def nodes(self):
        return Graph.split_nodes(self.edges)

    @property
    def edges(self):
        return deepcopy(self._edges)

    @property
    def matrix_adj(self):
        m = len(self.nodes)
        matrix = pd.DataFrame(np.zeros((m, m)), columns=self.nodes, index=self.nodes)
        for (node_1, node_2), cost in zip(self.edges, self.weights.values()):
            matrix[node_2][node_1] = cost
        return matrix

    @staticmethod
    def split_nodes(edges):
        a, b = zip(*edges)
        return set(a).union(set(b))

    @staticmethod
    def extract_weights(edges) -> Dict[Tuple[str, str], float]:
        return {x[:-1]: x[-1] for x in edges}

    @staticmethod
    def extract_edges(edges):
        return [x[:-1] for x in edges]
