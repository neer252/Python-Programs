n=float(input())
tip=input()
tax=input()
totaltip=float(n)*float(float(tip)/100)
totaltax=float(n)*float(float(tax)/100)
totalamount=n+totaltip+totaltax
print int(round(totalamount))
