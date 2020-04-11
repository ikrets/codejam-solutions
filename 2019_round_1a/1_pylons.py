import numpy as np

T = int(input())

def build_graph(R, C):
    graph = np.ones((R * C, R * C), dtype=np.bool)
    graph[np.arange(R * C), np.arange(R * C)] = False

    index = lambda i, j: i * C + j
    all_indices_x = np.repeat(np.arange(R), C)
    all_indices_y = np.tile(np.arange(C), R)

    for x in range(R):
        for y in range(C):
            prohibited = (all_indices_x == x) | (all_indices_y == y)
            prohibited |= (all_indices_x + all_indices_y == x + y)
            prohibited |= (all_indices_x - all_indices_y == x - y)

            prohibited_x = all_indices_x[prohibited]
            prohibited_y = all_indices_y[prohibited]

            graph[index(x, y), index(prohibited_x, prohibited_y)] = False
            graph[index(prohibited_x, prohibited_y), index(x, y)] = False

    return graph

def solve_graph(graph):
    current_v = np.argmin(np.sum(graph, axis=1))
    solution = [current_v]
    for _ in range(graph.shape[0] - 1):
        adjacent_v = graph[current_v]
        if not np.any(adjacent_v):
            return False
            
        next_v = np.argmin(np.sum(graph[adjacent_v], axis=1))
        next_v = np.where(adjacent_v)[0][next_v]
        graph[:, current_v] = False
        graph[current_v, :] = False
        current_v = next_v
        solution.append(current_v)

    return solution
    

for t in range(T):
    R, C = [int(n) for n in input().split(' ')]
    
    graph = build_graph(R, C)
    solution = solve_graph(graph)
    
    from_index = lambda i: (i // C, i % C)
    if not solution:
        print('Case #{}: IMPOSSIBLE'.format(t + 1))
    else:
        print('Case #{}: POSSIBLE'.format(t + 1))
        for index in solution:
            x, y = from_index(index)
            print('{} {}'.format(x + 1, y + 1))