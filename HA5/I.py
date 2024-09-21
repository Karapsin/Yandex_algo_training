K = int(input())
input_str = input()

same_length_ways = 0
output = 0

for i in range(K, len(input_str)):
    if input_str[i] == input_str[i-K]:
        same_length_ways = same_length_ways + 1
        output = output + same_length_ways
    else:
        same_length_ways = 0

print(output)