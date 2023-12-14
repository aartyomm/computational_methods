import matplotlib.pyplot as plt
import numpy as np
from algorithms import Algorithm


def show_graph(algorithms: list[Algorithm]):
    fig, ax = plt.subplots()
    n = len(algorithms[0].ans)
    x = np.array([i for i in range(1, n + 1)])
    for algorithm in algorithms:
        y = np.array(algorithm.ans)
        ax.plot(x, y, label=algorithm.name)
    ax.set_xlabel('Время')
    ax.set_ylabel('S')
    ax.legend(prop={'size': 9}, loc='lower right')
    plt.show()




