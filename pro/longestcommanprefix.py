def comp(s1,s2):
    count=0
    if len(s1)<len(s2):
        n=len(s1)
    else:
        n=len(s2)
    for a in range(0,n):
        if s1[a]==s2[a]:
            count+=1
        else:
            break
    return s1[:count]
num=input("enter the no of string:")
l=[]
for x in range(0,num):
    l.append(raw_input())
for x in range(0,num-1):
    
    l[x+1]=comp(l[x],l[x+1])
print l.pop()
