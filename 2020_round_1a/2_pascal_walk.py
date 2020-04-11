import math

T = int(input())

for t in range(T):
    print('Case #{}:'.format(t + 1))

    N = int(input())
    if N > 4:
        n = int((-1 + math.sqrt(-1 + 8 * (N - 1))) / 2)
        reached_sum = n * (n + 1) // 2 + 1
        leftover = N - reached_sum
        print('1 1')
        for i in range(n):
            print('{} {}'.format(i + 2, 2 if i else 1))
        for i in range(n + 2, n + 2 + leftover):
            print('{} 1'.format(i - 1))
    else:
        for i in range(N):
            print('{} 1'.format(i + 1))
    