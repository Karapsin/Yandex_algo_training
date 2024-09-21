g, S_len = map(int, input().split())
W = input()
S = input()

my_dic = dict()
sub_dic = dict()

for char in W:
    if char not in my_dic.keys():
        my_dic[char] = 0
        sub_dic[char] = 0
    my_dic[char] = my_dic[char] + 1

keys_set = set(my_dic.keys())

for i in range(g):
    if S[i] in keys_set:
        sub_dic[S[i]] = sub_dic[S[i]] + 1


def dict_check(dic1, dic2):
    keys_list = list(keys_set)
    result = True
    for key in keys_list:
        if dic1[key] != dic2[key]:
            result = False
            break
    return result


def output_change(output, dic1, dic2):
    if dict_check(dic1, dic2):
        output = output + 1
    return output


output = output_change(0, my_dic, sub_dic)
for i in range(g, S_len):

    prev_char = S[i - g]
    next_char = S[i]

    if prev_char in keys_set:
        sub_dic[prev_char] = sub_dic[prev_char] - 1

    if next_char not in keys_set:
        continue
    else:
        sub_dic[next_char] = sub_dic[next_char] + 1

    output = output_change(output, my_dic, sub_dic)

print(output)