from abc import ABC
from copy import deepcopy
from dataclasses import dataclass

from ev_path.nodes import NodeABC


@dataclass
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

    def __hash__(self):
        return hash((self.node_1, self.node_2, self.weight))

    def __eq__(self, other: 'EdgeABC'):
        return self.node_1 == other.node_1 and \
               self.node_2 == other.node_2 and \
               self.weight and other.weight

    def __str__(self):
        return f"Edge({self.node_1} -> {self.node_2} : {self.weight})"

    def __repr__(self):
        return self.__str__()


class StreetEdge(EdgeABC):

    def __init__(self, node_1: NodeABC, node_2: NodeABC, real_weight: float):
        super().__init__(node_1, node_2, real_weight)
