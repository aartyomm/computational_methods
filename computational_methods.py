import numpy as np
from random import randint
from scipy.optimize import linear_sum_assignment
import matplotlib.pyplot as plt
from hungarian_algorithm import hungarian_algorithm_max, hungarian_algorithm_min

n = 5
P = np.eye(n)

def generator(n):    #генерирует матрицу размером n*n, значения от 0 до 1 (не включая границы)
    P = np.eye(n)
    for i in range (n):
        P[i][0] = randint(1, 9999) / 10000
        for j in range (1, n):
            b = randint(1, 99) / 100
            P[i][j] = P[i][j - 1] * b
    return P

def hungarian_algorithm_py(P, mode):   #mode: 1 - max, 0 - min
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
    used = [0] * rows
    for i in range(cols):
        max_val = -1000000
        min_val = 1000000
        pos = -1
        if mode == 0:
            for j in range (rows):
                if used[j] == 0:
                    min_val = min(min_val, P[j][i])
                    if min_val == P[j][i]:
                        pos = j
            used[pos] = 1
        if mode == 1:
            for j in range (rows):
                if used[j] == 0:
                    max_val = max(max_val, P[j][i])
                    if max_val == P[j][i]:
                        pos = j
            used[pos] = 1
        s = s + P[pos][i]
    return s

def greedy_thrifty_algorithm(P, theta):
    s = 0
    rows, cols = P.shape
    used = [0] * rows
    for i in range(theta):
        max_val = -1000000
        pos = -1
        for j in range (rows):
            if used[j] == 0:
                max_val = max(max_val, P[j][i])
                if max_val == P[j][i]:
                    pos = j
        used[pos] = 1
        s = s + P[pos][i]
    for i in range(theta + 1, cols):
        min_val = 1000000
        pos = -1
        for j in range (rows):
            if used[j] == 0:
                min_val = min(min_val, P[j][i])
                if min_val == P[j][i]:
                    pos = j
        used[pos] = 1
        s = s + P[pos][i]
    return s

def thrifty_greedy_algorithm(P, theta):
    s = 0
    rows, cols = P.shape
    used = [0] * rows
    for i in range(theta):
        min_val = 1000000
        pos = -1
        for j in range (rows):
            if used[j] == 0:
                min_val = min(min_val, P[j][i])
                if min_val == P[j][i]:
                    pos = j
        used[pos] = 1
        s = s + P[pos][i]
    for i in range(theta + 1, cols):
        max_val = -1000000
        pos = -1
        for j in range (rows):
            if used[j] == 0:
                max_val = max(max_val, P[j][i])
                if max_val == P[j][i]:
                    pos = j
        used[pos] = 1
        s = s + P[pos][i]
    return s

def tester(n, rep):    #замеряет время работы алгоритмов на матрице размера от 2 до n с шагом s.
    res_hap_min = []
    res_hap_max = []
    res_ha_min = []
    res_ha_max = []
    res_g_min = []
    res_g_max = []
    res_gt = []
    res_tg = []
    x = []
    M = generator(n)
    for i in range(2, n + 1):
        P = M[0:i, 0:i]    #на каждом из n шагов считаем rep (50) раз на матрице размером i*i, полученной из исходной матрицы размером n*n
        for j in range (rep):
            hap_min = []
            hap_max = []
            ha_min = []
            ha_max = []
            g_min = []
            g_max = []
            gt = []
            tg = []

            cnt = hungarian_algorithm_py(P, 1) #max
            hap_max.append(cnt)

            cnt = hungarian_algorithm_py(P, 0) #min
            hap_min.append(cnt)

            cnt = greedy_algorithm(P, 1) #max
            g_max.append(cnt)

            cnt = greedy_algorithm(P, 0) #min
            g_min.append(cnt)
            
            cnt = hungarian_algorithm_max(P, i, i) #max
            ha_max.append(cnt)

            cnt = hungarian_algorithm_min(P, i, i) #min
            ha_min.append(cnt)
            
            cnt = greedy_thrifty_algorithm(P, int(i/2))
            gt.append(cnt)

            cnt = thrifty_greedy_algorithm(P, int(i/2))
            tg.append(cnt)
            
        res_hap_min.append(sum(hap_min)/len(hap_min))
        res_hap_max.append(sum(hap_max)/len(hap_max))
        res_ha_min.append(sum(ha_min)/len(ha_min))
        res_ha_max.append(sum(ha_max)/len(ha_max))
        res_g_min.append(sum(g_min)/len(g_min))
        res_g_max.append(sum(g_max)/len(g_max))
        res_gt.append(sum(gt)/len(gt))
        res_tg.append(sum(tg)/len(tg))
        x.append(i)
    
    plt.plot(x, res_hap_min, color='b', alpha = 0.5, ls='-.')
    plt.plot(x, res_hap_max, color='g', alpha = 0.5)
    plt.plot(x, res_ha_min, color='r', alpha = 0.5, ls='-.')
    plt.plot(x, res_ha_max, color='c', alpha = 0.5)
    plt.plot(x, res_g_min, color='m', alpha = 0.5, ls='-.')
    plt.plot(x, res_g_max, color='y', alpha = 0.5)
    plt.plot(x, res_gt, color='k', alpha = 0.5, ls=':')
    plt.plot(x, res_tg, color='maroon', alpha = 0.5, ls=':')
    plt.legend(["венгерский мин python", "венгерский макс python", "венгерский мин",
                "венгерский макс", "бережливый", "жадный", "жадно-бережливый",
                "бережливо-жадный"], prop={'size': 9}, loc="center right")
    
    plt.grid(True)
    plt.xlabel("Время")
    plt.ylabel("S")
        
    
        
def draw_tc_points(a, color):
    x2 = []
    y2 = []
    for p in a:
        x2.append(p.x)
        y2.append(p.y)
    plt.plot(x2, y2, 'o-' + str(color), alpha = 0.5)

    plt.grid(True)


tester(20, 50)

#draw_tc_points(tester(1000, 100, 0, 100, 1), 'r')
#draw_tc_points(tester(1000, 100, 0, 100, 2), 'g')
#draw_tc_points(tester(1000, 100, 0, 100, 3), 'b')
#draw_tc_points(tester(1000, 100, 0, 100, 4), 'y')

#plt.xlabel("Размер матрицы")
#plt.ylabel("Время работы, с")
#plt.text(0, 0.15, s = "Hungarian algorithm MAX", color = 'r')
#plt.text(0, 0.125, s = "Hungarian algorithm MIN", color = 'g')
#plt.text(0, 0.1, s = "Greedy algorithm MAX", color = 'b')
#plt.text(0, 0.075, s = "Greedy algorithm MIN", color = 'y')



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