import random

def task_1(A):
    possible_ans = {i for i in range(-9, 10)}
    set_a = set(A)

    common = possible_ans & set_a
    return max(common)

def task_2(N, K):
    MAX_DIGIT = 9
    digits = [int(i) for i in str(N)]
    for i, _ in enumerate(digits):
        allow_to_add = MAX_DIGIT - digits[i]
        if K < allow_to_add:
            allow_to_add = K
        K -= allow_to_add
        digits[i] += allow_to_add

    print(f"N={N}, K={K}")
    print(digits)

    ret = int(''.join([str(d) for d in digits]))
    return ret

def task_3(N, K):
    return

if __name__ == "__main__":
    # print(task_1([-6, -91, 1011, -100, 84, -22, 0, 1, 473]))
    # print(task_2(512, 10))
    # print(task_2(285, 20))
    # print(task_2(random.randint(100, 999), random.randint(0, 30)))
    print(task_2(512, 0))
