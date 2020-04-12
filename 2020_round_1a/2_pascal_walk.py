import math

T = int(input())

def comb(n, k):
    return math.factorial(n) // math.factorial(k) // math.factorial(n - k)

def calc_exit_cost(n, k, last_action):
    s = 0
    if k == 0:
        return 0

    while k > 0:
        k -= 1
        s += comb(n, k)

    return s

def solve(n, k, actions, N):
    if N == 0:
        return actions

    choice = [c for c in [(n + 1, k), (n + 1, k + 1), (n, k - 1)]
              if c[1] >= 0 and c != actions[-2] and c[1] <= c[0] // 2]

    max_value = 0
    max_cost = 0

    for c in choice:
        cost = comb(*c)
        exit_cost = calc_exit_cost(*c, actions[-2])

        if cost + exit_cost <= N and cost + exit_cost > max_value:
            max_cost = cost
            max_value = cost + exit_cost
            max_choice = c

    return solve(max_choice[0], max_choice[1], actions + [max_choice], N - max_cost)
    

for t in range(T):
    print('Case #{}:'.format(t + 1))

    N = int(input())
    solution = solve(0, 0, [(0, 0), (0, 0)], N - 1)
    for s in solution[1:]:
        print(s[0] + 1, s[1] + 1)
    