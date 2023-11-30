import numpy as np
from random import randint
from dataclasses import dataclass
from scipy.optimize import linear_sum_assignment
import matplotlib.pyplot as plt
import time

@dataclass
class tc:   #класс точка с координатами time и count
    x: float
    y: float

n = 5
P = np.eye(n)

def generator(n, q, r):    #генерирует матрицу размером n*n, значения от q до r
    P = np.eye(n)
    for i in range (n):
        for j in range (n):
            P[i][j] = randint(q, r)
    return P

def hungarian_algorithm(P, mode):   #mode: 1 - max, 0 - min
    s = 0
    rows, cols = P.shape
    if mode == 1:
        row_ind, col_ind = linear_sum_assignment(P, True) #max
    if mode == 0:
        row_ind, col_ind = linear_sum_assignment(P, False) #min
    for i in range (rows):
        s = s + P[row_ind[i]][col_ind[i]]
    return s

#def greedy_algorithm(P, mode):   #mode: 1 - max, 0 - min
#    s = 0
#    rows, cols = P.shape
#    for i in range(rows):
#        if (mode == 0):
#            j = np.argmin(P[i])
#        if (mode == 1):
#            j = np.argmax(P[i])
#        s = s + P[i][j]
#        P = np.delete(P, j, 1)    #1 - столбец, 0 - строка
#    return s

def greedy_algorithm(P, mode):   #mode: 1 - max, 0 - min
    s = 0
    rows, cols = P.shape
    used = [0] * cols
    for i in range(rows):
        max_val = -1000000
        min_val = 1000000
        pos = -1
        if mode == 0:
            for j in range (cols):
                if used[j] == 0:
                    min_val = min(min_val, P[i][j])
                    if min_val == P[i][j]:
                        pos = j
            used[pos] = 1
        if mode == 1:
            for j in range (cols):
                if used[j] == 0:
                    max_val = max(max_val, P[i][j])
                    if max_val == P[i][j]:
                        pos = j
            used[pos] = 1
        s = s + P[i][pos]
    return s
        
def tester(n, s, q, r, alg):    #замеряет время работы алгоритмов на матрице размера от 2 до n с шагом s. значения элементов от q до r
    res = []
    if alg == 1:
        print('Hungarian algorithm MAX')
    if alg == 2:
        print('Hungarian algorithm MIN')
    if alg == 3:
        print('Greedy algorithm MAX')
    if alg == 4:
        print('Greedy algorithm MIN')
    for i in range(2, n + 1, s):
        P = generator(i, q, r)
        if alg == 1:
            start_time = time.time()
            cnt = hungarian_algorithm(P, 1) #max
            end_time = time.time()
        if alg == 2:
            start_time = time.time()
            cnt = hungarian_algorithm(P, 0) #min
            end_time = time.time()
        if alg == 3:
            start_time = time.time()
            cnt = greedy_algorithm(P, 1) #max
            end_time = time.time()
        if alg == 4:
            start_time = time.time()
            cnt = greedy_algorithm(P, 0) #min
            end_time = time.time()
        
        elapsed_time = round(end_time - start_time, 6)
        print(i, end=' ')
        print(elapsed_time)
        res.append(tc(i, elapsed_time))
    
    print('\n')
    return res
        
def draw_tc_points(a, color):
    x2 = []
    y2 = []
    for p in a:
        x2.append(p.x)
        y2.append(p.y)
    plt.plot(x2, y2, 'o-' + str(color), alpha = 0.5)

    plt.grid(True)



draw_tc_points(tester(1000, 100, 0, 100, 1), 'r')
draw_tc_points(tester(1000, 100, 0, 100, 2), 'g')
draw_tc_points(tester(1000, 100, 0, 100, 3), 'b')
draw_tc_points(tester(1000, 100, 0, 100, 4), 'y')

plt.xlabel("Размер матрицы")
plt.ylabel("Время работы, с")
plt.text(0, 0.15, s = "Hungarian algorithm MAX", color = 'r')
plt.text(0, 0.125, s = "Hungarian algorithm MIN", color = 'g')
plt.text(0, 0.1, s = "Greedy algorithm MAX", color = 'b')
plt.text(0, 0.075, s = "Greedy algorithm MIN", color = 'y')



#P = np.array([[2, 4, 1, 3, 3], [1, 5, 4, 1, 2], [3, 5, 2, 2, 4], [1, 4, 3, 1, 4], [3, 2, 5, 3, 5]])
#d = greedy_algorithm(P, 1)
#print(d, "\n")
#print(P, "\n")
#row_ind, col_ind = linear_sum_assignment(P, True) #max
#print(row_ind, "\n")
#print(col_ind, "\n")
#s = 0
#for i in range (n):
#    s = s + P[row_ind[i]][col_ind[i]]
#print(s)

#row_ind, col_ind = linear_sum_assignment(P, False) #min
#print(row_ind, "\n")
#print(col_ind, "\n")
#s = 0
#for i in range (n):
#    s = s + P[row_ind[i]][col_ind[i]]
#print(s)