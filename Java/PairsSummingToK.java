class PairsSummingToK {
	int findPairsSummingToK(int[] a, int m, int k) {

	    // Start from 0
	    // Find sum == k
	    // int currSum = 0;
	    // int count = 0;
	    // for(int i=0; i<a.length; i++) {
	        
	    //     findPairs();
	    //     if(currSum == k) {
	    //         count++;
	    //     }
	        
	    //     currSum += a[i];
	    // }
	    
	    int count = 0; // Initialize result
	 
	        // Consider all possible pairs and check their sums
	    for (int i = 0; i <= a.length-m; i++) {
	    	System.out.println("\nI --> "+i);
	        for (int j = i + 1; j < i+m; j++) {
	        	for(int x = j+1; x<i+m; x++) {
	        		 if ((a[j] + a[x]) == k){	
	        		 	System.out.println("J --> "+j+ " X --> "+x);
		                count++;
		            }
	        	}

	            // System.out.println("J --> "+j);
	            if ((a[i] + a[j]) == k){
	            	System.out.println("I --> "+i+ " J --> "+j);
	            	// System.out.println("A[i] "+a[i]+" A[j] "+a[j]);
	                count++;
	            }
	            	
	            
	        }   
	        System.out.println("COUNT " + count);
	    }   
	                
	    return count;
	}


	public static void main(String[] args) {
		PairsSummingToK p = new PairsSummingToK();
		int[] a = {2, 4, 7, 5, 3, 5, 8, 5, 1, 7};
		int m = 4;
		int k = 10;
		System.out.println("PairsSummingTo" + p.findPairsSummingToK(a, m, k));
	}
}