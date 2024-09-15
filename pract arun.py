class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
    def Insert_End(self,val):
        NewNode=Node(val)
        if self.head is None:
            self.head=NewNode
            self.tail=self.head
        else:
            self.tail.next=NewNode
            self.tail=NewNode

    def display(self):
        temp=self.head
        while(temp!=None):
            print(temp.value,end=" ")
            temp=temp.next

singly=linkedlist()
singly.Insert_End(12)
singly.display()
        
            
