# https://www.gatevidyalay.com/a-algorithm-a-algorithm-example-in-ai/
from ev_path.edges import StreetEdge
from ev_path.nodes import Node

graph_edges = [
    StreetEdge(Node('a'), Node('b'), 6),
    StreetEdge(Node('b'), Node('a'), 6),
    StreetEdge(Node('a'), Node('f'), 3),
    StreetEdge(Node('f'), Node('a'), 3),
    StreetEdge(Node('b'), Node('c'), 3),
    StreetEdge(Node('c'), Node('b'), 3),
    StreetEdge(Node('c'), Node('d'), 2),
    StreetEdge(Node('d'), Node('c'), 2),
    StreetEdge(Node('d'), Node('e'), 1),
    StreetEdge(Node('e'), Node('d'), 1),
    StreetEdge(Node('c'), Node('e'), 5),
    StreetEdge(Node('e'), Node('c'), 5),
    StreetEdge(Node('d'), Node('e'), 8),
    StreetEdge(Node('e'), Node('d'), 8),
    StreetEdge(Node('e'), Node('j'), 5),
    StreetEdge(Node('j'), Node('e'), 5),
    StreetEdge(Node('e'), Node('i'), 5),
    StreetEdge(Node('i'), Node('e'), 5),
    StreetEdge(Node('f'), Node('g'), 1),
    StreetEdge(Node('g'), Node('f'), 1),
    StreetEdge(Node('f'), Node('h'), 7),
    StreetEdge(Node('h'), Node('f'), 7),
    StreetEdge(Node('g'), Node('i'), 3),
    StreetEdge(Node('i'), Node('g'), 3),
    StreetEdge(Node('i'), Node('h'), 2),
    StreetEdge(Node('h'), Node('i'), 2),
    StreetEdge(Node('i'), Node('j'), 3),
    StreetEdge(Node('j'), Node('i'), 3),
]

expected = [Node('a'), Node('f'), Node('g'), Node('i'), Node('j')]
expected_cost = 10
start_node = Node('a')
end_node = Node('j')

_heuristic = {
    Node('a'): 10,
    Node('b'): 8,
    Node('c'): 5,
    Node('d'): 7,
    Node('e'): 3,
    Node('f'): 6,
    Node('g'): 5,
    Node('h'): 3,
    Node('i'): 1,
    Node('j'): 0,
}


def heuristic(node):
    return _heuristic[node]
