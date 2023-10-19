#include <iostream>
#include <unordered_map>

using namespace std;

class KeyValueStore {
    unordered_map<string, string> store;     // main store
    unordered_map<string, string> transactionState;  // current transaction changes

    bool inTransaction = false;
    const string DELETED = "<DELETED>";

public:
    // Basic operations
    void set(const string &key, const string &value) {
        if (inTransaction) transactionState[key] = value;
        else  store[key] = value;
    }

    bool get(const string &key, string &value) {
        if (inTransaction && transactionState.count(key)) {
            if (transactionState[key] == DELETED) return false;
            value = transactionState[key];
            return true;
        }
        if (store.count(key) && store[key] != DELETED) {
            value = store[key];
            return true;
        }
        return false;
    }

    void deleteKey(const string &key) {
        if (inTransaction) {
            transactionState[key] = DELETED;
        } else {
            store.erase(key);
        }
    }

    // Transaction operations
    void begin() {
        if (inTransaction) {
            cout << "Already in a transaction. Commit or rollback the current one before starting a new one." << endl;
            return;
        }
        transactionState.clear();
        inTransaction = true;
    }

    void commit() {
        if (!inTransaction) {
            cout << "No transaction to commit!" << endl;
            return;
        }
        for (const auto &pair : transactionState) {
            if (pair.second == DELETED) {
                store.erase(pair.first);
            } else {
                store[pair.first] = pair.second;
            }
        }
        transactionState.clear();
        inTransaction = false;
    }

    void rollback() {
        if (!inTransaction) {
            cout << "No transaction to rollback!" << endl;
            return;
        }
        transactionState.clear();
        inTransaction = false;
    }
};

int main() {
    KeyValueStore kvStore;

    // Basic set and get operations without a transaction
    kvStore.set("a", "apple");
    kvStore.set("b", "banana");

    string value;
    if (kvStore.get("a", value)) {
        cout << "Value of 'a': " << value << endl; // Should print "apple"
    }

    // Start a transaction
    kvStore.begin();

    // Delete a key within a transaction
    kvStore.deleteKey("a");

    // The key "a" should not be retrievable during the transaction after the delete
    if (!kvStore.get("a", value)) {
        cout << "'a' not found during the transaction after delete." << endl;
    }

    // Rollback the transaction
    kvStore.rollback();

    // After rolling back, "a" should be retrievable again
    if (kvStore.get("a", value)) {
        cout << "Value of 'a' after rollback: " << value << endl; // Should print "apple"
    }

    // Start another transaction
    kvStore.begin();

    // Delete a key within the second transaction and add another key
    kvStore.deleteKey("b");
    kvStore.set("c", "cherry");

    // Commit the transaction
    kvStore.commit();

    // The key "b" should not be retrievable after the commit since it was deleted
    if (!kvStore.get("b", value)) {
        cout << "'b' not found after commit." << endl;
    }

    // "c" should be retrievable as it was added in the second transaction and then committed
    if (kvStore.get("c", value)) {
        cout << "Value of 'c': " << value << endl; // Should print "cherry"
    }

    return 0;
}
