def check_1(index, target, target_list):
    if target_list[index] < target:
        return False
    else:
        return True

N, K = map(int, input().split())
target_list = list(map(int, input().split()))
input_list = list(map(int, input().split()))

for target in input_list:
    left = 0
    right = N - 1
    while left < right:
        mid = (left + right)//2
        if check_1(mid, target, target_list):
            right = mid
        else:
            left = mid + 1

    if left > 0:
        dist1 = abs(target_list[left] - target)
        dist2 = abs(target_list[left - 1] - target)

        if dist1 < dist2:
            print(target_list[left])
        elif dist1 > dist2:
            print(target_list[left - 1])
        else:
            print(min(target_list[left], target_list[left - 1]))

    else:
        print(target_list[left])

