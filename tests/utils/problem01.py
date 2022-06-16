edges = [
    ('A', 'B', 5),
    ('B', 'A', 5),
    ('A', 'C', 4),
    ('C', 'A', 4),
    ('B', 'C', 1),
    ('C', 'B', 1),
    ('B', 'D', 5),
    ('D', 'B', 5),
    ('C', 'D', 8),
    ('D', 'C', 8),
    ('C', 'E', 10),
    ('E', 'C', 10),
    ('D', 'Z', 6),
    ('Z', 'D', 6),
    ('E', 'Z', 5),
    ('Z', 'E', 5),
    ('D', 'E', 2),
    ('E', 'D', 2),
]

expected = ['A', 'C', 'B', 'D', 'Z']
expected_cost = 16
start_node = 'A'
end_node = 'Z'

_heuristic = {
    'A': 11,
    'B': 8,
    'C': 8,
    'D': 4,
    'E': 2,
    'Z': 0,
}


def heuristic(node):
    return _heuristic[node]
