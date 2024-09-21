def DEPOSIT(acc_dic, name, sum):
    if name not in acc_dic.keys():
        acc_dic[name] = 0

    acc_dic[name] = acc_dic[name] + sum

    return acc_dic

def WITHDRAW(acc_dic, name, sum):
    return DEPOSIT(acc_dic, name, -sum)

def BALANCE(acc_dic, name):
    if name not in acc_dic.keys():
        print('ERROR')
    else:
        print(int(acc_dic[name]))

def TRANSFER(acc_dic, name1, name2, sum):

    acc_dic = WITHDRAW(acc_dic, name1, sum)
    return DEPOSIT(acc_dic, name2, sum)

def INCOME(acc_dic, p):
    clients_list = list(acc_dic.keys())
    for client in clients_list:
        if acc_dic[client]>0:
            acc_dic[client] = acc_dic[client] + int(acc_dic[client]*((p/100)))

    return acc_dic

import sys
acc_dic = dict()
for line in sys.stdin.read().rsplit('\n'):

    if line == '':
        break

    input_list = line.split()

    if input_list[0]=='DEPOSIT':
        acc_dic = DEPOSIT(acc_dic, input_list[1], int(input_list[2]))

    elif input_list[0] == 'WITHDRAW':
        acc_dic = WITHDRAW(acc_dic, input_list[1], int(input_list[2]))

    elif input_list[0] == 'BALANCE':
        BALANCE(acc_dic, input_list[1])

    elif input_list[0] == 'TRANSFER':
        acc_dic = TRANSFER(acc_dic, input_list[1], input_list[2], int(input_list[3]))

    elif input_list[0] == 'INCOME':
        acc_dic = INCOME(acc_dic, int(input_list[1]))