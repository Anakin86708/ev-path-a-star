import logging

import matplotlib.pyplot as plt
import networkx as nx

from ev_path.astar import AStar
from ev_path.data import city01
from ev_path.data.city01 import nodes
from ev_path.graph import Graph
from ev_path.heuristics import EuclideanHeuristic, ManhattanHeuristic

logging.basicConfig()

if __name__ == '__main__':
    e = city01.edges_roads
    log_level = 1

    g = Graph(e)
    start_node = nodes['Kearny X California']
    end_node = nodes['Jones X Valejo']
    heuristic = EuclideanHeuristic(end_node)
    astar_adimissivel = AStar(g, heuristic.heuristic)
    astar_adimissivel.logger.setLevel(log_level)

    cost, final_path, path = astar_adimissivel.path_from_to(start_node, end_node)
    astar_adimissivel.draw_tree(start_node, end_node, path)
    plt.savefig('results/tree_adm.svg', format='svg')
    plt.show()
    plt.cla()

    astar_adimissivel.draw_path(start_node, end_node, path)
    plt.savefig('results/path_adm.svg', format='svg')
    plt.show()
    plt.cla()

    print(f'Cost: {cost}')
    print('Final path')
    print(final_path)

    G_adimissivel = nx.DiGraph(g.matrix_adj)
    pos = {}
    height = []
    for node in G_adimissivel.nodes:
        node_g = g.get_nodes_by_name(node).pop()
        pos[node] = (node_g.x, node_g.y)
        height.append(node_g.height)
    nx.draw_networkx(G_adimissivel, pos=pos, with_labels=False, node_size=height)
    plt.savefig('results/graph_adm.svg', format='svg')
    plt.show()
    plt.cla()

    # Não adimissível
    heuristic = ManhattanHeuristic(end_node)
    astar_nao_adimissivel = AStar(g, heuristic.heuristic)
    astar_nao_adimissivel.logger.setLevel(log_level)

    cost, final_path, path = astar_nao_adimissivel.path_from_to(start_node, end_node)
    astar_nao_adimissivel.draw_tree(start_node, end_node, path)
    plt.savefig('results/tree_nao_adm.svg', format='svg')
    plt.show()
    plt.cla()

    astar_nao_adimissivel.draw_path(start_node, end_node, path)
    plt.savefig('results/path_nao_adm.svg', format='svg')
    plt.show()
    plt.cla()

    print(f'Cost: {cost}')
    print('Final path')
    print(final_path)

    G_adimissivel = nx.DiGraph(g.matrix_adj)
    pos = {}
    height = []
    for node in G_adimissivel.nodes:
        node_g = g.get_nodes_by_name(node).pop()
        pos[node] = (node_g.x, node_g.y)
        height.append(node_g.height)
    nx.draw_networkx(G_adimissivel, pos=pos, with_labels=False, node_size=height)
    plt.savefig('results/graph_nao_adm.svg', format='svg')
    plt.show()
