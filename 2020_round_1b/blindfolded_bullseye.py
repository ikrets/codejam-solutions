readline_int = lambda: [int(v) for v in input().split(' ')]
T, A, B = readline_int()

def find(fix, find_X, start, end):
    i = start
    j = end

    while abs(j - i) != 1:
        m = i + (j - i) // 2

        if find_X:
            print('{} {}'.format(m, fix))
        else:
            print('{} {}'.format(fix, m))

        answer = input()
        if answer == 'MISS':
            j = m
        else:
            i = m

    if find_X:
        print('{} {}'.format(j, fix))
    else:
        print('{} {}'.format(fix, j))
    
    answer = input()
    return i if answer == 'MISS' else j

for t in range(T):
    centers = [(x, y) for x in [-5 * 10**8, 5 * 10**8] for y in [-5 * 10**8, 5 * 10**8]] + [(0, 0)]
    for p_x, p_y in centers:
        print('{} {}'.format(p_x, p_y))
        answer = input()
        if answer != 'MISS':
            break

    l = find(p_x, False, p_y, -10**9)
    r = find(p_x, False, p_y, 10**9)
    c_y = l + (r - l) // 2

    ll = find(c_y, True, p_x, -10**9)
    rr = find(c_y, True, p_x, 10**9)
    c_x = ll + (rr - ll) // 2

    print('{} {}'.format(c_x, c_y))
    answer = input()
    diffs = [(x, y) for x in [2, 1, -1, -2] for y in [2, 1, -1, -2]]
    for x_d, y_d in diffs:
        if answer == 'CENTER':
            break

        print('{} {}'.format(c_x + x_d, c_y + y_d))
        answer = input()