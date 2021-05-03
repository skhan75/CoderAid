/**
    Given a string s, find the length of the longest substring without repeating characters.

     
    Example 1:

    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.
    Example 2:

    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.
    Example 3:

    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
    Example 4:

    Input: s = ""
    Output: 0
     

    Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.
**/
import java.util.HashSet;

public class LengthOfLongestSubstring {

    public int getLengthOfLongestSubstring(String s) {
        int i = 0; // pointer of the pivot
        int j = 0; // pointer of the slider index
        int max = 0; // max result

        HashSet<Character> set = new HashSet<Character>();

        // move the slider till the end of the string
        while(j < s.length()) {

            // If its a unique character in the sequence
            if(!set.contains(s.charAt(j))) {
                set.add(s.charAt(j));
                j++;

                max = Math.max(max, set.size());
            } else {
                set.remove(s.charAt(i));
                i++;
            }
        }
        return max;
    }

    public static void main(String[] args) {
        LengthOfLongestSubstring lengthOfLongestSubstring = new LengthOfLongestSubstring();
        System.out.println("Maximum length of longest substring is "+ lengthOfLongestSubstring.getLengthOfLongestSubstring("abcabcab"));
    }
}

