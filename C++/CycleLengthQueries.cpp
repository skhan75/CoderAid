#include <iostream>
#include <vector>

int getParent(int node)
{
    return node / 2;
}

int getLeftChild(int node)
{
    return 2 * node;
}

int getRightChild(int node)
{
    return 2 * node + 1;
}

int getDistance(int u, int v)
{
    int distance = 1;
    while (u != v)
    {
        if (u > v)
        {
            u = getParent(u);
        }
        else
        {
            v = getParent(v);
        }
        distance++;
    }
    return distance;
}

std::vector<int> cycleLengthQueries(int n, const std::vector<std::vector<int>> &queries)
{
    std::vector<int> result;

    for (const auto &query : queries)
    {
        int u = query[0];
        int v = query[1];

        int distance = getDistance(u, v);
        result.push_back(distance);
    }

    return result;
}

int main()
{
    int n = 3;
    std::vector<std::vector<int>> queries = {{5, 3}, {4, 7}, {2, 3}};

    std::vector<int> result = cycleLengthQueries(n, queries);

    for (int res : result)
    {
        std::cout << res << " ";
    }
    std::cout << std::endl;

    return 0;
}
