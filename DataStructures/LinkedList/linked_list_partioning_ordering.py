from SinglyLinkedList import LinkedList

def partition(linked_list, pivot):
    current = linked_list.head
    left_to_pivot = LinkedList()
    right_to_pivot = LinkedList()

    while current is not None:
        if current.data <= pivot:
            if left_to_pivot.head is None:
                left_to_pivot.head = left_to_pivot.tail = current
            else:
                left_to_pivot.tail.next = current
                left_to_pivot.tail = current

        else:
            if right_to_pivot.head is None:
                right_to_pivot.head = right_to_pivot.tail = current
            else:
                right_to_pivot.tail.next = current
                right_to_pivot.tail = current

        # left_to_pivot.print_list()
        right_to_pivot.print_list()
        current = current.next


    return left_to_pivot


if __name__ == "__main__":

    pivot = int(input().strip())

    # CREATING INPUT FOR THE PROBLEM
    linked_list = LinkedList()
    elements = [1,4,3,2,5,2,3]
    # 1. Creating linked list with some nodes
    for n in elements:
        linked_list.append(n)

    left_to_pivot = partition(linked_list, pivot)
    # left_to_pivot.print_list()
    # print(left_to_pivot)
