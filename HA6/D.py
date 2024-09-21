def check(cand_d, n, a, b, w, h):
    block_width = (a + 2*cand_d)
    block_height = (b + 2*cand_d)
    block_size = block_width*block_height

    option1 = (w // block_width) * (h // block_height)
    option2 = (w // block_height) * (h // block_width)

    if option1 >= n:
        if option1*block_size <= w * h:
            return True
        else:
            return False
    elif option2 >= n:
        if option2*block_size <= w * h:
            return True
        else:
            return False
    else:
        return False


n, a, b, w, h = map(int, input().split())

left = 0
right = max(w, h) + 1

while left < right:
    mid = (right + left + 1)//2
    if check(mid, n, a, b, w, h):
        left = mid
    else:
        right = mid - 1

print(right)