import java.util.*;

public class SecondarDiagonalSort {
	

	public int[][] diagonalSort(int[][] mat) {

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


		// Update upper half of the matrix 
		for(int d=0; d<m; d++) {
			int row = d;
			int col = 0;
			List<Integer> currentSortedDiagonals = diagonals.get(d);
			while(row>=0) {
				int element = currentSortedDiagonals.get(col);
				mat[row][col] = element;
				row--;
				col++;
			}
			diagonalCount++;
		}

		// Update bottom half of the matrix
		for(int d=1; d<m; d++) {
			int row = m-1;
			int col = d;

			int i=0;
			List<Integer> currentSortedDiagonals = diagonals.get(row+d); // 4 5 6
			while(col<m && i<col) {
				int element = currentSortedDiagonals.get(i);
				mat[row][col] = element;
				i++;	
				row--;
				col++;
			}
			diagonalCount++;
		}

	

		return mat;

	}


	public static void main(String[] args) {
		SecondarDiagonalSort ds = new SecondarDiagonalSort();

		int[][] mat = { 
			{1,3,9,4},
			{9,5,7,7},
			{3,6,9,7},
			{1,2,2,2} 
		};

		int[][] res = ds.diagonalSort(mat);
		for(int i=0; i<res.length; i++) {
			for(int j=0; j<res.length; j++) {
				System.out.print(res[i][j] + " ");
			}
			System.out.println();
		}
	}
}