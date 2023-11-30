import numpy as np
import math
import copy

def hungarian_algorithm_min(a, n, m):

    b = copy.deepcopy(a)
    b_1 = np.insert(b, 0, 0, axis=0)
    c = np.insert(b_1, 0, 0, axis=1)

    u = np.array([0] * (n+1))
    v = np.array([0] * (m+1))
    p = np.array([0] * (m+1))
    way = np.array([0] * (m+1))

    for i in range(1, n+1):
        p[0] = i
        j0 = 0

        minv = np.array([math.inf] * (m+1))
        used = np.array([False] * (m+1))

        while p[j0] != 0:
            used[j0] = True
            i0 = p[j0]
            delta = math.inf
            for j in range(1, m+1):
                if not used[j]:
                    cur = c[i0][j] - u[i0] - v[j]
                    if cur < minv[j]:
                        minv[j] = cur
                        way[j] = j0
                    if minv[j] < delta:
                        delta = minv[j]
                        j1 = j

            for j in range(0, m+1):
                if used[j]:
                    u[p[j]] += delta
                    v[j] -= delta
                else:
                    minv[j] -= delta

            j0 = j1

        while j0:
            j1 = way[j0]
            p[j0] = p[j1]
            j0 = j1


    ans = np.array([0] * (n+1))
    for j in range(1, m+1):
        ans[p[j]] = j

    res = 0
    for i in range(1, n + 1):
        res += c[i][ans[i]]
        #print(ans[i])
    return res

def hungarian_algorithm_max(a, n, m):

    b = copy.deepcopy(a)
    b_1 = np.insert(b, 0, 0, axis=0)
    c = np.insert(b_1, 0, 0, axis=1)
    d = copy.deepcopy(c)

    max_row = np.array([0.] * (m + 1))

    for i in range(1, n+1):
        max_row[i] = c[i][0]
        for j in range(1, m+1):
            max_row[i] = max(max_row[i], c[i][j])
            c[i][j] *= -1

    for i in range(1, n+1):
        for j in range(1, m+1):
            c[i][j] += max_row[i]

    u = np.array([0.] * (n + 1))
    v = np.array([0.] * (m + 1))
    p = np.array([0] * (m + 1))
    way = np.array([0] * (m + 1))

    for i in range(1, n + 1):
        p[0] = i
        j0 = 0

        minv = np.array([math.inf] * (m + 1))
        used = np.array([False] * (m + 1))

        while p[j0] != 0:
            used[j0] = True
            i0 = p[j0]
            delta = math.inf
            for j in range(1, m + 1):
                if not used[j]:
                    cur = c[i0][j] - u[i0] - v[j]
                    if cur < minv[j]:
                        minv[j] = cur
                        way[j] = j0
                    if minv[j] < delta:
                        delta = minv[j]
                        j1 = j

            for j in range(0, m + 1):
                if used[j]:
                    u[p[j]] += delta
                    v[j] -= delta
                else:
                    minv[j] -= delta

            j0 = j1

        while j0:
            j1 = way[j0]
            p[j0] = p[j1]
            j0 = j1

    ans = np.array([0] * (n + 1))
    for j in range(1, m + 1):
        ans[p[j]] = j

    res = 0
    for i in range(1, n + 1):
        res += d[i][ans[i]]
        #print(ans[i])
    return res




# if __name__ == '__main__':
#     n = 4
#     a = [[4, 2, 2/3, 1/6], [15, 7.5, 2.5, 5/8], [6, 3, 1, 1/4], [12, 6, 2, 0.5]]
#     #a = np.array([[7, 6, 5.1, 4], [6, 5.1, 4, 2], [5, 4, 2, 1], [4, 2, 1, 0.5]])
#     #a = np.array([[7, 3, 6, 9, 5], [7, 5, 7, 5, 6], [7, 6, 8, 8, 9], [3, 1, 6, 5, 7], [2, 4, 9, 9, 5]])
#     #a = [[16, 32/3, 64/9, 128/27], [16, 4, 1, 1/4], [16, 8, 4, 2], [16, 16/3, 16/9, 16/27]]
#
#     result_min = hungarian_algorithm_min(a, n, n)
#     result_max = hungarian_algorithm_max(a, n, n)
#
#     print(result_min, result_max)











