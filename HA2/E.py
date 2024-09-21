size = int(input())
input_list = list(map(int, input().split()))

max_res = input_list[0]
max_res_index = [0]

def is_5_end(input_int):
    if input_int%5==0 and input_int%10!=0:
        return True
    else:
        return False

candidates_index_list = list()
candidates_res_list = list()
for i in range(1, len(input_list)):

    if input_list[i] == max_res:
        max_res_index.append(i)

    if input_list[i]>max_res:
        max_res = input_list[i]
        max_res_index = [i]

    if i<(len(input_list)-1):
        if is_5_end(input_list[i]) and input_list[i]>input_list[i+1]:
            candidates_index_list.append(i)
            candidates_res_list.append(input_list[i])

candidates_res_list_filtered = list()
for i in range(len(candidates_index_list)):
    if candidates_index_list[i] > max_res_index[0]:
        candidates_res_list_filtered.append(candidates_res_list[i])


if len(candidates_res_list_filtered)==0:
    print(0)
else:

    if len(candidates_res_list_filtered)!=1:
        cands_results = candidates_res_list_filtered
        max_res = cands_results[0]
        for i in range(len(cands_results)):
            if cands_results[i]>=max_res:
                max_res = cands_results[i]
    else:
        max_res = candidates_res_list_filtered[0]

    res = len(input_list)
    for i in range(len(input_list)):
        if max_res>=input_list[i]:
            res=res-1


    print(res+1)
