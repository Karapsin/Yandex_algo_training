N, R, C = map(int, input().split())
input_list = list()
for _ in range(N):
    input_list.append(int(input()))

input_list.sort()

def check(sol_cand, input_list, R, C):
    brigades = 0

    first_index = 0
    last_index = first_index + (C - 1)
    while True:
        if (input_list[last_index] - input_list[first_index]) <= sol_cand:
            brigades += 1
            first_index = last_index + 1
            last_index = first_index + (C - 1)

        else:
            first_index += 1
            last_index += 1

        if last_index > len(input_list) - 1:
            break

    if brigades < R:
        return False
    else:
        return True

left = 0
right = input_list[-1] - input_list[0]
while left < right:
    mid = (left + right)//2
    if check(mid, input_list, R, C):
        right = mid
    else:
        left = mid + 1

print(left)