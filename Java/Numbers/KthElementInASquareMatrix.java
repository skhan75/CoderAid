public class KthElementInASquareMatrix {

	public int kthElement(int A, int k) {
		int n = A.length;
		int minDiff = Integer.MAX_VALUE;
		int r, c;

		if(k%n == 0) {
			r = (int)Math.floor(k/n)-1;
			c = n-1;
		} else {
			r = (int)Math.floor(k/n);
			c = (k%n)-1;
		}
		
		return A[r][c];
	}

	public static void main(String[] args) {
		KthElementInASquareMatrix k = new KthElementInASquareMatrix();
		int[][] matrix = {{1,5,9},{10,11,13},{12,13,15}};
		System.out.println("4th element is " + k.(matrix, 4));
	}
}