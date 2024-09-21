input_set = set(map(int, input().split()))
input_num = input()

my_set = set()
for num in input_num:
    if not(num in my_set):
        my_set.add(int(num))

res = my_set - input_set

if len(res)==0:
    print(0)
else:
    print(len(res))