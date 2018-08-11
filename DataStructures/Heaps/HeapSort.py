# heapsort

def max_heapify(arr, parent, heap_size):
  left_child = parent * 2       #left(i)
  right_child = left_child + 1  #right(i)

  if left_child <= heap_size and arr[left_child] > arr[parent]:
    largest = left_child

  else:
    largest = parent

  if right_child <= heap_size and arr[right_child] > arr[largest]:
    largest = right_child

  if parent != largest:
    arr[parent], arr[largest] = arr[largest], arr[parent]
    max_heapify(arr, largest, heap_size)

def build_max_heap(arr, heap_size):
  for i in range(heap_size/2 - 1, 0, -1):
    max_heapify(arr, i, heap_size)

def heap_sort(arr, heap_size):
  build_max_heap(arr, heap_size)
  for i in range(len(arr[1:]), 1, -1):
    arr[1], arr[i] = arr[i], arr[1]
    heap_size = heap_size - 1
    max_heapify(arr, 1, heap_size)

def main():
  # we shall consider the arrst from element 1, not 0
  arr = [0, 16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
  heap_size = len(arr[1:])
  heap_sort(arr, heap_size)
  print arr[1:]

if __name__ == "__main__":
  main()
