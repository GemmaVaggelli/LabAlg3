from Grafo import Graph
from timeit import default_timer as timer
import numpy as np
import matplotlib.pyplot as plt


def test_increasing_probability_and_nodes(prob_increment, max_dimension, dim_increment):
    start = timer()
    dim = 1
    container = [[[], []] for i in range(0, int(100 / prob_increment) + 1)]  # la prima lista sono i tempi,la seconda è il numero di scc 
    # una sottolista per ogni probabilità
    while dim <= max_dimension:
        prob = 0
        while prob <= 100:
            g = Graph(dim)
            g.randomize_graph_with_probability(prob)

            start = timer()
            g.strongly_connected_components()
            end = timer()

            container[int(prob / prob_increment)][0].append(end - start)
            container[int(prob / prob_increment)][1].append(len(g.roots_of_scc))

            prob += prob_increment
        dim += dim_increment

    end = timer()
    print("Tempo totale per creare un grafo e trovare SCC", end - start)

    return container


#GRAFICI
def plot_sccs_and_time(container, prob_increment):
    for i in range(len(container)):  # aumentiamo la probabilità di presenza di archi
        y1 = container[i][1]  # contiene il vettore di quante SCC ci sono per una certa dim
        y2 = container[i][0]  # contiene il tempo per trovare le SCC per ogni dim
        x1 = np.arange(0, len(y1), 1)
        #PLOT1
        plt.xlabel('#  di nodi')
        plt.ylabel('SCC e Tempo')
        plt.grid()
        plt.plot(x1, y1)
        plt.plot(x1, y2)
        plt.title('Numero di SCC per una probabilità di presenza di archi di: {}%  '.format(i * prob_increment))
        plt.legend(['Numero di SCC', 'Tempo per calcolare SCC'])
        plt.savefig('prob{}_scc_and_time.png'.format(i * prob_increment), bbox_inches='tight')
        plt.clf()
        #PLOT2 - ora creo il plot per visualizzare meglio l' evoluzione del tempo all'aumentare della probabilità 
        plt.title('Tempo per trovare SCC per una probabilità di presenza di archi di: {}%  '.format(i * prob_increment))
        plt.xlabel('#  di nodi ')
        plt.ylabel('Tempo')
        plt.grid()
        plt.plot(x1, y2, color='green')
        plt.savefig('prob{}_and_time.png'.format(i * prob_increment), bbox_inches='tight')
        plt.clf()

    ##prob_and_scc_PLOT3##
    plt.xlabel('probabilità')
    plt.ylabel('SCC')

    x = np.arange(0, 101, prob_increment)
    y = []
    for i in range(0, 101, prob_increment):
        y.append(container[int(i/prob_increment)][1][100])


    plt.grid()
    plt.plot(x, y)

    plt.title('Numero di SCC al variare della probabilità ')
    plt.legend(['Numero di SCC', 'Tempo per calcolare SCC'])
    plt.savefig('prob_and_scc.png', bbox_inches='tight')
    plt.clf()

def test_with_avg_and_plot(times, prob_increment, max_dimension, dim_increment):
    start = timer()
    container_avg = [[[], []] for i in range(0, int(100 / prob_increment) + 1)]
    y = []

    for i in range(times):
        # y è composta da containers
        y.append(test_increasing_probability_and_nodes(prob_increment, max_dimension, dim_increment))
        

    for i in range(int(max_dimension / dim_increment)):
        for actual_prob in range(0, 101, prob_increment):
            avg_time = 0
            avg_sccs = 0
            
            for k in range(len(y)):
                avg_time += y[k][int(actual_prob / prob_increment)][0][i]  # tempo
                avg_sccs += y[k][int(actual_prob / prob_increment)][1][i]  # sccs
            avg_time = avg_time / len(y)
            avg_sccs = avg_sccs / len(y)
            container_avg[int(actual_prob / prob_increment)][0].append(avg_time)
            container_avg[int(actual_prob / prob_increment)][1].append(avg_sccs)
    end = timer()
    print("Tempo per calcolare la media: ", end - start)

    plot_sccs_and_time(container_avg, prob_increment)



# pb sta per l'incremento percentuale della probabilità volta per volta
test_with_avg_and_plot(times=5, prob_increment=10, max_dimension=150, dim_increment=1)
