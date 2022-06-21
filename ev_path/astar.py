import logging
from copy import deepcopy
from functools import reduce
from operator import itemgetter
from queue import PriorityQueue
from typing import List, Dict, Set

import networkx as nx
import numpy as np
import pandas as pd
from networkx.drawing.nx_pydot import graphviz_layout

from ev_path.graph import Graph
from ev_path.nodes import NodeABC


class AStar:

    def __init__(self, graph: Graph, heuristic_func):
        self._graph = deepcopy(graph)
        self.heuristic_func = heuristic_func
        self.logger = logging.getLogger(__name__)

    @property
    def graph(self):
        """
        :return: Returns a graph's copy.
        """
        return deepcopy(self._graph)

    def path_from_to(self, start_node: NodeABC, end_node: NodeABC) -> tuple[
        float | int, list[NodeABC], Dict[NodeABC, NodeABC]]:
        self.are_nodes_present_on_graph(start_node, end_node)

        came_from = {}
        opened = PriorityQueue()
        opened.put((0, start_node, None))
        closed = set()

        while opened.qsize() > 0:
            _, current_node, previous = opened.get()  # acts like pop()
            came_from[current_node] = previous
            closed.add(current_node)

            min_opened_cost = opened.queue[0][0] if opened.qsize() > 0 else float('inf')
            cost_current_node = self.avaliation_function(start_node, previous, current_node, came_from)
            self.logger.debug(f"Minimum cost: {min_opened_cost}")
            self.logger.debug(f"Cost current node: {cost_current_node}")

            # Path found
            if current_node == end_node and cost_current_node < min_opened_cost:
                cost = self.real_cost(start_node, end_node, came_from)
                path_found = self.recreate_path_to_start(start_node, end_node, came_from)
                self.logger.info(f"Path found: {path_found}")
                self.logger.info(f"Real cost: {cost}")
                return cost, path_found, came_from

            # Nodes that can be reached from current_node
            possible_nodes = self._get_neighbours_from_current_node(closed, current_node)

            for connected_node in possible_nodes:
                cost_connected_node = self.avaliation_function(start_node, current_node, connected_node, came_from)

                if self._node_already_in_opened(connected_node, opened):
                    for queue_node in filter(lambda x: x[1] == connected_node, opened.queue):
                        cost_on_queue_node = queue_node[0]
                        if cost_on_queue_node >= cost_connected_node:
                            opened.queue.remove(queue_node)
                            opened.put((cost_connected_node, connected_node, current_node))

                else:
                    opened.put((cost_connected_node, connected_node, current_node))

            self.logger.info(f"Current node: {current_node}")
            self.logger.info(f"Previous node: {previous}")
            self.logger.info(f"Complete path: {self.recreate_path_to_start(start_node, current_node, came_from)}")
            self.logger.info(f"Opened nodes: {opened.queue}")
            self.logger.info(f"Closed nodes: {closed}")
            self.logger.info("##########\n")

    def draw_tree(self, start_node: NodeABC, end_node: NodeABC, path: Dict[NodeABC, NodeABC]):
        """
        Draws the tree of the A* algorithm.
        """
        names = {x.name for x in (path.keys() | path.values()) if x is not None}
        adj_matrix = pd.DataFrame(np.zeros((len(names), len(names))),
                                  columns=names,
                                  index=names)
        for k, v in path.items():
            if v is None:
                continue
            root = v
            child = list(filter(lambda x: x == k, path.keys()))
            if child:
                for c in child:
                    adj_matrix.loc[root.name, c.name] = 1
        tree = nx.DiGraph(adj_matrix)
        pos = graphviz_layout(tree, prog='dot')
        nx.draw(tree, pos, with_labels=True)

    def _get_neighbours_from_current_node(self, closed: Set, current_node: NodeABC) -> Set[NodeABC]:
        """
        Get all the nodes that can be reached from current_node and that are not on the closed list.

        :param closed: Represents the nodes that already have been opened.
        :param current_node: Current node.
        :return: Set with nodes that can be reached and have not been opened.
        """
        graph_matrix_adj = self.graph.matrix_adj
        connected_nodes = graph_matrix_adj.index[graph_matrix_adj.loc[current_node.name] != 0]
        return reduce(set.union, map(self.graph.get_nodes_by_name, connected_nodes)).difference(closed)

    def avaliation_function(self, start_node, current_node, connected_node, path):
        path = deepcopy(path)
        path[connected_node] = current_node  # Used to connect to the analized node
        return self.heuristic_func(connected_node) + self.real_cost(start_node, connected_node, path)

    def real_cost(self, start_node, current_node, path):
        path_to_start = self.recreate_path_to_start(start_node, current_node, path)
        return sum([self.graph.get_weight_between(n1, n2) for n1, n2 in
                    zip(path_to_start, path_to_start[1:])])

    @staticmethod
    def recreate_path_to_start(start_node: NodeABC, current_node: NodeABC, path: Dict) -> List[NodeABC]:
        """

        :param start_node: Graph's starter node.
        :param current_node: Graph's current node.
        :param path: Maps the actual previous and the actual node.
        :return: Returns a List containing the path.
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
            raise ValueError(f"Node \"{start_node if start_node not in self.graph.nodes else end_node}\" not in graph")
        return True

    @staticmethod
    def _node_already_in_opened(connected_node, opened: PriorityQueue):
        queue = list(map(itemgetter(1), opened.queue))
        return connected_node in queue
