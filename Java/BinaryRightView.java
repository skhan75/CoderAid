List<Integer> visibleValues;

public List<Integer> rightSideView(TreeNode root) {
	List<Integer> visibleValues = new ArrayList<>();
	if(root == null)
	    return visibleValues;

	Queue<TreeNode> queue = new ArrayDeque<>();

	queue.offer(root);

	while(!queue.isEmpty()) {
	    int size = queue.size();

	    for(int i=0; i<size; i++) {
	        TreeNode current = queue.poll();
	        if(i == size - 1)
	            visibleValues.add(current.val);

	        if(current.left!=null) queue.offer(current.left);
	        if(current.right!=null) queue.offer(current.right);
	    }
	}

	return visibleValues;
	}
}