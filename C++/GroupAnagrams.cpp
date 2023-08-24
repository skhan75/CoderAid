#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

vector<vector<string>> groupAnagrams(vector<string> &words)
{
    unordered_map<string, vector<string>> anagramGroups;

    // Group words by their sorted version
    for (const string &word : words)
    {
        string sortedWord = word;
        sort(sortedWord.begin(), sortedWord.end());
        anagramGroups[sortedWord].push_back(word);
    }

    // Convert the hashmap values to the final result
    vector<vector<string>> result;
    for (const auto &pair : anagramGroups)
    {
        result.push_back(pair.second);
    }

    return result;
}

int main()
{
    vector<string> words = {"cat", "dog", "tac", "god", "act"};

    vector<vector<string>> anagramGroups = groupAnagrams(words);

    // Print the anagram groups
    for (const auto &group : anagramGroups)
    {
        for (const string &word : group)
        {
            cout << word << " ";
        }
        cout << endl;
    }

    return 0;
}