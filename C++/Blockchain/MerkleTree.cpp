/**
 * A Merkle Tree is a binary tree in which every leaf node is labelled with cryptographic hash
 * of a data block, and every non leaf node is labelled with the cryptographic hash of the labels 
 * of its child nodes.
*/
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <iomanip>
#include <openssl/sha.h>

using namespace std;

class MerkleTree {

private:
    vector<string> transactions;
    vector<string> tree;

    // Helper to compute a SHA256 hash
    string sha256(const string& data) {
        unsigned char hash[SHA224_DIGEST_LENGTH]; // used to store the resulting hash
        SHA256_CTX sha256;
        SHA256_Init(&sha256);
        SHA256_Update(&sha256, data.c_str(), data.size());
        SHA256_Final(hash, &sha256);

        stringstream ss;
        for(int i=0; i<SHA224_DIGEST_LENGTH; i++)
            ss << hex << setw(2) << setfill('0') << (int)hash[i];

        return ss.str();
    }

    // Recursive function to build Merkle Tree
    void buildTree(int pos, int l, int r) {
        if(l == r) {
            tree[pos] = sha256(transactions[l]);
            return;
        }
        int mid = (l + r) / 2;
        buildTree(2*pos+1, l, mid); // build left child
        buildTree(2*pos+2, mid+1, r); // build right child
        tree[pos] = sha256(tree[2*pos+1] + tree[2*pos+2]); // build the root
    }

   

public:
    // Constructor takes a list of transactions and builds the tree
    MerkleTree(const vector<string>& transactions) : transactions(transactions) {
        tree.resize(2*transactions.size()-1);
        buildTree(0, 0, transactions.size()-1);
    }

    string getRoot() {
        return tree[0];
    }

    // Get a Merkle proof for a given transaction index
    vector<string> getProof(int idx) {
        vector<string> proof;
        int pos = transactions.size() - 1 + idx;
        while(pos) {
            if(pos%2 == 0) proof.push_back(tree[pos - 1]);
            else proof.push_back(tree[pos + 1]);
            pos = (pos-1)/2;
        }
        return proof;
    }

    bool verifyProof(const string& tx, const vector<string>& proof) {
        string hash = sha256(tx);
        for (const auto& sibling : proof) {
            hash = sha256(hash + sibling);
        }
        return hash == getRoot();
    }


};

int main() {
    vector<string> transactions = {"tx1", "tx2", "tx3", "tx4"};
    MerkleTree mt(transactions);

    cout << "Merkle Root: " << mt.getRoot() << endl;

    int idx = 2;
    vector<string> proof = mt.getProof(idx);
    cout << "Merkle Proof for transaction " << idx + 1 << ":" << endl;
    for (const auto& p : proof) cout << p << endl;

    if (mt.verifyProof(transactions[idx], proof)) cout << "Proof is valid!" << endl;
    else cout << "Proof is invalid!" << endl;

    return 0;
}