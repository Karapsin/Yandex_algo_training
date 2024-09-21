n, r = map(int, input().split())
input_list = list(map(int, input().split()))

left = 0
right = 1
pairs = 0
while right <= (n-1):
    dist = input_list[right] - input_list[left]
    if dist <= r:
        right = right + 1
    else:
        pairs = pairs + (n - right)
        left = left + 1
print(pairs)