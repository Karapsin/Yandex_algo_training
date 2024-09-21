def fast_sol(N, L, input_list):
    def how_many_less_or_same(sorted_list, num):
        if num >= sorted_list[-1]:
            return len(sorted_list)
        else:
            left = 0
            right = len(sorted_list) - 1
            while left < right:
                mid = (left + right) // 2
                if sorted_list[mid] <= num:
                    left = mid + 1
                else:
                    right = mid

            return left

    def check(sol_cand, list1, list2):
        total_less_or_equal = how_many_less_or_same(list1, sol_cand) + how_many_less_or_same(list2, sol_cand)
        if total_less_or_equal < L:
            return False
        else:
            return True

    output = list()
    for i in range(N):
        current_list1 = input_list[i]
        for j in range(i + 1, N):
            current_list2 = input_list[j]
            left = 0
            right = L
            while left < right:
                mid = (left + right) // 2
                if check(current_list1[mid], current_list1, current_list2):
                    right = mid
                else:
                    left = mid + 1

            output.append(current_list1[left])

    return output

def slow_sol(N, L, input_list):
    output = list()
    for i in range(N - 1):
        current_list1 = input_list[i].copy()
        for j in range(i + 1, N):
            current_list2 = input_list[j].copy()
            current_list1.extend(current_list2)
            merged = sorted(current_list1)
            output.append(merged[L - 1])

    return output

import random as rd
num = 0

while True:
    N = rd.randint(2, 3)
    L = rd.randint(1, 5)
    rand_input_list = [0]*N
    for i in range(N):
        inner_list = [0]*L
        for j in range(L):
            inner_list[j] = rd.randint(-30, 30)

        rand_input_list[i] = inner_list

    fast_list = fast_sol(N, L, rand_input_list)
    slow_list = slow_sol(N, L, rand_input_list)

    bad = False
    for i in range(len(fast_list)):
        if fast_list[i]!=slow_list[i]:
            bad = True
            break

    if bad:
        break

    num += 1
    print(num)
