#include <iostream>
#include <vector>
using namespace std;

vector<int> sumOfDistancesInTree(int n, vector<vector<int>> &edges)
{
    vector<vector<int>> adjList(n);
    vector<int> subtreeSize(n, 1);
    vector<int> answer(n, 0);

    // Create adjacency list
    for (vector<int> &edge : edges)
    {
        int u = edge[0], v = edge[1];
        adjList[u].push_back(v);
        adjList[v].push_back(u);
    }

    // Perform DFS to calculate subtree sizes
    calculateSubtreeSizes(0, -1, adjList, subtreeSize);

    // Perform DFS to calculate answer array
    calculateAnswer(0, -1, adjList, subtreeSize, answer, n);

    return answer;
}

// DFS to calculate subtree sizes
void calculateSubtreeSizes(int node, int parent, vector<vector<int>> &adjList, vector<int> &subtreeSize)
{
    for (int child : adjList[node])
    {
        if (child != parent)
        {
            calculateSubtreeSizes(child, node, adjList, subtreeSize);
            subtreeSize[node] += subtreeSize[child];
        }
    }
}

// DFS to calculate answer array
void calculateAnswer(int node, int parent, vector<vector<int>> &adjList, vector<int> &subtreeSize, vector<int> &answer, int n)
{
    for (int child : adjList[node])
    {
        if (child != parent)
        {
            answer[child] = answer[node] + (n - subtreeSize[child]) - subtreeSize[child];
            calculateAnswer(child, node, adjList, subtreeSize, answer, n);
        }
    }
}

// Main function
int main()
{
    int n = 6;
    vector<vector<int>> edges = {{0, 1}, {0, 2}, {2, 3}, {2, 4}, {2, 5}};

    vector<int> answer = sumOfDistancesInTree(n, edges);

    cout << "Sum of distances for each node:" << endl;
    for (int i = 0; i < n; i++)
    {
        cout << "Node " << i << ": " << answer[i] << endl;
    }

    return 0;
}