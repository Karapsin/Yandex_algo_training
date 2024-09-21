def check(d_cand, a, b, c):
    avg_grade = (2 * a + 3 * b + 4 * c + 5 * d_cand) * 2
    if avg_grade < 7 * (a + b + c + d_cand):
        return False
    else:
        return True

a = int(input())
b = int(input())
c = int(input())

left = 0
right = a + b + c + 1
while left < right:
    mid = (left + right) // 2
    if check(mid, a, b, c):
        right = mid
    else:
        left = mid + 1

print(left)
