T = int(input())
readline_int = lambda: [int(v) for v in input().split(' ')]

def reverse_solution(solution, flip_x, flip_y):
    new_sol = []
    for s in solution:
        if s == 'E':
            new_sol.append('W' if flip_x else 'E')
        if s == 'W':
            new_sol.append('E' if flip_x else 'W')
        if s == 'N':
            new_sol.append('S' if flip_y else 'N')
        if s == 'S':
            new_sol.append('N' if flip_y else 'S')
    
    return ''.join(new_sol)

def solve(X, Y):
    S = X + Y

    if not S:
        return ''

    if not S % 2:
        return False

    if S == 1 or S & 2:
        if X % 2:
            head = 'E'
            X -= 1
        else:
            head = 'N'
            Y -= 1
    else:
        if X % 2:
            head = 'W'
            X += 1
        else:
            head = 'S'
            Y += 1

    tail = solve(X >> 1, Y >> 1)
    if tail == False:
        return False
    
    return head + tail
             
for t in range(T):
    X, Y = readline_int()
    if X < 0:
        flip_X = True
        X = -X
    else:
        flip_X = False
    if Y < 0:
        flip_Y = True
        Y = -Y
    else:
        flip_Y = False

    solution = solve(X, Y)

    if not solution:
        print('Case #{}: IMPOSSIBLE'.format(t + 1))
    else:
        solution = reverse_solution(solution, flip_X, flip_Y)
        print('Case #{}: {}'.format(t + 1, ''.join(solution)))