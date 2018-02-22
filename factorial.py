x=input("enter the number:")
if x>=0:
    z=1
    for y in range(1,x+1):
        z=z*y
    print 'factorial of the given number is ' + str(z) 
else:
        print 'enter the valid number'
