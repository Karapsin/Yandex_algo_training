def fast_sol(N, K, input_list):
    left = 0
    right = 0
    my_dic = dict()
    uniq_species_num = 0

    best_length = N + 1
    best_length_start = -1
    best_length_end = -1

    while right < N:

        # right expansion
        while right < N:

            current_tree = input_list[right]
            if current_tree not in my_dic:
                my_dic[current_tree] = 0

            if my_dic[current_tree] == 0:
                uniq_species_num = uniq_species_num + 1

            my_dic[current_tree] = my_dic[current_tree] + 1

            if uniq_species_num == K:
                break
            else:
                right = right + 1

        if left == right and K == 1:
            best_length_start = best_length_end = right + 1
            break

        # left shrinking
        if uniq_species_num == K:
            while left < right:
                current_tree = input_list[left]
                removal_tree_num = my_dic[current_tree]

                if (removal_tree_num - 1) > 0:
                    my_dic[current_tree] = my_dic[current_tree] - 1
                    left = left + 1
                else:
                    # best res update
                    if (right - left) < best_length:
                        best_length = right - left
                        best_length_start = left + 1
                        best_length_end = right + 1

                    my_dic[current_tree] = my_dic[current_tree] - 1
                    uniq_species_num = uniq_species_num - 1
                    left = left + 1
                    right = right + 1
                    break
        else:
            break

    return (best_length_start, best_length_end)

def slow_sol(N, K, input_list):
    best_res = N + 1
    best_start = -1
    best_end = -1
    for i in range(K-1, N):
        left = 0
        right = i
        while right < N:
            if len(set(input_list[left:(right+1)])) == K:
                if (right - left) < best_res:
                    best_res = right - left
                    best_start = left + 1
                    best_end = right + 1

            left = left + 1
            right = right + 1

    return  (best_start, best_end)


import random
n = 0
while True:

    N = random.randint(1, 6)
    K = random.randint(1, 3)

    input_list = []
    for _ in range(N):
        input_list.append(random.randint(1, K))

    if len(set(input_list))==K:
        fast = fast_sol(N, K, input_list)
        slow = slow_sol(N, K, input_list)

        if (fast[0]!=slow[0] or fast[1]!=fast[1]):
            print('finish')
            break

        n = n + 1
        print(n)
