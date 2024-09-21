def check(index, target, target_list):
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
        mid = (left+right)//2
        if check(mid, target, target_list):
            right = mid
        else:
            left = mid + 1

    if target_list[left] == target:
        print('YES')
    else:
        print('NO')



