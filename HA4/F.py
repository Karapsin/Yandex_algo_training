import sys
input_list = sys.stdin.read().rsplit()

names_dic = dict()
for i in range(0, len(input_list) - 2, 3):
    name = input_list[i]
    product = input_list[i+1]
    quantity = input_list[i+2]
    if name not in names_dic.keys():
        names_dic[name] = dict()

    if product not in names_dic[name].keys():
        names_dic[name][product] = 0

    names_dic[name][product] = names_dic[name][product] + int(quantity)

names_list = sorted(list(names_dic.keys()))
for name in names_list:
    products_list = sorted(list(names_dic[name].keys()))
    print(name+':')
    for prod in products_list:
        print(prod + ' ' + str(names_dic[name][prod]))