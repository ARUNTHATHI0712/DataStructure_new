class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class DLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert_end(self,data):
        NewNode=Node(data)
        if (self.head is None):
            self.head=NewNode
            self.tail  =NewNode
        else:
            self.tail.next=NewNode
            NewNode.Prev=self.tail
            self.tail=NewNode
    def insert_begin(self,data):
        NewNode=Node(data)
        if (self.head is None):
            self.head=None
            self.tail  =None
        else:
            NewNode.Next=self.head
            self.head.prev=NewNode
            self.head=NewNode
    def insert_position(self,pos,data):
        NewNode=Node(data)
        if (self.head is None):
            self.head=None
            self.tail  =None
        else:
            temp=self.head
            c=0
            while(temp.next!=None):
                if(c==pos-1):
                    break
                temp=temp.next
                c=c+1
            NewNode.next=temp.next
            NewNode.Prev=temp
            temp.next=NewNode
            NewNode.next.Prev=NewNode
    def Display(self):
            temp=self.head
            while(temp.next!=None):
                print(temp.data,end='->')
                temp=temp.next

Doubly= DLL( )
Doubly.insert_end(10)
Doubly.insert_end(12)
Doubly.insert_end(14)
Doubly.Display()
            
            
        
        
