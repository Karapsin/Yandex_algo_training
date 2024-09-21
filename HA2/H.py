input_list = list(map(int, input().split()))

first_max = None
second_max = None
third_max = None
first_min = None
second_min = None
first_max_index = -1
second_max_index = -1
third_max_index = -1
for i in range(len(input_list)):
    if first_max is None or input_list[i]>first_max:
        third_max = second_max
        second_max = first_max
        first_max = input_list[i]
        first_max_index = i

    elif second_max is None or (input_list[i]>second_max and i!=first_max_index):
        third_max = second_max
        second_max = input_list[i]
        second_max_index = i

    elif third_max is None or (input_list[i]>third_max and i!=second_max_index):
        third_max = input_list[i]
        third_max_index = i

    if first_min is None or input_list[i]<first_min:
        second_min = first_min
        first_min = input_list[i]
    elif second_min is None or input_list[i]<second_min:
        second_min = input_list[i]

if first_min is None or second_min is None or (first_max*second_max*third_max>first_max*first_min*second_min):
    print(first_max, second_max, third_max)
else:
    print(first_max, first_min, second_min)