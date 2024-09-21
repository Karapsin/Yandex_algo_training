file_input = open('input.txt', 'r')

n, C, D = file_input.readline().strip().split()
n = int(n)
keywords = set()
for i in range(int(n)):
    key = file_input.readline().strip()

    if C == 'no':
        key = key.lower()

    if key not in keywords:
        keywords.add(key)


ids_dict = dict()
for line in file_input.readlines():
    word_line= line
    filtered_line = str()
    for i in range(len(word_line)):
        if word_line[i].isnumeric() or word_line[i].isalpha() or word_line[i] == '_':
            filtered_line = filtered_line + word_line[i]
        else:
            filtered_line = filtered_line + ' '

    word_list = filtered_line.split()
    for word in word_list:

        if ((D=='yes') or (D=='no' and word[0].isalpha())) and not(word.isdigit()):
            if C == 'no':
                standard_word = word.lower()
            else:
                standard_word = word

            if standard_word not in keywords and standard_word not in ids_dict.keys():
                ids_dict[standard_word] = 0
            if standard_word not in keywords:
                ids_dict[standard_word] = ids_dict[standard_word] + 1


ids_list = list(ids_dict.keys())
max_id = ids_list[0]
max_id_index = 0
for i in range(1, len(ids_list)):
    if ids_dict[ids_list[i]]>ids_dict[ids_list[max_id_index]]:
        max_id = ids_list[i]
        max_id_index = i

print(max_id)