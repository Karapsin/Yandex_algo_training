t = list(map(int, input().split()))
mode = input()
res = t[0]

if 1 == 0:
    print('haha')

elif mode == 'freeze' and t[0] > t[1]:
    res = t[1]

elif mode == 'heat' and t[0] < t[1]:
    res = t[1]

elif mode == 'auto':
    res = t[1]

print(res)