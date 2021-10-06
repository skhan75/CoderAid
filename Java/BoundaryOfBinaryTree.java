
List<Integer> result;
public List<Integer> boundaryOfBinaryTree(TreeNode root) {
	result = new ArrayList<>();

	if(root == null)
		return result;

	result.add(root.val);

	getLeftBoundaryNodes(root.left);
	getLeafNodes(root.left);
	getLeafNodes(root.right);
	getRightBoundaryNodes(root.right);

	return result;
}

private void getLeftBoundaryNodes(TreeNode node) {
	if(node == null)
		return;

	if(node.left != null) {
		result.add(node.val)
		getLeftBoundaryNodes(node.left);
	} else if(node.right != null) {
		result.add(node.val);
		getLeftBoundaryNodes(node.right);
	}	
}

private void getRightBoundaryNodes(TreeNode node) {
	if(node == null) 
		return null;

	if(node.right != null) {
		getLeftBoundaryNodes(node.right);
		result.add(node.val)
	} else if(node.left != null) {
		getLeftBoundaryNodes(node.left);
		result.add(node.val)
	}	
}

private void getLeafNodes(TreeNode node) {
	if(node == null)
		return;

	getLeafNodes(node.left);
	getLeafNodes(node.right);

	if(node.left == null && node.right == null)
		result.add(node.val);
}