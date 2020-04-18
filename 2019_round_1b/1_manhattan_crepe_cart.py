import numpy as np
T = int(input())

for t in range(T):
    P, Q = [int(v) for v in input().split(' ')]
    x_votes = np.zeros(Q + 1, dtype=np.int32)
    y_votes = np.zeros(Q + 1, dtype=np.int32)
    
    for _ in range(P):
        x, y, direction = input().split(' ')
        x, y = int(x), int(y)

        if direction == 'S':
            y_votes[:y] += 1
        if direction == 'N':
            y_votes[y + 1:] += 1
        if direction == 'W':
            x_votes[:x] += 1
        if direction == 'E':
            x_votes[x + 1:] += 1
            
    print('Case #{}: {} {}'.format(t + 1, 
                                   np.argmax(x_votes),
                                   np.argmax(y_votes)))