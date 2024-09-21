n, k = map(int, input().split())
cards_list = list(map(int, input().split()))

cards_dict = dict()
for card in cards_list:
    if card not in cards_dict:
        cards_dict[card] = 0

    cards_dict[card] = cards_dict[card] + 1

cards = sorted(list(cards_dict.keys()))
keys_num = len(cards)

right = 0
output = 0

two_more_cnt = 0
for left in range(keys_num):
    while right < keys_num and cards[left]*k >= cards[right]:
        if cards_dict[cards[right]] >= 2:
            two_more_cnt = two_more_cnt + 1

        right = right + 1

    el_num = right - left
    if cards_dict[cards[left]] >= 2:
        #other_keys_num = right - left - 1
        #output = output + other_keys_num #где ключ первый и второй элемент
        #output = output + other_keys_num #где ключ и второй, и третий элемент
        #output = output + other_keys_num #где ключ первый и третий элемент

        output = output + 3*(el_num - 1)

    if cards_dict[cards[left]] >= 3:
        output = output + 1 #где ключ первый, второй и третий элемент

    output = output + (el_num - 1) * (el_num - 2)*3

    if cards_dict[cards[left]] >= 2:
        two_more_cnt = two_more_cnt - 1

    output = output + two_more_cnt*3


print(int(output))