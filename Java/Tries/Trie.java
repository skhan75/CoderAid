import java.util.*;

/*
The complexity of creating a trie is O(W*L), 
where W is the number of words, and L is an average length of the word: 
you need to perform L lookups on the average for each of the W words in the set.

Same goes for looking up words later: you perform L steps for each of the W words.

Hash insertions and lookups have the same complexity: 
for each word you need to check equality, 
which takes O(L), for the overall complexity of O(W*L).

If you need to look up entire words, hash table is easier. 
However, you cannot look up words by their prefix using a hash table;
If prefix-based lookups are of no interest to you, use a hash table; otherwise, use a trie.
*/
public class Trie {

	static class TrieNode {
		Map<Character, TrieNode> children;
		boolean isEndOfWord;

		TrieNode() {
			isEndOfWord = false;
			children = new HashMap<>();
		}
	}

	private final TrieNode root; 

	public Trie() {
		root = new TrieNode();
	}

	public void insert(String word) {
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
		current.isEndOfWord = true; 
	}


	public boolean search(String word) {
		TrieNode current = root; 

		for(int i=0; i<word.length(); i++) {
			char ch = word.charAt(i);

			TrieNode node = current.children.get(ch);

			if(node == null) {
				return false;
			}

			current = node; 
		}
		return current.isEndOfWord;
	}

	public boolean hasPrefix(String prefix) {
		TrieNode current = root; 

		for(int i=0; i<prefix.length(); i++) {
			char ch = prefix.charAt(i);

			TrieNode node = current.children.get(ch);

			if(node == null) {
				return false;
			}

			current = node; 
		}
		return true;
	}


	public static void main(String[] args) {
		Trie trie = new Trie();

		trie.insert("Hello");
		trie.insert("Kitty");
		trie.insert("Help");
		trie.insert("world");

		System.out.println(trie.search("Kitty")); // T
		System.out.println(trie.search("Hello")); // T
		System.out.println(trie.search("Kiit")); // F
		System.out.println(trie.search("Helpp")); // F
		System.out.println();
		System.out.println(trie.hasPrefix("Kit")); // T
		System.out.println(trie.hasPrefix("Hell")); // T
		System.out.println(trie.hasPrefix("tit")); // F
	}
}