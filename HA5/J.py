#списал из разбора :(
n = int(input())
coords_list = list()
for _ in range(n):
    x, y = map(int, input().split())
    coords_list.append((x, y))

output = 0
for i in range(n):
    used = set()
    neigh = []
    for j in range(n):
        vec_x = coords_list[i][0] - coords_list[j][0]
        vec_y = coords_list[i][1] - coords_list[j][1]

        length = vec_x**2 + vec_y**2
        neigh.append(length)
        if (vec_x, vec_y) in used:
            output = output - 1
        used.add((vec_x, vec_y))

    neigh.sort()
    right = 0
    for left in range(len(neigh)):
        while right < len(neigh) and neigh[left] == neigh[right]:
            right = right + 1
        output = output + right - left - 1

print(output)