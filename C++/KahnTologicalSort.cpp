#include <iostream>
#include <vector>
#include <queue>
using namespace std;

vector<int> topologicalSort(vector<vector<int>>& graph) {
   
    vector<int> indegree(graph.size(), 0);

    // For every neighbor of every node, create an indegree
    // Calculate the in-degree (number of incoming edges) for each node in the graph
    // and store it in a data structure, such as an array or hash map.
    for(int i=0; i<graph.size(); i++) {
        for(int neighbor: graph[i])
            indegree[neighbor]++;
    }

    queue<int> q;
    vector<int> result;

    // Enqueue all nodes with an in - degree of 0 into the queue.
    for(int i=0; i<graph.size(); i++)
        if(indegree[i] == 0)
            q.push(i);

    while(!q.empty()) {
        int current = q.front();
        q.pop();
        result.push_back(current);

        // Process neighbors of the current node
        for(int neighbor: graph[current]) {
            // Reduce the indegree of this neighbor because it has been explored
            indegree[neighbor]--;
            // Enqueue the neighbor if the indegree becomes 0
            if(indegree[neighbor] == 0)
                q.push(neighbor);
        }
    }

    // Check if the graph contains cycles
    // If the number of nodes in the "result" list is equal to the total number of nodes in the graph, 
    // then the graph is a DAG, and the "result" list represents a valid topological ordering. 
    // Otherwise, the graph contains cycles and cannot be topologically sorted.
    if(result.size() != graph.size()) {
        return {};
    }

    return result;
}

int main() {
    int numNodes = 6;
    vector<vector<int>> graph(numNodes);
    vector<int> inDegree(numNodes, 0);

    // Add directed edges to the graph
    graph[2].push_back(3);
    graph[3].push_back(1);
    graph[4].push_back(0);
    graph[4].push_back(1);
    graph[5].push_back(0);
    graph[5].push_back(2);

    vector<int> sortedNodes = topologicalSort(graph);

    // Print the topological sort order
    cout << "Topological Sort Order: ";
    for (int node : sortedNodes) {
        cout << node << " ";
    }
    cout << endl;

    return 0;
}