#include <iostream>
#include <vector>
#include <queue>
#include <limits>

using namespace std;

const int INF = numeric_limits<int>::max();

int minCost(int maxTime, vector<vector<int>> &edges, vector<int> &passingFees)
{
    int n = passingFees.size();

    // Create adjacency list to represent the graph
    vector<vector<pair<int, int>>> graph(n);
    for (const auto &edge : edges)
    {
        int u = edge[0];
        int v = edge[1];
        int time = edge[2];
        graph[u].emplace_back(v, time);
        graph[v].emplace_back(u, time);
    }

    // Create a 2D DP table to store the minimum cost
    vector<vector<int>> dp(n, vector<int>(maxTime + 1, INF));

    // Create a priority queue for Dijkstra's algorithm
    priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, greater<>> pq;

    // Push the starting city (0) with time 0 and cost 0
    pq.push({0, {0, 0}});
    dp[0][0] = passingFees[0];

    // Dijkstra's algorithm
    while (!pq.empty())
    {
        int cost = pq.top().first;
        int u = pq.top().second.first;
        int time = pq.top().second.second;
        pq.pop();

        // Skip if the cost or time exceeds the maximum
        if (cost > dp[u][time] || time > maxTime)
            continue;

        // Explore neighbors of the current city
        for (const auto &neighbor : graph[u])
        {
            int v = neighbor.first;
            int travelTime = neighbor.second;

            int newTime = time + travelTime;
            int newCost = cost + passingFees[v];

            // Update DP table and enqueue the neighbor if a better cost is found
            if (newTime <= maxTime && newCost < dp[v][newTime])
            {
                dp[v][newTime] = newCost;
                pq.push({newCost, {v, newTime}});
            }
        }
    }

    // Find the minimum cost from any time <= maxTime at the destination city (n - 1)
    int minCost = INF;
    for (int time = 0; time <= maxTime; time++)
    {
        minCost = min(minCost, dp[n - 1][time]);
    }

    return (minCost == INF) ? -1 : minCost;
}

int main()
{
    int maxTime = 30;
    vector<vector<int>> edges = {{0, 1, 10}, {1, 2, 10}, {2, 5, 10}, {0, 3, 1}, {3, 4, 0}, {4, 5, 15}};
    vector<int> passingFees = {5, 1, 2, 20, 20, 3};

    int result = minCost(maxTime, edges, passingFees);
    cout << "Minimum cost: " << result << endl;

    return 0;
}