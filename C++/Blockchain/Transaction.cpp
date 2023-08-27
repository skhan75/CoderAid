/**
 *  Problem: Transaction Pool Optimization

    Background:
    -----------
    In a blockchain-based system, transactions that are initiated by users are collected in a pool before they are added to a block and committed to the blockchain. Due to hardware and network constraints, only a limited number of transactions can be added to a block at a time. For this reason, transactions in the pool may need to be prioritized based on certain criteria.

    Task:
    -----
    You are given a list of transactions in the transaction pool. Each transaction has:

    transactionID: A unique identifier for the transaction.
    fee: The transaction fee (intrinsic value of processing the transaction).
    weight: A measure of computational 'weight' or complexity of the transaction.
    Design an algorithm that selects a subset of transactions to be added to the next block such that:

    The combined weight of the selected transactions is below a given threshold maxWeight.
    The total fee from the selected transactions is maximized.
    Return the list of transactionIDs for the selected transactions.

    Function Signature:
    vector<int> prioritizeTransactions(vector<Transaction> transactions, int maxWeight);
*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Transaction {
    int transactionID;
    int fee;
    int weight;
};

vector<int> prioritizeTransactions(const vector<Transaction>& transactions, int maxWeight) {
    int n = transactions.size();

    vector<vector<int>> dp(n, vector<int>(maxWeight+1, 0));

    for (int i = 0; i < n; i++) {
        for (int w = 0; w <= maxWeight; w++) {
            if (i > 0) dp[i][w] = dp[i-1][w];  // Start by not including the i-th transaction
            if (transactions[i].weight <= w) 
                dp[i][w] = max(dp[i][w], (i > 0 ? dp[i-1][w-transactions[i].weight] : 0) + transactions[i].fee);
        }
    }

    vector<int> selectedTransactions;
    int w = maxWeight;
    for (int i = n-1; i >= 0 && w > 0; i--) {
        if (i == 0 || dp[i][w] != dp[i-1][w]) {
            selectedTransactions.push_back(transactions[i].transactionID);
            w -= transactions[i].weight;
        }
    }
    reverse(selectedTransactions.begin(), selectedTransactions.end());

    return selectedTransactions;
}

vector<vector<int>> memo;
int prioritizeTransactionsRecursive(const vector<Transaction>& transactions, int index, int remainingWeight) {
    // Base cases
    if (index == transactions.size() || remainingWeight == 0) return 0;

    // If this subproblem is already solved, return the answer
    if (memo[index][remainingWeight] != -1) return memo[index][remainingWeight];
    
    // Exclude the current transaction
    int excludeTransaction = prioritizeTransactionsRecursive(transactions, index + 1, remainingWeight);

    int includeTransaction = 0;
    if (transactions[index].weight <= remainingWeight) {
        includeTransaction = transactions[index].fee + prioritizeTransactionsRecursive(transactions, index + 1, remainingWeight - transactions[index].weight);
    }

    // Store the result and return
    return memo[index][remainingWeight] = max(excludeTransaction, includeTransaction);
}

int main() {
    vector<Transaction> transactions = {
        {1, 5, 3},
        {2, 2, 1},
        {3, 8, 6},
        {4, 3, 2}
    };
    int maxWeight = 7;
    vector<int> result = prioritizeTransactions(transactions, maxWeight);
    for (int id : result) {
        cout << id << " ";
    }

    vector<Transaction> transactions = {
        {5, 3},
        {2, 1},
        {8, 6},
        {3, 2}
    };
    int resultRecursive = prioritizeTransactionsRecursive(transactions, 0, maxWeight);
    cout << resultRecursive;
    return 0;
}
