"""
PROBLEM: Word Break
Consider the following dictionary
{ i, like, sam, sung, samsung, mobile, ice,
  cream, icecream, man, go, mango}

Input:  ilike
Output: Yes
The string can be segmented as "i like".

Input:  ilikesamsung
Output: Yes
The string can be segmented as "i like samsung"
or "i like sam sung".
"""

"""
Optimized Approach - Dynamic Programming:
----------------------------------------
We memoize the result of the subproblems and use it find other possible substrings

Complexity:
-----------
    - we're gonna be iterating for all n characters of string (worst case)
    - For each found word, we look for all other substrings after that word
    - Hence Time complexity is O(n x k), where k is smaller than n 
"""

def word_break(str):
    size = len(str)

    if size == 0:
        return True

    # Create a DP table to store the result of the subproblems.
    # T[i] will be True if the segment is found in the dictionary, else False
    T = [False for _ in range(size+1)]

    for i in range(1,size+1):

        # If current T[i] is False, then check if current prefix can make
        # it True
        if T[i] is False and dictionaryContains(str[0:i]):
            T[i] = True

        # IF T[i] is True, then check for all the substrings from i+1 th character
        # and store their result
        if T[i] is True:

            # If i is True, that means we have reached the last prefix and its
            # safe to say its True
            if i == size:
                return True

            for j in range(i+1, size+1):
                if T[j] is False and dictionaryContains(str[i:j]):
                    T[j] = True

                if j == size and T[j] is True:
                    return True

    return False


def dictionaryContains(word):
    if word in dictionary:
        return True

    return False

dictionary = [
    "mobile","samsung","sam","sung",
    "man","mango","icecream","and",
    "go","i","like","ice","cream"
]
assert word_break("ilikesamsung") == True
assert word_break("iiiiiiii") == True
assert word_break("") == True
assert word_break("samsungandmango") == True
assert word_break("samsungandmangok") == False
