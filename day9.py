#double linkedlist
'''class Node:
    def __init__(self,value):
        self.previous=None
        self.data=value
        self.next=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    def isEmpty(self):
        if self.head is None:
            return True
        return False
    def length(self):
        temp=self.head
        count=0
        while temp is not None:
            temp = temp.next
            count+=1
        return count
    def insertAtBeginning(self,value):
        new_node = Node(value)
        if self.isEmpty():
            self.head=new_node
        else:
            new_node.next = self.head
            self.head.previous= new_node
            self.head=new_node
    def insertAtEnd(self,value):
        new_node=Node(value)
        if self.isEmpty():
            self.insertAtBeginning(value)
        else:
            temp=self.head
            while temp.next is not None:
                temp = temp.next
            temp.next=new_node
            new_node.previous=temp
    def insertAtPosition(self,value,position):
        temp = self.head
        count = 0
        while temp is not None:
            if count==position-1:
                break
            count+=1
            temp = temp.next
        if position == 1:
            self.insertAtBeginning(value)
        elif temp is None:
            print("There are less than {}-1 elements in the linkedlist.Cannot insert at {} position.".format(position, position))
        elif temp.next is None:
            self.insertAtEnd(value)
        else:
            new_node = Node(value)
            new_node.next=temp.next
            new_node.previous=temp
            temp.next.previous=new_node
            temp.next = new_node
    def deleteFromPosition(self,position):
        if self.isEmpty():
            print("Linked List is empty. cannot delete elements")
        elif(position==1):
            self.deleteFromBeginning()
        else:
            temp=self.head
            count=1
            while temp is not None:
                if count==position:
                    break
                temp=temp.next
                count+=1
            if temp is None:
                    print("There are less than {} elements in the linked list.cannot delete element.".format(position))
                    return
            elif temp.next is None:
                    self.deletionFromLast()
                    return
            temp.previous.next=temp.next
            temp.next.previous=temp.previous
            temp.next=None
            temp.Previous=None
    def deleteFromBeginning(self):
         if self.isEmpty():
             print("Linked List is empty.Cannot delete elements.")
         elif self.head.next is None:
             self.head=None
         else:
             self.head = self.head.next
             self.head.previous = None
    def deletionFromLast(self):
        if self.isEmpty():
            print("Linked List is empty.Cannot delete elements")
        elif self.head.next is None:
            self.head=None
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.previous.next = None
            temp.previous = None
    def printLinkedList(self):
        temp = self.head
        while temp is not None:
            print(temp.data,sep=" ")
            temp=temp.next
   
x = DoublyLinkedList()
print(x.isEmpty())
x.insertAtEnd(5)
#x.printLinkedList()
x.insertAtEnd(15)
x.insertAtEnd(25)
x.insertAtEnd(35)
x.printLinkedList()
print("no of nodes",x.length())
x.deleteFromBeginning()
x.deleteFromPosition(3)
x.printLinkedList()'''

#postfix evaluation
class Evaluate:
    def __init__(self,capacity):
        self.top=-1
        self.capacity=capacity
        self.array=[]
    def isEmpty(self):
        return True if self.top==-1 else False
    def peek(self):
        return self.array[-1]
    def pop(self):
        if not self.isEmpty():
            self.top-=1
            return self.array.pop()
        else:
            return  "$"
    def push(self,op):
        self.top+=1
        self.array.append(op)
    def evaluatePostfix(self,exp):
        for i in exp:
            if i.isdigit():
                self.push(i)
            else:
                val1=self.pop()
                val2=self.pop()
                self.push(str(eval(val2 + i +val1)))
        return int (self.pop())

exp = "231*+9-"
obj=Evaluate(len(exp))
print("postfix evaluation: %d" %(obj.evaluatePostfix(exp)))
        
                    
