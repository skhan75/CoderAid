import java.util.*;

public class WordBreak {

	public boolean wordBreakBfs(String s, List<String> wordDict) {

		Queue<Integer> queue = new LinkedList<Integer>();
		boolean[] visited = new boolean[s.length()];

		queue.add(0);
		
		while(!queue.isEmpty()) {

			int start = queue.poll();
			
			for(int end=start+1; end<=s.length(); end++) {
				if(wordDict.contains(s.substring(start, end))){
					queue.add(end);
					if(end == s.length()) {
						return true;
					}
				}
			}
			visited[start] = true;
		}

		return false;
	}

	public boolean wordBreakDP(String s, List<String> wordDict) {

		boolean[] dp = new boolean[s.length()+1];
		Arrays.fill(dp, false);

		// Null string is always present in the dictionary
		dp[0] = true;

		for(int i=1; i<=s.length(); i++) {
			for(int j=0; j<i; j++) {
				if(dp[j] && wordDict.contains(s.substring(j, i))) {
					dp[i] = true;
				}
			}
		}

		return dp[s.length()];
	}


	public static void main(String[] args) {
		WordBreak wb = new WordBreak();
		String s = "leetcode";
		List<String> wordDict = new ArrayList<String>();

		wordDict.add("leet");
		wordDict.add("code");

		System.out.println(wb.wordBreakBfs(s, wordDict)); 
		System.out.println(wb.wordBreakDP(s, wordDict)); 
	}
}