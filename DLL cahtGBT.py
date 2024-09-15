class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None  # Pointer to the previous node
        self.next = None  # Pointer to the next node

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def create(self):
        size = int(input("Enter the size of the list: "))
        for i in range(size):
            data = int(input("\nEnter the list element: "))
            newnode = Node(data)
            if self.head is None:
                self.head = self.tail = newnode
            else:
                newnode.prev = self.tail
                self.tail.next = newnode
                self.tail = newnode

    def display(self):
        print("Displaying the elements in the list:")
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next
        print()  # for a new line after displaying

    def insertatfront(self):
        newnode = Node(int(input("\nEnter the element to insert at the front: ")))
        if self.head is None:
            self.head = self.tail = newnode
        else:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode

    def insertatmiddle(self):
        newnode = Node(int(input("\nEnter the element to insert in the middle: ")))
        pos = int(input("Enter the position: "))
        if pos == 1:
            self.insertatfront()
        else:
            current = self.head
            for i in range(1, pos - 1):
                if current is not None:
                    current = current.next
            if current is None or current.next is None:
                self.insertatend()
            else:
                newnode.next = current.next
                newnode.prev = current
                current.next.prev = newnode
                current.next = newnode

    def insertatend(self):
        newnode = Node(int(input("\nEnter the element to insert at the end: ")))
        if self.head is None:
            self.head = self.tail = newnode
        else:
            self.tail.next = newnode
            newnode.prev = self.tail
            self.tail = newnode

    def deleteatfront(self):
        if self.head is None:
            print("List is empty.")
        else:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None

    def deleteatend(self):
        if self.head is None:
            print("List is empty.")
        else:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None

    def deleteatmiddle(self):
        pos = int(input("\nEnter the position to delete: "))
        if self.head is None:
            print("List is empty.")
        elif pos == 1:
            self.deleteatfront()
        else:
            current = self.head
            for i in range(1, pos):
                if current is not None:
                    current = current.next
            if current is None or current == self.tail:
                self.deleteatend()
            else:
                current.prev.next = current.next
                current.next.prev = current.prev
                del current

    def count(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        print("Count of elements:", count)

    def search(self):
        item = int(input("Enter an element to search: "))
        current = self.head
        while current:
            if current.data == item:
                print(f"{item} is present in the list.")
                return
            current = current.next
        print(f"{item} is not present in the list.")

# Main Program Loop
obj = DoublyLinkedList()

while True:
    print("\n\n***DOUBLY LINKED LIST***\n")
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
