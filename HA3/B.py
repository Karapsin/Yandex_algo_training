input_list = list(map(int, input().split()))
input_set= set(map(int, input().split()))

output = set()
for i in range(len(input_list)):
    if input_list[i] in input_set:
        output.add(input_list[i])

print(*sorted(output))
