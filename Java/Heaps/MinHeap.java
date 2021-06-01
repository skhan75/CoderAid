/**
	Time Complexities:
	- extractMin() --> O(logn)
	- insert() --> O(logn)
**/
class MinHeap {

	private int capacity, size;
	private int[] heap;
	int FRONT = 1;

	MinHeap(int capacity) {
		this.capacity = capacity;
		this.size = 0;
		heap = new int[this.capacity+1];
		heap[0] = Integer.MIN_VALUE;
	}

	// parent = child / 2
	int getParent(int child) {
		return child/2;
	}

	int getLeftChild(int parent) {
		return (2 * parent);
	}

	int getRightChild(int parent) {
		return (2 * parent) + 1;
	}

	boolean hasParent(int child) {
		return getParent(child) >= 0;
	}

 	boolean isLeaf(int pos) {
        if (pos >= (size / 2) && pos <= size) {
            return true;
        }
        return false;
    }

	void swap(int a, int b) {
		int tmp;
		tmp = heap[a];
		heap[a] = heap[b];
		heap[b] = tmp;
	}

	void insert(int e) {
		if(size >= capacity){
			return;
		}

		heap[++size] = e;
		int current = size;

		while(heap[current] < heap[getParent(current)]) {
			swap(current, getParent(current));
			current = getParent(current);
		}
	}

	int extract_min() {
		if(size == 0){
			throw new IndexOutOfBoundsException("No more elements in heap !");
		}
		// Get the front minimum element
		int minElement = heap[FRONT];

		// Put the last leaf node element to the front
		heap[FRONT] = heap[size--];

		// Heapify Down
		minHeapify(FRONT);

		return minElement;
	}

	void minHeapify(int idx) {
		// Start with front element
		if(!isLeaf(idx)) {
			int leftChild = getLeftChild(idx);
			int rightChild = getRightChild(idx);

			if(heap[idx] > heap[leftChild] || heap[idx] > heap[rightChild]) {
				// If left is smaller than right, then swap parent with left
				if(heap[leftChild] < heap[rightChild]) {
					swap(idx, leftChild);
					minHeapify(leftChild);
				} else { // Else if right is smaller than left, then swap parent with right
					swap(idx, rightChild);
					minHeapify(rightChild);
				}
			}
		}
	}

	public void printMinHeap() {
        for (int i = 1; i <= size / 2; i++) {
            System.out.print(" PARENT : " + heap[i]
                             + " LEFT CHILD : " + heap[2 * i]
                             + " RIGHT CHILD :" + heap[(2 * i) + 1]);
            System.out.println();
        }
    }


	public static void main(String[] args) {
		MinHeap mh = new MinHeap(15);

		mh.insert(5);
        mh.insert(3);
        mh.insert(17);
        mh.insert(10);
        mh.insert(84);
        mh.insert(19);
        mh.insert(6);
        mh.insert(22);
        mh.insert(9);

	    mh.printMinHeap();

	    System.out.println("Extracted minimum --> "+mh.extract_min());
	    System.out.println("Extracted minimum --> "+mh.extract_min());
	    System.out.println("Extracted minimum --> "+mh.extract_min());
	}
}