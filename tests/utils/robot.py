from ev_path.edges import StreetEdge
from ev_path.nodes import Node

graph = [
    StreetEdge(Node('S'), Node('B'), 4),
    StreetEdge(Node('B'), Node('S'), 4),

    StreetEdge(Node('S'), Node('D'), 5),
    StreetEdge(Node('D'), Node('S'), 5),

    StreetEdge(Node('D'), Node('E'), 2),
    StreetEdge(Node('E'), Node('D'), 2),

    StreetEdge(Node('B'), Node('E'), 1),
    StreetEdge(Node('E'), Node('B'), 1),

    StreetEdge(Node('D'), Node('H'), 3),
    StreetEdge(Node('H'), Node('D'), 3),

    StreetEdge(Node('H'), Node('J'), 1),
    StreetEdge(Node('J'), Node('H'), 1),

    StreetEdge(Node('J'), Node('K'), 6),
    StreetEdge(Node('K'), Node('J'), 6),

    StreetEdge(Node('K'), Node('T'), 2),
    StreetEdge(Node('T'), Node('K'), 2),

    StreetEdge(Node('T'), Node('L'), 3),
    StreetEdge(Node('L'), Node('T'), 3),

    StreetEdge(Node('I'), Node('L'), 4),
    StreetEdge(Node('L'), Node('I'), 4),

    StreetEdge(Node('G'), Node('I'), 3),
    StreetEdge(Node('I'), Node('G'), 3),

    StreetEdge(Node('E'), Node('F'), 6),
    StreetEdge(Node('F'), Node('E'), 6),

    StreetEdge(Node('F'), Node('G'), 4),
    StreetEdge(Node('G'), Node('F'), 4),

    StreetEdge(Node('G'), Node('C'), 1),
    StreetEdge(Node('C'), Node('G'), 1)
]

expected = [
    Node('S'),
    Node('D'),
    Node('H'),
    Node('J'),
    Node('K'),
    Node('T'),
]

start_node = Node('S')
end_node = Node('T')

_heuristic = {
    Node('S'): 5,
    Node('B'): 4,
    Node('D'): 4,
    Node('E'): 3,
    Node('F'): 2,
    Node('G'): 3,
    Node('C'): 4,
    Node('H'): 3,
    Node('J'): 2,
    Node('K'): 1,
    Node('T'): 0,
    Node('L'): 1,
    Node('I'): 2
}


def heuristic(node_name) -> float:
    return _heuristic[node_name]
