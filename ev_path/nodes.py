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

    def __hash__(self):
        return hash((self.name, self.x, self.y, self.height))

    def __eq__(self, other: "NodeABC"):
        return self.name == other.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


class Node(NodeABC):
    """
    This representation of Node should only be used for testing purposes or when the position of the node in the
    space is irrelevant, as it considers all coordinates as zero.
    """

    def __init__(self, name: str):
        """
        Only the name is necessary, as the others values are all set as zero.

        :param name: Name that represents this node.
        :type name: str
        """
        super().__init__(name, 0, 0, 0)


class StreetIntersectionNode(NodeABC):

    def __init__(self, name: str, x: float, y: float, height: float):
        super().__init__(name, x, y, height)
