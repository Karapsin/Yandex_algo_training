input_list = list(map(int, input().split()))
N = input_list[0]
M = input_list[1]
K = input_list[2]

coords_list = list()
n = 0
while n < K:
    coords_list.append(list(map(int, input().split())))
    n = n + 1

grid = list()
for i in range(N):
    grid.append([0] * M)

if K == 0:
    for i in range(len(grid)):
        print(*grid[i])

else:
    n = 0
    for i in range(N):
        for j in range(M):
            if coords_list[n][0] == (i + 1) and coords_list[n][1] == (j + 1):
                grid[i][j] = '*'
                n = n + 1

            if n > (K - 1):
                break
        if n > (K - 1):
            break

    for i in range(N):
        for j in range(M):
            n = 0
            if grid[i][j] != '*':
                if i - 1 >= 0:
                    if j - 1 >= 0 and grid[i - 1][j - 1] == '*':
                        n = n + 1
                    if grid[i - 1][j] == '*':
                        n = n + 1
                    if j + 1 <= (M - 1) and grid[i - 1][j + 1] == '*':
                        n = n + 1

                if j - 1 >= 0 and grid[i][j - 1] == '*':
                    n = n + 1
                if j + 1 <= (M - 1) and grid[i][j + 1] == '*':
                    n = n + 1

                if i + 1 <= (N - 1):
                    if j - 1 >= 0 and grid[i + 1][j - 1] == '*':
                        n = n + 1
                    if grid[i + 1][j] == '*':
                        n = n + 1
                    if j + 1 <= (M - 1) and grid[i + 1][j + 1] == '*':
                        n = n + 1

                grid[i][j] = n

    for i in range(len(grid)):
        print(*grid[i])