#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <map>
#include <iomanip>

using namespace std;

class HashLibrary {
private:
    map<string, string> hashStorage; // key value storage for hashes
    string computeHash(const string& data) {
        unsigned long long total = 0;
        int prime = 31;

        for(char c : data) total = total * prime + c;

        stringstream ss;
        ss << hex << total;
        string result(ss.str());

        // Adding extra padding for fixed length output
        while(result.length() < 32) result = "0" + result;

        return result.substr(0, 32);
    }

public:
    string hashString(const string& input) {
        return computeHash(input);
    }

    string hashFile(const string& filename) {
        ifstream file(filename);
        if (!file.is_open()) throw runtime_error("Could not open file.");
        stringstream contentStream;
        contentStream << file.rdbuf();
        file.close();

        return computeHash(contentStream.str());
    }

    bool verifyString(const string& input, const string& hash) {
        return computeHash(input) == hash;
    }

    bool verifyFile(const string& filename, const string& hash) {
        return hashFile(filename) == hash;
    }

    void storeHash(const string& id, const string& hash) {
        hashStorage[id] = hash;
    }

    string retrieveHash(const string& id) {
        if (hashStorage.find(id) == hashStorage.end()) throw runtime_error("ID not found.");
        return hashStorage[id];
    }
};

int main() {
    HashLibrary hasher;
    string hash = hasher.hashString("Hello, World!");
    hasher.storeHash("greeting", hash);

    cout << "Hash of 'Hello, World!': " << hash << endl;
    cout << "Hash retrieved with ID 'greeting': " << hasher.retrieveHash("greeting") << endl;
    cout << "Verification of 'Hello, World!': " << hasher.verifyString("Hello, World!", hash) << endl;

    return 0;
}