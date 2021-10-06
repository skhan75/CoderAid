

class LinkedList<T> {

	Node<T> head, tail;
	int size = 0;

	static class Node<T> {
		T val;
		Node<T> next;

		Node(T val) {
			this.val = val;
			this.next = null;
		}
	}


	LinkedList() {
		head = tail = null;
	}

	public boolean addLast(T e) {
		Node<T> node = new Node(e);

		if(this.head==null)
			head = tail = node;
		else 
			tail.next = node;
		
		tail = node; 
		size++;
		return true;
	}

	public Node get(int i) {
		int k = 1;
		Node current = this.head;
		

		while(current.next != null) {

			if(i == k)
				break;
			
			k++;
			current = current.next;
		}

		return current;
	}

	public boolean removeAt(int i) {

		if(head == null) return false;
		Node current = head;


		if (i<0 || i >= size())
	        throw new IndexOutOfBoundsException();
	    

	    if(i==0){
	    	System.out.println("current removing "+head.val);
			head = head.next;

			// return true;
		} else {

			for(int j=0; j<i; j++) {
				System.out.println(j);
				current = current.next;
			}

			if(current==null || current.next==null) return false;
			
			Node next = current.next.next;
			current.next = next;
		}

		size--;
		
		return true;
	}

	public int size() {
		return this.size;
	}


	public static void main(String[] args) {
		LinkedList l = new LinkedList();
		l.addLast(1);
		l.addLast(2);
		l.addLast(3);
		System.out.println("Size "+l.size());
		System.out.println("Value at 2nd position --> "+l.get(2).val);

		System.out.println("Value at 2nd position removed --> "+l.removeAt(1));

		System.out.println("Size "+l.size());

	}
}