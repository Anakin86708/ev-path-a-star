from abc import ABC
from copy import deepcopy

from ev_path.nodes import NodeABC


class EdgeABC(ABC):

    def __init__(self, node_1: NodeABC, node_2: NodeABC, real_weight: float):
        self._node_1 = node_1
        self._node_2 = node_2
        self.weight = real_weight

    @property
    def node_1(self):
        return deepcopy(self._node_1)

    @property
    def node_2(self):
        return deepcopy(self._node_2)


class StreetEdge(EdgeABC):

    def __init__(self, node_1: NodeABC, node_2: NodeABC, real_weight: float):
        super().__init__(node_1, node_2, real_weight)
