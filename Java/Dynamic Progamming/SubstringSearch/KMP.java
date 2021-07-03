class KMP {

	boolean hasSubstring(char[] text, char[] pattern){
		int[] prefixArr = createPrefixArray(pattern);

		// Window indices
		int i=0, j=0;

		// Iterate over main string and pattern
		while(i<text.length && j<prefixArr.length) {

			// When ever the characters are same, we 
			// keep moving in the right direction of both indices
			if(text[i] == pattern[j]) {	
				i++;
				j++;
			} else { // we check what is the next point we can check from pattern
				if(j!=0){
					j = prefixArr[j-1];	
				} else {
					i++;
				}
			}
		}

		// if pattern was able to reach its end within the string
		// The pattern is a substring
		if(j==pattern.length){
			return true;
		}

		return false;
	}


	// Creating the prefix array from the pattern
	private int[] createPrefixArray(char[] pattern) {
		int pivot=0;
		int[] prefixArr = new int[pattern.length];

		for(int i=1; i<pattern.length;) {

			if(pattern[i] == pattern[pivot]) {
				prefixArr[i] = pivot+1;
				pivot += 1;
				i++;
			} else {
				if(pivot!=0) {
					pivot = prefixArr[pivot-1];
				} else {
					prefixArr[i] = 0;
					i++;
				}
			}
		}

		return prefixArr;
	}


	public static void main(String[] args) {
		KMP kmp = new KMP();
		String mainString = "acacabbbccbbacacabacacabacacaccbabbacacabac";
		String pattern = "acacabacacabacacac";
		System.out.println("Has Substring "+kmp.hasSubstring(mainString.toCharArray(), pattern.toCharArray()));
		
		 
	}
}