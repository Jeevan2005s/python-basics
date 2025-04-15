
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        i=self.head 
        while i.next:
            i=i.next
        i.next=new_node
    def remove(self,data):
        i=self.head
        j=None
        while i:
            if i.data==data:
                if j:
                    j.next=i.next
                else:
                    self.head=i.next
            p=i
            i=i.next            
    def insert(self,data,pos):
        new_node=Node(data)
        if pos==0:
            new_node.next=self.head
            self.head=new_node
            return
        i=self.head
        for j in range(pos-1):
            i=i.next
        new_node.next=i.next
        i.next=new_node    
    def display(self):
        print("display")
        i=self.head
        while i:
            print(i.data)
            i=i.next 
    def length(self):
        count=0
        i=self.head
        while i:
            i=i.next
            count+=1
        print("length of the linked list is",count)                   

l=LinkedList()
l.append(1)
l.append(2)
l.append(3)
l.display()
l.insert(5,3)
l.display()
l.length()

