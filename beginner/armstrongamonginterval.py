x=input()
y=input()
for c in range(x,y):
    a=str(c)
    l=list(reversed(a))

    n=len(a)
    l2=[int(z)**n for z in (l) ]
    b=sum(l2)

    if b==int(a):
        print b
    else:
        pass
