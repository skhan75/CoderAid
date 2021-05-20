class MinHeap:

    def __init__(self, capacity):
        self.capacity=capacity
        self.size=0
        self.items = [None]*self.capacity

    def get_left_child_index(self, parent_index):
        return 2 * parent_index + 1

    def get_right_child_index(self, parent_index):
        return 2 * parent_index + 2

    def get_parent_index(self, child_index):
        return (child_index - 1) // 2

    def has_left_child(self, index):
        return self.get_left_child_index(index) < self.size

    def has_right_child(self, index):
        return self.get_right_child_index(index) < self.size

    def has_parent(self, index):
        return self.get_parent_index(index) >= 0

    def left_child(self, index):
        return self.items[self.get_left_child_index(index)]

    def right_child(self, index):
        return self.items[self.get_right_child_index(index)]

    def parent(self, index):
        return self.items[self.get_parent_index(index)]

    def swap(self, index_one, index_two):
        temp = self.items[index_one]
        self.items[index_one] = self.items[index_two]
        self.items[index_two] = temp

    def ensure_extra_capacity(self):
        if self.size == self.capacity:
            self.items = self.items.extend([None]*(2*self.capacity))
            self.capacity = self.capacity * 2

    def peek(self):
        if self.size == 0:
            raise ValueError('Out of capacity')

        return self.items[0]

    def find_min(self, item):
        return self.items[0]


    # Extracts the minimum elements and removes it from the array
    def extract_min(self):
        if self.size == 0:
            raise ValueError('Out of capacity')

        item = self.items[0]
        self.items[0] = self.items[self.size - 1]
        self.items.pop(self.size - 1)
        self.size -= 1
        self.heapify_down()
        return item

    def insert(self, item):
        self.ensure_extra_capacity()
        # First add the element to the last
        self.items[self.size] = item
        self.size += 1
        # Now bubble up till you get the right spot to insert
        self.heapify_up()

    def heapify_up(self):
        index = self.size - 1
        while(self.has_parent(index) and self.parent(index) > self.items[index]):
            # Swap values with parent
            self.swap(self.get_parent_index(index), index)
            # and the walk upwards
            index = self.get_parent_index(index)


    def heapify_down(self):
        # Start with the root element
        index = 0
        # As long as have children keep walking down till you find the perfect fit
        # If it doesn't have left chile, it surely wouldn't have right child
        while(self.has_left_child(index)):
            # Considering left child has the smallest element
            smaller_item_index = self.get_left_child_index(index)
            # Checking if its not the left child but the right child which is smallest
            if(self.has_right_child(index) and self.right_child(index) < self.left_child(index)):
                smaller_item_index = self.get_right_child_index(index)

            # If it is already smaller than its left and right child, then we break
            if self.items[index] < smaller_item_index:
                break

            # Else
            self.swap(index, smaller_item_index)
            # Change the current index to the downward child's index
            index = smaller_item_index

    def print_heap(self):
        for item in self.items:
            if item is not None:
                print (item)



if __name__ == "__main__":
    mh = MinHeap(10)

    mh.insert(1)
    mh.insert(2)
    mh.insert(10)
    mh.insert(6)
    mh.insert(4)
    mh.insert(15)
    mh.print_heap()
    print('\n')

    print ('Extracted minimum',mh.extract_min())
    mh.print_heap()
