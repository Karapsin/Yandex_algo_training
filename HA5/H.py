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

n, k = map(int, input().split())
input_str = input()

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

print(best_length, best_start)
