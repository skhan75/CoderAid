/**
	Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

	Notice that you may not slant the container.

	 

	Example 1:


	Input: height = [1,8,6,2,5,4,8,3,7]
	Output: 49
	Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
	Example 2:

	Input: height = [1,1]
	Output: 1
	Example 3:

	Input: height = [4,3,2,1,4]
	Output: 16
	Example 4:

	Input: height = [1,2,1]
	Output: 2
	 

	Constraints:

	n == height.length
	2 <= n <= 105
	0 <= height[i] <= 104
**/

public class ContainerWithMostWater {


	public int maxArea(int[] heights) {
		// Max left pivot
		int left=0, right=heights.length-1, maxArea=0;
		
		// Area = height * breadth

		while(left < right) {

			// pick the smallest height line out of two to calculate area
			int height = Math.min(heights[left], heights[right]);
			int breadth = right - left;

			int currentArea = height * breadth;

			maxArea = Math.max(maxArea, currentArea);

			// If left pivot is smaller than right pivot, then 
			// that is the maximum area we can get, so ove the left pivot towards right
			// Else move right backward
			if(heights[left] < heights[right]) {
				left++;
			} else {
				right--;
			}
		}

		return maxArea;

	}

	public static void main(String[] args) {
		ContainerWithMostWater containerWithMostWater = new ContainerWithMostWater();
		int[] input = {1,8,6,2,5,4,8,3,7};
]		System.out.println("Maximum area for water fill is "+ containerWithMostWater.maxArea(input));
	}

}