size=input("enter the sizeof array:")
l=[]
for x in range(size):
    l.append(input())
k=input()
print sum(l[:k])


