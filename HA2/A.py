#A
def is_ascending(input_list):
    lower_index = -1
    for i in range(len(input_list)-1):
        if input_list[i+1] <= input_list[i]:
            lower_index = i
            break

    if lower_index == -1:
        print('YES')
    else:
        print('NO')

is_ascending(list(map(int, input().split())))