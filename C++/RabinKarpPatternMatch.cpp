#include <iostream>
#include <vector>

// Function to search for a pattern within a text using Rabin-Karp algorithm
std::vector<int> rabinKarpSearch(const std::string &pattern, const std::string &text)
{
    std::vector<int> occurrences;

    int patternLength = pattern.length();
    int textLength = text.length();

    const int prime = 31;    // Prime number for hashing
    const int mod = 1e9 + 9; // Modulo value to avoid integer overflow

    // Calculate the highest power of prime raised to patternLength
    int patternPower = 1;
    for (int i = 0; i < patternLength - 1; ++i)
    {
        patternPower = (patternPower * prime) % mod;
    }

    // Calculate the hash values for pattern and the initial window in the text
    int patternHash = 0;
    int windowHash = 0;
    for (int i = 0; i < patternLength; ++i)
    {
        patternHash = (patternHash * prime + pattern[i]) % mod;
        windowHash = (windowHash * prime + text[i]) % mod;
    }

    // Iterate through each possible window in the text
    for (int i = 0; i <= textLength - patternLength; ++i)
    {
        // Check if the hash values match
        if (patternHash == windowHash)
        {
            // Check if the characters in the window match the pattern
            bool match = true;
            for (int j = 0; j < patternLength; ++j)
            {
                if (text[i + j] != pattern[j])
                {
                    match = false;
                    break;
                }
            }
            // If all characters match, add the starting index to occurrences
            if (match)
            {
                occurrences.push_back(i);
            }
        }

        // Update the window hash value for the next iteration
        if (i < textLength - patternLength)
        {
            windowHash = (prime * (windowHash - text[i] * patternPower) + text[i + patternLength]) % mod;
            if (windowHash < 0)
            {
                windowHash += mod;
            }
        }
    }

    return occurrences;
}

// Example usage
int main()
{
    std::string text = "ababcababcabc";
    std::string pattern = "abc";
    std::vector<int> occurrences = rabinKarpSearch(pattern, text);

    std::cout << "Pattern found at indices: ";
    for (int index : occurrences)
    {
        std::cout << index << " ";
    }
    std::cout << std::endl;

    return 0;
}
