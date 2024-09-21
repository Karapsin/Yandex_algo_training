n1 = int(input())
n2 = int(input())
n3 = int(input())

res='YES'

if(1==0
     or (n1+n3)<=n2
     or (n1+n2)<=n3
     or (n2+n3)<=n1
):
    res = 'NO'

print(res)