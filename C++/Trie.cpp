#include <iostream>
#include <unordered_map>

using namespace std;

struct TrieNode {
    // Mapping from character to the next node
    unordered_map<char, TrieNode*> children;
    // To mark the end of a word
    bool isEndOfWord;

    TrieNode() : isEndOfWord(false) {}
};

class Trie {
private:
    TrieNode* root;
    
public:
    Trie() {
        root = new TrieNode();
    }

    // Insert a word into the Trie
    void insert(string word) {
        TrieNode* curr = root;
        for (char c : word) {
            if (curr->children.find(c) == curr->children.end()) 
                curr->children[c] = new TrieNode();
            curr = curr->children[c];
        }
        curr->isEndOfWord = true;
    }

    // Search for a word in the Trie
    bool search(string word) {
        TrieNode* curr = root;
        for (char c : word) {
            if (curr->children.find(c) == curr->children.end()) return false;
            curr = curr->children[c];
        }
        return curr->isEndOfWord;
    }

    // Check if there's any word in the Trie that starts with the given prefix
    bool startsWith(string prefix) {
        TrieNode* curr = root;
        for (char c : prefix) {
            if (curr->children.find(c) == curr->children.end()) return false;
            curr = curr->children[c];
        }
        return true;
    }

    // Destructor to clean up memory
    ~Trie() {
        // Recursive delete can be used to delete all nodes
        clear(root);
    }

private:
    void clear(TrieNode* node) {
        for (auto &pair : node->children) clear(pair.second);
        delete node;
    }
};

int main() {
    Trie trie;
    trie.insert("apple");
    cout << trie.search("apple") << endl;    // Returns true
    cout << trie.search("app") << endl;      // Returns false
    cout << trie.startsWith("app") << endl;  // Returns true
    trie.insert("app");
    cout << trie.search("app") << endl;      // Returns true
    return 0;
}
