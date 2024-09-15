class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def add_to_empty(self, data):
        if self.head is not None:
            return
        new_node = Node(data)
        self.head = new_node
        self.head.next = self.head

    def add_to_begin(self, data):
        if self.head is None:
            self.add_to_empty(data)
            return
        new_node = Node(data)
        new_node.next = self.head.next
        self.head.next = new_node

    def add_to_end(self, data):
        if self.head is None:
            self.add_to_empty(data)
            return
        new_node = Node(data)
        new_node.next = self.head.next
        self.head.next = new_node
        self.head = new_node

    def traverse(self):
        if self.head is None:
            print("Circular linked list is empty")
            return
        current = self.head.next
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head.next:
                break
        print()

cll = CircularLinkedList()
cll.add_to_empty(10)
cll.add_to_begin(20)
cll.add_to_end(30)
cll.add_to_end(40)

print("Circular Linked List:")
cll.traverse()
