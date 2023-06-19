from tsp_utilities import *


def tsp_LK(D, tour,
          length):
    n = len(tour)
    succ = tsp_tour_to_succ(tour)
    for i in range(n): succ[tour[i]] = tour[(i + 1) % n]
    tabu = [[0 for _ in range(n)] for _ in range(n)]
    iteration=0
    last_a, a = 0, 0
    improved = True
    while a != last_a or improved:
        improved = False
        iteration += 1
        b = succ[a]
        path_length = length - D[a][b]
        path_modified = True
        while path_modified:
            path_modified=False
            ref_struct_cost = length
            c=best_c=succ[b]
            while succ[c] != a:
                d = succ[c]
                if path_length - D[c][d] + D[c][a]+ D[b][d] < length:
                    best_c = c
                    ref_struct_cost = path_length - D[c][d] + D[c][a] + D[b][d]
                    break
                if tabu[c][d] != iteration and \
                                 path_length + D[b][d] < ref_struct_cost:
                    ref_struct_cost = path_length + D[b][d]
                    best_c = c
                c = d
            if ref_struct_cost < length:  # Admissible reference structure
                path_modified = True
                c, d = best_c, succ[best_c]
                tabu[c][d] = tabu[d][c] = iteration
                path_length += (D[b][d] - D[c][d])
                i, si, succ[b] = b, succ[b], d
                while i != c:
                    succ[si], i, si = i, si, succ[si]
                b = c

                if path_length + D[a][b] < length:
                    length = path_length + D[a][b]
                    succ[a], last_a = b, b
                    improved = True
                    tour = tsp_succ_to_tour(succ)
        succ = tsp_tour_to_succ(tour)
        a = succ[a]
    return tour, length


def tsp_2opt_best(d, tour,
length):
        n = len(tour)
        best_delta = -1
        while best_delta < 0:
            best_delta = float(1000000)
            best_i = best_j = -1
            for i in range(n - 2):
                j=i+2
                while j < n and(i>0 or j<n-1):
                    delta =\
                    d[tour[i]][tour[j]] + d[tour[i+1]][tour[(j+1)%n]] \
                  - d[tour[i]][tour[i+1]] - d[tour[j]][tour[(j+1)%n]]
                if delta < best_delta:
                    best_delta = delta
                    best_i, best_j = i, j
                    j += 1
            if best_delta < 0:
                length += best_delta
                i, j = best_i+1, best_j # Reverse path from best_i+1 to best_j
                while i < j:
                    tour[i], tour[j] = tour[j], tour[i]
                    i,j=i +1,j-1
        return tour, length