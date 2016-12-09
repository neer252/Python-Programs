n= input()
s = set(map(int, raw_input().split()))
k=int(raw_input())
for i in range(0,k):
    lis=raw_input().split(" ")
    print lis
    if lis[0]=="pop":
        s.pop()
    elif lis[0]=="discard":
        s.discard(int(lis[1]))
    elif lis[0]=="remove":
        s.remove(int(lis[1]))

sum1=sum(s)
print sum1
