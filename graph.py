import matplotlib.pyplot as plt
import numpy as np
from algorithms import Algorithm


def show_graph(algorithms: list[Algorithm]):
    n = len(algorithms[0].ans)
    x = np.array([i for i in range(1, n + 1)])

    for algorithm in algorithms:
        y = np.array(algorithm.ans)
        plt.plot(x, y, label=algorithm.name)
    plt.xlabel('Время')
    plt.ylabel('S')
    plt.legend(prop={'size': 9}, loc='lower right')
    plt.show()



