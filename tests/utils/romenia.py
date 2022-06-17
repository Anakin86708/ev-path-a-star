from ev_path.edges import StreetEdge
from ev_path.nodes import Node

graph_cities = [
    StreetEdge(Node('Arad'), Node('Sibiu'), 140),
    StreetEdge(Node('Sibiu'), Node('Arad'), 140),
    StreetEdge(Node('Arad'), Node('Zerind'), 75),
    StreetEdge(Node('Zerind'), Node('Arad'), 75),
    StreetEdge(Node('Arad'), Node('Timisoara'), 118),
    StreetEdge(Node('Timisoara'), Node('Arad'), 118),
    StreetEdge(Node('Zerind'), Node('Oradea'), 71),
    StreetEdge(Node('Oradea'), Node('Zerind'), 71),
    StreetEdge(Node('Timisoara'), Node('Lugoj'), 111),
    StreetEdge(Node('Lugoj'), Node('Timisoara'), 111),
    StreetEdge(Node('Lugoj'), Node('Mehadia'), 70),
    StreetEdge(Node('Mehadia'), Node('Lugoj'), 70),
    StreetEdge(Node('Mehadia'), Node('Dobreta'), 75),
    StreetEdge(Node('Dobreta'), Node('Mehadia'), 75),
    StreetEdge(Node('Dobreta'), Node('Craiova'), 120),
    StreetEdge(Node('Craiova'), Node('Dobreta'), 120),
    StreetEdge(Node('Oradea'), Node('Sibiu'), 151),
    StreetEdge(Node('Sibiu'), Node('Oradea'), 151),
    StreetEdge(Node('Sibiu'), Node('Fagaras'), 99),
    StreetEdge(Node('Fagaras'), Node('Sibiu'), 99),
    StreetEdge(Node('Sibiu'), Node('Rimnicu Vilcea'), 80),
    StreetEdge(Node('Rimnicu Vilcea'), Node('Sibiu'), 80),
    StreetEdge(Node('Rimnicu Vilcea'), Node('Craiova'), 146),
    StreetEdge(Node('Craiova'), Node('Rimnicu Vilcea'), 146),
    StreetEdge(Node('Rimnicu Vilcea'), Node('Pitesti'), 97),
    StreetEdge(Node('Pitesti'), Node('Rimnicu Vilcea'), 97),
    StreetEdge(Node('Craiova'), Node('Pitesti'), 138),
    StreetEdge(Node('Pitesti'), Node('Craiova'), 138),
    StreetEdge(Node('Fagaras'), Node('Bucharest'), 211),
    StreetEdge(Node('Bucharest'), Node('Fagaras'), 211),
    StreetEdge(Node('Pitesti'), Node('Bucharest'), 101),
    StreetEdge(Node('Bucharest'), Node('Pitesti'), 101),
    StreetEdge(Node('Bucharest'), Node('Giurgiu'), 90),
    StreetEdge(Node('Giurgiu'), Node('Bucharest'), 90),
    StreetEdge(Node('Bucharest'), Node('Urziceni'), 85),
    StreetEdge(Node('Urziceni'), Node('Bucharest'), 85),
    StreetEdge(Node('Urziceni'), Node('Vaslui'), 142),
    StreetEdge(Node('Vaslui'), Node('Urziceni'), 142),
    StreetEdge(Node('Vaslui'), Node('Iasi'), 92),
    StreetEdge(Node('Iasi'), Node('Vaslui'), 92),
    StreetEdge(Node('Iasi'), Node('Neamt'), 87),
    StreetEdge(Node('Neamt'), Node('Iasi'), 87),
    StreetEdge(Node('Urziceni'), Node('Hirsova'), 98),
    StreetEdge(Node('Hirsova'), Node('Urziceni'), 98),
    StreetEdge(Node('Hirsova'), Node('Eforie'), 86),
    StreetEdge(Node('Eforie'), Node('Hirsova'), 86),
]

expected = [
    Node('Arad'),
    Node('Sibiu'),
    Node('Rimnicu Vilcea'),
    Node('Pitesti'),
    Node('Bucharest'),
]
expected_cost = 418

start_city = Node('Arad')
end_city = Node('Bucharest')

_heuristic = {
    Node('Arad'): 366,
    Node('Bucharest'): 0,
    Node('Craiova'): 160,
    Node('Dobreta'): 242,
    Node('Eforie'): 161,
    Node('Fagaras'): 176,
    Node('Giurgiu'): 77,
    Node('Hirsova'): 151,
    Node('Iasi'): 226,
    Node('Lugoj'): 244,
    Node('Mehadia'): 241,
    Node('Neamt'): 234,
    Node('Oradea'): 380,
    Node('Pitesti'): 100,
    Node('Rimnicu Vilcea'): 193,
    Node('Sibiu'): 253,
    Node('Timisoara'): 329,
    Node('Urziceni'): 80,
    Node('Vaslui'): 199,
    Node('Zerind'): 374,
}


def heuristic(node_name) -> float:
    return _heuristic[node_name]
