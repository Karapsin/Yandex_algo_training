N = int(input())
input_list = list(map(int, input().split()))

true_chain_start = 0
opposite = N-1
for i in range(N):
    if input_list[i]!=input_list[opposite]:
        true_chain_start = i+1
        opposite = N-1

    elif input_list[i]==input_list[opposite]:
        opposite = opposite-1

if true_chain_start>=(N-1):
    extra = input_list[:(N-1)]
    extra.reverse()
    print(N-1)
    print(*extra)
else:
    extra = input_list[:true_chain_start]
    extra.reverse()
    print(true_chain_start)
    if true_chain_start!=0:
        print(*extra)