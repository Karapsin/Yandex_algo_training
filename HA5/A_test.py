def fast_sol(N, n_colors, M, m_colors):
    n_point = 0
    m_point = 0
    best_res = abs(n_colors[n_point] - m_colors[m_point])
    best_n_point = n_point
    best_m_point = m_point

    while True:
        if n_colors[n_point] < m_colors[m_point]:
            n_point = n_point + 1
        elif n_colors[n_point] > m_colors[m_point]:
            m_point = m_point + 1
        else:
            break

        if n_point > (N - 1) or m_point > (M - 1):
            break

        best_cand = abs(n_colors[n_point] - m_colors[m_point])
        if best_cand < best_res:
            best_res = best_cand
            best_n_point = n_point
            best_m_point = m_point

    return (n_colors[best_n_point], m_colors[best_m_point])

def slow_sol(N, n_colors, M, m_colors):

    best_res = abs(n_colors[0] - m_colors[0])
    best_n = n_colors[0]
    best_m = m_colors[0]
    for n in n_colors:
        for m in m_colors:
            if abs(n-m)<best_res:
                best_res = abs(n-m)
                best_n = n
                best_m = m

    return (best_n, best_m)


import random

proceed = True
count = 0
while proceed:
    N = random.randint(1, 100)
    n_colors = list()
    for _ in range(N):
        n_colors.append(random.randint(1, 100))

    M = random.randint(1, 100)
    m_colors = list()
    for _ in range(M):
        m_colors.append(random.randint(1, 100))

    n_colors = list(set(n_colors))
    m_colors = list(set(m_colors))

    n_colors.sort()
    m_colors.sort()

    N = len(n_colors)
    M = len(m_colors)

    fast_res = fast_sol(N, n_colors, M, m_colors)
    slow_res = slow_sol(N, n_colors, M, m_colors)
    count = count + 1

    if fast_res[0] != slow_res[0] or fast_res[1]!=slow_res[1]:
        break

    print(count)