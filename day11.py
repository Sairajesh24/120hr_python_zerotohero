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
    def female_sex(self):
        for index in range(self.front,self.rear+1):
            if 'female' in self.element[index].split("_"):
                print(self.element[index])
    def male_sex(self):
        for index in range(self.front,self.rear+1):
            if 'male' in self.element[index].split("_"):
                print(self.element[index])
queue1=Queue(5)
queue1.enqueue ("sai_20_male")
queue1.enqueue ("turi_22_male")
queue1.enqueue ("ipsa_20_female")
queue1.enqueue ("sandhya_23_female")
queue1.enqueue ("hima_22_male")
queue1.male_sex()
queue1.female_sex()
