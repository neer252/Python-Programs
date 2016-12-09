count=0
n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
a = map(int,raw_input().strip().split(' '))
for i in range(0,n):
    for j in range (i+1,n):
        if i<j and a[i]+a[j]%  k==0:
            count=count+1
print count
