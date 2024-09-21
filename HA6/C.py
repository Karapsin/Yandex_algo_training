def check(side, w, h, n):
    height_line = side//h
    width_line = side//w

    total = height_line * width_line

    if total < n:
        return False
    else:
        return True


w, h, n = map(int, input().split())

left = 0
right = w*h*n*2
while left < right:
    mid = (left + right)//2
    if check(mid, w, h, n):
        right = mid
    else:
        left = mid + 1

print(left)