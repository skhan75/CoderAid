// Matrix is Row and Column sorted
public class K_SmallestElementInASortedMatrix {

	public int kthSmallest(int[][] A, int k) {
		
		int n = A.length;
		int start = A[0][0], end = A[n-1][n-1];

		while(start < end) {
			int mid = start + (end-start) / 2;

			int count = getElementsCount(mid, A);

			if(count < k) { // We can get a bigger range of elements
				start = mid+1;
			} else {
				end = mid; 
			}
		}

		return end;
	}

	// This returns the count of elements less than or equal to k
	int getElementsCount(int i, int[][] A) {
		int n = A.length;
		int row = 0, col = n-1;

		int count = 0;

		// We start from right most bottom element
		while(row<n && col>=0) {

			// If k is greater than current row-col element, we move upwards in row
			if(A[row][col] <= i) {
				count += col+1;
				row += 1;
			} else {
				col -= 1;
			}
		}
		return count;
	}
	
	public static void main(String[] args) {
		K_SmallestElementInASortedMatrix ksmallest = new K_SmallestElementInASortedMatrix();

		int[][] matrix = {{1,5,9},{10,11,13},{12,13,15}};
		System.out.println("Kth smallest element is " + ksmallest.kthSmallest(matrix, 4));
	}
}