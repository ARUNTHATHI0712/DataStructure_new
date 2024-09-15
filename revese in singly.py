class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class Linked_list:
    def __init__(self):
        self.head=None
    
    def printLL(self):
        if self.head is  None:
            print("linked list is empty")
        else:
            n=self.head
            while(n is not None):
                print(n.data,end="-->")
                n=n.ref
    def add_begin(self,data):
        newnode=Node(data)
        newnode.ref=self.head
        self.head=newnode
   
        
    
    def reverse_print(self):
        nodes=[]
        n=self.head
        while n is not None:
            nodes.append(n.data)
            n=n.ref
        l=len(nodes)-1
        for i in range (l, -1, -1):
            print(nodes[i],end="-->")
            
            
        




            

LL=Linked_list()
LL.add_begin(10)
LL.add_begin(20)
LL.add_begin(30)
LL.add_begin(40)

LL.printLL()
print()
print("reversed LL:")
LL.reverse_print()
