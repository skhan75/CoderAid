import java.util.*;


class PairInt {
    int first, second;
    PairInt(){}
    PairInt(int first, int second) {
        this.first = first;
        this.second = second;
    }
}

class KClosestPoint {

	List<PairInt> closestLocations(List<PairInt> allLocations, int totalCrates, int capacity) {

		Map<PairInt, Double> distances = new HashMap<>(); 
		
		for(PairInt p : allLocations) {
			double dis = Math.sqrt(p.first*p.first + p.second*p.second);
			distances.put(p, dis);
		}

		List<PairInt> result = new ArrayList<>();

		// Now we can sort the distances by value
		distances.entrySet()
		  .stream()
		  .sorted(Map.Entry.comparingByValue())
		  .forEach(e -> {
		  	if(result.size() < capacity) {
		  		result.add(e.getKey());
		  	}
		  });

		return result;
	}

	public static void main(String[] args) {
		KClosestPoint kcp = new KClosestPoint();
		int[][] locations = { {1, 2}, {3, 4}, {1, -1} };

		List<PairInt> allLocations = new ArrayList<>();

		for(int[] loc : locations) {
			allLocations.add(new PairInt(loc[0], loc[1]));
		}

		int capacity = 2;
		int totalCrates = 3;


		List<PairInt> result = kcp.closestLocations(allLocations, totalCrates, capacity);

		for(PairInt p : result) {
			System.out.println(p.first+ "," + p.second);
		}
	}
}

