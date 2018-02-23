x=raw_input("enter the string:")
n=len(x)
if n%2==0:
    z=''
    a=0
    for y in range(0,n/2):
        z=z+x[a+1]+x[a]
        a=a+2
    print z
else:
    print "enter the valid string"
