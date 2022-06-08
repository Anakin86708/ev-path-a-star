from abc import ABC


class NodeABC(ABC):

    def __init__(self, name: str, x: float, y: float, height: float):
        self.name = name
        self._x = x
        self._y = y
        self._height = height

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def height(self):
        return self._height


class StreetIntersectionNode(NodeABC):

    def __init__(self, name: str, x: float, y: float, height: float):
        super().__init__(name, x, y, height)
