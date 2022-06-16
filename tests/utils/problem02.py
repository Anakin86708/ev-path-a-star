graph_edges = [
    ('a', 'b', 6),
    ('b', 'a', 6),
    ('a', 'f', 3),
    ('f', 'a', 3),
    ('b', 'c', 3),
    ('c', 'b', 3),
    ('c', 'd', 2),
    ('d', 'c', 2),
    ('d', 'e', 1),
    ('e', 'd', 1),
    ('c', 'e', 5),
    ('e', 'c', 5),
    ('d', 'e', 8),
    ('e', 'd', 8),
    ('e', 'j', 5),
    ('j', 'e', 5),
    ('e', 'i', 5),
    ('i', 'e', 5),
    ('f', 'g', 1),
    ('g', 'f', 1),
    ('f', 'h', 7),
    ('h', 'f', 7),
    ('g', 'i', 3),
    ('i', 'g', 3),
    ('i', 'h', 2),
    ('h', 'i', 2),
    ('i', 'j', 3),
    ('j', 'i', 3),
]

expected = ['a', 'f', 'g', 'i', 'j']
expected_cost = 10
start_node = 'a'
end_node = 'j'

_heuristic = {
    'a': 10,
    'b': 8,
    'c': 5,
    'd': 7,
    'e': 3,
    'f': 6,
    'g': 5,
    'h': 3,
    'i': 1,
    'j': 0,
}


def heuristic(node):
    return _heuristic[node]
