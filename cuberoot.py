def iscube(n):
    for ans in range(0, abs(n) + 1):
        if ans ** 3 == abs(n):
            break
    if ans ** 3 != abs(n):
        print n, 'is not a perfect cube!'
        return
    else:
       if n < 0:
           ans = -ans
    return ans
x=input("ENTER THE NUMBER:")
if iscube(x):
    print iscube(x)
