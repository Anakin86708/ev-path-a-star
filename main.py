import matplotlib.pyplot as plt
import networkx as nx
from data import city01

from ev_path.graph import Graph

if __name__ == '__main__':
    e = city01.edges_roads

    g = Graph(e)
    G = nx.DiGraph(g.matrix_adj)
    nx.draw_networkx(G)
    plt.show()

    print('hello world!')
