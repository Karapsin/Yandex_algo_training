input_list = list(map(int, input().split()))

first_max = None
second_max = None
first_min = None
second_min = None

for i in range(len(input_list)):

    if first_max is None or input_list[i]>first_max:
        second_max = first_max
        first_max = input_list[i]
    elif second_max is None or input_list[i]>second_max:
        second_max = input_list[i]

    if first_min is None or input_list[i]<first_min:
        second_min = first_min
        first_min = input_list[i]
    elif second_min is None or input_list[i]<second_min:
        second_min = input_list[i]

first_guess = first_max*second_max
second_guess = first_min*second_min

if first_guess>second_guess:
    print(second_max, first_max)
else:
    print(first_min, second_min)