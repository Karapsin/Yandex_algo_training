N = int(input())
prev_x, prev_y = map(int, input().split())
up_list = [0]
down_list = [0]
for _ in range(1, N):
    x, y = map(int, input().split())
    change = y - prev_y
    if change>=0:
        up_list.append(up_list[-1]+change)
        down_list.append(down_list[-1])
    else:
        up_list.append(up_list[-1])
        down_list.append(-change+down_list[-1])
    prev_y = y

for _ in range(int(input())):
    start, end = map(lambda x: int(x) - 1, input().split())
    if start < end:
        print(up_list[end] - up_list[start])
    else:
        print(down_list[start] - down_list[end])