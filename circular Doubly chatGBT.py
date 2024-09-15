class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def create(self):
        size = int(input("Enter the size of the list: "))
        for i in range(size):
            data = int(input("\nEnter the list element: "))
            newnode = Node(data)
            if self.head is None:
                self.head = newnode
                newnode.next = newnode.prev = newnode
            else:
                tail = self.head.prev
                tail.next = newnode
                newnode.prev = tail
                newnode.next = self.head
                self.head.prev = newnode

    def display(self):
        if self.head is None:
            print("List is empty.")
            return
        print("Displaying the elements in the list:")
        temp = self.head
        while True:
            print(temp.data, end=' ')
            temp = temp.next
            if temp == self.head:
                break
        print()  # for a new line after displaying

    def insertatfront(self):
        newnode = Node(int(input("\nEnter the element to insert at the front: ")))
        if self.head is None:
            self.head = newnode
            newnode.next = newnode.prev = newnode
        else:
            tail = self.head.prev
            newnode.next = self.head
            self.head.prev = newnode
            newnode.prev = tail
            tail.next = newnode
            self.head = newnode

    def insertatmiddle(self):
        newnode = Node(int(input("\nEnter the element to insert in the middle: ")))
        pos = int(input("Enter the position: "))
        temp = self.head
        for i in range(1, pos - 1):
            temp = temp.next
            if temp == self.head:
                break
        newnode.next = temp.next
        newnode.prev = temp
        temp.next.prev = newnode
        temp.next = newnode

    def insertatend(self):
        newnode = Node(int(input("\nEnter the element to insert at the end: ")))
        if self.head is None:
            self.head = newnode
            newnode.next = newnode.prev = newnode
        else:
            tail = self.head.prev
            tail.next = newnode
            newnode.prev = tail
            newnode.next = self.head
            self.head.prev = newnode

    def deleteatfront(self):
        if self.head is None:
            print("List is empty.")
        elif self.head.next == self.head:
            self.head = None
        else:
            tail = self.head.prev
            self.head = self.head.next
            self.head.prev = tail
            tail.next = self.head

    def deleteatend(self):
        if self.head is None:
            print("List is empty.")
        elif self.head.next == self.head:
            self.head = None
        else:
            tail = self.head.prev
            tail.prev.next = self.head
            self.head.prev = tail.prev

    def deleteatmiddle(self):
        if self.head is None:
            print("List is empty.")
        else:
            pos = int(input("\nEnter the position to delete: "))
            temp = self.head
            for i in range(1, pos):
                temp = temp.next
                if temp == self.head:
                    break
            if temp == self.head:
                self.deleteatfront()
            else:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev

    def count(self):
        if self.head is None:
            print("Count of elements: 0")
            return
        temp = self.head
        count = 0
        while True:
            count += 1
            temp = temp.next
            if temp == self.head:
                break
        print("Count of elements:", count)

    def search(self):
        item = int(input("Enter an element to search: "))
        if self.head is None:
            print(f"{item} is not present in the list.")
            return
        temp = self.head
        while True:
            if temp.data == item:
                print(f"{item} is present in the list.")
                return
            temp = temp.next
            if temp == self.head:
                break
        print(f"{item} is not present in the list.")

# Main Program Loop
obj = CircularDoublyLinkedList()

while True:
    print("\n\n***CIRCULAR DOUBLY LINKED LIST***\n")
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
