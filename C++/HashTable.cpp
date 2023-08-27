#include <iostream>
#include <vector>
#include <list>
#include <string>

using namespace std;

template <typename K, typename V>
class HashNode {
public:
    K key;
    V value;
    HashNode(const K &key, const V &value) : key(key), value(value) {}
};

template <typename K, typename V>
class HashTable {
    vector<list<HashNode<K, V>>> table;
    size_t totalSize;
    
    size_t _hash(const K &key) const {
        return hash<K>{}(key) % totalSize;
    }

public:
    HashTable(size_t size) : totalSize(size), table(size) {}

    void insert(const K &key, const V &value) {
        size_t hashIndex = _hash(key);
        HashNode<K, V> node(key, value);
        table[hashIndex].push_back(node);
    }

    bool get(const K &key, V &value) {
        size_t hashIndex = _hash(key);
        for (const auto &node : table[hashIndex]) {
            if (node.key == key) {
                value = node.value;
                return true;
            }
        }
        return false;
    }

    bool remove(const K &key) {
        size_t hashIndex = _hash(key);
        for (auto it = table[hashIndex].begin(); it != table[hashIndex].end(); ++it) {
            if (it->key == key) {
                table[hashIndex].erase(it);
                return true;
            }
        }
        return false;
    }
};

// Testing
int main() {
    HashTable<string, int> h(100);
    h.insert("Alice", 25);
    h.insert("Bob", 30);
    h.insert("Charlie", 35);

    int value;
    if (h.get("Alice", value)) cout << "Alice: " << value << endl;
    if (h.get("John", value)) cout << "John: " << value << endl;
    if (h.get("Charlie", value)) cout << "Charlie: " << value << endl;
}
