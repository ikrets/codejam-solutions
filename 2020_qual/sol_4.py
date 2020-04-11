#!/usr/bin/python3
import numpy as np
import sys

T, B = [int(n) for n in input().split(' ')]

def figure_out(array, start, end, possibilities):
    for i in range(start, end + 1):
        possible_values = {0: [], 1: []}
        
        if 'noop' in possibilities:
            possible_values[array[i]].append('noop')
        if 'flip' in possibilities:
            possible_values[1 - array[i]].append('flip')
        if 'rev' in possibilities:
            possible_values[array[-1 - i]].append('rev')
        if 'revflip' in possibilities:
            possible_values[1 - array[-1 - i]].append('revflip')
            
        if possible_values[0] and possible_values[1]:
            return i, possible_values
            
    return None, None
    
def apply_transform(array, transform):
    if transform == 'flip':
        return 1 - array
    if transform == 'rev':
        return array[::-1]
    if transform == 'revflip':
        return 1 - array[::-1]
        
    return array
    
    

for t in range(T):
    array = np.zeros(B, dtype=np.uint8)
    figuring_out = False
    
    i = 0
    queries = 0
    while i < B or figuring_out:
        if figuring_out:
            print(next_P + 1, flush=True)
            queries += 1
            c = int(input())
            
            possibilities = possible_values[c]
            print('Checked position: {}, result: {}, possibilities: {}'.format(next_P, 
                c,
                possibilities),
                    file=sys.stderr)
            if len(possibilities) == 1:
                array = apply_transform(array, possibilities[0])
                figuring_out = False
            else:
                next_P, possible_values = figure_out(
                        array, 
                        start=next_P + 1,
                        end=i // 2 + 1, 
                        possibilities=possibilities)
                if next_P is None:
                    array = apply_transform(array, possibilities[0])
                    figuring_out = False
                    
            continue
            
        P = i // 2 if i % 2 == 0 else B - i // 2 - 1
        
        print(P + 1, flush=True)
        queries += 1
        char = int(input())
        print('Queried {}, got {}'.format(P + 1, char), file=sys.stderr)
        
        array[P] = int(char)
        print('i {}, array guess: {}'.format(i, array), file=sys.stderr)
        
        if queries % 10 == 0 and queries:
            next_P, possible_values = figure_out(array, start=0, end=i // 2 + 1,
                    possibilities=['noop', 'flip', 'rev', 'revflip'])
            if next_P is not None:
                print('Started guessing: next check {}, possiblities: {}'.format(next_P, possible_values),
                        file=sys.stderr)
                figuring_out = True
            else:
                print('No guessing: array is invariant')
                figuring_out = False

            # if currently checked left side of the array, discard
            if i % 2 == 0:
                i -= 1
            
        i += 1
        
    print(''.join([str(n) for n in array]), flush=True)
    answer = input()
    if answer == 'Y':
        continue
    else:
        break
