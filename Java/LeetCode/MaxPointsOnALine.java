
import java.util.*;
class MaxPointsOnALine {
	// Points in a straight line
        // Horizontal Line --> Same X, Y Grows
        // Vertical Line --> Same Y, X Grows
        // Slant Line --> Have same slope, m = (y2-y1)/(x2-x1)
        
        
        // Given points we have to find what's the maximum points we can map on a slope
        
        // We can create a hashtable to store the key--slope<m> and value --> List<x,y>
        // Return the key with highest number of elements in the list
	
	public int getMaximumPointsOnALine(int[][] points) {
		Hashtable<Integer, LinkedList> hashtable = new Hashtable<Integer, LinkedList>();

		for(int i=0; i<points.length-1; i++){
			int y2 = points[i+1][1];
			int y1 = points[i][1];

			int x2 = points[i+1][0];
			int x1 = points[i][0];

			int m = (y2-y1)/(x2-x1);

			System.out.println("Slope "+m);
		}

		return 0;

	}


	public static void main(String[] args) {

		MaxPointsOnALine maxPointsOnALine = new MaxPointsOnALine();
		int[][] poins = {{1,1},{3,2},{5,3},{4,1},{2,3},{1,4}};
		maxPointsOnALine.getMaximumPointsOnALine(poins);
	}
}