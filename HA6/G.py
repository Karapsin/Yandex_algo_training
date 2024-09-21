def check(width_cand, n, m, t):
    bricks = width_cand * (2*m + 2*n + 4 - 4 *(1+ width_cand))
    if bricks <= t:
        return True
    else:
        return False

n = int(input())
m = int(input())
t = int(input())

left = t//(m * 2 + (n - 2) * 2)
right = max(n, m)//2

while left < right:
    mid = (right + left + 1) // 2
    if check(mid, n, m, t):
        left = mid
    else:
        right = right - 1

print(right)