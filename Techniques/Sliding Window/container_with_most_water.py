"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""

def max_area(height):
    max_area = 0
    left, right = 0, len(height)-1

    while left < right:
        # Area = height * breadth

        # Always pick the smallest line to maximize the area
        height = min(height[left], height[right])
        # breadth is the distance between the line i.e. difference of the indexes
        breadth = right - left

        current_area = height * breadth

        max_area = max(max_area, current_area)

        # If left line is smaller than right line, then move left forward
        if height[left] < height[right]:
            left+=1
        # Else move right backward
        else:
            right-=1

    return max_area



if __name__ == "__main__":
    print max_area([1,8,6,2,5,4,8,3,7])
