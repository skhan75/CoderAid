#include <unordered_map>
#include <vector>
#include <string>
#include <iostream>

using namespace std;

class Database {
    unordered_map<string, string> kvStore;              // key-value store
    vector<unordered_map<string, string>> transactions; // Stack of transaction data

public:
    /**
     * Adds a key-value pair to the database
     * transactions.back() retrieves the last (i.e., most recent, or 'back' of the vector)
     * The purpose of storing changes in a transaction instead of directly in the database
     * is to provide atomicity and isolation, which are crucial properties of database transactions.
     * */
    void set(string key, string value) {
        if (!transactions.empty()) // If there is a transaction in progress
            transactions.back()[key] = value; // Save change in the current transaction data
        else 
            kvStore[key] = value; // If no transaction, save directly to the store. 
    }

    // Returns the value for a given key if it exists
    string get(string key) {
        if (!transactions.empty()) {    // If there is a transaction in progress
            auto it = transactions.back().find(key); // Find key in the current transaction data
            if (it != transactions.back().end())     // If key was found
                return it->second;                   // Return its value
        }
        // If no transaction or key not found in transaction, return value from main database
        return kvStore[key];
    }

    // Deletes a key-value pair from the database
    void delete_key(string key) {
        if (!transactions.empty()) // If there is a transaction in progress
            transactions.back().erase(key); // Delete key from the current transaction data
        else kvStore.erase(key); // If no transaction, delete directly from the database
    }

    // Begins a new transaction
    void begin() {
        transactions.push_back(unordered_map<string, string>()); // Add a new transaction to the stack
    }

    // Rolls back the most recent transaction
    void rollback() {
        if (!transactions.empty()) // If there is a transaction in progress
            transactions.pop_back(); // Remove the most recent transaction
        else throw runtime_error("No transaction to rollback");
    }

    // Commits all transactions
    void commit() {
        if (!transactions.empty()) { // If there is a transaction in progress
            for (auto &transaction : transactions) // For each transaction
                for (auto &kv : transaction)  // For each key-value pair in the transaction
                    kvStore[kv.first] = kv.second; // Add the key-value pair to the main database
            transactions.clear(); // Clear all transactions
        }
        else throw runtime_error("No transaction to commit");
    }
};

int main() {
    Database db;

    // Set some key-value pairs
    db.set("Hello", "World");
    db.set("AI", "OpenAI");
    cout << db.get("Hello") << endl; // Outputs: World
    cout << db.get("AI") << endl;    // Outputs: OpenAI

    // Start a transaction
    db.begin();
    db.set("Hello", "OpenAI");
    cout << db.get("Hello") << endl; // Outputs: OpenAI (changed in transaction)

    // Rollback the transaction
    db.rollback();
    cout << db.get("Hello") << endl; // Outputs: World (change was rolled back)

    // Start a new transaction
    db.begin();
    db.set("Hello", "OpenAI");
    cout << db.get("Hello") << endl; // Outputs: OpenAI (changed in transaction)

    // Commit the transaction
    db.commit();
    cout << db.get("Hello") << endl; // Outputs: OpenAI (change was committed)

    // Delete a key
    db.delete_key("AI");
    cout << db.get("AI") << endl; // Outputs: (nothing)

    return 0;
}
