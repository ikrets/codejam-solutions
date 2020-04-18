T, W = [int(v) for v in input().split(' ')]

for t in range(T):
    print(210)
    S = int(input())

    R4 = S % 2 ** 60 // 2 ** 52
    R5 = S % 2 ** 52 // 2 ** 42
    R6 = S % 2 ** 42 // 2 ** 35

    print(51)
    S = int(input())

    S -= R6 * 2**8 + R5 * 2**10 + R4 * 2**12
    S %= 2**63

    R1 = S // 2**51
    R2 = S % 2**51 // 2**25
    R3 = S % 2**25 // 2**17

    print(' '.join(str(v) for v in [R1, R2, R3, R4, R5, R6]))
    answer = input()
    if answer == '-1':
        exit()