x=raw_input()
y=raw_input()
n1=len(x)
n2=len(y)
count=0
for a in range(0,n1):
    for b in range(0,n2):
        if x[a]==y[b]:
            count+=1
if count!=0:
    print "yes"
else:
    print "no"
