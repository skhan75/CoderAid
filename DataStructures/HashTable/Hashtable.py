#
# Author: Sami Ahmad Khan
# File_overview: HashTable implementation with collision handling and resizing
#

# Node for Hashed key-value pair
class HashEntry:
    def __init__(self, key, value):
        self.key = key
        self. value = value
        self.next = None

class HashTable:
    def __init__(self, capacity, load):
        self.capacity = capacity    # no of buckets in the hashtable
        self.load = load            # how full the hashtable can be before a resize happens
        self.cur_capacity = 0
        self.slots = [None] * self.capacity

    # Hash Function
    def hash(self, key):
        return key % self.capacity

    # Stores a key and value pair in the hashtable
    def set(self, key, value):
        key_hash = self.hash(key)
        slot = key_hash % self.capacity

        if self.slots[slot] is None:
            self.slots[slot] = HashEntry(key,value)
        else:
            self._set_linked_list(key, value, self.slots, slot)

        self.cur_capacity += 1
        current_load = float(self.cur_capacity) / float(self.capacity)

        if current_load >= self.load:
            self.resize()
        print self.slots

    # Retreives the value associated with the key
    def get(self, key):
        key_hash = self.hash(key)
        slot = key_hash % self.capacity

        if self.slots[slot] is not None:
            current_node = self.slots[slot]
            while current_node is not None:
                if current_node.key == key:
                    return current_node.value
                current_node = current_node.next

    # Create linked lsit to avoid collisions
    def _set_linked_list(self, key, value, slots, slot):
        current_node = self.slots[slot]
        while current_node is not None:
            if current_node.key == key:
                current_node.value = value
                current_node = None
            elif current_node.next is None:
                current_node.next = HashEntry(key, value)
                current_node = None
            else:
                current_node = current_node.next

    #resizing the hashtable with new capacity
    def _resize(self):
        new_capacity = self.capacity * 2
        new_slots = [None] * new_capacity

        # rehash all items into new slots
        for slot_index in range(0, len(self.slots)):
            current_node = self.slots[slot_index]
            while current_node is not None:
                key_hash = self.hash(current_node.key)
                new_slot = key_hash % new_capacity
                if new_slots[new_slot] is None:
                    new_slots[new_slot] = HashEntry(current_node.key, current_node.value)
                else:
                    self._set_linked_list(cur_node.key, cur_node.value, new_slots, new_slot)



if __name__ == "__main__":
    H = HashTable(10, 5)
    H.set(5,"dog")
    H.set(15, "cat")
    print H.get(5)
    print H.get(15)
