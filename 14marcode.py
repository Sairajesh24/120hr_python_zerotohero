# qn1
'''s=input().split()
x=[]
for i in s:
    x.append(len(i))
if len(x)>1:
    print(x)
else:
    x.append(0)
    print(x)'''

'''def fun(str1):
    l_count=0
    d_count=0
    for i in str1:
        if i.isalpha():
            l_count+=1
        elif i.isdigit():
            d_count+=1
        else:
            continue
    return [l_count,d_count]
print(fun('infosys 123'))'''


#qn2
'''lst1 = [item for item in input("Enter the list items : ").split()]
print(lst1)
x=int(input())
count=0
for i in range (0,len(lst1)):
    for j in range (i+1,len(lst1)):
        if (int(lst1[i])+int(lst1[j]))==x:
            count+=1
print(count)'''

#qn3
'''s=input()
if len(s)<2:
    print(-1)
else:
    print(s[0:2]+s[-2:])'''


#qn4

'''s=input()
if len(s)<3:
    print(s)
elif 'ing' in s[-3:]:
    print(s+'ly')
else:
    print(s+'ing')'''

#qn5
'''def eql(n):
    for i in str(n):
            if i not in str(double):
                return False
            else:
                continue
    return True
i=int(input())
double=2*i
if len(str(i))==len(str(double)) and eql(i)==True:
    print(True)
else:
    print(False)'''

#qn6
'''list_of_marks=[12,18,25,24,2,5,18,20,20,21]
def find_more_than_average():
    global list_of_marks
    marks=0
    count=0
    for x in list_of_marks:
        marks+=x
    average=marks/len(list_of_marks)
    for x in list_of_marks:
        if x>average:
            count+=1
    percentage=(count*100)/len(list_of_marks)
    return percentage
def generate_frequency():
    freq=[]
    global list_of_marks
    for x in range(26):
        count=0
        for y in list_of_marks:
            if x == y:
                count+=1
        freq.append(count)
    return  freq
def sort_marks():
    global list_of_marks
    list_of_marks=sorted(list_of_marks)
    return list_of_marks
print(find_more_than_average())
print(generate_frequency())
print(sort_marks())'''

#qn7

'''def translate(dict1,list1):
    list2=[]
    for i in list1:
        list2.append(dict1[i])
    return list2
dict1={"merry":"god","christmas":"jul","and":"och","happy":"goat","new":"nytt","year":"ar"}
list1=["merry","christmas"]
print(translate(dict1,list1))'''

#qn8
n1=int(input())
n2=int(input())
array=[i for i in range(n1,n2+1)]
print(array)
l1=[array[i:j+1] for i in range ]


        
