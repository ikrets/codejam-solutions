T = int(input())

def solve(patterns):
    p = []
    q = []
    r = []

    for pattern in patterns:
        p.append(pattern[0])
        r.append(pattern[-1])
        left = 1 if pattern[0] != '*' else 0
        right = -1 if pattern[-1] != '*' else len(pattern)

        if pattern[left:right]:
            q.append(pattern[left:right])
        else:
            q.append('0')

    solution_left = []        
    solution_right = []

    while True:
        letters = set(l for l in p if l not in '*0')
        if len(letters) > 1:
            return None
        if len(letters) == 1:
            if any(l == '0' for l in p):
                return None

            solution_left.append(letters.pop())
            for i in range(len(patterns)):
                if p[i] not in '*':
                    if q[i][0] in '0*':
                        p[i] = q[i][0]
                    else:
                        p[i] = q[i][0]
                        q[i] = q[i][1:]
                        if not q[i]:
                            q[i] = ['0']
            continue

        letters = set(l for l in r if l not in '*0')
        if len(letters) > 1:
            return None
        if len(letters) == 1:
            if any(l == '0' for l in r):
                return None

            solution_right.append(letters.pop())
            for i in range(len(patterns)):
                if r[i] not in '*':
                    if q[i][-1] in '0*':
                        r[i] = q[i][-1]
                    else:
                        r[i] = q[i][-1]
                        q[i] = q[i][:-1]
                        if not q[i]:
                            q[i] = ['0']
            continue

        solution_middle = [''.join(subl) for subl in q]
        solution = solution_left + solution_middle + solution_right[::-1]
        solution = ''.join(solution)
        solution = ''.join([c for c in solution if c not in '0*'])
        return solution

for t in range(T):
    N = int(input())
    
    patterns = [list(input().strip(' ')) for _ in range(N)]
    
    solution = solve(patterns)
    if solution is not None:
        print('Case #{}: {}'.format(t + 1, solution))
    else:
        print('Case #{}: *'.format(t + 1))
        