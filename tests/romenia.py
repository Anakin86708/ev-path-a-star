graph_cities = [
    ('Arad', 'Sibiu', 140),
    ('Sibiu', 'Arad', 140),
    ('Arad', 'Zerind', 75),
    ('Zerind', 'Arad', 75),
    ('Arad', 'Timisoara', 118),
    ('Timisoara', 'Arad', 118),
    ('Zerind', 'Oradea', 71),
    ('Oradea', 'Zerind', 71),
    ('Timisoara', 'Lugoj', 111),
    ('Lugoj', 'Timisoara', 111),
    ('Lugoj', 'Mehadia', 70),
    ('Mehadia', 'Lugoj', 70),
    ('Mehadia', 'Dobreta', 75),
    ('Dobreta', 'Mehadia', 75),
    ('Dobreta', 'Craiova', 120),
    ('Craiova', 'Dobreta', 120),
    ('Oradea', 'Sibiu', 151),
    ('Sibiu', 'Oradea', 151),
    ('Sibiu', 'Fagaras', 99),
    ('Fagaras', 'Sibiu', 99),
    ('Sibiu', 'Rimnicu Vilcea', 80),
    ('Rimncu Vilcea', 'Sibiu', 80),
    ('Rimnicu Vilcea', 'Craiova', 146),
    ('Craiova', 'Rimnicu Vilcea', 146),
    ('Rimnicu Vilcea', 'Pitesti', 97),
    ('Pitesti', 'Rimnicu Vilcea', 97),
    ('Craiova', 'Pitesti', 138),
    ('Pitesti', 'Craiova', 138),
    ('Fagaras', 'Bucharest', 211),
    ('Bucharest', 'Fagaras', 211),
    ('Pitesti', 'Bucharest', 101),
    ('Bucharest', 'Pitesti', 101),
    ('Bucharest', 'Giurgiu', 90),
    ('Giurgiu', 'Bucharest', 90),
    ('Bucharest', 'Urziceni', 85),
    ('Urziceni', 'Bucharest', 85),
    ('Urziceni', 'Vaslui', 142),
    ('Vaslui', 'Urziceni', 142),
    ('Vaslui', 'Iasi', 92),
    ('Iasi', 'Vaslui', 92),
    ('Iasi', 'Neamt', 87),
    ('Neamt', 'Iasi', 87),
    ('Urziceni', 'Hirsova', 98),
    ('Hirsova', 'Urziceni', 98),
    ('Hirsova', 'Eforie', 86),
    ('Eforie', 'Hirsova', 86),
]

expected = [
    'Arad',
    'Sibiu',
    'Rimnicu Vilcea',
    'Pitesti',
    'Bucharest'
]

start_city = 'Arad'
end_city = 'Bucharest'

_heuristic = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Dobreta': 242,
    'Eforie': 161,
    'Fagaras': 176,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 100,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}


def heuristic(node_name) -> float:
    """
    Give the straight line distance from `node_name` to the end node.

    :param node_name: Current node.
    :return: Heuristic value.
    :rtype`: float
    """
    return _heuristic[node_name]
