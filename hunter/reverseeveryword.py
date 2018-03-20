x=raw_input("enter the string:")
z=x.split()
n=len(z)
b=''
for a in range(0,n):

    y= list(reversed(z[a]))
    b=b+''.join(y)+' '

print b
