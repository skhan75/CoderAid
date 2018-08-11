class Queue:

    def __init__(self, data):
        self.data = data
        self.s1 = []
        self.s2 = []

    def enqueue(self, element):
        self.s1.append(element)
        return self.s1

    def dequeue(self):
        for i in range(len(self.s1)):
            self.s2.append(self.s1.pop())

        return self.s2.pop()



input = [10, 20, 4 ,7, 12, 15, 19, 3, 2, 1]

q = Queue(input)

for i in input:
    print q.enqueue(i)

print q.dequeue()
print q.dequeue()
print q.dequeue()
print q.dequeue()
print q.dequeue()
print q.dequeue()
print q.dequeue()
print q.dequeue()
print q.dequeue()
