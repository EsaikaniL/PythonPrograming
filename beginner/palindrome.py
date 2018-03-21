x=raw_input("enter the string:")
y=list(reversed(x))
z=''.join(y)
if x==z:
    print "palindrome"
else:
    print "not palindrome"
