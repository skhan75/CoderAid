class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.previous = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def remove(self, node_value):
        current = self.head

        # if element is presnt at the head
        if node_value == current.data:
            removed = current.data
            self.head = current.next
            current.next.previous = None
            current = None

        # else
        while current is not None:
            current = current.next
            if current.data == node_value:
                removed = current.data
                current.previous.next = current.next
                current.next.previous = current .previous
                current = None

        return removed

    def size(self):
        return self.size

    # Print the List
    def print_list(self):
        temp = self.head
        while temp:
            print (temp.data, end=" --> ")  # Printing the list in the same line
            temp = temp.next
        print (None)


if __name__  == "__main__":
    d = DoublyLinkedList()
    d.push(1)
    d.push(3)
    d.print_list()
    print ('Removed', d.remove(1))
    d.print_list()
