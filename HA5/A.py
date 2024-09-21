N = int(input())

n_colors = list()
n_colors.extend(list(map(int, input().split())))

M = int(input())
m_colors = list()
m_colors.extend(list(map(int, input().split())))

#надо найти максимально близкие N и M
#двигаем тот указатель, у которого значение меньше чем у другого
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

    if n_point>(N-1) or m_point>(M-1):
        break

    best_cand = abs(n_colors[n_point] - m_colors[m_point])
    if best_cand < best_res:
        best_res = best_cand
        best_n_point = n_point
        best_m_point = m_point


print(n_colors[best_n_point], m_colors[best_m_point])