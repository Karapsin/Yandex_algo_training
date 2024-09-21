input_list = list(map(int, input().split()))
my_set = set()

uniq = 0
for i in range(len(input_list)):
    if not(input_list[i] in my_set):
        my_set.add(input_list[i])
        uniq = uniq + 1

(print(uniq))

my_set[1]