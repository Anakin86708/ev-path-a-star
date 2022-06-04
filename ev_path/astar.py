from copy import deepcopy
from typing import List, Dict

from ev_path.graph import Graph


class AStar:

    def __init__(self, graph: Graph, heuristic_func):
        self._graph = deepcopy(graph)
        self.heuristic_func = heuristic_func

    @property
    def graph(self):
        return deepcopy(self._graph)

    def path_from_to(self, start_node: str, end_node: str) -> List[str]:
        self.are_nodes_present_on_graph(start_node, end_node)

        path: Dict[str, str] = {start_node: ''}
        open_nodes: List[str] = [start_node]
        closed_nodes: List[str] = []
        cost_to_node: Dict[str, float] = {start_node: 0}

        graph_matrix_adj = self.graph.matrix_adj

        while open_nodes:
            current_node = open_nodes.pop()
            avaliation_nodes = {}

            possible_nodes = list(graph_matrix_adj.index[graph_matrix_adj.loc[current_node] != 0])
            for node in possible_nodes:
                avaliation_nodes[node] = self.heuristic_func(current_node, node) + \
                                         self.graph._weights[(current_node, node)]

    def are_nodes_present_on_graph(self, start_node, end_node):
        if start_node not in self.graph.nodes or end_node not in self.graph.nodes:
            raise ValueError(f"Node {start_node if start_node not in self.graph.nodes else end_node} not in graph")
        return True
