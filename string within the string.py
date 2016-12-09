s,f,c=raw_input(),raw_input(),0
for p in range(len(s)):
    if(s[p:p+len(f)]==f):
        c+=1
print c
