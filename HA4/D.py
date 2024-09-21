n = int(input())
input_n = list(map(int, input().split()))
k = int(input())
input_k = list(map(int, input().split()))

press_key_dic = dict()
for i in range(k):
    key = input_k[i]
    if key not in press_key_dic.keys():
        press_key_dic[key] = 0
    press_key_dic[key] = press_key_dic[key] + 1

for i in range(n):
    if press_key_dic[i+1]<=input_n[i]:
        print('NO')
    else:
        print('YES')