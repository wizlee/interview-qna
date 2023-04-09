import random

def task_1(A):
    '''
    Find the maximum single digit integer (including negative integers) from an integer list
    '''
    possible_ans = {i for i in range(-9, 10)}
    set_a = set(A)

    common = possible_ans & set_a
    return max(common)

def task_2(N, K):
    '''
    Compute the maximum possible outcome using integer, N which is incremented by at most integer, K step(s).
    N can only be incremented by 1 for each digit individually.
    '''
    MAX_DIGIT = 9
    digits = [int(i) for i in str(N)]
    print(f"N={N}, K={K}")
    print(digits)

    for i, _ in enumerate(digits):
        allow_to_add = MAX_DIGIT - digits[i]
        if K < allow_to_add:
            allow_to_add = K
        K -= allow_to_add
        digits[i] += allow_to_add

    ret = int(''.join([str(d) for d in digits]))
    return ret

from itertools import combinations
from collections import Counter
import string

def get_all_substr_moreThan2Char(string):
    length = len(string) + 1
    # only return  combinations with more than 1 char and combination that has even number of characters
    return set([string[x:y] for x, y in combinations(range(length), r=2) if (y > x + 1) and ((y - x) % 2 == 0)])

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

def task_4(S):
    '''
    From a word consisted of only lowercase alphabets, count the max number of "CONSECUTIVE" characters where each different character must have even count.

    Example (bracket is the max count) -> bdaaadadb(6) abacb(0) zthtzh(6)
    '''
    ret = 0

    cont_substr_list = get_all_substr_moreThan2Char(S)
    print(cont_substr_list)
    filtered_substr_list = []

    for ss in cont_substr_list:
        counter = Counter(ss)
        contiguous = True
        for _, cnt in counter.items():
            if cnt % 2 == 1: # odd number
                contiguous = False
                break

        if contiguous:
            filtered_substr_list.append(ss)

    if filtered_substr_list:
        ret = len(max(filtered_substr_list, key=len))

    return ret


def print_cutout(seq, idx):
    first_portion_remove_last_bracket = str(seq[:idx])[:-1]
    last_portion_remove_first_bracket = str(seq[-idx:])[1:]
    return print(f"{first_portion_remove_last_bracket}, ..., {last_portion_remove_first_bracket}")


if __name__ == "__main__":
    # print(task_1([-6, -91, 1011, -100, 84, -22, 0, 1, 473]))
    # ans = random.randint(-9, 9)
    # print(ans)
    # gen = [random.randint(-10000, 10000) if i != 500 else ans for i in range(1, 1001)]
    # print_cutout(gen, 100)
    # print(f"ans={ans}; calculated={task_1(gen)}")

    # print(task_2(512, 10))
    # print(task_2(285, 20))
    # print(task_2(286, 0))
    # print(task_2(random.randint(100, 999), random.randint(0, 30)))
    # print(task_2(512, 0))

    print(task_4("bdaaadadb"))
    print(task_4("abacb"))
    print(task_4("zthtzh"))
    # print(task_4(randomword(100000)))

    # Result
    # task 1 to 3 100%
    # task 4
    #   correctness 5 out of 7
    #   performance 0 out of 5
