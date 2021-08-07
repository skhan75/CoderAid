import java.util.*;

class MeanAndChessBoard {

	int[][] meanAndChessboard(int[][] matrix, int[][] queries) {

		int rows = matrix.length;
		int cols = matrix[0].length;

		int[] smallestWhites = new int[rows];
		Arrays.fill(smallestWhites, Integer.MAX_VALUE);
		int[] smallestBlacks = new int[rows];
		Arrays.fill(smallestBlacks, Integer.MAX_VALUE);
		
		// for every row in matrix
		for(int r=0; r<rows; r++) {
			int smallestBlack = Integer.MAX_VALUE;
			int smallestWhite = Integer.MAX_VALUE;

			for(int i=0; i<cols; i++) {

				if(r%2 == 0) { // Start white 
					if(i%2 == 0) {
						smallestWhites[r] = Math.min(smallestWhites[r], matrix[r][i]);
					} else {
						smallestBlacks[r] = Math.min(smallestBlacks[r], matrix[r][i]);
					}
				} else { // Start black 
					if(i%2 == 0) {
						smallestBlacks[r] = Math.min(smallestBlacks[r], matrix[r][i]);
					} else {
						smallestWhites[r] = Math.min(smallestWhites[r], matrix[r][i]);
					}
				}
			}
		}

		System.out.println("Smallest White "+Arrays.toString(smallestWhites));
		System.out.println("Smallest Black "+Arrays.toString(smallestBlacks));

		for(int q=0; q<queries.length; q++) {
			int iq = queries[q][0];
			int jq = queries[q][1];

			int ithSmallestWhite = smallestWhites[iq];
			int jthSmallestBlack = smallestBlacks[jq];

			System.out.println("ithSmallestWhite "+ithSmallestWhite);
			System.out.println("jthSmallestBlack "+jthSmallestBlack);

			double avg = (ithSmallestWhite + jthSmallestBlack)/2;

			System.out.println("AVG " + avg);
		}

		return null;
	}

	public static void main(String[] args) {
		MeanAndChessBoard m = new MeanAndChessBoard();
		int[][] matrix = {
			{2,0,4},
			{2,8,5},
			{6,0,9},
			{2,7,10},
			{4,3,4}
		};

		int[][] queries = {
			{0,0},
			{1,3}
		};

		m.meanAndChessboard(matrix, queries);
	}
}