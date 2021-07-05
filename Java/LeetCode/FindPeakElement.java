import java.util.Arrays;

class FindPeakElement {

	public int findPeakElement(int[] nums) {

		// Binary Search method
		// Find the mid first
		// Check its immediate neighbors --> if mid is greater than i-1 and i+! return mid 

		return searchUtil(0, nums.length-1, nums);
		

	}

	private int searchUtil(int left, int right, int[] nums) {
		int mid = left + (right-left) / 2;

		if(left == right) return left; 

		if(right > left) {

			if (nums[mid] < nums[mid+1]) return searchUtil(mid+1, right, nums);
			else return searchUtil(left, mid, nums);

		}

		return 0;
	}


	public static void main(String[] args) {
		FindPeakElement fpe = new FindPeakElement();

		int[] a1 = {1};
		int[] a2 = {1,2,1,3,5,6,4};
		int[] a3 = {2,1};

		System.out.println("Peak element of given "+Arrays.toString(a1)+" is "+fpe.findPeakElement(a1));
		System.out.println("Peak element of given "+Arrays.toString(a2)+" is "+fpe.findPeakElement(a2));
		System.out.println("Peak element of given "+Arrays.toString(a3)+" is "+fpe.findPeakElement(a3));
		
	}
}