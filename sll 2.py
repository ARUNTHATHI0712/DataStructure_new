class Node:
    def _init_(self,data):
        self.data=data
        self.next=None

class SLL:
    def _init_(self):
        self.head=None
        self.temp=None
    def creation(self):
        num=int(input("Enter the no of nodes:"))
        for i in range(num):
            data=int(input("Enter the data for nodes:"))
            newnode=Node(data)
            if self.head is None:
                self.head=newnode
                self.temp=newnode
            else:
                self.temp.next=newnode
                self.temp=newnode
    def display(self):
        self.temp=self.head
        while self.temp is not None:
            print(self.temp.data,end="->")
            self.temp=self.temp.next
    def insertAtBegin(self):
        data=int(input("Enter the data:"))
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode
    def insertAtEnd(self):
        data=int(input("Enter the data:"))
        newnode=Node(data)
        self.temp=self.head
        while self.temp.next is not None:
            self.temp=self.temp.next
        self.temp.next=newnode
    def insertAtAnyPosition(self):
        data=int(input("Enter the data:"))
        position=int(input("Enter the position:"))
        newnode=Node(data)
        self.temp=self.head
        for i in range(position-1):
            prev=self.temp
            self.temp=self.temp.next
        newnode.next=self.temp
        prev.next=newnode
linkedlist=SLL()
linkedlist.creation()
linkedlist.display()
linkedlist.insertAtBegin()
linkedlist.display()
linkedlist.insertAtEnd()
linkedlist.display()
linkedlist.insertAtAnyPosition()
linkedlist.display()
