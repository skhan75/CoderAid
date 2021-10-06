public class MinimumDifficultyJob {
	public int minDifficulty(int[] jobDifficulty, int d) {
        int numjobs = jobDifficulty.length;
        
        if(numjobs < d) return -1;
        
        int[][] dp = new int[d][numjobs]; // days,jobs
        
        
        dp[0][0] = jobDifficulty[0];
        
        // For day = 1, the minimum difficult job would be the max difficult job in that row
        for(int i=1; i<numjobs; ++i) {
            dp[0][i] = Math.max(dp[0][i-1], jobDifficulty[i]);
        }
        
        for(int day=1; day<d; ++day) {
            for(int job=1; job<numjobs; ++job) {
                dp[day][job] = Integer.MAX_VALUE;
                int lastDayDifficulty = jobDifficulty[job];
                
                // For a given day-job, what is that partition i, that gives us the Minimum of maxium sum of difficulties
                for(int i=job; i>=day; --i) {
                    lastDayDifficulty = Math.max(lastDayDifficulty, jobDifficulty[i]);
                    dp[day][job] = Math.min(dp[day][job], dp[day-1][i-1] + lastDayDifficulty);
                }
            }
        }
        
        return dp[d-1][numjobs-1];
        
    }

    public static void main(String[] args) {
    	MinimumDifficultyJob m = new MinimumDifficultyJob();
    	int[] jobDifficulty = {6,5,4,3,2,1};
    	System.out.println(m.minDifficulty(jobDifficulty, 2));
    }
}