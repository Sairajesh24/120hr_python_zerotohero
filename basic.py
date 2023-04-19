#datatypes

'''name="sai"
print("name",name,type(name))
mark=98.8
print("mark",mark,type(mark))
complexno=36+1j
print("complexno",complexno,type(complexno))'''



'''i=int(input())
if (i%3==0 & i%5==0):
    print("divisible by both")
elif(i%3==0):
    print("divisible by 3")
elif(i%5==0):
    print("divisible by 5")
else:
    print("invalid")'''

'''for i in range (100,0,-1):
    print(i,end=' ')
print()'''

#break
'''for i in range (100):
    if(i==50):
        pass
    print(i)
else:
        print("else")'''

'''def function(num1,num2):
    return type(num1),type(num2)
print(function(10,11.1))



def fun(name,roll,branch,coll="giet"):
    print(coll,name,roll,branch)
fun("sai",256,"cse")'''

'''def add(*var):
    sum=0
    for i in var:
        sum+=i
    print(sum)
add(10,20,30)'''

'''def mul(*var):
    product=1
    a=[]
    d=0
    for i in var:
        a.append(i)
    b=a[::-1]
    for j in b:
        if b[0]==7:
            d+=1
            break
        elif(j==7):
            break
        else:
            product*=j
    if (d==1):
        print(-1)
    else:
        print(product)
mul(4,7,4)'''

'''currency=input("currency name:")
price=float(input("how much:"))

if(currency=="Euro"):
    print(price*0.01417)
elif(currency=="British Pound"):
    print(price*0.0100)
elif(currency=="Australlian Dollar"):
    print(price*0.02140)
elif(currency=="Canadian Dollar"):
    print(price*0.02027)
else:
    print("-1")'''

'''adult=int(input("number of adults:"))
child=int(input("number of child:"))
x=adult*37550.0+child*(37550.0/3)
y=x*0.07
z=(x+y)-0.1*(x+y)
print("Total Ticket cost:",z)'''

rupee1=int(input("number of 1 rupee coins availabale:"))
rupee5=int(input("number of 5 rupee coins availabale:"))
neededamount=int(input("Amount to be made Rs:"))

def mincoin(rupee5,rupee1,neededamount):
    if (5*rupee5+rupee1<neededamount):
        print(-1)
    else:
        n1=neededamount//5
        n2=neededamount%5
        print("Rs.1 coin needed:",n2)
        print("Rs.5 coin needed:",n1)

mincoin(rupee5,rupee1,neededamount)
    
    


