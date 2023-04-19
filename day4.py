#qn1
'''def nearest_palindrome(n):
    rev=1
    while n>0:
        i=n%10
        rev=rev*10+i
        n=n//10
    return  rev
s=int(input())
x=nearest_palindrome(s+1)
if (s+1==x):
    print(x)
else:
    s+=1
    nearest_palindrome(s+1)'''


'''import sys
def Next_smallest_palindrome(num):
    for i in range(num+1,sys.maxsize):
        if str(i)==str(i)[::-1]:
            return i
print(Next_smallest_palindrome(99))
print(Next_smallest_palindrome(101))'''

#qn2
'''def max_visited_speciality(patient_medical_speciality_list,medical_specialist):
    max_visit=0
    P=patient_medical_speciality_list.count('P')
    E=patient_medical_speciality_list.count('E')
    O=patient_medical_speciality_list.count('O')
    if P>E and P>O:
        speciality=medical_speciality['P']
    elif E>O:
        speciality=medical_speciality['E']
    else:
        speciality=medical_speciality['O']
    return speciality
patient_medical_speciality_list=[301,'E',303,'O',302,'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"Ent"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)'''

#qn3
'''str1=input()
s1=[char for char in str1]
str2=input()
s2=[char for char in str2]
s3=[]
for i in s1:
     for j in s2:
         if j==' ':
             continue
         if j==i:
            if j in s3:
                 continue
            else:
                 s3.append(j)
for i in s3:
    print(i,end='')'''

#qn5
'''class Example:
    def __init__(self,num):
        self.num=num
    def set_num(self,num):
        self.num=num
    def get_num(self):
        return self.num
obj=Example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())'''

#qn6
'''class Customer:
    def __init__(self):
        cust_id = 100
c1=Customer()
print(c1.cust_id)'''      #AttributeError: 'Customer' object has no attribute 'cust_id'

#qn7
'''class Customer:
    def __init__(self,id):
        self.id = 100
c1=Customer(200)
print(c1.id)'''                #100

#qn8
'''class Book:
    def __init__(self):
        self.title=None
my_fav=Book()
my_fav.title="Head First Programming"
your_fav=Book()
your_fav.title="Learning Python"
my_fav.title="you"
print("My Favourite is",my_fav.title)
print("Your's is",your_fav.title)'''

#qn9
class Shoe:
    def __init__(self,price,material):
        self.price=price
        self.material=material

s1=Shoe(1000,"Canvas")
print(s1)
print(s1.price,s1.material)
        
