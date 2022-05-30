from copy import deepcopy
from typing import List, Tuple, Dict, Set

import numpy as np
import pandas as pd


class Graph:
    def __init__(self, edges_and_weights: List[Tuple[str, str, float]]):
        self._edges = self.extract_edges(edges_and_weights)
        self._weights = self.extract_weights(edges_and_weights)

    @property
    def nodes(self) -> Set[str]:
        return Graph.extract_nodes(self.edges)

    @property
    def edges(self) -> List[Tuple[str, str]]:
        return deepcopy(self._edges)

    @property
    def weights(self) -> Dict[Tuple[str, str], float]:
        return deepcopy(self._weights)

    @property
    def matrix_adj(self) -> pd.DataFrame:
        m = len(self.nodes)
        matrix = pd.DataFrame(np.zeros((m, m)), columns=self.nodes, index=self.nodes)
        for (node_1, node_2), cost in zip(self.edges, self._weights.values()):
            matrix.loc[node_1, node_2] = cost
        return matrix

    @staticmethod
    def extract_nodes(edges: List[Tuple[str, str]]) -> Set[str]:
        a, b = zip(*edges)
        return set(a).union(set(b))

    @staticmethod
    def extract_weights(edges) -> Dict[Tuple[str, str], float]:
        return {x[:-1]: x[-1] for x in edges}

    @staticmethod
    def extract_edges(edges: List[Tuple[str, str, float]]) -> List[Tuple[str, str]]:
        return [x[:-1] for x in edges]
