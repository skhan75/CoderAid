class BinarySearch {

	int search(int[] arr, int find) {
		return searchUtil(arr, 0, arr.length-1, find);
	}

	int searchUtil(int[] arr, int left, int right, int find) {

		if(right >= left) {

			int mid = left + (right-left) / 2;

			if(arr[mid] == find) {
				return mid;
			}

			// find in right sub array
			if(arr[mid] < find)  return searchUtil(arr, mid+1, right, find);
			// find in left sub array
			else return searchUtil(arr, left, mid-1, find);
		}

		return -1;
	}

	public static void main(String[] args) {
		BinarySearch bs = new BinarySearch();

		int arr[] = { 2, 3, 4, 10, 40 };

		System.out.println("Element found at " + bs.search(arr, 10));
		System.out.println("Element found at " + bs.search(arr, 40));
	}
}