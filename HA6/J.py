N, L = map(int, input().split())
input_list = [0]*N
for i in range(N):
    input_list[i] = list(map(int, input().split()))

def how_many_less_or_same(sorted_list, num):
    if num >= sorted_list[-1]:
        return len(sorted_list)
    else:
        left = 0
        right = len(sorted_list) - 1
        while left < right:
            mid = (left + right)//2
            if sorted_list[mid] <= num:
                left = mid + 1
            else:
                right = mid

        return left

def get_total_less_num(sol_cand, list1, list2):
    return how_many_less_or_same(list1, sol_cand) + how_many_less_or_same(list2, sol_cand)

def check(sol_cand, list1, list2):
    total_less_or_equal = get_total_less_num(sol_cand, list1, list2)
    if total_less_or_equal < L:
        return False
    else:
        return True

for i in range(N):
    current_list1 = input_list[i]
    for j in range(i + 1, N):
        current_list2 = input_list[j]
        left1 = min(current_list1[0], current_list2[0])
        right1 = max(current_list1[-1], current_list2[-1])
        while left1 < right1:
            mid = (left1 + right1) // 2
            if check(mid, current_list1, current_list2):
                right1 = mid
            else:
                left1 = mid + 1

        print(left1)