N = int(input())
my_dic = dict()

for i in range(N):

    w, h = map(int, input().split())
    if w not in my_dic.keys():
        my_dic[w] = -1

    if h > my_dic[w]:
        my_dic[w] = h

my_keys = list(my_dic.keys())
res = 0
for key in my_keys:
    res = res + my_dic[key]

print(res)