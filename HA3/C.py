input_data = list(map(int, input().split()))

a_set = set()
for i in range(input_data[0]):
    a_set.add(int(input()))

b_set = set()
for i in range(input_data[1]):
    b_set.add(int(input()))

common = a_set & b_set

output1 = a_set & common
output2 = a_set - common
output3 = b_set - common

print(len(output1))
print(*sorted(output1))
print(len(output2))
print(*sorted(output2))
print(len(output3))
print(*sorted(output3))

