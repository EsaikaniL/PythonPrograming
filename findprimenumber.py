x=input()
y=input()
if x<y:
    for z in range(x+1,y-1):
        if z%2!=0 and z%3!=0 and z%5!=0 and z%7!=0 and z!=1:
            print z
        elif z==2 or z==3 or z==5 or z==7:
            print z
else:
    print("enter the valid range")
