# Node Class --> The Node is where data is stored in the Linked List>
# Along with data each node also holds a pointer, which is a reference to the next node in the list
from __future__ import print_function
class Node:

    # Initializing Node object
    def __init__(self, data=None):
        self.data = data    # Assign Data
        self.next = None    # Initialize next as null


# Linked List Class
class LinkedList:

    # Linked List class contains a Node object
    def __init__(self):
        self.head = None
        self.tail = None

    # Adding element to the end of the list
    def append(self, data):
        node = Node(data)
        if not self.head:                   # If there is no head or list is empty
            self.head = self.tail = node    # Add data as head to the list
        else:
            self.tail.next = node           # Else add after the tail
        self.tail = node                    # and initialize the new node as the tail

    # Inserting element in the middle at specified position (pos)
    def insert(self, data, pos):
        node = Node(data)
        current = self.head
        count = 1

        while count < pos:                  # Iterate till we reach the desired position
            current = current.next
            count += 1

        node.next = current.next            # Add element after pos
        current.next = node

    # Adding element to the head of the list
    def add_first(self, data):
        node = Node(data)

        if not self.head and not self.tail:
            self.head = self.tail = node
        else:
            node.next = self.head           # Original head replaced by the new head node
            self.head = node                # New node is initialized as the new Head

    # Searching an element in the list
    def search(self, e):
        current = self.head
        count = 1                           # Keeping a counter to return position of searched element

        while current is not None:
            if e == current.data:
                return count
            else:
                current = current.next
                count += 1
        if current is None:
            raise ValueError("Data not in the List")

    # Removing an element from the list
    def remove(self, e):                    # e is the element to be removed
        if not self.head:
            pass
        current = self.head
        previous = None

        # Removing when the element is present at the head of the list
        if e == current.data:
            removed = e
            self.head = current.next
            current = None

        # Removing when element is present elsewhere
        while current is not None:          # Iterate till element is found in the list
            previous = current
            current = current.next
            if current.data == e:
                removed = e
                previous.next = current.next # When found make the prevous element point to next
                current = None               # And remove the current element
        return removed

    # Removing duplicates
    def remove_duplicates(self):
        if self.head is None:
            return

        current = self.head
        seen = set([current.data])

        while current.next:
            if current.next.data in seen:
                current.next = current.next.next
            else:
                seen.add(current.next.data)
                current = current.next


    # Reversing a Linked List without creating a new list
    def reverse_list(self):
        prev = None
        current = self.head                 # Intialize current as the head

        while current is not None:          # Traverse till the end of the list
            next =  current.next
            current.next = prev             # Remove the old link and add a new next link to previous element
            prev = current
            current = next
        self.head = prev                    # Initialize the last element of the original list as the new head

    # Returns the current size of the list
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    # Detects loop in the linked List
    def detect_loop(self):
        fast = slow = self.head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast is slow:
                break

        if fast is None and fast.next is None:
            return None

        while fast is not slow:
            fast = fast.next
            slow = slow.next

        return fast

    # Checks whether list is empty
    def is_empty(self):
        return self.head == None

    # Print the List
    def print_list(self):
        temp = self.head
        while temp:
            print (temp.data, end=" --> ")  # Printing the list in the same line
            temp = temp.next
        print (None)

if __name__ == "__main__":

    l = LinkedList()
    elems = [1,2,3,4,5,6,3,4]

    for e in elems:
        l.append(e)


    l.insert(9,3)
    l.insert(10,4)
    l.insert(7,5)
    l.print_list()
    print("Size: ",l.size(),'\n')

    l.add_first(11)
    l.add_first(8)
    l.print_list()
    print("Size: ",l.size(), '\n')

    print("Element found at: ",l.search(2), '\n')

    print ("Removed element: ",l.remove(11), '\n')
    l.print_list()
    print("Size: ", l.size(), '\n')

    l.remove_duplicates()
    l.print_list()

    l.reverse_list()
    l.print_list()

    l.detect_loop()
