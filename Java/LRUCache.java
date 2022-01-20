import java.util.*;

class LRUCache {

	private int capacity;
	private int size;
	private Map<Integer, DoublyLinkedNode> cache = new HashMap<>();
	private DoublyLinkedNode head, tail;

	LRUCache(int capacity) {
		this.capacity = capacity;
		this.size = 0;
		this.head = new DoublyLinkedNode();
		this.tail = new DoublyLinkedNode();

	}

	public int get(int key) {
		DoublyLinkedNode node = cache.get(key);
		if(node == null) {
			return -1;
		}
		moveLeastRecentToHead(node);
		return node.value;
	}

	public void put(int key, int value) {
		DoublyLinkedNode node = cache.get(key);

		if(node == null) {
			DoublyLinkedNode newNode = new DoublyLinkedNode(key, value);
			cache.put(key, newNode);
			addNodeToHead(newNode);
			size++;
			if(this.size > this.capacity) {
				DoublyLinkedNode poppedNode = popTail();
				cache.remove(poppedNode.getKey());
				size--;
			}
		} else {
			// update the key with the value
			node.value = value;
			moveLeastRecentToHead(node);
		}
	}


	private void moveLeastRecentToHead(DoublyLinkedNode node) {
		removeNode(node);
		addNodeToHead(node);
	}

	private void removeNode(DoublyLinkedNode node) {
		DoublyLinkedNode prev = node.prev;
		DoublyLinkedNode next = node.next;

		prev.next = next;
		next.prev = prev;
	} 

	private void addNodeToHead(DoublyLinkedNode node) {
		node.prev = head;
		node.next = head.next;
		head.next = node;
		head.next.prev = node;
	}

	private DoublyLinkedNode popTail() {
		DoublyLinkedNode poppedNode = tail.prev;
		removeNode(poppedNode);
		return poppedNode;
	}

	static class DoublyLinkedNode {
		Integer key;
		Integer value;
		DoublyLinkedNode prev;
		DoublyLinkedNode next;

		DoublyLinkedNode(Integer key, Integer value) {
			this.key = key;
			this.value = value;
		}

		DoublyLinkedNode() {
			this.key = null;
			this.value = null;
		}

		public Integer getKey() {
			return this.key;
		}
	}
}