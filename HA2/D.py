input_list = list(map(int, input().split()))
n = 0
for i in range(len(input_list)-2):
    if input_list[i]<input_list[i+1] and input_list[i+1]>input_list[i+2]:
        n = n + 1

print(n)