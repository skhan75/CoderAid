from Stack import Stack

def sort_stack(s):
    return merge_sort(s)

def merge_sort(s):
    left = Stack()
    right = Stack()

    if s.is_empty():
        return s

    mid = s.size() // 2

    while s.size() != 0:
        if s.size() <= mid:
            left.push(s.pop())
        else:
            right.push(s.pop())

    left = merge_sort(left)
    right = merge_sort(right)

    while left.size > 0 or right.size() > 0:
        if left.size() == 0:
            s.push(right.pop())
        elif right.size() == 0:
            s.push(left.pop())
        elif right.peek() < left.peek() or right.peek() == left.peek():
            s.push(left.pop())
        else:
            s.push(right.pop())

    reverse_stack = Stack()
    while s.size() > 0:
        reverse_stack.push(s.pop())

    return reverse_stack


if __name__ == "__main__":
    input = list(input().strip())

    s = Stack()
    for elem in input:
        s.push(elem)


    print (sort_stack(s))
