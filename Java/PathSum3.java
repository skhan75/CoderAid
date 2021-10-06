/* 
	Approach - I
	Time Complexity --> O(n^2) in worst case when the tree is skewed 
*/
public int pathSum(TreeNode root, int targetSum) {

	if(root == null)
		return 0;

	return pathSum(root.left, targetSum) // for every possible subtree 
		+ pathSum(root.right, targetSum)
		+ calculate(root, targetSum); // caclulate the count where sum == targetSum
}

int calculate(TreeNode node, int targetSum) {

	if(node == null)
		return 0;

	int count = 0;

	if(node.val == targetSum)
		count = 1;

	count += calculate(node.left, targetSum - node.val);
	count += calculate(node.right, targetSum - node.val);

	return count;

}


/* 
	Approach - II
	Prefix Sum Technique - Have a dictionary to store the running sum of the path and store the count of how many times we have 
	seen that value
	If we have seen runningSum - target in the dictionary, we can add 1 to the count
  	Time Complexity --> O(n)
*/
public int pathSum(TreeNode root, int targetSum) {
	HashMap<Integer, Integer> map = new HashMap<>();
	map.put(0,1); // take care of root node whose value is equal to sum or target
	return calculate(root, 0, targetSum, map);
}

int calculate(TreeNode root, int runningSum, int target, HashMap<Integer, Integer> map) {
	if(root == null)
		return 0;

	runningSum += root.val;

	int count = map.getOrDefault(runningSum - target, 0);
	map.put(runningSum, map.getOrDefault(runningSum, 0) + 1);

	count += calculate(root.left, runningSum, target, map) + calculate(root.right, runningSum, target, map);

	map.put(runningSum, map.get(runningSum) - 1);

	return count;
}
















