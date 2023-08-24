
#include <iostream>
#include <vector>
#include <stack>
#include <unordered_map>
#include <unordered_set>
using namespace std;

void topologicalSortUtil(int node, unordered_map<int, vector<int>> &graph, vector<bool> &visited, stack<int> &st) {
    visited[node] = true;
    for(int neighbor: graph[node]){
        if(!visited[neighbor]) 
            topologicalSortUtil(neighbor, graph, visited, st);
    }
    st.push(node);
}

vector<int> topologicalSort(unordered_map<int, vector<int>> &graph, int numNodes) {
    vector<bool> visited(numNodes, false);
    stack<int> st;
    for(auto& entry: graph) {
        int node = entry.first;
        if(!visited[node]){
            topologicalSortUtil(node, graph, visited, st);
        }
    }
    vector<int> result;
    while(!st.empty()) {
        result.push_back(st.top());
        st.pop();
    }
    return result;
}  

int main() {
    int numNodes = 6;
    unordered_map<int, vector<int>> graph;

    // Add edges to the graph
    graph[2].push_back(3);
    graph[3].push_back(1);
    graph[4].push_back(0);
    graph[4].push_back(1);
    graph[5].push_back(0);
    graph[5].push_back(2);

    vector<int> sortedNodes = topologicalSort(graph, numNodes);

    // Print the sorted order
    cout << "Topological Sort Order: ";
    for (int node : sortedNodes) {
        cout << node << " ";
    }
    cout << endl;

    return 0;
}
