def gen_seq(x1, d, a, c, m, L):
    x = [x1]
    for i in range(1, L):
        x.append(x[i - 1] + d)
        d = ((a*d + c) % m)

    return x

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

def check(sol_cand, list1, list2):
    total_less_or_equal = how_many_less_or_same(list1, sol_cand) + how_many_less_or_same(list2, sol_cand)
    if total_less_or_equal < L:
        return False
    else:
        return True

N, L = map(int, input().split())
input_list = [0]*N
for i in range(N):
    x1, d1, a, c, m = list(map(int, input().split()))
    input_list[i] = gen_seq(x1, d1, a, c, m, L)


for i in range(N):
    for j in range(i + 1, N):
        left1 = min(input_list[i][0], input_list[j][0])
        right1 = max(input_list[i][-1], input_list[j][-1])
        while left1 < right1:
            mid = (left1 + right1) // 2
            if check(mid, input_list[i], input_list[j]):
                right1 = mid
            else:
                left1 = mid + 1

        print(left1)
