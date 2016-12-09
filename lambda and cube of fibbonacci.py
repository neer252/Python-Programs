cube=lambda a:a*a*a
n=input("enter the limit:")
c,d,e=0,1,0
lis=[]
for i in range(n):
    if i<=1:
        e=i
    else:
        e=c+d
        c=d
        d=e
    lis.append(e)
print map(cube,lis)
