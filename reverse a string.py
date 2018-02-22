x=raw_input("enter the string:")
n=len(x)
e=''
for  y in range(-1,-(n+1),-1):
    z=x[y]
    e=e+z
print'reversed string = ' +e    
