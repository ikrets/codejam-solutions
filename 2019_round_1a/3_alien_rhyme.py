from collections import defaultdict

T = int(input())

def count(words, first=False):
    l_to_rest = defaultdict(lambda: [])
    ones_present = 0
    result = 0

    for w in words:
        if not w:
            ones_present += 1
        else:
            l_to_rest[w[0]].append(w[1:])

    for _, rests in l_to_rest.items():
        if len(rests) == 1:
            ones_present += 1
        if len(rests) == 2:
            result += 2
        if len(rests) > 2:
            c = count(rests)
            ones_present += len(rests) - c
            result += c

    if ones_present > 1 and not first:
        result += 2
        
    return result

        
for t in range(T):
    N = int(input())
    words = []
    for i in range(N):
        words.append(input()[::-1])

    c = count(words, first=True)
    print('Case #{}: {}'.format(t + 1, c))