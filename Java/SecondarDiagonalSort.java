import java.util.*;

public class SecondarDiagonalSort {
	

	public void diagonalSort(int[][] mat) {

		int m = mat[0].length;
		int diagonalCount = 0;

		Map<Integer, List<Integer>> diagonals = new HashMap<>();

		// Iterate over top half right diagonals 
		for(int d=0; d<m; d++) {
			int row = d;
			int col = 0;

			while(row>=0) {
				List<Integer> currentDiagonal = diagonals.getOrDefault(diagonalCount, new ArrayList<>());
				currentDiagonal.add(mat[row][col]);
				diagonals.put(diagonalCount, currentDiagonal);
				row--;
				col++;
			}

			diagonalCount++;
		}

		// Iterate over bottom half right diagonals 
		for(int d=1; d<m; d++) {
			int row = m-1;
			int col = d;

			while(col<m) {
				List<Integer> currentDiagonal = diagonals.getOrDefault(diagonalCount, new ArrayList<>());
				currentDiagonal.add(mat[row][col]);
				diagonals.put(diagonalCount, currentDiagonal);
				row--;
				col++;
			}
			diagonalCount++;
		}

		// Sort each diagonal elements list in the list of diagonals
		for(List<Integer> dl : diagonals.values()) {
			Collections.sort(dl);
		}

		for(List<Integer> dl : diagonals.values()) {
			
			System.out.println(dl);
		}

		// Now add the sorted diagonals back int the original matrix
		for(int row=0; row<m; row++) {
			for(int col=0; col<m; col++) {
				// int diag = Math.abs(row-col);
				// System.out.println(diag);
			}
			// System.out.println();
		}



	}


	public static void main(String[] args) {
		SecondarDiagonalSort ds = new SecondarDiagonalSort();

		int[][] mat = { 
			{1,3,9,4},
			{9,5,7,7},
			{3,6,9,7},
			{1,2,2,2} 
		};

		ds.diagonalSort(mat);
	}
}