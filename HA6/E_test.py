import math
def fast_sol(a, b, c):
    def check(d_cand, a, b, c):
        avg_grade = (2 * a + 3 * b + 4 * c + 5 * d_cand)/(a + b + c + d_cand)
        if avg_grade <= 3.5:
            return False
        else:
            return True

    left = 0
    right = a + b + c + 1
    while left < right:
        mid = (left + right) // 2
        if check(mid, a, b, c):
            right = mid
        else:
            left = mid + 1

    return left

def slow_sol(a, b, c):
    sigma = a + b + c
    total = 2 * a + 3 * b + 4 * c

    res = (3.5 * sigma - total)/1.5
    if res<0:
        return 0
    else:
        return math.ceil(res)

import random
num = 0
while True:
    a = random.randint(1, 10**15)
    b = random.randint(1, 10**15)
    c = random.randint(1, 10**15)

    if a + b + c >= 1:
        if fast_sol(a, b, c)!=slow_sol(a, b, c):
            break

    num = num + 1
    print(num)



