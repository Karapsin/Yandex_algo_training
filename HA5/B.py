N, K = map(int, input().split())
input_list = list(map(int, input().split()))

output = 0
left = 0
right = 0
current_sum = input_list[right]

while True:
    if current_sum<K:
        right = right + 1
        if right > (N-1):
            break
        current_sum = current_sum + input_list[right]

    elif right <= (N-1):
        if current_sum == K:
            output = output + 1
        current_sum = current_sum - input_list[left]
        left = left + 1

print(output)