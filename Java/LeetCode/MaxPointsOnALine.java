
import java.util.*;
class MaxPointsOnALine {

	static class Slope {
		int numerator;
		int denominator;
		public Slope(int numerator, int denominator) {
			this.numerator=numerator;
			this.denominator=denominator;
		}

		public int hashCode() {
			return Objects.hash(numerator, denominator);
		}

		public boolean equals(Object o) {
			if(this==o) return true;
			if(o==null || !(o instanceof Slope)) return false;
			Slope other = (Slope)o;
			return other.numerator*other.denominator==numerator*denominator;
		}
	}

	public int gcd(int a, int b) {
		if(a==0) return b;
		return gcd(b%a, a);
	}

	public int getMaximumPointsOnALine(int[][] points) {
		int n = points.length, ans = 0;

		if(n < 3) {
			return n;
		}

		// Pick a point and then make every slope possible from that point and calculate the max points possible from 
		// any of such slope
		for(int i=0; i<n; i++) {

			Map<Slope, Integer> map = new HashMap<Slope, Integer>();

			int duplicate = 1, maxPoints = 1;

			for(int j=i+1; j<n; j++) {
				int dy = points[i][1] - points[j][1];
				int dx = points[i][0] - points[j][0];
				

				if(dx==0 && dy==0) duplicate++;

				else {
					// get the greatest common factor to reduce the numerator and denominator to simplest form
					int factor = gcd(dy, dx);

					Slope slope = new Slope(dy/factor, dx/factor);
					
					// Add the slope to the map if not present and initialize its value as 0 if not present
					// Get the current no of points of the current slope and then increment by 1
					int pointsInCurrentLine = map.getOrDefault(slope, 0) + 1;
					map.put(slope, pointsInCurrentLine);

					maxPoints = Math.max(maxPoints, pointsInCurrentLine);
				}
			}

			ans = Math.max(ans, duplicate+maxPoints);
		}

		return ans;

	}


	public static void main(String[] args) {

		MaxPointsOnALine maxPointsOnALine = new MaxPointsOnALine();
		int[][] points1 = {{1,1},{3,2},{5,3},{4,1},{2,3},{1,4}};
		System.out.println("Maximum Points on a line is  "+maxPointsOnALine.getMaximumPointsOnALine(points1));

		int[][] points2 = {{0,0},{1,-1},{1,1}};
		System.out.println("Maximum Points on a line is  "+maxPointsOnALine.getMaximumPointsOnALine(points2));

		int[][] points3 = {{1,1},{2,2},{3,3}};
		System.out.println("Maximum Points on a line is  "+maxPointsOnALine.getMaximumPointsOnALine(points3));
	}
}