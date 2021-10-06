
public int trap(int[] height) {

	// We have to find Min(Max(left, right)) - height of current block

	if(height.length == 0)
		return 0;

	int res = 0;
	int n = height.length;

	int[] maxLeft = new int[n];
	int[] maxRight = new int[n];

	// Calculate maximum from left
	maxLeft[0] = 0; // No left at 0
	for(int i=1; i<n; i++)
		maxLeft[i] = Math.max(maxLeft[i-1], height[i]);

	// Calculate maximum from right 
	maxRight[n01] = height[n-1]; // No left at 0
	for(int i=n-2; i>=0; i--)
		maxRight[i] = Math.max(maxRight[i+1], height[i]);

	for(int i=0; i<n; i++)
		res += Math.min(maxLeft[i], maxRight[i]) - height[i];

	return res;
}