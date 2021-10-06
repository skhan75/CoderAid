

public List<TreeNode> generateTrees(int n) {

	if(n==0)
		return new LinkedList<>();

	return generateTrees(1, n);
}

public List<TreeNode> generateTrees(int start, int end){
	LinkedList<TreeNode> result = new LinkedList<>();
	
	if(start > end){
		result.add(null);
		return result;
	}

	// decision making
	for(int i=start; i<=end; i++) {

		LinkedList<TreeNode> leftSubtrees = generateTrees(start, i-1);
		LinkedList<TreeNode> rightSubtrees = generateTrees(i+1, end);


		for(TreeNode l : leftSubtrees) {
			for(TreeNode r : rightSubtrees){
				TreeNode currentRoot = new TreeNode(i);
				currentRoot.left = l;
				currentRoot.right = r;
				result.add(currentRoot);
			}
		}
	}

	return result;
}