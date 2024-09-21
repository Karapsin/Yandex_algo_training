N, K = map(int, input().split())
input_list = list(map(int, input().split()))

if K == 1:
    print(1, 1)
else:
    left = 0
    right = 0
    my_dic = dict()
    uniq_species_num = 0

    best_length = N + 1
    best_length_start = -1
    best_length_end = -1

    while right < N:

        #right expansion
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

        #left shrinking
        if uniq_species_num == K:
            while left<right:
                current_tree = input_list[left]
                removal_tree_num = my_dic[current_tree]

                if (removal_tree_num - 1) > 0:
                    my_dic[current_tree] = my_dic[current_tree] - 1
                    left = left + 1
                else:
                    #best res update
                    if (right - left ) < best_length:
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

    print(best_length_start, best_length_end)
