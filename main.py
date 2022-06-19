import logging

import matplotlib.pyplot as plt
import networkx as nx

from ev_path.astar import AStar
from ev_path.data import city01
from ev_path.data.city01 import nodes
from ev_path.graph import Graph
from ev_path.heuristics import EuclideanHeuristic

logging.basicConfig()

if __name__ == '__main__':
    e = city01.edges_roads

    g = Graph(e)
    start_node = nodes['Leavenworth X California']
    end_node = nodes['Jones X Valejo']
    heuristic = EuclideanHeuristic(end_node)
    astar = AStar(g, heuristic.heuristic)
    astar.logger.setLevel(logging.INFO)

    cost, path = astar.path_from_to(start_node, end_node)

    print(path)

    G = nx.DiGraph(g.matrix_adj)
    nx.draw_networkx(G)
    plt.show()
