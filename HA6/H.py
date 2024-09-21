def check(size_cand, input_list, K):
    if sum([x//size_cand for x in input_list]) < K:
        return False
    else:
        return True

N, K = map(int, input().split())
input_list = list()
max_val = -1
for _ in range(N):
    current_input = int(input())
    if current_input > max_val:
        max_val = current_input
    input_list.append(current_input)

left = 0
right = max_val
while left < right:
    mid = (left + right + 1) // 2
    if check(mid, input_list, K):
        left = mid
    else:
        right = mid - 1

print(right)