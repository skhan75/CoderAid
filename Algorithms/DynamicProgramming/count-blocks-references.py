#
# You are given a doubly linked list and an array of references to nodes on the linked list.
# How many "blocks" are there present in the linked list? A "block" is defined as a group of
# nodes on the list with references directed at them and adjacent to eachother.

# For example

# [node #0] -><-[node#1] -><-[node#2] -><-[node#3]

# node[] nodes = {ref_to_node#0, ref_to_node#2, ref_to_node#3};

# Is two blocks because the first block is at node #0.
# Node #1 has no incomming reference. Node #2 and Node #3 have references are are adjacent so it's just one block.

# Implement using JAVA: Hint: You can try using a HashMap.
#

from DoublyLinkedList import LinkedList

def count_blocks(linked_list, references):
    s = set()
    block_count = 0
    for i in range(len(references)):
        block_count += 1
        if references[i].previous in s or references[i].next in s :
            block_count -= 1
        s.add(references[i])

    return block_count


if __name__ == "__main__":
    # CREATING INPUT FOR THE PROBLEM
    linked_list = LinkedList()
    elements = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    # 1. Creating linked list with some nodes
    for n in elements:
        linked_list.push(n)
    # User Input
    inputs = [1,4,3,5,6,10] # --> 3 block
    # 2. Creating node of references from inputs
    current = linked_list.head
    references = []

    while current is not None:
        if current.data in inputs:
            references.append(current)
        current = current.next


    # RESULT
    count = count_blocks(linked_list, references)
    print ('Block Count ', count)
