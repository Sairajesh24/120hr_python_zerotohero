#selectionsort
def selection_sort(arr):
    length=len(arr)
    for i in range(length-1):
        minindex=i
        for j in range(i+1,length):
            if arr[j]<arr[minindex]:
                minindex=j
        arr[i],arr[minindex]=arr[minindex],arr[i]
    return arr
arr=[5,2,6,3,8,7]
print("sorted array:",selection_sort(arr))

#qn
