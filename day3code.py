#qn1
'''mylist=[9,3,6,1,5,0,8,2,4,7]
list_b=[6,4,6,2,2]
x=[]
for i in list_b:
    for j in range(0,len(mylist)):
        if(mylist[j]==i):
            x.append((i,j))
print(x)

print([(i,mylist.index(i))  for i in list_b])

print(dict((i,mylist.index(i))  for i in list_b))

result={ }
for i in list_b:
    result[i]=mylist.index(i)
print(result)

result={i:mylist.index(i) for i in list_b}
print(result)'''

#qn2
'''sentences=["a new world record was set",
           "in the holy city of ayodhya",
           "on the eve of diwali on tuesday",
           "with over three lakh diya or earthen lamps",
           "lit up simultaneously on the banks of the sarayu river"]
stpwords=['for','a','of','the','was','and','to','in','on','with']
result=[]
for i in sentences:
    row_data=[]
    for word in i.split():
        if word not in stpwords:
            row_data.append(word)
    result.append(row_data)
print(result)'''

#qn3
'''l=[i for i in input().split(',')]
i5=l.index('5')
i8=l.index('8')
ans=sum([int(i) for i in l[:i5]+l[i8+1:]])+int("".join(l[i5:i8+1]))
print(ans)'''


'''num=3,2,6,5,1,4,8,9
x=[]
m=[]
sum=0
for i in range(len(num)):
       if num[i]==5 or num[i]==8:
           x.append(i) #x=[3,6]
for j in range(len(num)):
    if j<x[0]:
        sum+=num[j]
    elif j> x[1]:
        sum+=num[j]
print(sum)
#print(int("".join(num[x[0]:x[1]+1]))+sum)'''

#qn4
'''s=input().split(",")
stt=[]
numm=[]
for i in s:
    s1,n=i.split(":")
    stt.append(s1)
    numm.append(n)
def rotate(ss,n):
    n=str(n)
    s=0
    for i in n:
        s+=int(i)**2
    if s%2==0:
        return ss[-1]+ss[:-1]
    else:
        return ss[2]+ss[:2]
for i in range(len(numm)):
    print(rotate(stt[i],numm[i]))'''

#qn5

n=int(input())
def isprime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True
def hprime(n):
    temp=n
    while(temp>0):
        if n%temp==0:
            if isprime(temp):
                return temp
        temp-=1
sum=0
for i in range(n,n+9):
    sum=sum+hprime(i)
print(sum)

