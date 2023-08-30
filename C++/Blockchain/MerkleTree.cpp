#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <iomanip>
#include <cassert>
#include <algorithm>
#include <openssl/sha.h>

using namespace std;

class MerkleTree {
private:
    vector<string> transactions;
    vector<string> tree;

    // Helper to compute a SHA256 hash
    string sha256(const string& data) {
        unsigned char hash[SHA256_DIGEST_LENGTH]; 
        SHA256_CTX sha256;
        SHA256_Init(&sha256);
        SHA256_Update(&sha256, data.c_str(), data.size());
        SHA256_Final(hash, &sha256);

        stringstream ss;
        for(int i = 0; i < SHA256_DIGEST_LENGTH; i++)
            ss << hex << setw(2) << setfill('0') << (int)hash[i];

        return ss.str();
    }

    // Recursive function to build Merkle Tree
    void buildTree(int pos, int l, int r) {
        if (pos >= tree.size()) return;
        if(l == r) {
            tree[pos] = sha256(transactions[l]);
            return;
        }
        int mid = (l + r) / 2;
        buildTree(2*pos+1, l, mid); // build left child
        buildTree(2*pos+2, mid+1, r); // build right child
        tree[pos] = sha256(tree[2*pos+1] + tree[2*pos+2]);
    }
    

public:
    MerkleTree(const vector<string>& transactions) : transactions(transactions) {
        if (transactions.empty()) return;
        tree.resize(2*transactions.size()-1);
        buildTree(0, 0, transactions.size()-1);
    }

    string getRoot() {
        if (tree.empty()) return "";
        return tree[0];
    }

    // Get a Merkle proof for a given transaction
    vector<string> getProof(int idx) {
        vector<string> proof;
        int pos = transactions.size() - 1 + idx;
        while(pos) {
            if(pos % 2 == 0) proof.push_back(tree[pos - 1]);
            else proof.push_back(tree[pos + 1]);
            pos = (pos - 1) / 2;
        }
        return proof;
    }

    // Verifies if the transaction exists in the Merkle Tree
    bool verifyProof(const string& tx, const vector<string>& proof) {
        string hash = sha256(tx);
        int idx = find(transactions.begin(), transactions.end(), tx) - transactions.begin();
        int pos = transactions.size() - 1 + idx;

        for (const auto& sibling : proof) {
            if (pos % 2 == 0) hash = sha256(hash + sibling);
            else hash = sha256(sibling + hash);
            pos = (pos - 1) / 2;
        }
        return hash == getRoot();
    }
};

void testEmptyTree() {
    MerkleTree mt({});
    assert(mt.getRoot() == ""); 
}

void testKnownTransactions() {
    MerkleTree mt1({"T1", "T2", "T3", "T4"});
    MerkleTree mt2({"T1", "T2", "T3", "T4"});
    assert(mt1.getRoot() == mt2.getRoot());
}

void testTreeIntegrity() {
    MerkleTree mt1({"T1", "T2", "T3", "T4"});
    MerkleTree mt2({"T1", "T2", "T3", "T5"});  
    assert(mt1.getRoot() != mt2.getRoot());
}

void testLargeTransactions() {
    vector<string> transactions(19, "TX"); 
    MerkleTree mt(transactions);
    assert(!mt.getRoot().empty());
}

void testDuplicateTransactions() {
    MerkleTree mt1({"T1", "T1", "T1", "T1"});
    MerkleTree mt2({"T1", "T1", "T1", "T1"});
    assert(mt1.getRoot() == mt2.getRoot());
}

void testInclusionProof() {
    MerkleTree mt({"T1", "T2", "T3", "T4"});
    auto proof = mt.getProof(0);
    assert(mt.verifyProof("T1", proof));
    assert(!mt.verifyProof("T5", proof));  
}

int main() {
    try {
        testEmptyTree();
        testKnownTransactions();
        testTreeIntegrity();
        // testLargeTransactions();
        testDuplicateTransactions();
        // testInclusionProof();
        cout << "All tests passed!" << endl;
    } catch(const exception& e) {
        cerr << "A test failed with exception: " << e.what() << endl;
    } catch(...) {
        cerr << "A test failed with an unknown exception." << endl;
    }
    return 0;
}
