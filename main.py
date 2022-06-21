import logging

import matplotlib.pyplot as plt

from ev_path.astar import AStar
from ev_path.data import city01
from ev_path.data.city01 import nodes
from ev_path.graph import Graph
from ev_path.heuristics import EuclideanHeuristic, ManhattanHeuristic

logging.basicConfig()

if __name__ == '__main__':
    e = city01.edges_roads
    log_level = 1

    start_node = nodes['Kearny X California']
    end_node = nodes['Jones X Valejo']

    g = Graph(e)
    g.draw()
    plt.savefig('results/graph.svg', format='svg')
    plt.show()
    plt.cla()

    # Adimissível
    heuristic = EuclideanHeuristic(end_node)
    astar_adimissivel = AStar(g, heuristic.heuristic)
    astar_adimissivel.logger.setLevel(log_level)

    cost, final_path, path = astar_adimissivel.path_from_to(start_node, end_node)
    astar_adimissivel.draw_tree(start_node, end_node, path)
    plt.savefig('results/tree_adm.svg', format='svg')
    plt.show()
    plt.cla()

    astar_adimissivel.draw_tree_on_space(start_node, end_node, path)
    plt.savefig('results/path_adm.svg', format='svg')
    plt.show()
    plt.cla()

    print(f'Cost: {cost}')
    print('Final path')
    print(final_path)

    # Não adimissível
    heuristic = ManhattanHeuristic(end_node)
    astar_nao_adimissivel = AStar(g, heuristic.heuristic)
    astar_nao_adimissivel.logger.setLevel(log_level)

    cost, final_path, path = astar_nao_adimissivel.path_from_to(start_node, end_node)
    astar_nao_adimissivel.draw_tree(start_node, end_node, path)
    plt.savefig('results/tree_nao_adm.svg', format='svg')
    plt.show()
    plt.cla()

    astar_nao_adimissivel.draw_tree_on_space(start_node, end_node, path)
    plt.savefig('results/path_nao_adm.svg', format='svg')
    plt.show()
    plt.cla()

    print(f'Cost: {cost}')
    print('Final path')
    print(final_path)
