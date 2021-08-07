import java.util.*;
class PackBlocks {

	int packBlocks(int[] blocks, int height) {
	    int L = blocks.length;
	    
	    Arrays.sort(blocks);
	    Map<Integer, Integer> table = new HashMap<>();
	    
	    int maxWidth = 0, pivot = 0;
	    
	    int firstFill = (int)Math.ceil((double)L/height); // 3
	    int otherFills = (int)Math.floor((double)L/height); // 2

	    System.out.println(firstFill);
	    System.out.println(otherFills);
	    
	    int sumWidths = 0;
	    for(int i=0; i<firstFill; i++) {
	        sumWidths += blocks[i];
	        pivot++;
	    }
	    table.put(0, sumWidths); // 1,3,1
	    
	    for(int r=1; r<height && r<blocks.length; r++) {
	        sumWidths = 0;
	        for(int j=0; j<otherFills; j++) {
	            sumWidths += blocks[pivot+j];
	        }
	        pivot++;
	        table.put(r, sumWidths);
	    }
	    
	    for (Map.Entry e : table.entrySet()) {
	        maxWidth = Math.max(maxWidth,(int)e.getValue());
	    }
	    
	    return maxWidth;
	}


	public static void main(String[] args) {
		PackBlocks p = new PackBlocks();
		// int[] blocks = {1, 3, 1, 3, 3};
		// int[] blocks = {9, 6, 5, 7, 1, 6, 2, 6, 10, 3};
		// int[] blocks = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1};
		// int height = 1000000000;

		int[] blocks = {9999, 9997, 9995, 9997, 9998, 9995, 9995, 10000, 9999, 9999};
		int height = 86;
		
		System.out.println(p.packBlocks(blocks, height));

	}
}