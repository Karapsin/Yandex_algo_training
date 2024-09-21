a = int(input())
b = int(input())
c = int(input())

res = 'NO SOLUTION'

if c>=0 and a!=0:
    x = ((c**2)-b)/a
    if (a*x+b)>=0 and x.is_integer():
        res = int(x)
elif c>=0 and a==0 and (c**2)==b:
    res = 'MANY SOLUTIONS'


print(res)
