class Node:
    def __init__(self,coeff,expo):
        self.coeff=coeff
        self.expo=expo
        self.next=None

class polynomial_list:
    def __init__(self):
        self.head=None
        self.tail=None

    def insert(self,coeff,expo):
        NewNode=Node(coeff,expo)
        if self.head is None:
            self.head=NewNode
            self.tail=NewNode
        else:
            if self.head.expo<expo:
                NewNode.next=self.head
                self.head=NewNode
            elif self.tail.expo>expo:
                self.tail.next=NewNode
                self.tail=NewNode
            else:
                temp=self.head
                prev=None
                while (temp!=None and temp.expo>expo):
                    prev=temp
                    temp=temp.next
                if (temp.expo==expo):
                    temp.coeff += coeff
                else:
                    prev.next=NewNode
                    NewNode.next=temp
    def display(self):
        temp=self.head
        while(temp):
          print(temp.coeff,'x',temp.expo,end='+')
          temp=temp.next

v=polynomial_list()
for i in range(3):
    coeff,expo=map(int,input().split())
    v=insert(coeff,expo)
v.display

def add(temp1,temp2):
         adob=polynomial_list()
         while (temp1 and temp2):
             if temp1.expo==temp2.expo:
                 adob.insert(temp1.coeff,temp2.coeff,temp1.expo)
                 temp1=temp1.next
                 temp2=temp2.next
             elif temp1.expo>temp2.expo:
                 adob.insert(temp1.coeff,temp1.expo)
                 temp1=temp1.next
             else:
                adob.insert(temp2.coeff,temp.expo)
                temp2=temp2.next
         while (temp1):
            adob.insert(temp1.coeff,temp1.expo)
            temp1=temp1.next
         while (temp2):
            adob.insert(temp2.coeff,temp2.expo)
            temp2=temp2.next
            adob.dispaly()

def  eval(temp,val):
         s=0
         while(temp):
             s=s+temp.coeff*value**temp.expo
             temp=temp.next
             print(s)
             eval(v.head)
            
            
        
