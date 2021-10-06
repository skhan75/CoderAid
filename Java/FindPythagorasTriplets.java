import java.util.*;

class FindPythagorasTriplets {
	
	List<List<Integer>> findPythagorasTriplets(int[] nums) {
		List<List<Integer>> result = new ArrayList<>();

		// First find the maximum in the array
		int maximum = 0; 
		for(int i=0; i<nums.length; i++) 
			maximum = Math.max(maximum, nums[i]);

		// intialize a hash list
		int[] hash = new int[maximum+1];

		// Increase the count of array elements
    	// in hash table
		for(int i=0; i<nums.length; i++)
			hash[nums[i]]++;

		// Iterate for all possible a that exists
		for(int i=1; i<maximum+1; i++) {
			List<Integer> current = new ArrayList<>();

			// if a doesnt exist
			if(hash[i] == 0)
				continue;

			// Iterate for all possible b
			for(int j=1; j<maximum+1; j++) {

				// If a and b are same and there is only one a. Or b doesnt exist
				if(i==j && hash[i] == 1 || hash[j] == 0)
					continue;

				// Get c
				int val = (int)Math.sqrt(i*i + j*j);

				// When c is not a perfect squre
				if(val*val != (i*i + j*j))
					continue;

				// When c exceeds tha maxmimum value, we ignore
				if(val > maximum) 
					continue;

				if(hash[val] == 1) {// That means there exist a c^2 for a^2 and b^2
					current.add(i);
					current.add(j);
					current.add(val);
				}
			}

			result.add(current);
		}

		return result;
		
	}
	
	public static void main(String[] args) {
		FindPythagorasTriplets f = new FindPythagorasTriplets();
		int[] nums = {2, 3, 4, 5, 7, 12, 13};
		System.out.println(f.findPythagorasTriplets(nums));
	}
}