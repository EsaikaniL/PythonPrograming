num=input("enter no of integers:")
l=[]
sum=''
for x in range(0,num):
    l.append(input())
l.sort()
for x in range(-1,-(num+1),-1):
    sum=sum+str(l[x])
print sum
