public List<List<Integer>> threeSum(int[] nums) {

	Arrays.sort(nums);
	List<List<Integer>> output = new ArrayList<>();

	for(int i=0; i<nums.length; i++) {
		if(i==0 || nums[i]!=nums[i-1]){
			int low = i+1;
			int high = nums.length - 1;
			int target = -nums[i];

			while(low<high) {

				if(nums[low] + nums[high] == target) {
					output.add(Arrays.asList(nums[i], nums[low], nums[high]));

					// skip duplicates and find other pairs as possible
					while(low<high && nums[low] == nums[low+1]) low++;
					while(low<high && nums[high] == nums[high-1]) high--;

					low++;
					high--;


				} 
				else if(nums[low] + nums[high] > target) high--;
				else low++;
			}
		}
	}

	return output;
}