"""
думаю корректнее проверять ab, а не просто а или просто б,
т.е., делать сет из '03', '12', ...
но такое решение не проходит, возможно косяк в тестах

или я мудак
"""

N = int(input())

true_cnt = 0
a_set = set()
for i in range(N):
    a, b = map(int, input().split())

    if (1 == 1
        and (int(a)+int(b))==(N-1)
        and not(a in a_set)
        and int(a)>=0
        and int(b)>=0
       ):
        a_set.add(a)

print(len(a_set))

