import java.util.*;

class KthLargestElement {

	int findKthLargestElement(int[] arr, int k) {

		PriorityQueue<Integer> minHeap = new PriorityQueue<Integer>();

		for(int i=0; i<k; i++) 
			minHeap.add(arr[i]);
		
		for(int i=k; i<arr.length; i++) {

			if(arr[i] > minHeap.peek()) {
				minHeap.poll();
				minHeap.add(arr[i]);
			}
		}

		return minHeap.peek();
	}

	
	public static void main(String[] args) {
		KthLargestElement k = new KthLargestElement();
		int[] arr = {3,2,1,4,5,6,9,7};
		System.out.println(k.findKthLargestElement(arr , 3));
	}
}