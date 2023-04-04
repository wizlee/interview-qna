import random

def prac_1():
    a = [i for i in random.randint(0, 20)]
    low, mid, high = [], len(a) // 2, []
    low = a[:mid]
    high = a[mid:]

    print(a)
    print(low)
    print(high)

def prac_2():
    a = [random.randint(0, 19) for _ in range(10)]
    b = [f"even! {i}" if i % 2 == 0 else "Not even" for i in a]

    print(a)
    print(b)

def prac_3():
    test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4, 5]
    test_set = set(test)

    # using test_set is not compulsory but will make this more performant
    print(max(test_set, key = test.count))

def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

def prac_4():
    d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
    parrot(**d)

'''
Starting here is the section for attempting Codality practice rounds
https://app.codility.com/demo/take-sample-test/
'''

def prac_5(A):
    MAX_RET = 100000
    sort_a = sorted(set(A))
    if sort_a[-1] <= 0:
        return 1

    min_positive_int = min(sort_a, key=lambda i: i > 0)
    print(f"min_positive_int={min_positive_int}")
    if min_positive_int > 1:
        return 1

    min_positive_int_not_in_list = min_positive_int
    index_of_min_positive_int = sort_a.index(min_positive_int)
    for i in range(index_of_min_positive_int, len(sort_a)):
        if sort_a[i] <= min_positive_int_not_in_list:
            min_positive_int_not_in_list += 1

        if min_positive_int_not_in_list >= MAX_RET:
            return MAX_RET

    print(f"min_positive_int_not_in_list={min_positive_int_not_in_list}")
    return min_positive_int_not_in_list

# Interesting article and ref: https://pbedn.github.io/post/2018-05-18-codility-demo-test/
def prac_6(A):
    MAX_RET = 100000
    m = max(A)
    if m <= 0:
        return 1

    if m > MAX_RET:
        m = MAX_RET
    else:
        m += 2

    possible = set(e for e in range(1, m)) - set(A)
    return min(possible)

if __name__ == "__main__":
    # prac_1()
    # prac_2()
    # prac_3()
    # prac_4()
    # prac_5([1, 3, 6, 4, 1, 2])
    print(prac_6([1, 3, 6, 4, 1, 2]))
