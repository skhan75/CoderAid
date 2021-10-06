class LRUCache {

	private int capacity;
	private int size;
	private Map<Integer, DoublyLinkedNode> cache = null;
	DoublyLinkedNode head, tail;

	LRUCache(int capacity) {
		this.capacity = 0;
		this.size = 0;
		this.head = new DoublyLinkedNode();
		this.tail = new DoublyLinkedNode();
		this.cache = new HashMap<>();

		head.next = tail;
		tail.prev = head;
	}

	public int get(int key) {
		DoublyLinkedNode node = cache.get(key);
		if(node == null)
			return -1;

		// move the accessed node to the head
		moveToHead(node);

		return node.value;
	}

	public void put(int key, int value) {
		DoublyLinkedNode node = cache.get(key);

		if(node == null) {
			DoublyLinkedNode newNode = new DoublyLinkedNode();
			newNode.key = key;
			newNode.value = value;

			cache.put(key, value);
			addNode(newNode);

			size++;

			if(size > capacity){
				// pop the least recent from tail
				DoublyLinkedNode tail = popTail();
				cache.remove(tail.key);
				size--;
			}
		} else {
			// just update the value
			node.value = value;
			moveToHead(node);
		}
	}

	private void moveToHead(DoublyLinkedNode node){
		// First we remove the node
		removeNode(node);
		addNode(node);
	}

	private DoublyLinkedNode popTail() {
		DoublyLinkedNode res = tail.prev;
		removeNode(res);
		return res;
	}

	private void removeNode(DoublyLinkedNode node) {
		DoublyLinkedNode prev = node.prev;
		DoublyLinkedNode next = node.next;

		prev.next = next;
		next.prev = prev;
	}


	static class DoublyLinkedNode {
		int key;
		int value;
		DoublyLinkedNode head;
		DoublyLinkedNode tail;
	}

}