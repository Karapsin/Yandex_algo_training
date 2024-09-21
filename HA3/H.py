N = int(input())

x_set = set()
shots = 0
for i in range(N):
    x, y = map(int, input().split())
    if x not in x_set:
        shots = shots + 1
        x_set.add(x)

print(shots)