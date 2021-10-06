import java.util.*;

class Trie {

	TrieNode root;

	private class TrieNode {
		Map<Character, TrieNode> children;
		boolean endofword;

		TrieNode() {
			children = new HashMap<Character, TrieNode>();
			endofword = false;
		} 
	}

	Trie() {
		root = new TrieNode();
	}

	void insert(String word) {
		TrieNode current = root; 
		for(int i=0; i<word.length(); i++) {
			
			char ch = word.charAt(i);

			TrieNode node = current.children.get(ch);
			if(node == null) {
				node = new TrieNode();
				current.children.put(ch, node);
			}

			current = node; 
		}

		current.endofword = true; // added the word successfully
	}

	boolean search(String word) {
		return searchUtil(root, word, 0);
	}

	boolean searchUtil(TrieNode current, String word, int i) {
		// base case	
		if(i==word.length()) 
			return current.endofword;

		char ch = word.charAt(i);
		TrieNode node = current.children.get(ch);

		if(node == null) 
			return false;

		return searchUtil(node, word, i+1);
	}

	public String dfs() {
		String ans = "";
		Stack<TrieNode> stack = new Stack<>();
		stack.push(root);

		while(!stack.isEmpty()) {
			TrieNode node = stack.pop();

			if(!node.endofword && )
		}

	}


	public static void main(String[] args) {
		Trie trie = new Trie();

		String[] words = {"abc"};

		for(String word : words) {
			trie.insert(word);
		}

		System.out.println(trie.search("abc")); // should be true
	}
}