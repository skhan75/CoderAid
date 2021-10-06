/*
Input
["WordDistance", "shortest", "shortest"]
[[["practice", "makes", "perfect", "coding", "makes"]], ["coding", "practice"], ["makes", "coding"]]

Output
[null, 3, 1]
*/

private String[] words;
public WordDistance(String[] words) {

	this.words = words;
}


public int shortest(String word1, String word2) {

	int l1 = -1, 
		l2 = -1;
	int minDistance = Integer.MAX_VALUE;

	for(int i=0; i<words.length; i++) {

		if(words[i].equals(word1))
			l1 = i;
		else if(words[i].equals(word2))
			l2 = i;

		if(l1!=-1 && l2!=-1)
			minDistance = Math.min(minDistance, Math.abs(l1-l2));
	}

	return minDistance;
}