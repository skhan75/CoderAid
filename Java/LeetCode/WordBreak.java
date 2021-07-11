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


	public static void main(String[] args) {
		WordBreak wb = new WordBreak();
		String s = "leetcode";
		List<String> wordDict = new ArrayList<String>();

		wordDict.add("leet");
		wordDict.add("code");

		System.out.println(wb.wordBreakBfs(s, wordDict)); 
	}
}