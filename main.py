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
    start_node = nodes['Kearny X California']
    end_node = nodes['Jones X Valejo']
    heuristic = EuclideanHeuristic(end_node)
    astar = AStar(g, heuristic.heuristic)
    astar.logger.setLevel(logging.INFO)

    cost, final_path, path = astar.path_from_to(start_node, end_node)
    astar.draw_tree(start_node, end_node, path)
    plt.savefig('tree.svg', format='svg')
    plt.show()
    plt.cla()

    astar.draw_path(start_node, end_node, path)
    plt.savefig('path.svg', format='svg')
    plt.show()
    plt.cla()

    print(final_path)

    G = nx.DiGraph(g.matrix_adj)
    pos = {}
    height = []
    for node in G.nodes:
        node_g = g.get_nodes_by_name(node).pop()
        pos[node] = (node_g.x, node_g.y)
        height.append(node_g.height)
    nx.draw_networkx(G, pos=pos, with_labels=False, node_size=height)
    plt.savefig('graph.svg', format='svg')
    plt.show()
