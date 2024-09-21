input_str1 = input()
input_str2 = input()

genes_list1 = list()
for i in range(1, len(input_str1)):
    genes_list1.append(input_str1[i-1]+input_str1[i])

genes_list2 = list()
for i in range(1, len(input_str2)):
    genes_list2.append(input_str2[i-1]+input_str2[i])

uniq_genes = set()
for i in range(len(genes_list2)):
    if not(genes_list2[i] in uniq_genes):
        uniq_genes.add(genes_list2[i])

index = 0
for i in range(len(genes_list1)):
    if genes_list1[i] in uniq_genes:
        index = index + 1

print(index)