def rect_extend(rect, k):
    ll, ul, ur, lr = rect
    return (ll-k, ul+k, ur-k, lr+k)

def rect_intersect(rect1, rect2):
    ll1, ul1, ur1, lr1 = rect1
    ll2, ul2, ur2, lr2 = rect2

    ll = max(ll1, ll2)
    ul = min(ul1, ul2)
    ur = max(ur1, ur2)
    lr = min(lr1, lr2)

    return (ll, ul, ur, lr)



t, d, n = map(int, input().split())
pos_rect = (0, 0, 0, 0)

for iteration in range(n):
    nav_x, nav_y = map(int, input().split())

    pos_rect = rect_extend(pos_rect, t)
    nav_rect = rect_extend((nav_x+nav_y, nav_x+nav_y, nav_x-nav_y, nav_x-nav_y), d)

    pos_rect = rect_intersect(pos_rect, nav_rect)

res = list()
for diag_up in range(pos_rect[0], pos_rect[1]+1):
    for diag_down in range(pos_rect[2], pos_rect[3]+1):
        if (diag_up + diag_down)%2==0:
            x = int((diag_up + diag_down)/2)
            y = int(diag_up - x)
            res.append((x, y))

print(len(res))
for elem in res:
    print(*elem)