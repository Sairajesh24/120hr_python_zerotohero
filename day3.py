#list comperehension
'''print([i for i in range(11)])


print([i for i in range(11) if i%2 != 0])

mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print([[j**2 if j%2!=0 else j**3  for j in i] for i in mat])'''

'''mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
result=[]
for row in mat:
    row_data=[]
    for ele in row:
        if ele%2 !=0:
            row_data.append(ele**2)
        else:
            row_data.append(ele**3)
    result.append(row_data)
print(result)'''


