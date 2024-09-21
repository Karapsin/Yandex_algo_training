N = int(input())

lang_list = list()
for i in range(N):
    lang_num = int(input())
    current_set = set()
    for j in range(lang_num):
        lang = input()
        current_set.add(lang)

    lang_list.append(current_set)

all_lang_set = lang_list[0]
uni_lang_set = lang_list[0]

for i in range(1, len(lang_list)):
    all_lang_set = all_lang_set | lang_list[i]
    uni_lang_set = uni_lang_set & lang_list[i]

all_lang_list = list(all_lang_set)
uni_lang_list = list(uni_lang_set)

print(len(uni_lang_list))
for i in range(len(uni_lang_list)):
    print(uni_lang_list[i])

print(len(all_lang_list))
for i in range(len(all_lang_list)):
    print(all_lang_list[i])