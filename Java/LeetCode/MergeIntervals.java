import java.util.Arrays;
import java.util.LinkedList;

public class MergeIntervals {

    public int[][] merge(int[][] intervals) {
        // Sort by start times
        Arrays.sort(intervals, (a,b) -> a[0] - b[0]);
        LinkedList<int[]> merged = new LinkedList<>();
        
        for(int[] interval : intervals){
            if(merged.isEmpty() || merged.getLast()[1] < interval[0]) { // non overlapping
                merged.add(interval);
            } else { // overlapping
                merged.getLast()[1] = Math.max(interval[1], merged.getLast()[1]);
            }
        }

        return merged.toArray(new int[merged.size()][2]);
    }
    
    public static void main(String[] args) {
        MergeIntervals m = new MergeIntervals();
        int[][] intervals = {{1,3},{2,6},{8,10},{15,18}};

        int[][] result = m.merge(intervals);
        for(int i=0; i<result.length; i++) {
            System.out.println(Arrays.toString(result[i]));
        }
    }
}
