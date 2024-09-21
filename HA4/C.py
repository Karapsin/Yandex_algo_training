import sys
input_list = sys.stdin.read().rsplit()

word_dic = dict()
for word in input_list:
    if word not in word_dic:
        word_dic[word] = 0
    word_dic[word] = word_dic[word] + 1

my_keys = list(word_dic.keys())
max_key = [my_keys[0]]
for key in my_keys:
    if word_dic[key]>word_dic[max_key[0]]:
        max_key = [key]
    elif word_dic[key]==word_dic[max_key[0]]:
        max_key.append(key)

print(sorted(max_key)[0])