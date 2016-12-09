n, m = raw_input("ENTER THE NO OF ELEMENTS IN ARRAY AND SETS:").split(" ")
arr = [int(x) for x in raw_input("ENTER THE VALUES FOR ARRAY:").split()]
A = set([int(y) for y in raw_input("ENTER THE VALUES FOR SET A:").split()])
B = set([int(z) for z in raw_input("ENTER THE VALUES FOR SET B:").split()])
count = [1 if x in A else -1 if x in B else 0 for x in arr]#sets are disjoint
print "HAPPINESS:" ,sum(count)
