import numpy as np
from itertools import permutations

T = int(input())

def search_trace_then_square(N, diag, i, K):
    min_v = 1 if i == 0 else diag[i - 1]
    for v in range(1, N + 1):
        diag_copy = diag.copy()
        diag_copy[i] = v

        if i == N - 1:
            if np.sum(diag_copy) == K:
                res = search_square_no_diag(np.diag(diag_copy), 0, 1)
            else:
                res = None
        else:
            res = search_trace_then_square(N, diag_copy, i + 1, K)

        if res is not None:
            return res

    return None

def search_square_no_diag(arr, i, j):
    N = arr.shape[0]
    values = set(np.arange(1, N + 1)) - set(arr[i, :j]) - set(arr[:i, j]) - set([arr[i, i], arr[j, j]])
    for v in values:
        arr_copy = arr.copy()
        arr_copy[i, j] = v
        
        if j < N - 1:
            i_new = i
            j_new = j + 1
        elif i < N - 1:
            i_new = i + 1
            j_new = 0

        if i_new == j_new:
            if i_new != N - 1:
                j_new += 1
            else:
                return arr_copy

            
        res = search_square_no_diag(arr_copy, i_new, j_new)
        if res is not None:
            return res
    
    return None
    
def find_perm_with_trace(square, K):
    N = square.shape[0]
    
    for row_perm in permutations(np.arange(N)):
        for col_perm in permutations(np.arange(N)):
            perm_square = square[row_perm, :]
            perm_square = perm_square[:, col_perm]
            if np.trace(perm_square) == K:
                return perm_square

            perm_square = square[:, col_perm]
            perm_square = perm_square[row_perm, :]
            if np.trace(perm_square) == K:
                return perm_square
                
    return None

for t in range(T):
    N, K = [int(n) for n in input().split(' ')]
    
    arr = np.zeros((N, N), dtype=np.uint8)
    square = search_trace_then_square(N, np.zeros(N).astype(np.uint8), 0, K)
    # print(square)
    
    # perm_square = find_perm_with_trace(square, K)
    if square is None:
        print('Case #{}: IMPOSSIBLE'.format(t + 1))
    else:
        print('Case #{}: POSSIBLE'.format(t + 1))
        for i in range(N):
            print(' '.join([str(n) for n in square[i]]))
    
