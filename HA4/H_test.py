def fast_sol(g, S_len, W, S):
    my_dic = dict()
    for char in W:
        if char not in my_dic.keys():
            my_dic[char] = 0
        my_dic[char] = my_dic[char] + 1

    keys_list = list(my_dic.keys())
    sub_dic = dict()
    for key in keys_list:
        sub_dic[key] = 0

    for i in range(g):
        if S[i] in sub_dic.keys():
            sub_dic[S[i]] = sub_dic[S[i]] + 1

    def dict_check(dic1, dic2):
        keys_list = list(dic1.keys())
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
    for i in range(1, S_len - g + 1):
        if S[i - 1] in sub_dic.keys():
            sub_dic[S[i - 1]] = sub_dic[S[i - 1]] - 1

        if S[i + g - 1] not in my_dic.keys():
            continue
        else:
            sub_dic[S[i + g - 1]] = sub_dic[S[i + g - 1]] + 1

        output = output_change(output, my_dic, sub_dic)

    return output

def slow_sol(g, S_len, W, S):
    my_dic = dict()
    for char in W:
        if char not in my_dic.keys():
            my_dic[char] = 0
        my_dic[char] = my_dic[char] + 1

    res = 0
    for i in range(0, S_len - g + 1):
        sub_word = S[i:(i + g)]
        sub_dic = dict()
        is_ok = True
        for char in sub_word:
            if char not in my_dic.keys():
                is_ok = False
                break
            else:
                if char not in sub_dic.keys():
                    sub_dic[char] = 0
                sub_dic[char] = sub_dic[char] + 1

                if sub_dic[char] > my_dic[char]:
                    is_ok = False
                    break

        if is_ok:
            res = res + 1

    return res

import random
import string

proceed = True
n = 0
while proceed:
    S_len = random.randint(2, 100)
    g = random.randint(1, S_len-1)

    W = str()
    for i in range(g):
        W = W + random.choice(string.ascii_letters)

    S = str()
    for i in range(S_len):
        S = S + random.choice(string.ascii_letters)

    if fast_sol(g, S_len, W, S)!=slow_sol(g, S_len, W, S):
        proceed = False
    else:
        n = n + 1
        print(n)
