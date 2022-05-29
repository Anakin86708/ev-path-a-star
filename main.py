import matplotlib.pyplot as plt
import networkx as nx

from ev_path.graph import Graph

if __name__ == '__main__':
    e = [
        # ('a', 'b', 10.0),
        ('a', 'c', 15),
        ('b', 'a', 10),
        ('b', 'e', 8),
        ('b', 'f', 5),
        ('c', 'a', 15),
        ('c', 'd', 20),
        ('c', 'e', 4),
        ('d', 'c', 20),
        ('d', 'e', 6),
        ('e', 'c', 4),
        ('e', 'd', 6),
        ('e', 'b', 10),
        ('e', 'z', 12),
        ('f', 'b', 13),
        ('f', 'z', 15),
        ('z', 'f', 7),
        ('z', 'e', 9),
    ]

    g = Graph(e)
    G = nx.DiGraph(g.matrix_adj)
    nx.draw_networkx(G)
    plt.show()

    print('hello world!')
