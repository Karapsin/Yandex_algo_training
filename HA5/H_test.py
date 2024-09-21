def change_dict(dict, key, value):
    if key not in dict:
        dict[key] = 0

    dict[key] = dict[key] + value

    return dict

def is_dict_ok(dict, k):
    result = True
    for key in dict:
        if dict[key] > k:
            result = False
            break
    return result

def dict_from_str(input_str):
    my_dict = dict()
    for char in input_str:
        if char not in my_dict:
            my_dict[char] = 0
        my_dict[char] = my_dict[char] + 1

    return my_dict

def get_dict_max_val(dict):
    max_val = -1
    for key in dict:
        if dict[key] > max_val:
            max_val = dict[key]

    return max_val


def slow_sol(input_str, k, n):
    best_res = -1
    best_res_start = -1
    for i in range(len(input_str)):
        for j in range(i+1, len(input_str)):
            new_str = input_str[i:(j+1)]
            str_dict = dict_from_str(new_str)

            if get_dict_max_val(str_dict)<=k and ((j+1)-i)>best_res:
                best_res = j + 1 - i
                best_res_start = i + 1

    if best_res == -1:
        best_res = n
        best_res_start = 1


    return (best_res, best_res_start)

def fast_sol(input_str, k, n):
    left = 0
    right = 1
    best_length = -1
    best_start = -1
    str_dict = change_dict(dict(), input_str[0], 1)

    while right < n:
        str_dict = change_dict(str_dict, input_str[right], 1)
        if is_dict_ok(str_dict, k):
            right = right + 1
        else:
            if (right - left) > best_length:
                best_length = right - left
                best_start = left + 1

            str_dict = change_dict(str_dict, input_str[left], -1)

            left = left + 1
            right = right + 1

    if (right - left) > best_length:
        best_length = right - left
        best_start = left + 1

    return (best_length, best_start)

import random
import string

num = 0
while True:
    n = random.randint(1, 10)
    k = random.randint(1, n)

    input_str = str()
    for _ in range(n):
        input_str = input_str + random.choice(string.ascii_letters).lower()

    fast = fast_sol(input_str, k, n)
    slow = slow_sol(input_str, k, n)

    if fast[0]!=slow[0]:
        break

    num = num + 1
    print(num)

