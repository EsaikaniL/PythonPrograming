x1=input("enter the number:")
if x1>0:
    x=str(x1)
    n=len(x)
    z=''
    for y in range(-1,-(n+1),-1):
        z=z+x[y]
    print int(z) 
else:
    print("enter valid number")
