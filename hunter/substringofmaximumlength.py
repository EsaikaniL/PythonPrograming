x=raw_input("enter the string:")
n=len(x)
sum=''
y=list(reversed(x))
x1=''.join(y)
if x==x1:
    for a in range(0,n-1):
        sum=sum+x[a]
    print sum
else:
    print x
