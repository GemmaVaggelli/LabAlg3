from random import randint
from Nodi import Node
from SortingAlg import merge_sort


class Graph:
    def __init__(self, number_of_nodes):
        self.number_of_nodes = number_of_nodes
        self.nodes = []
        self.roots_of_scc = []
        self.permutation = []
        self.reversed_order = []
        self.time = None
        for i in range(0, number_of_nodes):
            self.nodes.append(Node(i))

    def add_branch(self, src, dest, weight):
        self.nodes[src].adj.append([dest, weight])

    def print_graph(self):
        for u in range(0, self.number_of_nodes):
            print(self.nodes[u].name, ": ", self.nodes[u].adj)

    def randomize_graph_with_probability(self, probability):
        if 0 < probability <= 100:
            for u in range(0, self.number_of_nodes):
                for j in range(0, self.number_of_nodes):
                    random = randint(1, 100)
                    if random < probability:
                        self.add_branch(u, j, randint(1, 10))

    def normal_adj_list(self):
        list = []
        for i in range(self.number_of_nodes):
            list.append([])
            for j in range(len(self.nodes[i].adj)):
                list[i].append(self.nodes[i].adj[j])
        return list

    def dfs(self, print_roots_of_dff=False):
        for i in range(len(self.nodes)):
            self.nodes[i].color = 'white'
            self.nodes[i].pi = None
        self.time = 0

        for u in self.nodes:
            if u.color == 'white':
                self.dfs_visit(u, print_roots_of_dff)
                if print_roots_of_dff:
                    self.roots_of_scc.append(u.name)

    def dfs_visit(self, u, print_roots_of_dff):  # il nodo u
        self.time += 1
        u.d = self.time
        u.color = 'gray'
        for i in range(len(u.adj)):
            if print_roots_of_dff:
                node_name = u.adj[i][0]
                correct_position = self.permutation[node_name]
            else:
                correct_position = u.adj[i][0]

            v = self.nodes[correct_position]
            if v.color == 'white':
                v.pi = u.name
                # print("dal nodo", u.name, "sto aprendo il nodo : ", v.name)
                self.dfs_visit(v, print_roots_of_dff)

        u.color = 'black'
        self.time += 1
        u.f = self.time
        if not print_roots_of_dff:
            self.reversed_order.insert(0, u)
        

    def trasposta(self):
        reversed_adj_list = [[] for i in range(self.number_of_nodes)]
        for u in self.nodes:
            for v in u.adj:
                reversed_adj_list[v[0]].append([u.name, v[1]])
        for i in range(self.number_of_nodes):
            self.nodes[i].adj = reversed_adj_list[i]

    ##calcola la permutazione dopo il mergesort
    def calculate_permutation(self):
        for i in range(self.number_of_nodes):
            self.permutation.append(-1)
        for i in range(self.number_of_nodes):
            self.permutation[self.nodes[i].name] = i

    def strongly_connected_components(self):
        self.dfs()
        self.trasposta()
        self.nodes = self.reversed_order
        self.calculate_permutation()
        self.dfs(print_roots_of_dff=True)
