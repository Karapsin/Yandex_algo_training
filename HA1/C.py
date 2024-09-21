def transform_input(str_input):
    return str_input.replace('+7', '8').replace('-', '').replace(')', '').replace('(', '')

n1 = transform_input(input())
n2 = transform_input(input())
n3 = transform_input(input())
n4 = transform_input(input())

res1 = 'NO'
res2 = 'NO'
res3 = 'NO'

if n2==n1 or ('8495'+n2)==n1 or ('8495'+n1)==n2:
    res1 = 'YES'

if n3 == n1 or ('8495'+n3)==n1 or ('8495'+n1)==n3:
    res2 = 'YES'

if n4==n1 or ('8495'+n4)==n1 or ('8495'+n1)==n4:
    res3 = 'YES'

print(res1)
print(res2)
print(res3)