class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise ValueError('Empty Stack')
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise ValueError('Empty Stack')
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def print_stack(self):
        print (self.stack)

if __name__ == "__main__":
    s = Stack()
    print (s.is_empty())
    s.push(1)
    s.push(5)
    s.push(8)
    s.push(2)
    s.push('a')
    s.push('b')
    print (s.peek())
    print (s.size())
    print (s.pop())
    s.print_stack()
