from Grafo import Graph
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

g = Graph(5)
g.randomize_graph_with_probability(100)
g.print_graph()

def list_to_matrix(adj_list):
    n = len(adj_list)
    adj_matrix = np.zeros((n, n))
    np.fill_diagonal(adj_matrix, 0)

    for i in range(n):
        for j, w in adj_list[i]:
            adj_matrix[i, j] = w
    return adj_matrix


admat_of_g = list_to_matrix(g.normal_adj_list())


admatrix = nx.from_numpy_matrix(admat_of_g, create_using=nx.DiGraph)

layout = nx.spring_layout(admatrix)
nx.draw(admatrix, pos=layout, with_labels=True)
nx.draw_networkx_edge_labels(admatrix, pos=layout, edge_labels=nx.get_edge_attributes(admatrix, "peso"))
plt.savefig("Grafo.png")
plt.clf()

g.strongly_connected_components()
print(g.roots_of_scc)


