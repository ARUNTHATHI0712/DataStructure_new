class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.temp = None

    def create(self):
        size = int(input("Enter the size of the list: "))
        for i in range(size):
            data = int(input("\nEnter the list element: "))
            newnode = Node(data)
            if self.head is None:
                self.head = newnode
                self.temp = newnode
            else:
                self.temp.next = newnode
                self.temp = newnode

    def display(self):
        self.temp = self.head
        print("Displaying the elements in the list:")
        while self.temp is not None:
            print(self.temp.data, end=' ')
            self.temp = self.temp.next
        print()  # for a new line after displaying

    def insertatfront(self):
        newnode = Node(int(input("\nEnter the element to insert at the front: ")))
        newnode.next = self.head
        self.head = newnode

    def insertatmiddle(self):
        newnode = Node(int(input("\nEnter the element to insert in the middle: ")))
        pos = int(input("Enter the position: "))
        i = 1
        self.temp = self.head
        while i < pos - 1:
            self.temp = self.temp.next
            i += 1
        newnode.next = self.temp.next
        self.temp.next = newnode

    def insertatend(self):
        newnode = Node(int(input("\nEnter the element to insert at the end: ")))
        self.temp = self.head
        while self.temp.next is not None:
            self.temp = self.temp.next
        self.temp.next = newnode
        newnode.next = None

    def deleteatfront(self):
        if self.head is not None:
            self.temp = self.head
            self.head = self.head.next
            del self.temp
        else:
            print("List is empty.")

    def deleteatend(self):
        if self.head is None:
            print("List is empty.")
        if self.temp is not None:
            self.temp = self.head
            self.temp=self.temp.next
            del self.head

    def deleteatmiddle(self):
        pos = int(input("\nEnter the position: "))
        i = 1
        self.temp = self.head
        prev = None
        while i < pos:
            prev = self.temp
            self.temp = self.temp.next
            i += 1
        if prev is None:
            self.head = self.head.next
        else:
            prev.next = self.temp.next
        del self.temp

    def count(self):
        self.temp = self.head
        count = 0
        while self.temp is not None:
            count += 1
            self.temp = self.temp.next
        print("Count of elements:", count)

    def search(self):
        item = int(input("Enter an element to search: "))
        self.temp = self.head
        while self.temp:
            if self.temp.data == item:
                print(f"{item} is present in the list.")
                return
            self.temp = self.temp.next
        print(f"{item} is not present in the list.")

# Main Program Loop
obj = Linkedlist()


print("\n\n***SINGLY LINKED LIST***\n")
print("1. Create")
print("2. Display")
print("3. Insert at front")
print("4. Insert at end")
print("5. Insert at middle")
print("6. Deletion at front")
print("7. Deletion at end")
print("8. Deletion at middle")
print("9. Count the elements")
print("10. Search the element")
print("11. Exit")
while True:
    option = int(input("Enter your choice (1-11): "))
    if option == 1:
        obj.create()
        obj.display()
    elif option == 2:
        obj.display()
    elif option == 3:
        obj.insertatfront()
        obj.display()
    elif option == 4:
        obj.insertatend()
        obj.display()
    elif option == 5:
        obj.insertatmiddle()
        obj.display()
    elif option == 6:
        obj.deleteatfront()
        obj.display()
    elif option == 7:
        obj.deleteatend()
        obj.display()
    elif option == 8:
        obj.deleteatmiddle()
        obj.display()
    elif option == 9:
        obj.count()
    elif option == 10:
        obj.search()
    elif option == 11:
        break
    else:
        print("Invalid choice")
