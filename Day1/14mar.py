#list-->ordered-->default index

list1=[]
print(list1,type(list1))


list2=['sai',23,True,30+3j]
print(list2)

#append=extend
#append=adding one element
#extend=adding more than one element
list5=[]
list5.extend([503,4543])
print(list5)
list5.extend([434,988])
print(list5)
list5.insert(0,67)
print(list5)
list5.remove(434)
print(list5)
'''list5.remove(433)-->error
print(list5)'''
print(list5.pop())#pop right side element
print(list5.pop(0))
del list5[1]
print(list5)
