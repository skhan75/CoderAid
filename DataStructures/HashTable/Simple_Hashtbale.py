
def create_hashtable(capacity):
    # table = [None] * capacity
    #
    # Below is for collision handling
    table = [[] for _ in range(capacity) ]
    insert(table, capacity, 12, 'CAT')
    insert(table, capacity, 11, 'DOG')
    insert(table, capacity, 5, 'RAT')
    print (insert(table, capacity, 15, 'KITTY'))

def hash(x, capacity):
    return x % capacity

def insert(table, capacity, key, value):
    table[hash(key, capacity)].append(value)
    # table[hash(key, capacity)] = value
    return table



create_hashtable(10)
