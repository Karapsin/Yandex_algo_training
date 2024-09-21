def check(time_cand, x, y, N):

    first_copy_time = min(x, y)
    adj_time = time_cand - first_copy_time

    perfomance = (adj_time // x) + (adj_time // y) + 1
    if perfomance < N:
        return False
    else:
        return True

N, x, y = map(int, input().split())

left = 0
right = N * max(x, y)
while left < right:
    mid = (left + right) // 2
    if check(mid, x, y, N):
        right = mid
    else:
        left = mid + 1

print(left)
