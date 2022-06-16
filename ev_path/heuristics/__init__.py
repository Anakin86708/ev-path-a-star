from abc import ABC, abstractmethod
from copy import deepcopy

from ev_path.nodes import NodeABC


class HeuristicABC(ABC):

    def __init__(self, end_node: NodeABC):
        self._end_node = end_node

    @property
    def end_node(self) -> NodeABC:
        return deepcopy(self._end_node)

    @abstractmethod
    def heuristic(self, node: NodeABC) -> float:
        pass


class EuclideanHeuristic(HeuristicABC):

    def __init__(self, end_node: NodeABC):
        super().__init__(end_node)

    def heuristic(self, node: NodeABC) -> float:
        delta_x = (node.x - self.end_node.x)
        delta_y = (node.y - self.end_node.y)
        delta_height = (node.height - self.end_node.height)
        return (delta_x ** 2 + delta_y ** 2 + delta_height ** 2) ** 0.5


class ManhattanHeuristic(HeuristicABC):

    def __init__(self, end_node: NodeABC):
        super().__init__(end_node)

    def heuristic(self, node: NodeABC) -> float:
        pass
