N = int(input())
stress_dic = dict()
for i in range(N):
    word = input()
    standard_word = word.lower()

    if standard_word not in stress_dic.keys():
        stress_dic[standard_word] = set()

    stress_dic[standard_word].add(word)

def get_upper_indexies_list(word):
    upper_indexies_list = list()
    for i in range(len(word)):
        count = 0
        if word[i].isupper():
            upper_indexies_list.append(i)
            count = count + 1
            if count > 1:
                break

    return upper_indexies_list


check_str = input().split()
mistakes = 0

for word in check_str:
    up_idx_list = get_upper_indexies_list(word)

    if len(up_idx_list)!=1:
        mistakes = mistakes + 1

    elif word.lower() in stress_dic.keys() and word not in stress_dic[word.lower()]:
        mistakes = mistakes + 1

print(mistakes)