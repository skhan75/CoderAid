"""
Find number of substrings of length k whose sum of ASCII value of characters is divisible by k

COMPLEXITY:
    - Runtime: O(log n)
    - Space Complexity: O(1)
"""

def k_maximum_sum(s, k):
    sum, count = 0, 0

    # Finding sum of k ascii characters of the substring
    for i in range(k):
        sum += ord(s[i])

    if sum%k == 0:
        count += 1

    window_sum = sum
    for i in range(k, len(s)):
        window_sum += ord(s[i]) - ord(s[i-k])
        if window_sum % 3 == 0:
            count+=1

    return count


# Driver Code
s = "bcgabc"
k = 3
ans = k_maximum_sum(s, k)
print(ans)
