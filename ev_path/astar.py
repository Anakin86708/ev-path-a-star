from copy import deepcopy
from queue import PriorityQueue
from typing import List, Dict

from ev_path.graph import Graph


class AStar:

    def __init__(self, graph: Graph, heuristic_func):
        self._graph = deepcopy(graph)
        self.heuristic_func = heuristic_func

    @property
    def graph(self):
        """
        :return: Returns a graph's copy.
        """
        return deepcopy(self._graph)

    def path_from_to(self, start_node: str, end_node: str) -> List[str]:
        self.are_nodes_present_on_graph(start_node, end_node)

        distances = {(start_node, end_node): 0}
        came_from = {}
        opened = PriorityQueue()
        opened.put((0, start_node, None))
        closed = set()

        graph_matrix_adj = self.graph.matrix_adj
        while opened.qsize() > 0:
            _, current_node, previous = opened.get()  # acts like pop()
            came_from[current_node] = previous
            closed.add(current_node)

            if current_node == end_node:
                break

            possible_nodes = set(graph_matrix_adj.index[graph_matrix_adj.loc[current_node] != 0]).difference(
                set(closed))
            
            for connected_node in possible_nodes:
                cost_node = self.avaliation_function(start_node, current_node, connected_node, came_from)
                opened.put((cost_node, connected_node, current_node))
        return self.recreate_path_to_start(start_node, end_node, came_from)

    def avaliation_function(self, start_node, current_node, connected_node, path):
        return self.heuristic_func(current_node, connected_node) + self.real_cost(start_node, current_node, path)

    def real_cost(self, start_node, current_node, path):
        path_to_start = self.recreate_path_to_start(start_node, current_node, path)
        return sum([self.graph.weights[(n1, n2)] for n1, n2 in zip(path_to_start, path_to_start[1:])])

    @staticmethod
    def recreate_path_to_start(start_node, current_node, path: Dict) -> List[str]:
        """

        :param start_node: Graph's starter node.
        :param current_node: Graph's current node.
        :param path: Maps the actual previous and the actual node. #HELP ARIEL
        :return: Returns a List containing the path. #HELP ARIEL
        """
        path_list = [current_node]
        node = current_node
        while node != start_node:
            node = path[node]
            path_list.append(node)
        path_list.reverse()
        return path_list

    def are_nodes_present_on_graph(self, start_node, end_node) -> bool:
        """

        :param start_node: Graph's starter node.
        :param end_node: Graph's goal node.
        :return: Returns an exception if the node is not in the graph or a True value if it is.
        :rtype: Boolean
        :raise:
            ValueError: explicacao
        """
        if start_node not in self.graph.nodes or end_node not in self.graph.nodes:
            raise ValueError(f"Node {start_node if start_node not in self.graph.nodes else end_node} not in graph")
        return True

