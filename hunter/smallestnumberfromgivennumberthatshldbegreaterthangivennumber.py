x=str(input("enter the number:"))
y=list(x)
sum=''
y.sort()
sum=sum+y.pop()
n=len(y)
for a in range(0,n):
    sum=sum+y[a]
if int(x)<int(sum):
    print sum
else:
    print "impossible"
