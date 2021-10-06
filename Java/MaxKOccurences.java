import java.util.*;
class MaxKOccurences {

	int[] maxKOccurences(String sequence, String[] words) {

		int n= words.length; 
		int[] result = new int[n];
		
		if (n==0 || sequence.length() == 0)
			return result; 
		
		for (int i=0;i< n;i++) {
			String word = words[i];
			
		    int count = 0;
		    String tmp = word;

			while (true) {
				int index = sequence.indexOf(tmp);
				if (index == -1) 
					break;
				else {
					count++;
					tmp += word;
				}
			}
		
			result[i] = count;
		}
	
		return result;
	}

	public static void main(String[] args) {
		MaxKOccurences m = new MaxKOccurences();
		String[] words = {"ab", "babc", "bca"};
		System.out.println(Arrays.toString(m.maxKOccurences("ababcbabc", words)));
	}
}