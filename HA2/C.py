size = int(input())
input_list = list(map(int, input().split()))
n = int(input())
min_diff = abs(input_list[0]-n)
ans = input_list[0]

for i in range(len(input_list)):
    diff = abs(input_list[i]-n)
    if diff<min_diff:
        min_diff = diff
        ans = input_list[i]

print(ans)