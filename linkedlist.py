
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        print(self.data)
        print(self.next)
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

    def display(self):
        print("display")
        i=self.head
        while i:
            print(i.data)
            i=i.next        

l=LinkedList()
l.append(1)
l.append(2)
l.append(3)
l.display()