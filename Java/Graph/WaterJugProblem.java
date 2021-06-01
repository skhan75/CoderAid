import java.util.*;

class WaterJugProblem {

	class Pair {
		int first, second;

		Pair(int first, int second) {
			this.first = first;
			this.second = second;
		}
	}
	// (x,y) 

	private void getSolutionPaths(int x, int y, int target ) {

		// We create a visited list to keep a track of all the states visited
		int visited[][] = new int[1000][1000];
		for(int[] i : visited){
            Arrays.fill(i, -1);
        }

		boolean isSolvable = false;

		Vector<Pair> path = new Vector<Pair>(); // result list of paths from initial state to the solution state
		Queue<Pair> queue = new LinkedList<Pair>(); // queue to maintain states

		Pair initialPair = new Pair(0,0);
		queue.add(initialPair); // Initializing with initial state when both jugs are empty

		while(!queue.isEmpty()) {

			// Get the current pair

			Pair p = queue.peek();
			queue.poll();


			if(p.first > x || p.second > y || p.first < 0 || p.second < 0) {
				continue;
			}

			// if this state is already visited
            if (visited[p.first][p.second] > -1) {
                continue;
            }
 
			path.add(p);
			visited[p.first][p.second] = 1;

			// If we have reached the final state, then we print the solution
			if(p.first == target || p.second == target) {
				isSolvable = true;

				if(p.first == target) {
					if(p.second!=0){
						path.add(new Pair(p.first, 0));
					}
				} else {
					if(p.first != 0){
						path.add(new Pair(0, p.second));
					}
				}

				int sz = path.size();
                for (int i = 0; i < sz; i++)
                    System.out.println("(" + path.get(i).first
                        + ", " + path.get(i).second + ")");
                break;
			}

			// If we have not reached the target, we keep looking in different pairs
			queue.add(new Pair(x, p.second)); // Fill Jug 1
			queue.add(new Pair(p.first, y));  // Fill Jug 2

			for(int poured=0; poured<Math.max(x,y); poured++) {

				// Pour amount from jug1 to jug2 
				int jug1Qty = p.first - poured; // Took from Jug 1
				int jug2Qty = p.second + poured; // Put in Jug 2

				// Now check if these two quanties form a correct state pair
				if((jug1Qty==0 && jug1Qty>=0) || jug2Qty == y) {
					queue.add(new Pair(jug1Qty, jug2Qty));
				}

				// Pour from Jug2 to Jug1
				jug2Qty = p.second - poured; // Took from Jug 2
				jug1Qty = p.first + poured; // Pour in Jug1

				if((jug2Qty==0 && jug2Qty>=0) || jug1Qty == x) {
					queue.add(new Pair(jug1Qty, jug2Qty));
				}
				
			}

			queue.add(new Pair(x, 0)); // Empty Jug2
			queue.add(new Pair(0, y)); // Empty Jug1
		}


			// No, solution exists if ans=0
	        if (!isSolvable)
	            System.out.print("No solution");


	}

	public static void main(String[] args) {

		int jug1=4, jug2=3, target=2;

		System.out.println("Path from initial state " +
                "to solution state ::");
 
        WaterJugProblem wjp = new WaterJugProblem();

        wjp.getSolutionPaths(jug1, jug2, target);
	}
}