from collections import defaultdict

T, N, M = [int(v) for v in input().split(' ')]

def solve(possible_ms, max_m, checked_mod, checked_mod_value):
    new_possible_ms = set()
    for v in possible_ms:
        if v % checked_mod == checked_mod_value:
            new_possible_ms.add(v)

    return new_possible_ms
    
        

for t in range(T):
    possible_ms = set(range(1, M + 1))
    for mod in [17, 15, 13, 11]:
        print(' '.join([str(mod)] * 18))
        mods = [int(v) for v in input().split(' ')]
        mod_value = sum(mods) % mod

        possible_ms = solve(possible_ms, max_m=M, checked_mod=mod,
                            checked_mod_value=mod_value)

        if len(possible_ms) == 1:
            break

    possible_mods = set(range(2, 19)) - set([17, 15, 13, 11])
    for _ in range(3): 
        if len(possible_ms) == 1:
            break

        splits = {}
        for mod in possible_mods:
            different_mod_values = set()
            for possible_m in possible_ms:
                different_mod_values.add(possible_m % mod)
            splits[mod] = len(different_mod_values)

        best_mod = max(splits.keys(), key=lambda k: splits[k])
        possible_mods.remove(best_mod)
        print(' '.join([str(best_mod)] * 18))
        mods = [int(v) for v in input().split(' ')]
        mod_value = sum(mods) % best_mod

        possible_ms = solve(possible_ms, 
                            max_m=M, 
                            checked_mod=best_mod,
                            checked_mod_value=mod_value)

    print(possible_ms.pop())
    answer = input()
    if answer != '1':
        exit()