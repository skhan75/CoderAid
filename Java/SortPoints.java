import java.util.*;

class Point {
	private int x;
    private int y;

    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }

    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public String toString() {
    	return "Point(" + x + ", " + y + ")";
    }

    public Point() {}
}

class SortPoints {

	void sort(int[][] coordinates) {

		List<Point> points = new ArrayList<Point>();
		for(int[] c : coordinates) {
			points.add(new Point(c[0], c[1]));
		}

		Collections.sort(points, new Comparator<Point>() {
			public int compare(Point o1, Point o2) {
				if(o1.getX() != o2.getX()) {
					return Integer.compare(o1.getX(), o2.getX());
				} else {
					return Integer.compare(o1.getY(), o2.getY());
				}
			}
		});

		for(Point p : points) {
			System.out.println(p.toString());
		}
	}

	public static void main(String[] args) {
		SortPoints sp = new SortPoints();
		int[][] coordinates = {
			{-1,3},
			{-5,-3},
			{3,5},
			{2,4},
			{-3,-2},
			{-1,4},
			{5,5}
		};
		sp.sort(coordinates);
	}
}