input_list = list()
input_finished = False
while not (input_finished):
    current_input = int(input())
    if current_input != -2000000000:
        input_list.append(current_input)
    else:
        input_finished = True

is_constant = True
is_ascending = True
is_weakly_ascending = True
is_descending = True
is_weakly_descending = True
is_random = True

for i in range(len(input_list) - 1):
    if is_constant:
        if input_list[i + 1] != input_list[i]:
            is_constant = False

    if is_ascending:
        if input_list[i + 1] <= input_list[i]:
            is_ascending = False

    if is_weakly_ascending:
        if input_list[i + 1] < input_list[i]:
            is_weakly_ascending = False

    if is_descending:
        if input_list[i + 1] >= input_list[i]:
            is_descending = False

    if is_weakly_descending:
        if input_list[i + 1] > input_list[i]:
            is_weakly_descending = False

if is_constant or is_ascending or is_descending:
    is_weakly_ascending = False
    is_weakly_descending = False

check = (is_constant + is_ascending + is_weakly_ascending + is_descending + is_weakly_descending)

if check != 0:
    is_random = False

if check != 1 and check != 0:
    print('RANDOM')
    is_constant, is_ascending, is_weakly_ascending, is_descending, is_weakly_descending, is_random = False, False, False, False, False, False

if is_constant:
    print('CONSTANT')
if is_ascending:
    print('ASCENDING')
if is_weakly_ascending:
    print('WEAKLY ASCENDING')
if is_descending:
    print('DESCENDING')
if is_weakly_descending:
    print('WEAKLY DESCENDING')
if is_random:
    print('RANDOM')

