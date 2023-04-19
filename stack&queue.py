class Queue:
    def __init__(self,max_size):
        self.max_size=max_size
        self.element=[None]*self.max_size
        self.front=0
        self.rear=-1
    def is_empty (self):
        if(self.front>self.rear):
            return True
        return False
    def is_full(self):
        if self.rear==self.max_size-1:
            return True
        return False
    def enqueue(self,data):
        if self.is_full():
            print("queue is full")
        else:
            self.rear+=1
            self.element[self.rear]=data
    def dequeue(self):
            if self.is_full():
                print("queue is full")
            else:
                self.data=self.element[front]
                self.front+=1
    def display(self):
        for index in range(self.front,self.rear+1):
            print(self.element[index])
    def get_max_size(self):
        return self.max_size
queue1=Queue(7)
print ("Is it full", queue1.is_full())
print ("is it empty", queue1.is_empty())
queue1.enqueue (1)
queue1.enqueue (2)
queue1.enqueue (4)
queue1.enqueue (7)
queue1.enqueue (5)
print("even:",end=' ' )
for index in range(queue1.front,queue1.rear+1):
            if queue1.element[index] %2==0:
                print(queue1.element[index],end=' ' )
print("\nodd:",end=' ')
for index in range(queue1.front,queue1.rear+1):
            if queue1.element[index] %2!=0:
                print(queue1.element[index],end=' ' )
