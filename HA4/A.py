n = int(input())

syn_dic = dict()
for i in range(n):
    w1, w2 = input().split()
    syn_dic[w1] = w2
    syn_dic[w2] = w1

input_word = input()

print(syn_dic[input_word])

