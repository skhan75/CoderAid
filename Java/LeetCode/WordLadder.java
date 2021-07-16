import java.util.*;

public class WordLadder {

	static class Pair<U,V> {
		U key; 
		V value;

		Pair(U a, V b) {
			this.key = a;
			this.value = b;
		}

		U getKey() {
			return this.key;
		}
		V getValue() {
			return this.value;
		}
	}
	
	public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        
        Map<String, List<String>> allCombosDict = new HashMap<>();
        int n = beginWord.length();


        System.out.println("-->"+beginWord.substring(0,1));
        
        for(String word : wordList) {
            for(int i=0; i<word.length(); i++) {
           		String newWord = word.substring(0,i)+"*"+word.substring(i+1, n);
           		List<String> transformations = allCombosDict.getOrDefault(newWord, new ArrayList<>());
           		transformations.add(word);
           		allCombosDict.put(newWord, transformations);
            }
        }

        allCombosDict.entrySet().forEach(entry -> {
		    System.out.println("| "+entry.getKey() + " : " + entry.getValue()+" |");
		});

        // Now we BFS 
        Queue<Pair<String, Integer>> queue = new LinkedList<>();
        queue.add(new Pair(beginWord, 1));

        Map<String, Boolean> visited = new HashMap<>();
        visited.put(beginWord, true);

        while(!queue.isEmpty()) {

        	Pair<String, Integer> node = queue.remove();
        	String currentWord = node.getKey();
        	int currentLevel = node.getValue();

        	for(int i=0; i<n; i++) {

        		// Immediate words for the current word
        		String newWord = currentWord.substring(0,i)+"*"+currentWord.substring(i+1, n);
        		
        		// Next iterate all the neihbors that can be formed from the current new word
        		for(String neighborWord : allCombosDict.getOrDefault(newWord, new ArrayList<>())) {
        			// If any of the neighbor word matched the end word, we return that level + 1
        			if(neighborWord.equals(endWord)) {
        				return currentLevel+1;
        			}

        			// Else we add it the queue and look for other intermediate words
        			if(!visited.containsKey(neighborWord)) {
        				queue.add(new Pair(neighborWord, currentLevel+1));
        				visited.put(neighborWord, true);
        			}
        		}
        	}
        }
        return 0;
    }

	public static void main(String[] args) {
		WordLadder wl = new WordLadder();

		List<String> wordList = new ArrayList<>();
		wordList.add("hot");
		wordList.add("dot");
		wordList.add("dog");
		wordList.add("lot");
		wordList.add("log");
		wordList.add("cog");

		System.out.println(wl.ladderLength("hit", "cog", wordList));
	}
}