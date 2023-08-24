#include <unordered_map>
#include <iostream>

using namespace std;

int lengthOfLongestSubstring(string s) {
    int n = s.size();
    int left=0, right=0, ans=0;
    unordered_map<char, int> map;

    // sliding the right poointer until no duplicate is found
    while(right < n) {
        char r_ch = s[right];
        map[r_ch]++;
        // Now we slide left until r_ch's count is > 1 in left side of window
        while(map[r_ch] > 1) {
            char l_ch = s[left];
            map[l_ch]--;
            left++;
        }
        ans = max(ans, right-left+1);
        right++;
    }
    return ans;
}

int main() {
    string s = "abcabcbb";
    cout << lengthOfLongestSubstring(s) << endl;
    return 0;
}



/**       L R
 *  a b c a c c b b
 * 
 * 
 * 
 * map (
 *  a: 1
 *  b: 0
 *  c: 1
 * )
*/