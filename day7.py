#stack
'''class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1
    def is_full(self):
        if(self.__top==self.__max_size-1):
            return True
        return False
    def is_empty(self):
        if(self.__top==-1):
            return True
        return False
    def push(self,data):
        if (self.is_full()):
            print("The stack is full")
        else:
            self.__top+=1
            self.__elements[self.__top]=data
    def pop(self):
        if (self. is_empty()):
            print("The stack is empty")
        else:
            data=self.__elements[self.__top]
            self.__top-=1
            return data
    def display(self):
        if(self.is_empty()):
            print("the stack is empty")
        else:
            index=self.__top
            while(index>=0):
                print(self.__elements[index])
                index-=1
    def get_max_size(self):
        return self.__max_size

ball_stack=Stack (4)
print ("Is it empty-", ball_stack.is_empty())
ball_stack.push(5)
print ("Is it empty-", ball_stack.is_empty())
ball_stack.push(6)
ball_stack.push(7)
ball_stack.push(8)
ball_stack.display()
print("size of the stack-", ball_stack.get_max_size())
print ("the elemnt deleted-", ball_stack.pop())
print ("after deleting the element-")
ball_stack.display()
print("size of the stack-", ball_stack.get_max_size())'''

#queue
'''class Queue:
    def __init__ (self, max_size):
        self. __max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self. __front=0
    def is_full (self):
        if self.__rear==self.__max_size-1:
            return True
        return False
    def is_empty (self):
        if(self.__front>self.__rear):
            return True
        return False
    def enqueue (self, data): #100
        if (self.is_full()):
           print ("Queue is full!!!")
        else:
            self.__rear+=1#4
            self.__elements [self.__rear] =data#100
               # [100,200, 300, 400, 500,]
    def dequeue (self):
        if (self.is_empty()):
            print ("Queue is empty!!!") 
        else:
            data=self.__elements [self.__front]
            self.__front+=1
            return data
    def display(self):
        for index in range(self.__front,self.__rear+1):
            print(self.__elements[index])
    def get_max_size(self):
            return self.__max_size
queue1=Queue(4)
print ("Is it full", queue1.is_full())
print ("is it empty", queue1.is_empty())
queue1.enqueue (100)
queue1.display()
queue1.enqueue (200)
queue1.enqueue (300)
queue1.enqueue (400)
queue1.display()
queue1.enqueue (500)'''

#qn1
'''class Queue:
    def __init__ (self, max_size):
        self. __max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self. __front=0
    def is_full (self):
        if self.__rear==self.__max_size-1:
            return True
        return False
    def is_empty (self):
        if(self.__front>self.__rear):
            return True
        return False
    def enqueue (self, data): #100
        if (self.is_full()):
           print ("Queue is full!!!")
        else:
            self.__rear+=1#4
            self.__elements [self.__rear] =data#100
               # [100,200, 300, 400, 500,]
    def dequeue (self):
        if (self.is_empty()):
            print ("Queue is empty!!!") 
        else:
            data=self.__elements [self.__front]
            self.__front+=1
            return data
    def display(self):
        for index in range(self.__front,self.__rear+1):
            print(self.__elements[index])
        def get_max_size(self):
            return self.__max_size
    def check(self,s,e):
        self.count=0
        self.s=s
        self.e=e
        for index in range(self.__front,self.__rear+1):
            for i in range(self.s,self.e+1):
                if self.__elements[index] %i ==0:
                    self.count+=1
                    if self.count==self.e:
                            print(self.__elements[index])
                            self.count=0
                else:
                    break
queue1=Queue(5)
#print ("Is it full", queue1.is_full())
#print ("is it empty", queue1.is_empty())
queue1.enqueue (5040)
#queue1.display()
queue1.enqueue (10080)
queue1.enqueue (7113)
queue1.enqueue (2520)
#queue1.display()
queue1.enqueue (2500)
print("elements are:")
queue1.display()
print("output")
queue1.check(1,10)'''

#or
'''class Queue:
    def _init_(self,max_size):
        self.max_size=max_size
        self.elements=[None]*self.max_size
        self.rear=-1
        self.front=0
    def isempty(self):
        if self.front>self.rear:
            return True
        return False
    def isfull(self):
        if self.rear==self.max_size-1:
            return True
        return False
    def enqueue(self,number):
        if self.isfull():
            print("Queue is full")
        else:
            self.rear+=1
            self.elements[self.rear]=number
            print(number,"is enqueue")
    def dequeue(self):
        if self.empty():
            print("Queue is empty")
        else:
            val=self.elements[self.front]
            self.front+=1
            print(val,"is dequeued")
            return val
    def display(self):
        if self.isempty():
            print("Queue is empty")
        else:
            for i in range(self.front,self.rear+1):
                print(self.elements[i])
q=Queue(4)
q.enqueue(13983)
q.enqueue(10080)
q.enqueue(7113)
q.enqueue(2520)
for i in range(q.front,q.rear+1):
    flag=0
    for j in range(1,11):
        if q.elements[i]%j==0:
            flag+=1
        if flag==10:
            print(q.elements[i])'''

#qn2
'''list1 = ['A', 'app', 'a', 'd', 'ke', 'th', 'doc', 'awa']
list2 = ['y', 'tor', 'e', 'eps', 'ay', None, 'le', 'n']
new_lst1=list2[::-1]
new_list=[]
print(list1+list2)
for i in range(len(list1)):
    if new_lst1[i] is not None:
        new_list.append(list1[i] + new_lst1[i])
    else:
        new_list.append(list1[i])

output = '  '.  join(new_list)
print(output)'''

#qn3-merge two list into  queue.
'''class Queue:
    def __init__(self,max_size):
        self.max_size=max_size
        self.elements=[None]*self.max_size
        self.rear=-1
        self.front=0
    def isempty(self):
        if self.front>self.rear:
            return True
        return False
    def isfull(self):
        if self.rear==self.max_size-1:
            return True
        return False
    def enqueue(self,number):
        if self.isfull():
            print("Queue is full")
        else:
            self.rear+=1
            self.elements[self.rear]=number
            # print(number,"is enqueued")
    def dequeue(self):
        if self.isempty():
            print("Queue is Empty")
        else:
            val=self.elements[self.front]
            self.front+=1
            # print(val,"is dequeued")
            return val
    def display(self):
        if self.isempty():
            print("Queue is empty")
        else:
            for i in range(self.front,self.rear+1):
                print(self.elements[i],end=',')
    def maxsize(self):
        return self.max_size
q1=Queue(3)
q2=Queue(6)
q3=Queue(q1.maxsize()+q2.maxsize())
q1.enqueue(3)
q1.enqueue(6)
q1.enqueue(8)
q2.enqueue('b')
q2.enqueue('y')
q2.enqueue('q')
q2.enqueue('c')
q2.enqueue('h')
q2.enqueue('t')
# print("hi")
while(q1.rear>=q1.front and q2.front<=q2.rear):
    q3.enqueue(q1.elements[q1.front])
    q3.enqueue(q2.elements[q2.front])
    q1.front+=1
    q2.front+=1
    # print(q1.front)
    # print(q2.front)
if q1.isempty():
    if not q2.isempty():
        while(q2.front<=q2.rear):
            q3.enqueue(q2.elements[q2.front])
            q2.front+=1
else:
    if not q1.isempty():
        while(q1.front<=q1.rear):
            q3.enqueue(q1.elements[q1.front])
            q1.front+=1
q3.display()'''

#SLinkedlist
'''class SLinkedList:
    def __init__(self):
        self.headval = None
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval
list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
list.headval.nextval = e2
e2.nextval = e3
list.listprint()'''
