#Linear search in Python
'''def linearsearch(array,n,x):
    #Going through array subsequently
    for i in range(0,n):
        if(array[i] == x):
            return i
    return -1

array=[2,4,0,1,9]
x=1
n=len(array)
result = linearsearch(array,n,x)
if (result == -1):
    print("Element not found")
else:
    print("Element found at index:",result)'''


#Binary search
'''def binarySearch(array,x,low,high):
    while low<=high:
        mid = low+(high-low)//2
        if array[mid]==x:
            return mid
        elif array[mid]<x:
            low=mid+1
        else:
            high = mid+1
    return -1
array=[2,3,4,5,6,7,8,9]
x=4
high=len(array)-1
result=binarySearch(array,x,0,high)
if (result == -1):
    print("Element not found")
else:
    print("Element found at index:",result)'''

#Binary Tree
'''class Node:
    def __init__(self,item):
        self.left=None
        self.right=None
        self.val = item
def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.val) + "->", end=' ')
        inorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.val) + "->", end=' ')
def preorder(root):
    if root:
        print(str(root.val) + "->", end=' ')
        preorder(root.left)
        preorder(root.right)
root = Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(4)
print("inorder traversal")
inorder(root)
print("\npreorder traversal")
preorder(root)
print("\ninorder traversal")
postorder(root)'''

#Binary Search Tree operations in Python
class Node:
    def __init__(self, key):
        self.left = None
        self.key = key
        self.right = None
    
    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(str(root.key) + ">", end=' ')
            self.inorder(root.right)
    
    def Insert(node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = Node.Insert(node.left, key)
        else:
            node.right = Node.Insert(node.right, key)
        return node

