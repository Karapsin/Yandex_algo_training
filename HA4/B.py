import sys
input_list = sys.stdin.read().rsplit()

word_dic = dict()
output_list = list()
for word in input_list:
    if word not in word_dic:
        output_list.append(0)
        word_dic[word] = 0
    else:
        word_dic[word] = word_dic[word] + 1
        output_list.append(word_dic[word])

print(*output_list)