#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

class DifferentialBackup {
private:
    unordered_map<string, string> datastore; // The main datastore where key-value pairs are held
    unordered_map<string, string> lastFullBackup; // A snapshot of the last full backup
    vector<unordered_map<string, string>> diffs;  // A list of differential backups since the last full backup

public:
    DifferentialBackup() {}

    void put(const string& key, const string& value) {
        datastore[key] = value;
    }

    void del(const string& key) {
        datastore.erase(key);
    }

    // Store the differences from the last full backup
    void backup() {
        unordered_map<string, string> currentDiff;
        
        for (const auto& [key, value] : datastore) {
            if (lastFullBackup.find(key) == lastFullBackup.end() || lastFullBackup[key] != value)
                currentDiff[key] = value;
        }

        // Add deletions to the diff
        for (const auto& [key, _] : lastFullBackup) {
            if (datastore.find(key) == datastore.end()) {
                currentDiff[key] = "";  // using an empty string to indicate deletion
            }
        }

        diffs.push_back(currentDiff);
    }

    void restore(int backupVersion) {
        if (backupVersion < 0 || backupVersion >= diffs.size()) {
            cout << "Invalid backup version" << endl;
            return;
        }

        datastore = lastFullBackup;
        for (int i = 0; i <= backupVersion; ++i) {
            for (const auto& [key, value] : diffs[i]) {
                if (value.empty()) {
                    datastore.erase(key);
                } else {
                    datastore[key] = value;
                }
            }
        }
    }

    void makeFullBackup() {
        lastFullBackup = datastore;
        diffs.clear();
    }

    string get(const string& key) {
        if (datastore.find(key) != datastore.end()) {
            return datastore[key];
        }
        return "Key not found";
    }
};

int main() {
    DifferentialBackup db;
    db.put("user1", "Alice");
    db.put("user2", "Bob");
    db.backup();

    db.put("user2", "Charlie");
    db.put("user3", "Dave");
    db.del("user1");
    db.backup();

    cout << "Current value of user2: " << db.get("user2") << endl;
    db.restore(0);
    cout << "Restored to Backup 0, value of user2: " << db.get("user2") << endl;
    db.restore(1);
    cout << "Restored to Backup 1, value of user2: " << db.get("user2") << endl;

    return 0;
}
