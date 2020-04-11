T = int(input())

def solve(patterns, pointers):
    result = []
    while True:
        letter = None
        star_letter = None
        first_star_letter = None

        letter_pointers = []
        star_letter_pointers = []
        first_star_letter_pointers = []

        for i in range(N):
            if patterns[i][pointers[i]] != '*':
                if letter is None:
                    letter = patterns[i][pointers[i]]
                    letter_pointers.append(i)
                else:
                    if patterns[i][pointers[i]] != letter:
                        return None
                    else:
                        letter_pointers.append(i)

        for i in range(N):
            if patterns[i][pointers[i]] == '*':
                if pointers[i] == 0:
                    continue

                while pointers[i] >= 1 and patterns[i][pointers[i] - 1] == '*':
                    pointers[i] -= 1

                if pointers[i] > 1:
                    if star_letter is None or star_letter == patterns[i][pointers[i] - 1]:
                        star_letter = patterns[i][pointers[i] - 1]
                        star_letter_pointers.append(i)

                        if letter and letter == star_letter:
                            pointers[i] -= 2
                        
                elif pointers[i] == 1:
                    if first_star_letter is None or first_star_letter == patterns[i][pointers[i] - 1]:
                        first_star_letter = patterns[i][pointers[i] - 1]
                        first_star_letter_pointers.append(i)

                        if letter and letter == first_star_letter:
                            pointers[i] -= 2

        for i in letter_pointers:
            pointers[i] -= 1

        if not letter and not star_letter and not first_star_letter:
            return ''.join(reversed(result))

        if letter:
            result.append(letter)
        elif star_letter:
            result.append(star_letter)
            for p in star_letter_pointers:
                pointers[p] -= 2
        else:
            result.append(first_star_letter)
            for i in range(N):
                letter_star = pointers[i] == 1 and patterns[i][1] == '*' and patterns[i][0] == first_star_letter
                letter = pointers[i] == 0 and patterns[i][0] == first_star_letter
                star = pointers[i] == 0 and patterns[i][0] == '*'
                if not letter and not letter_star and not star:
                    return None
            return ''.join(reversed(result))

        any_finished = any(pointers[i] == -1 for i in range(len(pointers)))
        all_finished = all(pointers[i] == -1 or (pointers[i] == 0 and patterns[i] == '*')  
                       for i in range(len(pointers)))

        if any_finished and not all_finished:
            return None
        if all_finished:
            return ''.join(reversed(result))
            

for t in range(T):
    N = int(input())
    
    patterns = [list(input().strip(' ')) for _ in range(N)]
    pointers = [len(p) - 1 for p in patterns]
    
    solution = solve(patterns, pointers)
    if solution is not None:
        print('Case #{}: {}'.format(t + 1, solution))
    else:
        print('Case #{}: *'.format(t + 1))
        