"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
"""
from collections import Counter

def minimum_window_substring(s, t):

    if not t or not s:
        return ""

    if len(s) < len(t):
        return ""

    # Store the count of t in a lookup table
    t_map = Counter(t)

    # Required no of elements to represent a t (pattern)
    required = len(t_map)

    # Filter all the characters from s thats in t into a new list along with their index
    filtered_s = []
    for i, ch in enumerate(s):
        if ch in t_map:
            filtered_s.append((i, ch))

    left, right = 0, 0
    window_counts = {}
    formed = 0
    ans = float("inf") # MAX_INT
    range = 0,0 # Range of indexes of the minimum sized window


    # Now look at the characters only in the filtered list. This helps to reduce our search.
    while right < len(filtered_s):
        # Get the current character where the right pointer is pointing to
        right_char = filtered_s[right][1]
        # Now increament the count of that character on the windows_count table
        window_counts[right_char] = window_counts.get(right_char, 0) + 1

        # If current chacrater has been seen the required no of times as in pattern t
        # increament formed by 1
        if window_counts[right_char] == t_map[right_char]:
            formed += 1


        # Now if all the characters have been seen and formed is now equal to required size of pattern
        # we can move the left pointer towards right
        while left <= right and formed == required:
            # Get the character where left pointer is pointing to
            left_char = filtered_s[left][1]

            # And now check if the reduced window size has all the characters
            # Either ways save the smallest window possible
            start = filtered_s[left][0]
            end = filtered_s[right][0]

            if end-start+1 < ans:
                ans = end-start+1
                range = (start, end)

            # Decreament that character count as that has been seen
            window_counts[left_char] -= 1
            # Now reduce the window size moving left towards right
            # and check if window_counts has still all the elemernts
            # If not, decremanet formed, so the right can move more right
            if window_counts[left_char] < t_map[left_char]:
                formed-=1


            left+=1

        right+=1

    return range




if __name__ == "__main__":
    output = minimum_window_substring("ADOBECODEBANC", "ABC")
    print(output)
