a=str(input("enter the integer"))
n=len(a)
l=list(reversed(a))
l2=[int(x)**n for x in (l) ]
b=sum(l2)
if b==int(a):
    print "yes"
else:
    print "no"
