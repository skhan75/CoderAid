import java.util.*;

public class WordBreak {

	Map<String, List<String>> dp = new HashMap<>();

	public List<String> wordBreak(String s, List<String> wordDict) {
		List<String> result = new ArrayList<>(); 

		if(dp.containsKey(s)) return dp.get(s);

		for(String word : wordDict) {

			if(s.length() < word.length()) {
				continue;
			}

			if(s.substring(0, word.length()).equals(word)) {
				
				if(word.length() == s.length()) {
					result.add(word);
				} else {
					List<String> tmp = wordBreak(s.substring(word.length()), wordDict);
					for(String t : tmp) {
						result.add(word + " " + t);
					}
				}
			} 
		}

		dp.put(s, result);

		return result;
	}


	public static void main(String[] args) {
		WordBreak wb = new WordBreak();
		String s = "catsanddog";
		List<String> wordDict = new ArrayList<String>();

		wordDict.add("cat");
		wordDict.add("cats");
		wordDict.add("and");
		wordDict.add("sand");
		wordDict.add("dog");

		System.out.println(wb.wordBreak(s, wordDict)); 
	}
}