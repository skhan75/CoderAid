#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <iomanip>
#include <openssl/sha.h>

using namespace std;

class Block {

private:
    string prevHash;
    string blockHash;
    vector<string> transactions;

    // Helper to compute SHA256 hash
    string sha256(const string& data) {
        unsigned char hash[SHA256_DIGEST_LENGTH];
        SHA256_CTX sha256;
        SHA256_Init(&sha256);
        SHA256_Update(&sha256, data.c_str(), data.size());
        SHA256_Final(hash, &sha256);

        stringstream ss;
        for (int i = 0; i < SHA256_DIGEST_LENGTH; i++)
            ss << hex << setw(2) << setfill('0') << (int)hash[i];

        return ss.str();
    }

public:
    Block(string prevHash, vector<string> transactions) : prevHash(prevHash), transactions(transactions) {
        string txString;
        for(const auto& tx : transactions) txString += tx;
        blockHash = sha256(prevHash + txString);
    }

    string getBlockHash() const {
        return blockHash;
    }

    string getPrevHash() const {
        return prevHash;
    }

    vector<string> getTransactions() {
        return transactions;
    }
};


class SimpleBlockchain {

private:
    vector<Block> chain;
    // For test purposes
    friend void tamperLastBlock(SimpleBlockchain &bc, const vector<string> &transactions);

public:
    SimpleBlockchain() {
        // Add Genesis block
        chain.emplace_back("0", vector<string>{"Genesis Block"});
    }

    void addBlock(vector<string> transactions) {
        string prevHash = (chain.empty()) ? "" : chain.back().getBlockHash();
        Block newBlock(prevHash, transactions);
        chain.push_back(newBlock);
    }

    bool verifyIntegrity() const {
        for(size_t i=1; i<chain.size(); i++) 
            if(chain[i].getPrevHash() != chain[i-1].getBlockHash()) return false;
        return true;
    }
};

void tamperLastBlock(SimpleBlockchain& bc, const vector<string>& transactions) {
    if(bc.chain.empty()) return;
    string incorrectPrevHash = "INCORRECT_HASH_VALUE";
    Block tamperedBlock(incorrectPrevHash, transactions);
    bc.chain.back() = tamperedBlock;  // Tamper the last block directly
}

int main() {
    SimpleBlockchain bc;
    bc.addBlock({"TX1", "TX2"});
    bc.addBlock({"TX3", "TX4"});

    // Check blockchain integrity before tampering
    if (bc.verifyIntegrity()) {
        cout << "Blockchain is valid!" << endl;
    } else {
        cout << "Blockchain has been tampered with!" << endl;
    }

  // Now, let's simulate tampering by modifying a block directly.
    tamperLastBlock(bc, {"TX5", "TX6"});

    // Check blockchain integrity after tampering
    if (bc.verifyIntegrity()) {
        cout << "Blockchain is valid!" << endl;
    } else {
        cout << "Blockchain has been tampered with!" << endl;
    }
    return 0;
}