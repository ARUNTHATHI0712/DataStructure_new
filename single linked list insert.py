class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def Insert_End(self,val):
        NewNode = Node(val)
        if self.head is None:
            self.head = NewNode
            self.tail=self.head
        else:
            self.tail.next=NewNode
            self.tail=NewNode
    def Display(self):
        temp=self.head
        while(temp!=None):
            print(temp.value,end='->')
            temp=temp.next

Singly= LinkedList( )
Singly.Insert_End(10)
Singly.Insert_End(12)
Singly.Insert_End(14)
Singly.Display()
