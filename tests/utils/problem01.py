from ev_path.edges import StreetEdge
from ev_path.nodes import Node

edges = [
    StreetEdge(Node('A'), Node('B'), 5),
    StreetEdge(Node('B'), Node('A'), 5),
    StreetEdge(Node('A'), Node('C'), 4),
    StreetEdge(Node('C'), Node('A'), 4),
    StreetEdge(Node('B'), Node('C'), 1),
    StreetEdge(Node('C'), Node('B'), 1),
    StreetEdge(Node('B'), Node('D'), 5),
    StreetEdge(Node('D'), Node('B'), 5),
    StreetEdge(Node('C'), Node('D'), 8),
    StreetEdge(Node('D'), Node('C'), 8),
    StreetEdge(Node('C'), Node('E'), 10),
    StreetEdge(Node('E'), Node('C'), 10),
    StreetEdge(Node('D'), Node('Z'), 6),
    StreetEdge(Node('Z'), Node('D'), 6),
    StreetEdge(Node('E'), Node('Z'), 5),
    StreetEdge(Node('Z'), Node('E'), 5),
    StreetEdge(Node('D'), Node('E'), 2),
    StreetEdge(Node('E'), Node('D'), 2),
]

expected = [Node('A'), Node('C'), Node('B'), Node('D'), Node('Z')]
expected_cost = 16
start_node = Node('A')
end_node = Node('Z')

_heuristic = {
    Node('A'): 11,
    Node('B'): 8,
    Node('C'): 8,
    Node('D'): 4,
    Node('E'): 2,
    Node('Z'): 0,
}


def heuristic(node):
    return _heuristic[node]
